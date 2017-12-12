---
layout: post
title: Deep Q-Learning in Flappy Bird Game
excerpt: "Implementation of Deep Q-Learning algorithm to Play Flappy Bird."
modified: 2017-04-26T14:17:25-04:00
categories: article
tags: [artificial intelligence, deep learning, reinforcement learning, computer vision]
comments: true
share: true
image:
  teaser: /images/articles/2017-04-26-Flappy-Bird-AI/flappybird_teaser.png
---

### Preface

Although I am a beginner to Deep Reinforcement Learning, I have a strong feeling that many details in one learning program on a certain task could be applied to another learning program on a different task. These details include the implementation of algorithms, the tuning of the parameters, the construction of input data, and the way of optimization, under different circumstances of the problems. Therefore, I think it is necessary to keep these intuitions and "discoveries" somewhere, because human brain tends to forget things and becomes confused if things are overwelming.

### Introduction

Deep Q-Learning has been widely used to play video games. I firstly noticed this application in some blogs, including [Ben Lau's blog](https://yanpanlau.github.io/2016/07/10/FlappyBird-Keras.html) and [songrotek's blog](http://blog.csdn.net/songrotek/article/details/50580904). Although these two people were not the very first authors implementing Deep Q-Learning to the Flappy Bird game, they improved the implementation to some extent. Ben Lau employed Keras library to implement neural network, which makes code easy to understand. Songrotek, though did not use Keras library, wrapped the learning algorithm to class object, which makes it convenience to study other general Deep Q-Learning problems. After reading their blogs and codes, I became very interested in this application and wanted to implement Deep Q-Learning on this game by myself after learning sufficient theories from the Udacity Machine Learning Nanodegree courses. (Strictly speaking, my very first Deep Q-Learning project was the smartcab project from the Udacity Machine Learning Nanodegree courses. It might be a good project for beginners, however, it is a little bit problematic regarding the concept of Q-Learning, and of hardly any realistic usages.) The overall implementation of Deep Q-Learning on the Flappy Bird game was following the two blogers' implementations I mentioned above. However, I combined both of their advantages and wrote a Deep Q-Learning algorithm that uses Keras library and was wrapped in class object. In addition to this, I also used some tricks in my own implementation to accelerate the training. 

<br />

![]({{ site.url }}/images/articles/2017-04-26-Flappy-Bird-AI/fb.jpg)

### Setting Up Deep Q-Learning Algorithm

#### Touch the Algorithm

The [NIPS 2013 Deep Q-Learning algorithm](https://www.cs.toronto.edu/~vmnih/docs/dqn.pdf) was implemented.

![]({{ site.url }}/images/articles/2017-04-26-Flappy-Bird-AI/NIPS_2013.png)

#### Input Image

The raw screenshot of the game requires to be preprocessed before send as input to the learning algorithm. The size of image matters a lot for the training efficiency and performance. Ben Lau and songrotek used 80 x 80 images as input. However, this did not retain the original height/width ratio of the raw image. So I changed it to 72 x 40, which matches the original height/width ratio. This might also reduce the calculation task to the computer to some extent.

<br />

The Flappy Bird game API used black background, which makes us convenient to manipulate image using OpenCV to maximize the contrast between bird, background, and the barriers. It might be a good habit to always check the preprocessed image using your bare eye. If your bare eye cannot distinguish things from the preprocessed images, the chance that the computer would do a good job on it might be low.

<br />

Game state frame determines how many frames of images are stacked together. Here, game_state_frame = 4. This means that 3 processing images and the current images are stacked into one single image, and are sent as input to the learning algorithm. Because in many games, the optimal actions to take is not only dependent on the current image. One may consider stacking of proceeding images together with the current image as a short video. The human and computer are using video, not single frame image, to determine the optimal actions.

#### Tuning of Hyperparameters

Learning rate is always important for the learning tasks. To tune the learning rate, I usually print the loss and Q-values on the screen during the training. If the learning rate is too high, the loss and Q-values will blow up in a short period of time.

#### Convolutional Neural Network (CNN)

Because I only have a desktop with Intel i7-6700 CPU and no graphic cards, I decided to use smaller CNN in the algorithm. It turned out that a smaller CNN worked very well for this game (probably because the game is simple). There is no need to use larger CNN unless you have sufficient computation resources.

### Improvement of Training

One of the key aspect of implementing Q-Learning is that the learning algorithm should learning different states as many as possible during the exploration stage. However, when I firstly started training, I found the bird always goes up and hit the barrier, which leads to a extremely poor training of algorithm. This is because the action the bird takes during the exploration stage is uniformly random between "flap" and "idle". Once the bird "flaps", it flies highier. The bird takes action at each frame, so it is almost garanteed the bird will goes up to the highest position and hit the barrier. To overcome this problem, I firstly tried to set the actions_per_frame from 1 to 3. This significantly increases the variety of bird flying during the exploration stage. However, the shortcoming of doing this is that the bird action frequence was limited. The bird might not be able to make actions in a state where it has to do something. Then I came up with another idea. I changed the uniform distribution between "flap" and "idle" making them uneven. I set the "flap" probability to 0.2 and the "idle" probability to 0.8, and it completely solves the problem. I am not sure if Ben Lau and songrotek has met such problems and if such problems could be overcomed by training with extremely long time. (It might be true because Ben Lau mentioned in his blog that he had to train millions of frames before the bird could actually fly well)

### Algorithm Performance

![]({{ site.url }}/images/articles/2017-04-26-Flappy-Bird-AI/flappy_bird_AI.gif)

<br />

The whole training took roughly 600,000 game frames in 36 hours, and the trained bird would never hit the barriers. It should also be noted that after training with 300,000 game frames, the bird started to fly reasonably, passing 0 to 100 barries in one single trial. 

### Links to GitHub

<https://github.com/leimao/Flappy_Bird_AI>