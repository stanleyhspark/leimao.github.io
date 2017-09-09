---
layout: post
title: "Vehicle Localization on Satellite Images via Learning Embeddings"
excerpt: "Learning Embedded Features of Paired Images in Deep Learning"
modified: 2017-09-08T14:17:25-04:00
categories: reading
tags: [Deep Learning, Computer Vision]
comments: true
share: true
---

### Introduction

Following the "Accurate Vision-based Vehicle Localization using Satellite Imagery" paper published in 2015 from Matthew Walter's group at Toyota Technological Institute at Chicago (TTIC), Matthew Walter's group published another paper titled "Satellite Image-based Localization via Learned Embeddings" on the same top using deep learning in 2017. The paper could be downloaded [here](https://github.com/leimao/Deep_Learning_Papers/raw/master/Computer_Vision/2017_Vehicle_Localization_on_Satellite_Images_via_Learning_Embeddings/2017_Vehicle_Localization_on_Satellite_Images_via_Learning_Embeddings.pdf), and my annotated paper could be downloaded [here](https://github.com/leimao/Deep_Learning_Papers/raw/master/Computer_Vision/2017_Vehicle_Localization_on_Satellite_Images_via_Learning_Embeddings/2017_Vehicle_Localization_on_Satellite_Images_via_Learning_Embeddings_annotated.pdf).

<br />

I commented on the 2015 paper several days ago suggesting that deep learning may be a much better technique solving the problem with fewer limitation and restrictions. The 2017 paper did present me a good deep learning approach solving the problem.

<br />

Unlike the old algorithm published in the 2015 paper, the new algorithm published in 2017 paper is a more generalized algorithm. In the old algorithm, the vehicle could only be localized in the area where it has visited, and the correspondence between ground image and satellite image has been built. In the new algorithm, the vehicle localization could also be achieved in unvisited area given the satellite image is provided, making it extremely useful for the general purposes. 

<br />

### New Algorithm

#### Overall

The whole algorithm consists basically two parts:
1. In the training stage, learning the embedded features of ground image and satellite images, respectively.
2. In the testing stage, apply particle filtering, and calculate embedded features for both ground images and satellite images, to find out the most probable pose (location and orientation) of the vehicle.

#### Learning Embedded Features

The concept of learning embedded features for ground image and satellite images are very simple. Basically the ground images and satellite images were put into the a paired convolutional neural network (Siamese Network), output the embedded feature vectors for both images and the difference between the two embedded feature vectors (Euclidean distance). Using a smart loss function, the neural network could learn to have similar embeded feature vectors for paired ground image and satellite image, and have distinct embedded feature vectors for unpaired ground image and satellite image. So when new ground image and satellite image come, if their embedded feature vectors output from the neural network is similar, they are very like to be paired.

<figure>
  <img src="{{ site.url }}/images/readings/2017-09-08-2017-Deep-Learning-Vehicle-Localization-Satellite-Image/siamese_network_CNN_embeddings.png"/>
</figure>

Their are some minor details in the implementation:
* Combine mid-level and high-level features because mid-level features tend to be invariant to illuminations, weathers, and seasons. (I learned it today)
* Using separate parameters for the paired convolutional neural networks seems work better.

#### Particle Filtering

I honestly have not heared of particle filtering before. But when I was reading the paper, I felt that it is like the Monte Carlo statistical inference procedures. I briefly checked it on Wikipedia. It is also called Sequential Monte Carlo (SMC) simulations. With a sequence of ground images, a lot of vehicle pose candidates proposed, and their corresponding embedded feature vectors, the system is likely to converge and find out the most probable pose for the vehicle. The result of particle filtering is as follows. The blue circles in the satellite image indicates the vehicle locations after particle filtering simulation. The bigger circle indicates the average of all the vehicle locations.

<figure>
  <img src="{{ site.url }}/images/readings/2017-09-08-2017-Deep-Learning-Vehicle-Localization-Satellite-Image/particle_filtering.png"/>
</figure>

I think I will make up more details when I learn particle filtering in the future. But I am quite sure that for the general idea I am correct.

### Closure

This is a great application of deep learning in generalized vehicle localization in satellite map. After sufficient training, the vehicle could be localized in any satellite map even if it has never visit it before. Once for all. So Brilliant.