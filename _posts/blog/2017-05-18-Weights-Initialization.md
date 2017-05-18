---
layout: post
title: Mathematical Logics Behind The Weights Initialization
excerpt: "Understand why we initialize the weights in this way."
modified: 2017-05-16T14:17:25-04:00
categories: blog
tags: [Math, Machine Learning]
image:
  feature: site_logos/Logo Umbrella_Corporation.png
  credit: 
  creditlink: 
comments: true
share: true
---

### Motivation

When I was working on machine learning tasks, I used to initialize the weights in my model by the default settings of the machine learning too, because I "trust" the "intelligent tool" could alway provide the best solution to this. This often worked very well, and I did not spend too much time to understand what the tool did and why it did so.

### Why the weights initialization is important?

Think of logistic regression. Let us have an extreme case, if weights are badly chosen so that the linear additive output to activation function is extremely large or small. From the curve of logistic regression, we immediately know that the derivatives of logistic regression when x is very large or small is very small.

![](/images/blog/2017-05-18-Weights-Initialization/Logistic-curve.svg)






### Mathematics behind the weights initialization

I often saw a "gold solution" of the weights initialization on the internet, which states that "a good idea to choose initial weights of a neural network ramdonly from the range \\([-\frac{1}{\sqrt{n}}, frac{1}{\sqrt{n}}]\\)". However, people often ignored that this comes with an assumption "the inputs are normalized to have mean of 0 and variance (standard deviation^2) of 1". In this way, the 

