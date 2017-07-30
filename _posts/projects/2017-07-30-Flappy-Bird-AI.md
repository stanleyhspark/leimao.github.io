---
layout: post
title: Flappy Bird Game AI
excerpt: "Artificial Intelligence Playing Flappy Bird Game"
modified: 2017-07-30T14:17:25-04:00
categories: project
tags: [Artificial Intelligence]
image:
  feature: site_logos/Logo Umbrella_Corporation.png
  credit: 
  creditlink: 
comments: true
share: true
---

### Introduction

[Flappy Bird](https://en.wikipedia.org/wiki/Flappy_bird) is a very popular video game. Here I developed an AI to play Flappy Bird using Deep Q-Learning. 

The AI takes the real-time game image output as input. It was able to play Flappy Bird extremely well. It could play the game endlessly without failure, which might be considered "perfect".

Here is a demo showing the AI playing the Flappy Bird game.
![](https://github.com/leimao/Flappy_Bird_AI/blob/master/flappy_bird_AI.gif)

## Installation Dependence

* Python 2.7
* Tensorflow 1.0
* Keras 2.0.3
* Pygame 1.9.3
* OpenCV 2.4.13

## AI Features

The Flappy Bird AI was developed using Deep Convolutional Q-Learning Neural Network. 

The AI program was written in Python using Keras, which makes the code for neural network neat and easy to understand.

The AI was wrapped as class, which makes it universal for all different kind of easy video game APIs.

Some tricks, which accelerates the training efficiency and performance, were used in AI training. These tricks were not observed in other Flappy Bird AIs developed using Deep Convolutional Q-Learning Neural Network.

## Run AI in Flappy Bird

The AI needs to be trained before the game. To train the AI, run the command "python FlappyBird_AI.py -m train". The AI has already been trained and stored as AI_model.h5 file if you do not want to do the training.

In case of a break during the training, one can resume the training by running the command "python FlappyBird_AI.py -m resume".

To allow the trained AI to play the game, run the command "python FlappyBird_AI.py -m test".

## Optimization Notes

The training took roughly 600,000 game frames in 36 hours on a desktop with Intel i7-6700 CPU under the parameters I specified. 

Using latest GPU could accelerate the training, but I just could not afford one.

<https://leimao.github.io/journal/Flappy-Bird-AI.html>

## Disclaimer

This work was developed based on the previous works published on GitHub:

<https://github.com/yanpanlau/Keras-FlappyBird>

<https://github.com/songrotek/DRL-FlappyBird>