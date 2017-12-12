---
layout: post
title: Flappy Bird Game AI
excerpt: "Artificial Intelligence Playing Flappy Bird Game"
modified: 2017-07-30T14:17:25-04:00
categories: project
tags: [Artificial Intelligence]
image:
  teaser: /images/projects/2017-07-30-Flappy-Bird-AI/flappybird_teaser.png
comments: true
share: true
---

### Introduction

[Flappy Bird](https://en.wikipedia.org/wiki/Flappy_bird) is a very popular video game. Here I developed an AI to play Flappy Bird using Deep Q-Learning. 

<br />

The AI takes the real-time game image output as input. It was able to play Flappy Bird extremely well. It could play the game endlessly without failure, which might be considered "perfect".

<br />

Here is a demo showing the AI playing the Flappy Bird game.

<br />

<center><img width="240" height="240" src="{{ site.url }}/images/projects/2017-07-30-Flappy-Bird-AI/Flappy_Bird_gameplay.png"/></center>

### AI Features

The Flappy Bird AI was developed using Deep Convolutional Q-Learning Neural Network. It was written in Python using Keras, which makes the code for neural network neat and easy to understand. It was also wrapped as class, which makes it universal for all different kind of easy video game APIs.

<br />

Some tricks, which accelerates the training efficiency and performance, were used in AI training. These tricks were not observed in other Flappy Bird AIs developed using Deep Convolutional Q-Learning Neural Network.

### Installation and Dependence

All the Python source codes could be downloaded from my [GitHub](https://github.com/leimao/Flappy_Bird_AI).

<br />

To run the game and AI, the following dependences are required.
* Python 2.7
* Tensorflow 1.0
* Keras 2.0.3
* Pygame 1.9.3
* OpenCV 2.4.13

### Run AI to Play Flappy Bird

The AI needs to be trained before the game. To train the AI, run the command: 
{% highlight shell %}
python FlappyBird_AI.py -m train
{% endhighlight %}
The AI has already been trained and stored as AI_model.h5 file if you do not want to do the training.

In case of a break during the training, one can resume the training by running the command:
{% highlight shell %}
python FlappyBird_AI.py -m resume
{% endhighlight %}

To allow the trained AI to play the game, run the command:
{% highlight shell %}
python FlappyBird_AI.py -m test
{% endhighlight %}

### AI Demo

Here is a demo showing the AI playing the Flappy Bird game.

<br />

<center><img width="240" height="240" src="{{ site.url }}/images/projects/2017-07-30-Flappy-Bird-AI/flappy_bird_AI.gif"/></center>

