---
layout: post
title: "Google DeepDream in Python"
excerpt: "Digital art is soooooo cool! Learning to become an amatuer digital artist."
modified: 2017-09-14T14:17:25-04:00
categories: article
tags: [deep learning]
comments: true
share: true
image:
  teaser: /images/articles/2017-09-14-Google-DeepDream-Python/deepdream.jpg
---

### Introduction

I had been learning painting for more than six years during my childhood. But later this hobby ceased due to the heavy coursework in middle school. Since last year, digital art, a new form of modern art, has drawn my attention. Among digital art, it is the digital painting that currently attracts me the most. Using machine learning, deep learning in particular, one is able to generate images of certain object, or change the style of the image. 

<br />

I have seen many such images. Some of these images are just too unrealistic that ordinary people may have difficulties to understand them. For example, [DeepArt](https://deepart.io/) allows your to "Vanghogify" your image by applying different "Van Gogh style filters". But most of the images generated are not really my personal flavor (Maybe I just don't understand Van Gogh). But there is also chance that you can see digital images that are just brilliant and making sense! I got a chance to see a [blog post](https://www.boredpanda.com/inceptionism-neural-network-deep-dream-art/). In this blog post, the author presented images that basically change the style of one image to another using [Ostagram](http://www.ostagram.ru/static_pages/lenta?last_days=30), an image tool developed based on Google DeepDream. This may seem similar to DeepArt, but it was not only restricted to Van Gogh style. 

### Examples

Here I will show an image that I generated using Ostagram. The two input images are shown below. The left one is the image you want to modify. The right one is the image filter you want to apply. Here I chose Chicage as the image that I want to modify, and Stormwind as the image filter. Basically I want the Chicago city looks like Stormwind.

<div class = "titled-image">
<figure class = "titled-image">
    <img src = "{{ site.url }}/images/articles/2017-09-14-Google-DeepDream-Python/chicago.jpg">
    <figcaption>Chicago in the United States of America</figcaption>
</figure>
</div>
<div class = "titled-image">
<figure class = "titled-image">
    <img src = "{{ site.url }}/images/articles/2017-09-14-Google-DeepDream-Python/stormwind.jpg">
    <figcaption>Stormwind in World of Warcraft</figcaption>
</figure>
</div>
After "merging", the Chicago city now looks like the image below. Overall, the Chicago city now looks very Stormwind-styled. All the building are now made up of big rocks. The trees also look like the trees in Stormwind. The only big error is that the neural network treats the cloud in Chicago as the wall of buildings. So the cloud looks like big rock to some extent.
<div class = "titled-image">
<figure class = "titled-image">
    <img src = "{{ site.url }}/images/articles/2017-09-14-Google-DeepDream-Python/chicago-stormwind.jpg">
    <figcaption>Stormwind-styled Chicago</figcaption>
</figure>
</div>
I was so fascinated with it, and I really wanted to implement the algorithm and do some personalized fun stuff using Google DeepDream on my own!

### Learning Materials

Google DeepDream is a pre-trained neural network that is avaible to extract features of the image at different levels. By using this pre-trained neural network, one could easily make digital art on local machines without relying on web applications. Because the neural network is pre-trained, the number variables (i.e. the image size) we are optimizing is relatively smaller, the number of iterations we apply during optimization is small, and we have good algorithms, so the computation cost on local machines will be extremely low. I believe an ordinary $500 computer even without a graphical card could easily do this.

<br />

There are some online learning resources of using Google DeepDream to make your own digital art.

* [Google Official DeepDream Tutorial in Caffe](https://github.com/google/deepdream/blob/master/dream.ipynb)
([Download]({{ site.url }}/downloads/articles/2017-09-14-Google-DeepDream-Python/dream.ipynb))
* [Google Official DeepDream Tutorial in TensorFlow](https://github.com/tensorflow/tensorflow/blob/master/tensorflow/examples/tutorials/deepdream/deepdream.ipynb)
([Download]({{ site.url }}/downloads/articles/2017-09-14-Google-DeepDream-Python/deepdream.ipynb))
* [Google Research Blog](https://research.googleblog.com/2015/06/inceptionism-going-deeper-into-neural.html)
* [Siraj Raval's Video Tutorial](https://www.youtube.com/watch?v=MrBzgvUNr4w) (I know this guy from Udacity by the way -_-)
* [Siraj Raval's Code](https://github.com/llSourcell/deep_dream_challenge/blob/master/deep_dream.py)
([Download]({{ site.url }}/downloads/articles/2017-09-14-Google-DeepDream-Python/deep_dream.py))

### Basic Principles

Basically what these algorithms are doing to modify images is applying particular patterns that the neural network has learned to the image. Google DeepDream was trained to classify 1,000 objects and contains rich pattern information in each layer. To render these patterns, you can input a blank image with some noise to the initial neural layer of the network, and apply gradient ascent to maximize the sum of activations in a particular neural layer (for several iterations, since too many iteration will like make the image irrelavant). Similarly, to render certain neural network learned patterns in your specified image, you have to firstly decide which neural layer, which matches certain pattern, you will use, then input the image of interest to the initial neural layer, and apply gradient ascent to maximize the sum of activations in the neural layer desired. I think is what DeepArt is doing to "Vanghogify" images.

<br />

Further, to render user-defined patterns in your specified image, you have to change the optimization objective. You firstly input the pattern-containing "guide image" you specified to the neural network and you can extract the features of this guide image in different layers. Then you input the image that you want to modifiy to the neural network, you calculate the dot product of the features of the image and the corresponding guide image features in the same layer for each layer, find the layer that have the best match (highest dot product), and apply gradient descent to maximize the dot product in that layer (for several iterations). 

### Tricks

When the image you want to modify is high-resolution, meaning that the number of variable we are optimizing simutaneously is also large, this will result in the consumption of all the computation resource and memory that you have. To overcome this situation, a good strategy is to calculate the gradient by tile. But it seems that this will result in an image containing significant tile boundaries. So these smart guys thinks of applying random shifts to the image before every iteration helps avoid tile boundaries and improves the overall image quality. I looked at the code and understand how they did, but I think I have a little bit difficulty to understand why it will work. Intuitively I believe this will work, mathematically my scratches were not profound.

<br />

"Octaves" were also used in generating the pattern in the images and the concept of "octave" was briefly introduced in Siraj's video. Basically, you make the original image you want to modify smaller using interploation, followed the iterations to generate details by gradient ascent, resize the image larger using interploation, and use the larger image to generate more details by gradient ascent. I am not sure without this trick how the image looks like. I may investigate this in the future if I get chance.
