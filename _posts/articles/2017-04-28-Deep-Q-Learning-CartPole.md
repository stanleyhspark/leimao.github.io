---
layout: post
title: Deep Q-Learning in OpenAI-Gym CartPole
excerpt: "Implementation of Deep Q-Learning algorithm in OpenAI Gym environments."
modified: 2017-04-26T14:17:25-04:00
categories: article
tags: [artificial intelligence, deep learning, reinforcement learning]
comments: true
share: true
image:
  teaser: /images/articles/2017-04-28-Deep-Q-Learning-CartPole/cartpole.png
---

### Introduction

[OpenAI Gym](https://gym.openai.com/) is a platform where you could test your intelligent learning algorithm in various application, including games and virtual physics experiments. It provides APIs for all these applications for the convenience of integrating the algorithms into the application. The API is called "environment" in OpenAI Gym. On one hand, the environment only receives "action" instructions as input and outputs the observation, reward, signal of termination, and other information. On the other hand, your learning algorithm receives observation(s), reward(s), signal(s) of termination as input and outputs the action. So in principle, one can develop a learning algorithm and wrapped it into a class object. It could test all the enviroments in OpenAI Gym.

<br />

Because I have already implemented a Deep Q-Learning class to learn flappy bird, I think it would be very convenient to test the Deep Q-Learning algorithm in all these environments in OpenAI Gym.

![]({{ site.url }}/images/articles/2017-04-28-Deep-Q-Learning-CartPole/cartpole.png)

### Make OpenAI Deep Q-Learning Class

The environments in OpenAI Gym could be categorized into two classes regarding to their types of observation output. The video game environments usually outputs two-dimentional images as observation and the virtual physics experiments usually outputs one-dimentional numerical experiment observation data. Therefore, in addition to the existing Deep Q-Learning class for the two-dimentional image data, an additional Deep Q-Learning class that is suitable for learning from the one-dimentional data should be prepared for the OpenAI Gym environments.

### Test OpenAI Deep Q-Learning Class in OpenAI Gym CartPole-v0 Environment

CartPole environment is probably the most simple environment in OpenAI Gym. However, when I was trying to load this environment, there is an issue regarding the box2d component. To fix this, please take the following steps. Many thanks to this [blogger](http://kelisv.blogspot.com/2016/12/attributeerror-module-object-has-no.html) for the straightforward instruction. This bug might be fixed in the future release of OpenAI Gym according to someone related to OpenAI.

```shell
pip uninstall Box2D box2d-py
git clone https://github.com/pybox2d/pybox2d
cd pybox2d/
python setup.py clean
python setup.py build
python setup.py install
```

At first I thought it would be super easy to train the Q-Learning algorithm, given a similar Q-Learning algorithm was doing extremely well in Flappy Bird game after training with 60,000 game frames. However, I was wrong in some aspects. With some parameter setting details from [songrotek's code](https://gym.openai.com/evaluations/eval_kBouPnRtQCezgE79s6aA5A), I was able to overcome the problems and learned a lot. So I have to thank songrotek here.

#### Number of Game Frames

When I was implementing Deep Q-Learning algorithm on Flappy Bird game, I used the concept of integrating multiple game frames as input data, because a single game frame is not able to fully represent the current state of the game. For example, the moving direction and moving velocity could not be told from a single game frame. 

<br />

There lacks the detailed explanations to the physical meannings to the actions and the observation in most of the environments in OpenAI Gym. (I already complained it in the forum, but it seems that there is nobody responding. ) This is also true for the CartPole-v0 environment. So I was not sure whether I have to ignore the observations preceeding to the current observation. In principle, I think including the proceeding observations will not hurt. Because even if the proceeding observations are not relavent to the determination of action, the neuron network will gave zero weights to those observations after sufficient training. However, it turned out that increasing game frames did not helped the algorithm learn well. If I set the game frame to 1, the algorithm was able to play CartPole very well after 5,000 to 8,000 episodes. If I set the game frame to 4, at least within 10,000 episodes, the algorithm was not able to play. I could set the episode maximum to 100,000 in the future to see whether a good learning performance could be achieved. But for this CartPole game, introducing multiple game frames is bad. If I knew the physical meaning of the observation data, I would not even try introducing multiple game frames. (It really made me sad when the algorithm did not work at the beginning.)

#### Neural Network

Because the observation space of CartPole is only 3 and the action space of CartPole is only 2. I think this must be a very simple game. So I used one single layer of fully-connected neural network with only 20 hidden unit. It turned out that it worked just fine. It should be noted that there is no convolutional neural network in such applications.

#### Learning Rate

Learning rate is usually the most import parameter to the success of an algorithm in an application. Deep Learning is different to traditional Machine Learning. One may systematically explore all most all the hyperparameters in a Machine Learning task in a short period of time, however, the training of Deep Learning usually takes much longer time, which makes it much more difficult to tune deep learning hyperparameters using limited computation resources. In this situation, the experience, which I lack, becomes very important.

<br />

In this CartPole game, I firstly set the learning rate to 0.0001 in Adam Optimizer, and started to observe the loss during the training. The loss increased right after the start of training, and the learning performance was extremely poor. So I thought the learning rate is too high. I immediately terminated the program and set the learning rate to smaller numbers. After training with smaller learning rates, say 0.000001, the loss decreasd after the start of training. But it stopped decreasing when the loss reaches around 0.4. The learning performance, in some rare cases, is extremely good. However, for the most of the time, the learning performance is extremely poor. I did not understand what's happening at that time. Later, I think the optimization was trapped in local minimum at that time. The learning rate was too small for the optimization to overcome the barriers around the local minimum. That small learning rate in ordinary gradient descent leads to bad optimization outcome rarely happen in ordinary machine learning task to my knowledge, though it may take very long time to reach the minimum. I am not sure whether small learning rate sometimes would never lead the optimization to reach minimum if we use stochastic gradient descent, like what we used to use in Deep Learning tasks. 

<br />

It turned out that the learning rate of 0.0001 is the right one to use in CartPole game. The loss firstly increased then decreased. The algorithm was able to play CartPole very well after 5,000 to 8,000 episodes of training.

### Key Parameters

FC-20

```python
GAME_STATE_FRAMES = 1  # number of game state frames used as input
GAMMA = 0.9 # decay rate of past observations
EPSILON_INITIALIZED = 0.5 # probability epsilon used to determine random actions
EPSILON_FINAL = 0.01 # final epsilon after decay
BATCH_SIZE = 32 # number of sample size in one minibatch
LEARNING_RATE = 0.0001 # learning rate in deep learning
FRAME_PER_ACTION = 1 # number of frames per action
REPLAYS_SIZE = 1000 # maximum number of replays in cache
TRAINING_DELAY = 1000 # time steps before starting training for the purpose of collecting sufficient replays to initialize training
EXPLORATION_TIME = 10000 # time steps used for decaying epsilon during training before epsilon decreases to zero
```

### Algorithm Performance

**Before Training:**

![]({{ site.url }}/images/articles/2017-04-28-Deep-Q-Learning-CartPole/episode_0.gif)

**After Training:**

![]({{ site.url }}/images/articles/2017-04-28-Deep-Q-Learning-CartPole/episode_27000.gif)

**OpenAI Gym Evaluation**

<br />

Solved after 9919 episodes. Best 100-episode average reward was 200.00 ± 0.00.
<https://gym.openai.com/evaluations/eval_ewr0DWHeTmGE6x1NGQ1LiQ>

### Conclusions

Deep Q-Learning is a good technique to solve CartPole problem. However, it seems that it suffered from high variance and its convergences seems to be slow.

### Links to GitHub

<https://github.com/leimao/OpenAI_Gym_AI/tree/master/CartPole-v0/Deep_Q-Learning/2017-04-28-v1>

### Follow-up Optimizations

I used one single layer of fully-connected neural network with only 20 hidden unit in the first implementation. I found that increasing the depth and the size of neural network, and increasing the batch size for stochastic gradient descent could improve the learning efficiency and performance robustness. Personally I think the depth and the size of neural network helped to improve the robustness of performance, and the batch size helped to prevent random sampling bias and optimization bias during the stochastic gradient descent. As the result, the learning became faster, and the learning performance robustness was improved.

#### 2017-04-29-v1

**Parameters**

<br />

FC-128 -> FC-128

```python
GAME_STATE_FRAMES = 1  # number of game state frames used as input
GAMMA = 0.95 # decay rate of past observations
EPSILON_INITIALIZED = 0.5 # probability epsilon used to determine random actions
EPSILON_FINAL = 0.0001 # final epsilon after decay
BATCH_SIZE = 128 # number of sample size in one minibatch
LEARNING_RATE = 0.0005 # learning rate in deep learning
FRAME_PER_ACTION = 1 # number of frames per action
REPLAYS_SIZE = 2000 # maximum number of replays in cache
TRAINING_DELAY = 2000 # time steps before starting training for the purpose of collecting sufficient replays to initialize training
EXPLORATION_TIME = 10000 # time steps used for decaying epsilon during training before epsilon decreases to zero
```

**OpenAI Gym Evaluation**

<br />

Solved after 293 episodes. Best 100-episode average reward was 197.39 ± 1.68.

<br />

<https://gym.openai.com/evaluations/eval_Jr2oXkrS8KMUQEkCBurAw>

<br />

**Links to GitHub**

<br />

<https://github.com/leimao/OpenAI_Gym_AI/tree/master/CartPole-v0/Deep_Q-Learning/2017-04-29-v1>

#### 2017-04-29-v2

**Parameters**

<br />

FC-128 -> FC-128

```python
GAME_STATE_FRAMES = 1  # number of game state frames used as input
GAMMA = 0.95 # decay rate of past observations
EPSILON_INITIALIZED = 0.5 # probability epsilon used to determine random actions
EPSILON_FINAL = 0.0005 # final epsilon after decay
BATCH_SIZE = 128 # number of sample size in one minibatch
LEARNING_RATE = 0.0005 # learning rate in deep learning
FRAME_PER_ACTION = 1 # number of frames per action
REPLAYS_SIZE = 5000 # maximum number of replays in cache
TRAINING_DELAY = 1000 # time steps before starting training for the purpose of collecting sufficient replays to initialize training
EXPLORATION_TIME = 10000 # time steps used for decaying epsilon during training before epsilon decreases to zero
```

**OpenAI Gym Evaluation**

<br />

Solved after 138 episodes. Best 100-episode average reward was 196.58 ± 1.34.

<br />

<https://gym.openai.com/evaluations/eval_F90GxQxrQK2J6ESQkLVaA>

<br />

**Links to GitHub**

<br />

<https://github.com/leimao/OpenAI_Gym_AI/tree/master/CartPole-v0/Deep_Q-Learning/2017-04-29-v2>

### Notes

#### 2017-4-28

When I was training the algorithm, I found that if the algorithm was trained for sufficient long time, the learning performance would fluctuate. Say, the learning performance reached maximum at episode 5000 for 300 episodes. Then the learning performance dropped significantly. After training for some more time, the learning performance reached maximum again for another while. This phenomenon repeated throughout the training. From my personal point of view, the optimization might have deviated from the optimal because I could often see some large loss number even in the later stage of the training. Is it because the learning rate is sometimes to big to make cause the optimization jump out of the optimal, or it is often not possible to train an Deep Q-Learning algorithm to have an absolute perfect solution, or the neural network is just not sophiscated enough? I am not able to answer this question with my current knowledge.

<br />

I was also suprised that if counting game frames, it also took nearly 1,000,000 game frames to reach good performance. Recall the a similar algorithm only took 600,000 game frames to have a extremely good performance in Flappy Bird game. 

#### 2017-4-28

Specifically for the problem in OpenAI Gym, to achieve both learning efficiency and performance robustness, I think learning rate decay might be a good strategy. I may try it if I have chance in the future.

<br />

I also found that, in addition to Q-Learning, Policy Gradient might work better. I may implement this algorithm in the future.

<br />

<https://github.com/lancerts/Reinforcement-Learning>

<https://gym.openai.com/evaluations/eval_9niu4HNZTgm0VLJ0b8MUtA>