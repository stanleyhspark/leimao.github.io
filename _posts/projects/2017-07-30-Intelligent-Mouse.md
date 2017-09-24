---
layout: post
title: Intelligent Mouse
excerpt: "Maze Explorer and Maze Solver"
modified: 2017-07-30T14:17:25-04:00
categories: project
tags: [Artificial Intelligence]
image:
  teaser: /images/projects/2017-07-30-Intelligent-Mouse/micromouse_teaser.jpg
comments: true
share: true
---

### Introduction

[Micromouse](https://en.wikipedia.org/wiki/Micromouse) is a contest where small robot mice (micromouse) solve a maze. It is very popular in US, UK and Japan among the young juniors who are interested in designing robots and programming artificial intelligence. In Micromouse contest, the players are going to test their micromouse to solve the maze. 
The project goal is to design a micromouse that could explore and find destination efficiently in the virtual maze.

<br />

Here is a demo of a real micromouse contest.
<iframe width="560" height="315" src="https://www.youtube.com/embed/CLwICJKV4dw" frameborder="0" allowfullscreen></iframe>

A maze solver algorithm and a maze explorer algorithm were developed for micromouse using real-time dynamic programming. Equipped with such algorithms, the micromouse shows extremely potent ability in maze exploration optimal route planning.

### Source Codes

All the Python source codes could be downloaded from my [GitHub](https://github.com/leimao/Intelligent_Mouse).

<br />

The codes for the project includes the following files:
- maze.py   
  This script contains functions for constructing the maze objects.
- mouse.py  
  This script establishes the micromouse class controlling the actions of miromouse.
- observer.py
  This script contains some functions for micromouse movement visualization.
- planner.py
  This script contains the functions that decide micromouse's actions.
- showmaze.py
  This script can be used to create a visual demonstration of what a maze looks like.
  To run showmaze.py, run the following command in the shell:
  {% highlight shell %}python showmaze.py test_maze_01.txt{% endhighlight %}
- showmouse.py
  This script can be used to create a visual demonstration of how micromouse is exploring and solving the maze.
  To run showmouse.py, run the following command in the shell:
  {% highlight shell %}python showmouse.py test_maze_01.txt complete{% endhighlight %}
  {% highlight shell %}python showmouse.py test_maze_01.txt incomplete{% endhighlight %}
  where "complete" and "incomplete" designate the strategy of micromouse.
  Please also remember to hit "Enter" once in the shell to start the micromouse
- showplanner.py
  This script can be used to create a visual demonstration of the optimal actions of micromouse in the maze.
  To run showplanner.py, run the following command in the shell:
  {% highlight shell %}python showplanner.py test_maze_01.txt{% endhighlight %}
- test.py
  This script allows you to test your micromouse in different modes on different mazes.
  To run test.py, run the following command in the shell:
  {% highlight shell %}python test.py test_maze_01.txt{% endhighlight %}
  
The script uses the turtle module to visualize the maze; you can click on the window with the visualization after drawing is complete to close the window. 
To allow more changes to the micromouse, the scripts can be modified accordingly.

## Simulation Results

Watch the micromouse exploring and solving the maze on [YouTube](https://www.youtube.com/playlist?list=PLVLJFoX8B37F6t81x2bK_Pe86TU2txIFn).

<br />

Here is one of the demos showing the virtual micromouse explores and solves the virtual maze.
<iframe width="560" height="315" src="https://www.youtube.com/embed/8DZaQ8hyT10?list=PLVLJFoX8B37F6t81x2bK_Pe86TU2txIFn" frameborder="0" allowfullscreen></iframe>
