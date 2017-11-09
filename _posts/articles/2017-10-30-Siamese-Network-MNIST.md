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

Usually, the embeding feature is a high dimensional vector. The similarity of the embeding features is usually represented by the Euclidean distance in the high dimensional space.

Here is a typical Siamese Network with two input channels. The two identical sister networks shares the same weights. It should be noted that the two sister networks could be of the same or different architecture. Even if the two sister networks are of the same architecture, they do not have to share weights and use distinct weights. Usually, if the inputs are of different "type", the sister networks usually use distinct weights even if the architectures are the same.

<div class = "titled-image">
<figure class = "titled-image">
    <img src = "{{ site.url }}/images/articles/2017-10-30-Siamese-Network-MNIST/siamese_example.jpeg">
    <figcaption>Siamese Network</figcaption>
</figure>
</div>

I will first give an example