---
layout: post
title: Simple Illustration of Programmable Backpropagation
excerpt: "We understand backpropagation. But why it is programmable?"
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

Backpropagation is always one of my knowledge weaknesses in machine learning. I have understood it many times. However, I always forgot how it really works but simply remember it is basically about chain rules. I clearly remember that Andrew Ng once joked he sometimes cannot remember how backpropagation works so he often had to understand backpropagation again before he gave lectures in machine learning courses. Even if I refresh my mind by reading some related materials, I never understood why such tedious and complicated calculus could be programmable in our machine learning tools when we are working on neural networks. 

If you know how to calculate \\(\frac{\partial{e}}{\partial{b}}\\) in the following figure, you basically know how to do backpropagation.

![](/images/blog/2017-05-17-Programmable-Backpropagation/tree-eval-derivs.png)

[Here](http://colah.github.io/posts/2015-08-Backprop/) is a very simple and good illustration about the backpropagation. However, these materials are often over-simplified. The network they provided are not even the ordinary neural network we are using nowadays. Not even mention including the activation functions. 

Here, I presented the workflow of backpropagation in a neat way so that people could easily figure out the programmable logic inside the derivations. It is extremely tedious to type equations in MathJax. So I finally chose to use Word and transform the file to pdf for you guys to download. 

You can download my simple illustration of programmable backpropagation [here](/downloads/blog/2017-05-17-Programmable-Backpropagation/backpropagation.pdf). 

Backpropagation was always like a black box when I was working on machine learning tasks. I hope this materials could always remind me the mechanism of backpropagation and the importance of mathematics in computer science.
