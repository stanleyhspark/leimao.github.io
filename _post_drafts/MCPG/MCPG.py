'''
REINFORCE Monte Carlo Policy Gradient AI Player
Author: Lei Mao
Date: 5/2/2017
Introduction: 
The REINFORCE_AI used REINFORCE, one of the Monte Carlo Policy Gradient methods, to optimize the AI actions in certain environment.
'''

class OpenAI_REINFORCE_FC():

    def __init__(self, num_actions, num_features, rand_seed, mode):
    
        # Initialize the number of player actions available in the game
        self.num_actions = num_actions
        # Initialize the number of features in the state
        self.num_features = num_features
        # Determine the shape of input to the model
        self.input_shape = self.num_features * GAME_STATE_FRAMES
        # Initialize the model
        self.model = self.REINFORCE_FC_Setup()
        # Initialize episode replays used for caching game transitions in one single episode
        self.episode_states = list()
        self.episode_actions = list()
        self.episode_rewards = list()
        # Initialize time_step to count the time steps during training
        self.time_step = 0
        # Initialize the mode of AI
        self.mode = mode

        # Initialize random seed
        self.rand_seed = rand_seed
        # Set seed for psudorandom numbers
        random.seed(self.rand_seed)
        np.random.seed(self.rand_seed)
        
    def REINFORCE_FC_Setup(self):
    
        # Prepare Policy Neural Network
        # Note that we did not use regularization here
        model = Sequential()
        # FC layer_1
        model.add(Dense(36, activation = 'relu', input_dim = self.input_shape))
        # FC layer_2
        #model.add(Dense(64, activation = 'relu'))
        # FC layer_3
        #model.add(Dense(128, activation = 'relu'))
        # FC layer_4
        model.add(Dense(self.num_actions))
        # Optimizer
        optimizer = keras.optimizers.Adam(lr = LEARNING_RATE)
        # Compile the model
        model.compile(loss = keras.losses.mean_squared_error, optimizer = optimizer)
        
        return model

    def Store_Transition(self, state, action, mc_return):

        # Store game transitions used for updating the weights in the Policy Neural Network

        self.episode_replay.append((state, action, reward))

    def Calculate_Value(self):

        # The estimate of v(St) is updated in the direction of the complete return:
        # Gt = Rt+1 + gamma * Rt+2 + gamma^2 * Rt+3 + ... + gamma^(T-t+1)RT;
        # where T is the last time step of the episode.

        state_values = np.zeros_like(self.episode_rewards)
        state_values[-1] = self.episode_rewards[-1]
        for t in reversed(range(0, len(self.episode_rewards)-1)):
            state_values[t] = GAMMA * state_values[t+1] + self.episode_rewards[t]

        # Normalization to help the control of the gradient estimator variance
        state_values -= np.mean(state_values)
        state_values /= np.std(state_values)

        return state_values


