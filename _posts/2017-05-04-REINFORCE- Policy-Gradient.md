---
layout: post
title: "Monte Carlo Policy Gradient in OpenAI-Gym LunarLander"
categories: journal
tags: [documentation,sample]
image:
  feature: blog_images/2017-05-04-REINFORCE-Policy_Gradient/LunarLander.png
  teaser: blog_images/2017-05-04-REINFORCE-Policy_Gradient/LunarLander.png
  credit: 
  creditlink: ""
---

### Introduction

[LunarLander](https://gym.openai.com/envs/LunarLander-v2) is one of the learning environment in OpenAI Gym. I have actually tried to solve this learning problem using Deep Q-Learning which I have successfully used to train the CartPole environment in OpenAI Gym and the Flappy Bird game. However, I was not able to get good training performance in a reasonable amount of episodes. The lunarlander controlled by AI only learned how to steadily float in the air but was not able to successfully land within the time requested.

Here I am going to tackle this LunarLander problem using a new alogirthm called "REINFORCE" or "Monte Carlo Policy Gradient".

### Touch the Algorithm

Algorithm from [Sutton Book draft]()

![](/images/blog_images/2017-05-04-REINFORCE-Policy_Gradient/Sutton_REINFORCE.png)

Algorithm from [Silver Courseware](http://www0.cs.ucl.ac.uk/staff/D.Silver/web/Teaching.html)

![](/images/blog_images/2017-05-04-REINFORCE-Policy_Gradient/Silver_REINFORCE.png)

Note that the Gt item in Sutton's REINFORCE algorithm and the vt item in Silver's REINFORCE algorithm are the same thing.

Gt = Rt+1 + gamma * Rt+2 + gamma^2 * Rt+3 + ... + gamma^(T-t+1)RT

However, Silver's REINFORCE algorithm lacked a gamma^t item than Sutton's algorithm. I personally believe that Silver was wrong and Sutton was correct. It may not have an significanty impact on the optimization of the algorithm. I will confirm this and explore the effect of lacking this item if I have chance in the future. For now, I am going to implement Silver's REINFORCE algorithm without including the gamma^t item.

### Make OpenAI Deep REINFORCE Class

The main neural network in Deep REINFORCE Class taks the observation as input and outputs the softmaxed probability for all actions available.

This algorithm is very conceptually simple. However, I got stuck for a while when I firstly tried to implement it on my computer. We have got used to use deep learning libraries, such as tensorflow, to calculate derivatives for convenience. The tensorflow allows us to optimize the parameters in the neural network by minimizing some loss functions. However, from the REINFORCE algorithm, it seems that we have to manually calculate the derivatives and optimize the parameters through iterations. 

One of way to overcome this is to construct a loss function whose minimization derivative udpate is exactly the same to the one in the algorithm. One simple loss function could be (-log_p * vt) note that -log_p is the cross entropy of softmaxed action prediction and labeled action.

### Test OpenAI Deep REINFORCE Class in OpenAI Gym LunarLander Environment

#### Key Parameters

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

Before Training:

![](/images/blog_images/2017-04-28-OpenAI-Gym-CartPole/episode_0.gif)

After Training:

![](/images/blog_images/2017-04-28-OpenAI-Gym-CartPole/episode_27000.gif)

OpenAI Gym Evaluation

Solved after 9919 episodes. Best 100-episode average reward was 200.00 ¡À 0.00.
<https://gym.openai.com/evaluations/eval_ewr0DWHeTmGE6x1NGQ1LiQ>

### Conclusions

Deep Q-Learning is a good technique to solve CartPole problem. However, it seems that it suffered from high variance and its convergences seems to be slow.

### Links to GitHub

<https://github.com/leimao/OpenAI_Gym_AI/tree/master/CartPole-v0/Deep_Q-Learning/2017-04-28-v1>

### Follow-up Optimizations

I used one single layer of fully-connected neural network with only 20 hidden unit in the first implementation. I found that increasing the depth and the size of neural network, and increasing the batch size for stochastic gradient descent could improve the learning efficiency and performance robustness. Personally I think the depth and the size of neural network helped to improve the robustness of performance, and the batch size helped to prevent random sampling bias and optimization bias during the stochastic gradient descent. As the result, the learning became faster, and the learning performance robustness was improved.

#### 2017-04-29-v1

Parameters

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

OpenAI Gym Evaluation

Solved after 293 episodes. Best 100-episode average reward was 197.39 ¡À 1.68.

<https://gym.openai.com/evaluations/eval_Jr2oXkrS8KMUQEkCBurAw>

Links to GitHub

<https://github.com/leimao/OpenAI_Gym_AI/tree/master/CartPole-v0/Deep_Q-Learning/2017-04-29-v1>

#### 2017-04-29-v2

Parameters

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

OpenAI Gym Evaluation

Solved after 138 episodes. Best 100-episode average reward was 196.58 ¡À 1.34.

<https://gym.openai.com/evaluations/eval_F90GxQxrQK2J6ESQkLVaA>

Links to GitHub

<https://github.com/leimao/OpenAI_Gym_AI/tree/master/CartPole-v0/Deep_Q-Learning/2017-04-29-v2>

### Notes

#### 2017-4-28

When I was training the algorithm, I found that if the algorithm was trained for sufficient long time, the learning performance would fluctuate. Say, the learning performance reached maximum at episode 5000 for 300 episodes. Then the learning performance dropped significantly. After training for some more time, the learning performance reached maximum again for another while. This phenomenon repeated throughout the training. From my personal point of view, the optimization might have deviated from the optimal because I could often see some large loss number even in the later stage of the training. Is it because the learning rate is sometimes to big to make cause the optimization jump out of the optimal, or it is often not possible to train an Deep Q-Learning algorithm to have an absolute perfect solution, or the neural network is just not sophiscated enough? I am not able to answer this question with my current knowledge.

I was also suprised that if counting game frames, it also took nearly 1,000,000 game frames to reach good performance. Recall the a similar algorithm only took 600,000 game frames to have a extremely good performance in Flappy Bird game. 

#### 2017-4-28

Specifically for the problem in OpenAI Gym, to achieve both learning efficiency and performance robustness, I think learning rate decay might be a good strategy. I may try it if I have chance in the future.

I also found that, in addition to Q-Learning, Policy Gradient might work better. I may implement this algorithm in the future.

<https://github.com/lancerts/Reinforcement-Learning>

<https://gym.openai.com/evaluations/eval_9niu4HNZTgm0VLJ0b8MUtA>