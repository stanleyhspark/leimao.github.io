---
layout: post
title: "Google DeepDream API"
excerpt: "Doing Digital Art in Google DeepDream API"
modified: 2017-09-20T14:17:25-04:00
categories: project
tags: [deep learning, digital art]
comments: true
share: true
image:
  teaser: /images/projects/2017-09-20-Google-DeepDream-API/pilatus800_deepdream.jpeg
---

### Introduction

The introduction of Google DeepDream and its application in digital art can be found in my article ["Google DeepDream in Python"](https://leimao.github.io/article/Google-DeepDream-Python/).

### Description

The development of this API is still in progress. More functions will be added in the future.

### Requirements

* Python 3.6

### Dependencies

* tensorflow 1.3
* numpy
* PIL
* os
* sys
* zipfile
* six
* argparse

### Usage

#### List the available layers and the number of channels

To check the available layer names and channel numbers for the deepdream program. 

<br />

**Input**

{% highlight shell %}
python deepdream_api.py -l
{% endhighlight %}

**Output**
{% highlight shell %}
import/conv2d0_pre_relu/conv 64
import/conv2d1_pre_relu/conv 64
import/conv2d2_pre_relu/conv 192
import/mixed3a_1x1_pre_relu/conv 64
import/mixed3a_3x3_bottleneck_pre_relu/conv 96
import/mixed3a_3x3_pre_relu/conv 128
import/mixed3a_5x5_bottleneck_pre_relu/conv 16
import/mixed3a_5x5_pre_relu/conv 32
import/mixed3a_pool_reduce_pre_relu/conv 32
import/mixed3b_1x1_pre_relu/conv 128
import/mixed3b_3x3_bottleneck_pre_relu/conv 128
import/mixed3b_3x3_pre_relu/conv 192
import/mixed3b_5x5_bottleneck_pre_relu/conv 32
...
{% endhighlight %}
In the output, the layer name is on the left, the number of channels in the layer is on the right.


#### Preview the feature pattern of the neural network

To preview the feature pattern learned in a certain channel of a certain layer in the neural network. This is helpful for the user to select layers and channels used for image modification.

<br />

**Input**

<br />

-p layer_name channel_number, --preview layer_name channel_number

{% highlight shell %}
python deepdream_api.py -p mixed4d_3x3_bottleneck_pre_relu 20 feature_pattern.jpeg
{% endhighlight %}

**Output**

<div class = "titled-image">
<figure>
    <img src = "{{ site.url }}/images/projects/2017-09-20-Google-DeepDream-API/feature_pattern.jpeg">
    <figcaption>Feature Pattern Learned in the Neural Layers</figcaption>
</figure>
</div>

#### Render the image with the features from the neural network

Apply feature pattern learned in a certain channel of a certain layer in the neural network to the image that the user provided.

<br />

**Input**

<br />

-r image_path layer_name channel_number, --render image_path layer_name channel_number

{% highlight shell %}
python deepdream_api.py -r inputs/pilatus800.jpg mixed4d_3x3_bottleneck_pre_relu 20 pilatus800_deepdream.jpeg
{% endhighlight %}

<div class = "titled-image">
<figure>
    <img src = "{{ site.url }}/images/projects/2017-09-20-Google-DeepDream-API/pilatus800.jpg">
</figure>
</div>

**Output**

<div class = "titled-image">
<figure>
    <img src = "{{ site.url }}/images/projects/2017-09-20-Google-DeepDream-API/pilatus800_deepdream.jpeg">
</figure>
</div>

### More Functions

In the [Google Official DeepDream Tutorial in TensorFlow](https://github.com/tensorflow/tensorflow/blob/master/tensorflow/examples/tutorials/deepdream/deepdream.ipynb), they introduced Laplacian Pyramid Gradient Normalization to boost the low frequencies of the gradient. I basically have no idea of what that is. So I did not implement this in my API.

<br />

I also tried to add the features from a guide image to customize the pattern. However, it seems that my understanding of the optimzation objective is not correct (see my post on [StackFlow](https://stackoverflow.com/questions/46324533/controlling-dreams-in-tensorflow)). Therefore, I will hold this until I totally resolve my confusions.

### References

* [Google Official DeepDream Tutorial in Caffe](https://github.com/google/deepdream/blob/master/dream.ipynb)
* [Google Official DeepDream Tutorial in TensorFlow](https://github.com/tensorflow/tensorflow/blob/master/tensorflow/examples/tutorials/deepdream/deepdream.ipynb)
* [Google Research Blog](https://research.googleblog.com/2015/06/inceptionism-going-deeper-into-neural.html)
* [Siraj Raval's Video Tutorial](https://www.youtube.com/watch?v=MrBzgvUNr4w)
* [Siraj Raval's Code](https://github.com/llSourcell/deep_dream_challenge/blob/master/deep_dream.py)

### Link to GitHub

[DeepDream](https://github.com/leimao/DeepDream)