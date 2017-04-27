---
layout: post
title: "OpenAI Gym - CartPole"
categories: journal
tags: [documentation,sample]
image:
  feature: blog_images/2017-04-28-OpenAI-Gym-CartPole/OpenAI_logo.png
  teaser: blog_images/2017-04-28-OpenAI-Gym-CartPole/OpenAI_logo.png
  credit: 
  creditlink: ""
---

### Introduction

[OpenAI Gym](https://gym.openai.com/) is a platform where you could test your intelligent learning algorithm on various application, including games and virtual physics experiments. It provides APIs for all these applications for the convenience of integrating the application into the algorithms. The API is called "environment" in OpenAI Gym. On one hand, the environment only receives "action" instructions as input and outputs the observation, reward, signal of termination, and other information. On the other hand, your learning algorithm receives observation(s), reward(s), signal(s) of termination as input and outputs the action. So in principle, one can develop a learning algorithm and wrapped it into a class object. It could test all the enviroments in OpenAI Gym.

Because I have already implemented a Deep Q-Learning class to learn flappy bird, I think it would be very convenient to test the Deep Q-Learning algorithm in all these environments in OpenAI Gym.

### Make OpenAI Deep Q-Learning Class

The environments in OpenAI Gym could be categorized into two classes regarding to their types of observation output. The video game environments usually outputs two-dimentional images as observation and the virtual physics experiments usually outputs one-dimentional numerical experiment observation data. Therefore, in addition to the existing Deep Q-Learning class for the two-dimentional image data, an additional Deep Q-Learning class that is suitable for learning from the one-dimentional data would be prepared.

### Test OpenAI Deep Q-Learning Class in OpenAI Gym CartPole-v0 Environment

CartPole environment is probably the most simple environment in OpenAI Gym. However, when I was trying to load this environment, there is an issue regarding box2d. To fix this, take the following steps. Many thanks to this [blogger](http://kelisv.blogspot.com/2016/12/attributeerror-module-object-has-no.html) for the straightforward instruction. This bug might be fixed in the future release of OpenAI Gym according to someone related to OpenAI.

```
pip uninstall Box2D box2d-py
git clone https://github.com/pybox2d/pybox2d
cd pybox2d/
python setup.py clean
python setup.py build
python setup.py install
```

At first I thought it would be super easy to train the Q-Learning algorithm, given a similar Q-Learning algorithm was doing extremely well in Flappy Bird game after training with 60,000 game frames. However, I was wrong in some aspects. With some parameter details from [songrotek's code](https://gym.openai.com/evaluations/eval_kBouPnRtQCezgE79s6aA5A), I was able to overcome the problems and learned a lot. So I have to thank songrotek here.

#### Number of Game Frames

When I was implementing Deep Q-Learning algorithm on Flappy Bird game, I used the concept of integrating multiple game frames as input data, because a single game frame is not able to fully represent the current state of the game. For example, the moving direction and moving velocity could not be told from a single game frame. 

There lacks the detailed explanations to the physical meannings to the actions and the observation in most of the environments in OpenAI Gym. (I already complained it in the forum, but it seems that there is nobody responding. ) This is also true for the CartPole-v0 environment. So I was not sure whether I have to ignore the observations preceeding to the current observation. In principle, I think including the proceeding observations will not hurt. Because even if the proceeding observations are not relavent to the determination of action, the neuron network will gave zero weights to those observations after sufficient training. However, when it comes to this problem, it turned out that increasing game frames did not helped the algorithm learn well. If I set the game frame to 1, the algorithm was able to play CartPole very well after 5,000 to 8,000 episodes. However, if I set the game frame to 4, at least within 10,000 episodes, the algorithm was not able to play. I could set the episode maximum to 100,000 in the future to see whether a good learning performance could be achieved. But for this CartPole game, introducing multiple game frames is bad. If I knew the physical meaning of the observation data, I would not even try introducing multiple game frames. (It really made me sad when the algorithm did not work at the beginning.)

#### Neural Network

Because the observation space of CartPole is only 3 and the action space of CartPole is only 2. I think this is a very simple game. So I used one single layer of fully-connected neural network with only 20 hidden unit. It turned out that it works fine. It should be noted that there is no convolutional neural network in such applications.

#### Learning Rate

Learning rate is usually the most import parameter to the success of an algorithm in an application. Deep Learning is different to traditional Machine Learning. One may sysmentaically explore all most all the hyperparameters in a Machine Learning task in a short period of time, however, the training of Deep Learning usually takes much longer time, which makes it much more difficult to tune deep learning hyperparameters using limited computation resources. In this situation, the experience, which I lack, becomes very important.

In this CartPole game, I firstly set the learning rate to 0.0001, which is a number I usually use, in Adam Optimizer, and started to observe the loss during the training. The loss increased right after the start of training, and the learning performance was extremely poor. So I thought the learning rate is too high. I immediately terminated the program and set the learning rate to smaller numbers. After training with smaller learning rates, say 0.000001, the loss decreasd after the start of training. But it stopped decreasing when the loss reaches 0.4. The learning performance, in some cases, is extremely good. However, for most of the time, the learning performance is extremely poor. I did not quickly understand what's happening at that time. Later, I think the optimization is trapped in local minimum at that time. The learning rate was too small for the optimization to overcome the barriers around the local minimum.

It turned out that the learning rate of 0.0001 is the right one to use in CartPole game. The loss firstly increased then decreased. The algorithm was able to play CartPole very well after 5,000 to 8,000 episodes.

### Notes

When I was training the algorithm, I found that for sufficient long training time, the learning performance would fluctuate. Say, the learning performance reached maximum at episode 5000 for 300 episodes. Then the learning performance dropped significantly. After training with some more time, the learning performance reached maximum again for a while. This phenomenon repeated throughout the training. From my personal point of view, the optimization might have not reached the optimal because I could often see some large loss number even in the later stage of the training. Is it because the learning rate is sometimes to big to make cause the optimization jump out of the optimal, or it is often not possible to train an Deep Q-Learning algorithm to have an absolute perfect solution, or the neural network is just not sophiscated enough? I am not able to answer this question with my current knowledge.

I was also suprised that if counting game frames, it also took nearly 1,000,000 game frames to reach good performance. Recall the a similar algorithm only took 600,000 game frames to have a extremely good performance in Flappy Bird game. 

### Algorithm Performance


### Links to GitHub

<>