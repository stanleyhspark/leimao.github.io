---
layout: post
title: "Siamese Network on MNIST Dataset"
excerpt: "An introduction to Siamese Network and its implementation on MNIST dataset"
modified: 2017-09-14T14:17:25-04:00
categories: article
tags: [deep learning, siamese network]
comments: true
share: true
image:
  teaser: /images/articles/2017-10-30-Siamese-Network-MNIST/siamese_network.png
---



In progress.

### Introduction

Siamese Network is a semi-supervised learning network which produce the embeding feature representation for the input. By introducing multiple input channels in the network and appropriate loss functions, the Siamese Network is able to learn to represent similar inputs with similar embeding features, and epresent different inputs with different embeding features.

<br />

Usually, the embeding feature is a high dimensional vector. The similarity of the embeding features is usually represented by the Euclidean distance in the high dimensional space.

<br />

Here is a typical Siamese Network with two input channels. The two identical sister networks, which are Convolutional Neural Networks (CNN) in this case, share the same weights. In addition to CNN, the architecture generally could be any neural networks. It should be noted that the two sister networks could be of the same or different architecture.  Even if the two sister networks are of the same architecture, they do not have to share weights but use distinct weights. Usually, if the inputs are of different "type", the sister networks usually use different architectures, or use distinct weights for the same architecture.

<div class = "titled-image">
<figure class = "titled-image">
    <img src = "{{ site.url }}/images/articles/2017-10-30-Siamese-Network-MNIST/siamese_example.png">
    <figcaption>Siamese Network</figcaption>
</figure>
</div>

The two statue images were input into the two channels of the Siamese Network. The L2 distance (Euclidean distance) of the outputs of the two channels were calculated and subjected to minimizing the loss function $$l(x_1, x_2, \delta)$$.

http://hi.cs.waseda.ac.jp/~esimo/en/research/deepdesc/ 


I will first give an example of Siamese Network implementation using identical architectures with shared weights for the sister networks. Followed by an more complex example using different architectures or different weights with the same architecture.