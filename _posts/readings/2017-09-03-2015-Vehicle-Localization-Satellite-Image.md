---
layout: post
title: "Accurate Vehicle Localization via Satellite Images"
excerpt: "My Fisrt Reading on Sophisticated Computer Vision Problems"
modified: 2017-09-03T14:17:25-04:00
categories: reading
tags: [Computer Vision]
comments: true
share: true
---

I am still not sure which research path I should pursue if I am dedicated into deep learning. Is it computer vision, natural language processing, or reinforcement learning? So I tried to read some articles in these fields to get some more advanced ideas of these topics (Not basic ideas because I have done independently done elementary projects in all these tree fields).

<br />

The article I chose is titled "Accurate Vision-based Vehicle Localization using Satellite Imagery" from Matthew Walter's group at Toyota Technological Institute at Chicago (TTIC). I chose this one because TTIC is an independent institution geographically within the University of Chicago, and I am interested in his artificial intelligence and robotics research. The original article could be downloaded [here]({{ site.url }}/downloads/readings/2017-09-03-2015-Vehicle-Localization-Satellite-Image/1510.09171.pdf) and my annotated version could be downloaded [here]({{ site.url }}/downloads/readings/2017-09-03-2015-Vehicle-Localization-Satellite-Image/1510.09171_annotated.pdf).

<br />

I read through the whole article. I think I have questions regarding not only technical details but also its application significances.

<br />

The task described in the paper is complicated. Given a camera image from the vehicle, accurately determine its location on the satellite image. 

<br />

To do this, using the training dataset (camera image, the satellite image centered on the camera position), the authors tried to build the correlation between the camera image and the (local) satellite image. 

<br />

To do this, the author exacts features from these images. The features include RGB densities, edge potential and neural attributes. Although I have never done any edge potential and neural attributes work, it is easy to understand what they mean and how they could be derived. More importantly, probably to reduce the size of feature vectors, the authors regularily sampled points on the camera image and apply "stereo projection" to the points in the corresponding local satellite image. I have no idea how this is done but the author gave the reference to it. They sort of mentioned "depth learnining", making me wondering whether it is a machine learning problem or not. But this stereo projection was not discussed in detail in the paper. Only using these sampled feature pairs, the authors were able to build a "ground-satellite dictionary", in other words I think, a training dataset.

<br />

To build relations between the camera image and satellite image, the authors projected the ground image feature vectors and the satellite image feature vectors in the training dataset to another high-dimensional space, respectively. The authors then learn projection matrices for both projections so that the geographically close image vectors, and satellite images, are also close in the high dimensional space. To learn these two matrices, they proposed to solve the problem by analogy to ranking problems, which is brilliant.

<br />

Finally, given a new image (test data), they just have to slice the local satellite map along the available routes, do the same thing in the training stage, remove some unlikely candidates by depth clustering, use the learned matrices to do the projection, find out the closest ground/satellite image locations in the training sets for ground image and candidate satellite image respectively, find out the intersection. By a scoring function which contains the cardinality of the intersection and the distance of these location pairs, the algorithm could find out the location of ground image on the satellite map accurately. 

<br />

I was very surprised that this method could work much better than the bench mark models, because the method is complicated and contains a lot of sophisticated human engineering. Although it works well, I still have questions regarding its applications. From my understanding, in order to accurately locate the vehicle in the satellite map, the vehicle has to visit the much of the area in the satellite map and its location has to be accruately determined on the satellite map. If the car is in the area where the training dataset has no ground images in some vecinity, the location is never possible to be determined, because the correlation matrices might not have learned the correlation in these areas. It might be feasible if some company has the money and energy to explore all the world. But it is not possible for ordinary human drivers running in an less known city. The training data collection step raises my concern. 

<br />

Technically, the authors introduces a lot of non-linear sophisticated feature engineerings, some of which I never know. It might be possible to solve the problem using deep learning, which handles non-linear transformation well. The paper was published in 2015, and I am using my latest point of view in 2017. Not suprisingly, they published a new paper solving the same problem using deep learning in 2017. I think I will take a look at this paper soon.