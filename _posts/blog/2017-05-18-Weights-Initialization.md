---
layout: post
title: Mathematical Logics Behind The Weights Initialization
excerpt: "Understand why we initialize the weights in this way."
modified: 2017-05-18T14:17:25-04:00
categories: blog
tags: [Math, Machine Learning]
comments: true
share: true
---

### Motivation

When I was working on machine learning tasks, I used to initialize the weights in my model by the default settings of the machine learning too, because I "trust" the "intelligent tool" could always provide the best solution to this. This often worked very well, and I did not spend too much time to understand what the tool did and why it did so.

### Why the weights initialization is important?

Think of logistic regression. Let us have an extreme case, if weights are badly chosen so that the linear additive output to activation function is extremely large or small. From the curve of logistic regression, we immediately know that the derivatives of logistic regression when x is very large or small is extremely small.

![]({{ site.url }}/images/blog/2017-05-18-Weights-Initialization/Logistic-curve.svg)

When we are updating the weights in our final output layer or middle hidden layers using backpropagation, the derivative of the weights always contain the an item of the derivative of activation funtion at certain hidden nodes (You may check my [blog](https://leimao.github.io/blog/Programmable-Backpropagation/), [Multi-layer Perceptron on Wikipedia](https://en.wikipedia.org/wiki/Multilayer_perceptron) or any machine learning text books). If this derivative is very small, the learning of the weights would be extremely slow. It should be noted that this might not be totally overcomed by making learning rate bigger, because the big learning rate might be disasturous when some of the weights whose hidden nodes in the right range could be normally updated. Some logistic regression equation have \\(\beta\\) term (\\(g(x) = \frac{1}{1+\exp(-{\beta}x)}\\)), this term is the same to learning rate (You may see it after calculating the derivative of logistic regression by yourself).

<br />

Therefore, setting up the right weights is very important.

### Mathematics behind the weights initialization

I often saw a "gold solution" of the weights initialization on the internet, which states that "a good idea to choose initial weights of a neural network ramdonly from the range \\([-\frac{1}{\sqrt{n}}, \frac{1}{\sqrt{n}}]\\)", where n is the number of hidden nodes in the input layer. 

<br />

Under the assumption "the inputs are normalized to have mean of 0 and variance (standard deviation^2) of 1", the sum of the linear addition of all the outputs from the same layer before activation would have mean of 0 and variance of \\(\frac{1}{3}\\). At this range, the value the derivative of activation function would be reasonable. So our learning efficiency would be good.

<br />

But how did we get this? 

<br />

For uncorrelated two ramdonly variables, \\(Var(X+Y) = Var(X) + Var(Y)\\), and \\(Var(XY) = Var(X)Var(Y)\\). This is always true if we have more variables (see [Variance Property on Wikipedia](https://en.wikipedia.org/wiki/Variance)). The variance of uniform distribution \\([-\frac{1}{\sqrt{n}}, \frac{1}{\sqrt{n}}]\\) is \\(\frac{1}{3n}\\) (see [Uniform Distribution Property on Wikipedia](https://en.wikipedia.org/wiki/Uniform_distribution_(continuous))). So the sum of the variances of all n nodes in the input layer would have a variance of \\(\frac{1}{3n}\times{n}=\frac{1}{3}\\). This sum also has mean of 0 (I think I do not have to explain this).

### Additional idea?

How about initialize all the weights to zero?

<br />

Unfortunately, according to the backpropagation derivative update functions, there would be no update for any of the weights in the hidden layers but not the final output layer (You may check my [blog](https://leimao.github.io/blog/Programmable-Backpropagation/), [Multi-layer Perceptron on Wikipedia](https://en.wikipedia.org/wiki/Multilayer_perceptron) or any machine learning text books). You would only end up with a "single-layer" linear model that performs very bad.

