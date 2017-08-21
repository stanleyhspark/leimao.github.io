---
layout: post
title: "Backpropagation Through Max-Pooling Layer"
excerpt: "Ever Think of Backpropagation Through Max-Pooling Layer?"
modified: 2017-08-21T14:17:25-04:00
categories: blog
tags: [Math, Deep Learning]
comments: true
share: true
---

I have once come up with a question "how do we do backpropagation through max-pooling layer?". I have studied deep learning throughly, and implemented many deep learning algorithms. However, I was not sure about the answer to this question.

<br />

After checking on [StackExchange](https://datascience.stackexchange.com/questions/11699/backprop-through-max-pooling-layers), I found the short answer is "there is no gradient with respect to non maximum values".

<br />

I also maintained a copy of the mathematical derivation from StackExchange below. It is well illustrated and simple to understand.

<br />

So suppose you have a layer P which comes on top of a layer PR. Then the forward pass will be something like this:

<br />

$P_i = f(\sum_j W_{ij} PR_j)$,

<br />

where $P_i$ is the activation of the ith neuron of the layer P, $f$ is the activation function and W are the weights. So if you derive that, by the chain rule you get that the gradients flow as follows: 

<br />

$grad(PR_j) = \sum_i grad(P_i) f^\prime W_{ij}$.

<br />

But now, if you have max pooling,  $f = id$ for the max neuron and $f = 0$ for all other neurons, so $f^\prime = 1$ for the max neuron in the previous layer and $f^\prime = 0$ for all other neurons. So:

<br />

$grad(PR_{max\ neuron}) = \sum_i grad(P_i) W_{i\ {max\ neuron}}$,

<br />

$grad(PR_{others}) = 0$.