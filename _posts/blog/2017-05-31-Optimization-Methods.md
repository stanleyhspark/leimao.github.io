---
layout: post
title: Introduction to Ordinary Optimization Methods - To be Continued
excerpt: "Understand different optimization methods and become rational when we have to choose one of them."
modified: 2017-05-31T14:17:25-04:00
categories: blog
tags: [Math, Machine Learning]
comments: true
share: true
---

### Motivation

When I was working on optimization problems in machine learning tasks, I needed to select optimizer if I was using machine learning libraries such as scikit and tensorflow. Some common optimizers that we often see are stochastic gradient descent (SGD), Adam, momentum, etc. Somehow, I often used Adam optimizer and it always worked very well. I have some blurry ideas about how some of the optimizers, such as SGD and momentum, work without going into mathematical details. And I honestly do not know how to choose optimizer rationally given a certain problem. So it is often necessary to understand how the math works behind these optimization algorithms.

### Gradient Descent


### Newton Method

It is also called "Second Order" optimization methods. It uses Taylor Expansion upto the second order to approximate the target function. It should be noted that if we do Taylor Expansion approximation only upto the first order, the get the ordinary gradient descent method.

<br />

This method converges much faster than gradient descent because unlike ordinary gradient descent it can better foresee the local maximum or minimum when we are computing the gradients. However, the sacrifice is that the computation cost for the gradients, especially when the dimension of the data (number of features in the data) becomes larger, becomes much higher. Therefore, I actually hardly see this optimization method in solving machine learning tasks.

<br />

The mathmatical details of the Newton method for 1 variable and multiple variables could be found to this [article]({{ site.url }}/downloads/blog/2017-05-31-Optimization-Methods/newtonfull.pdf). You may also check the Wikipedia about the [Newton method](https://en.wikipedia.org/wiki/Newton%27s_method_in_optimization).

<br />

![]({{ site.url }}/images/blog/2017-05-31-Optimization-Methods/256px-Newton_optimization_vs_grad_descent.svg.png)

<br />

Newton Method (red) vs Gradient Descent (green)
