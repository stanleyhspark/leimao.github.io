---
layout: post
title: "Google DeepDream in Python"
excerpt: "Digital Art is Soooooo Cool! Learning to Become an Amatuer Digital Artist."
modified: 2017-09-14T14:17:25-04:00
categories: article
tags: [deep learning]
comments: true
share: true
image:
  teaser: /images/articles/2017-09-14-Google-DeepDream-Python/deepdream.jpg
---

I had been learning painting for more than six years during my childhood. But later this hobby vanished due to the heavy coursework in middle school. Since last year, digital art, a new form of modern art, has drawn my attention. Among digital art, it is the digital painting that currently attracts my attention most. Using machine learning, deep learning in particular, one is able to generate images of certain object from the model, or change the style of the image. I have seen many such images. Some of these images are just too unrealistic that ordinary people may have difficulties to understand them. For example, [DeepArt](https://deepart.io/) allows your to "Vanghogify" your image by applying different "Van Gogh style filters". But most of the images generated are not really my personal flavor (Maybe I just don't understand Van Gogh). But there is also chance that you can see digital images that are just brilliant and making sense! I got a chance to see a [blog post](https://www.boredpanda.com/inceptionism-neural-network-deep-dream-art/). In this blog post, the author presented images that basically change the style of one image to another using [Ostagram](http://www.ostagram.ru/static_pages/lenta?last_days=30), an image tool developed based on Google DeepDream. This may seem similar to DeepArt, but it was not only restricted to Van Gogh style. 

<br />

Here I will show an image that I generated using Ostagram. The two input images are shown below. The left one is the image you want to modify. The right one is the image filter you want to apply. Here I chose Chicage as the image that I want to modify, and Stormwind as the image filter. Basically I want the Chicago city looks like Stormwind.

<figure class = "titled-image">
    <img src = "{{ site.url }}/images/articles/2017-09-14-Google-DeepDream-Python/chicago.jpg">
    <figcaption>Chicago in the United States of America</figcaption>
</figure>

<figure class = "titled-image">
    <img src = "{{ site.url }}/images/articles/2017-09-14-Google-DeepDream-Python/stormwind.jpg">
    <figcaption>Stormwind in World of Warcraft</figcaption>
</figure>

After "merging", the Chicago city now looks like the image below. Overall, the Chicago city now looks very Stormwind-styled. All the building are now made up of big rocks. The trees also look like the trees in Stormwind. The only big error is that the neural network treats the cloud in Chicago as the wall of buildings. So the cloud looks like big rock to some extent.

<figure class = "titled-image">
    <img src = "{{ site.url }}/images/articles/2017-09-14-Google-DeepDream-Python/chicago-stormwind.jpg">
    <figcaption>Stormwind-styled Chicago</figcaption>
</figure>

I was so fascinated with it, and I really wanted to implement the algorithm and do some personalized fun stuff using Google DeepDream on my own!

<br />

Google DeepDream is a pre-trained neural network that is avaible to extract features of the image at different levels. By using this pre-trained neural network, one could easily make digital art on local machines without relying on web applications. Because the neural network is pre-trained, the computation cost on local machines will be extremely low. I think an ordinary $500 computer even without a graphical card could easily do this.

<br />

There are some online learning resources of using Google DeepDream to make your own digital art.

* [Google Official DeepDream Tutorial in TensorFlow](https://github.com/tensorflow/tensorflow/blob/master/tensorflow/examples/tutorials/deepdream/deepdream.ipynb) 

* [Siraj Raval's Video Tutorial](https://www.youtube.com/watch?v=MrBzgvUNr4w) (I know this guy from Udacity by the way -_-)
