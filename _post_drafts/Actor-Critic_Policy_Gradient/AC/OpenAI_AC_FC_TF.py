'''
Actor-Critic Policy Gradient AI Player
Author: Lei Mao
Date: 5/7/2017
Introduction: 
The ACPG_AI used Actor-Critic method to optimize the AI actions in certain environment. The critic updates network for the values of the states v(s).
'''

import os
import numpy as np
import tensorflow as tf

GAMMA = 0.99 # decay rate of past observations
LEARNING_RATE_ACTOR = 0.005 # learning rate of actor in deep learning
LEARNING_RATE_CRITIC = 0.005 # learning rate of critic in deep learning
RAND_SEED = 0 # random seed
SAVE_PERIOD = 100000 # period of time steps to save the model
LOG_PERIOD = 1000 # period of time steps to save the log of training
MODEL_DIR = 'model/' # path for saving the model
LOG_DIR = 'log/' # path for saving the training log

np.random.seed(RAND_SEED)
tf.set_random_seed(RAND_SEED)

class Actor():

    def __init__(self, num_actions, num_features):
    
        # Initialize the number of player actions available in the game
        self.num_actions = num_actions
        # Initialize the number of features in the observation
        self.num_features = num_features
        # Initialize the model
        self.model = self.Policy_FC_Setup()
        # Initialize tensorflow session
        self.saver = tf.train.Saver()
        self.sess = tf.Session()
        self.sess.run(tf.global_variables_initializer())
        # Initialize the episode number
        self.episode = 0
        # Initialize the number of time steps
        self.time_step = 0
        # Initialize the total number of time steps
        self.time_step_total = 0

    def Policy_FC_Setup(self):

        # Set up Policy Tensorflow environment
        with tf.name_scope('inputs'):

            self.tf_observation = tf.placeholder(tf.float32, [1, self.num_features], name = 'observation')
            self.tf_action = tf.placeholder(tf.int32, None, name = 'num_action')
            self.tf_value = tf.placeholder(tf.float32, None, name = 'state_value')

        # FC1
        fc1 = tf.layers.dense(
            inputs = self.tf_observation,
            units = 32,
            activation = tf.nn.tanh,  # tanh activation
            kernel_initializer = tf.random_normal_initializer(mean = 0, stddev = 0.3),
            bias_initializer = tf.constant_initializer(0.1),
            name='FC1')

        # FC2
        logits = tf.layers.dense(
            inputs = fc1,
            units = self.num_actions,
            activation = None,
            kernel_initializer = tf.random_normal_initializer(mean = 0, stddev = 0.3),
            bias_initializer = tf.constant_initializer(0.1),
            name='FC2')

        # Softmax
        self.action_probs = tf.nn.softmax(logits, name = 'action_probs')

        with tf.name_scope('loss'):

            # To maximize (log_p * V) is equal to minimize -(log_p * V)
            # Construct loss function mean(-(log_p * V)) to be minimized by tensorflow
            neg_log_prob = tf.nn.sparse_softmax_cross_entropy_with_logits(logits = logits, labels = self.tf_action) # this equals to -log_p
            self.loss = tf.reduce_mean(neg_log_prob * self.tf_value)

        with tf.name_scope('train'):

            self.optimizer = tf.train.AdamOptimizer(LEARNING_RATE_ACTOR).minimize(self.loss)

    def Policy_FC_Train(self, observation, action, value):

        observation = observation[np.newaxis, :]

        # Start gradient descent
        _, train_loss = self.sess.run([self.optimizer, self.loss], feed_dict = { self.tf_observation: observation, self.tf_action: action, self.tf_value: value})

        if self.time_step_total % SAVE_PERIOD == 0:
            if not os.path.exists(MODEL_DIR):
                os.makedirs(MODEL_DIR)
            self.saver.save(self.sess, MODEL_DIR + 'AI_Actor')

        self.time_step += 1
        self.time_step_total += 1

        return train_loss

    def Policy_FC_Restore(self):

        # Restore the trained FC policy network
        self.saver.restore(self.sess, MODEL_DIR + 'AI_Actor')

    def Episode_Update(self):

        # Update episode number when the new epsidoe starts
        self.episode += 1
        # Reset time_step to 0 when the new episode starts
        self.time_step = 0

    def Get_Action(self, observation):

        # Calculate action probabilities when given observation
        prob_weights = self.sess.run(self.action_probs, feed_dict = {self.tf_observation: observation[np.newaxis, :]})

        # Randomly choose action according to the probabilities
        action = np.random.choice(range(prob_weights.shape[1]), p = prob_weights.ravel())

        return action


class Critic():

    def __init__(self, num_features):
    
        # Initialize the number of features in the observation
        self.num_features = num_features
        # Initialize the model
        self.model = self.Value_FC_Setup()
        # Initialize tensorflow session
        self.saver = tf.train.Saver()
        self.sess = tf.Session()
        self.sess.run(tf.global_variables_initializer())
        # Initialize the episode number
        self.episode = 0
        # Initialize the number of time steps
        self.time_step = 0
        # Initialize the total number of time steps
        self.time_step_total = 0

    def Value_FC_Setup(self):

        # Set up State value Tensorflow environment
        with tf.name_scope('inputs'):

            self.tf_observation = tf.placeholder(tf.float32, [1, self.num_features], name = 'observation')
            self.tf_reward = tf.placeholder(tf.float32, None, name = 'reward')
            self.tf_value_next = tf.placeholder(tf.float32, None, name = 'state_value_next')

        # FC1
        fc1 = tf.layers.dense(
            inputs = self.tf_observation,
            units = 32,
            activation = tf.nn.tanh,  # tanh activation
            kernel_initializer = tf.random_normal_initializer(mean = 0, stddev = 0.3),
            bias_initializer = tf.constant_initializer(0.1),
            name='FC1')

        # FC2
        logits = tf.layers.dense(
            inputs = fc1,
            units = 1,
            activation = None,
            kernel_initializer = tf.random_normal_initializer(mean = 0, stddev = 0.3),
            bias_initializer = tf.constant_initializer(0.1),
            name='FC2')
        
        self.value = logits

        with tf.name_scope('loss'):

            self.loss = tf.square(self.tf_reward + GAMMA * self.tf_value_next - self.value)

        with tf.name_scope('train'):

            self.optimizer = tf.train.AdamOptimizer(LEARNING_RATE_CRITIC).minimize(self.loss)

    def Value_FC_Train(observation, reward, observation_next):
        
        value_next = self.sess.run(self.value, feed_dict = {self.tf_observation: observation[np.newaxis, :]})[0]

        _, train_loss = self.sess.run([self.optimizer, self.loss], feed_dict = { self.tf_observation: observation, self.tf_reward: reward, self.tf_value_next: value_next})

        if self.time_step_total % SAVE_PERIOD == 0:
            if not os.path.exists(MODEL_DIR):
                os.makedirs(MODEL_DIR)
            self.saver.save(self.sess, MODEL_DIR + 'AI_Critic')

        self.time_step += 1
        self.time_step_total += 1

        return train_loss

    def Value_FC_Restore(self):

        # Restore the trained FC policy network
        self.saver.restore(self.sess, MODEL_DIR + 'AI_Critic')

    def Episode_Update(self):

        # Update episode number when the new epsidoe starts
        self.episode += 1
        # Reset time_step to 0 when the new episode starts
        self.time_step = 0

    def Get_Value(self, observation):

        # Calculate state value when given observation
        state_value = self.sess.run(self.value, feed_dict = {self.tf_observation: observation[np.newaxis, :]})[0]

        return state_value

class OpenAI_ACPG_AI():

    def __init__(self, num_actions, num_features):
    
        # Initialize the number of player actions available in the game
        self.num_actions = num_actions
        # Initialize the number of features in the observation
        self.num_features = num_features
        # Initialize the actor
        self.actor = Actor(num_actions = num_actions, num_features = num_features)
        # Initialize the critic
        self.critic = Critic(num_features = num_features)
        # Initialize the episode number
        self.episode = 0
        # Initialize the number of time steps
        self.time_step = 0
        # Initialize the total number of time steps
        self.time_step_total = 0

    def Load(self):

        # Load trained actor and critic for test
        self.actor.Policy_FC_Restore()
        self.critic.Value_FC_Restore()

    def Train(self, observation, action, reward, done, observation_next):

        # Train the critic value network
        self.critic.Value_FC_Train(observation = observation, reward = reward, observation_next = observation_next)
        # Get the value of the current observation
        value = self.critic.Get_Value(observation = observation)
        # Train the actor policy network
        self.actor.Policy_FC_Train(observation = observation, action = action, value = value)
        if done:
            # Update episode information
            self.critic.Episode_Update()
            self.actor.Episode_Update()
    
    def Test(self, observation):

        # Get action instruction from the actor
        return self.actor.Get_Action(observation = observation)



