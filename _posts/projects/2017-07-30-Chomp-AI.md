---
layout: post
title: Chomp Game AI
excerpt: "Extremely Potent Chomp Game AI"
modified: 2017-07-30T14:17:25-04:00
categories: project
tags: [Artificial Intelligence]
image:
  teaser: /images/projects/2017-07-30-Chomp-AI/chomp_demo.png
comments: true
share: true
---

### Introduction

Chomp is a two-player strategy game played on a rectangular chocolate bar made up of smaller square blocks (cells). The players take it in turns to choose one block and "eat it" (remove from the board), together with those that are below it and to its right. The top left block is "poisoned" and the player who eats this loses.

<br />

The following image shows the basic rule of "eating" in Chomp.
<center><img width="480" height="480" src="{{ site.url }}/images/projects/2017-07-30-Chomp-AI/chomp_demo.png"/></center>

<br />

Chomp is actually a classic discrete mathematics problem. The player goes first was proved that it always have winning strategy, although the winning strategy might not be easily explicitly specified.

<br />

The purpose of the project is to develop a potent AI that can give explicit winning strategy during the game.

### Run the Game

The Chomp was developed using Python and PyGame. The player needs to install Python 2.7, Numpy and PyGame in order to run the game. The Python source code of the game and the AI can be downloaded from my [GitHub](https://github.com/leimao/Chomp_AI).

<br />

To install PyGame, it is extremely easy if you are using pip, simply run "pip install pygame" in the terminal.

<br />

To run the Chomp game, run the command in termimal:
{% highlight shell %}
python chomp_gui.py x m n
{% endhighlight %}

'x' designates who goes first in the game. It can be either 'Human' or 'AI'. 'm' and 'n' are the width and height of the rectangle. 'm' and 'n' are the positive integers no larger than AI_limit. In this version, the AI_limit is 12.

<br />

Here is a demo of playing Chomp with the AI.

<iframe width="560" height="315" src="https://www.youtube.com/embed/N-rvv6LUJ1o" frameborder="0" allowfullscreen></iframe>

### About the AI

The data for winning strategy was actually pre-calculated and saved in file. The AI will use the data to design winning strategy during the game.

<br />

The AI is extremely potent that it is guaranteed to win if it goes first. It also has extremely high winning rate (nearly 100%) against human players (mostly my friends) if human players goes first, because human players will likely make mistake during the game. Once the human player makes a mistake even if the human player goes first, the AI guarantees to win.

<br />

The AI has its limit. Because it relies on the pre-calculated data, and the data was calculated for the board size no larger than AI_limit x AI_limit.

### Future Plan

It might be good idea to add an interface layer asking the user to input game parameters in the GUI.

<br />

The python game should also be compiled for the univeral usage in different systems without installing Python environment and libraries.

### Acknowledgment

I would like to thank my old colleague Guotu Li at Duke University for his smart function to calculate the total number of game states during AI development.

