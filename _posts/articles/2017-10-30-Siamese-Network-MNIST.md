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

Here is a typical Siamese Network with two input channels ([Deep Convolutional Feature Point Descriptors](http://hi.cs.waseda.ac.jp/~esimo/en/research/deepdesc/)). The two identical sister networks, which are Convolutional Neural Networks (CNN) in this case, share the same weights. In addition to CNN, the architecture generally could be any neural networks. It should be noted that the two sister networks could be of the same or different architecture.  Even if the two sister networks are of the same architecture, they do not have to share weights but use distinct weights. Usually, if the inputs are of different "type", the sister networks usually use different architectures, or use distinct weights for the same architecture.

<div class = "titled-image">
<figure class = "titled-image">
    <img src = "{{ site.url }}/images/articles/2017-10-30-Siamese-Network-MNIST/siamese_example.png">
    <figcaption>Siamese Network</figcaption>
</figure>
</div>

The two statue images were input into the two channels of the Siamese Network. Because the two inputs are the same kind of inputs (image of objects), the two sister CNN shares weights between each other. The L2 distance (Euclidean distance) of the outputs of the two channels were calculated and subjected to the loss function $$l(x_1, x_2, \delta)$$ minimization. Here, the loss function is a function called contrastive loss function first proposed by Yann LeCunn ([Dimensionality Reduction by Learning an Invariant Mapping](http://yann.lecun.com/exdb/publis/pdf/hadsell-chopra-lecun-06.pdf)), which I will elaborate in the following sections. If the two images are representing the same object, the two outputs should be very close in the higher dimensional space, i.e., small L2 distance. Otherwise, the two outputs should be very far away from each other in the higher dimensional space, i.e., large L2 distance.

<br />

I will first give an example of my implementation of the Siamese Network using identical architectures with shared weights on MNIST dataset. Followed by an more complex example using different architectures or different weights with the same architecture.

### Siamese Network on MNIST Dataset

The whole Siamese Network implementation was wrapped as Python object. One can easily modify the counterparts in the object to achieve more advanced goals, such as replacing FNN to more advanced neural networks, changing loss functions, etc. See the [Siamese Network on MNIST](https://github.com/leimao/Siamese_Network_MNIST) in my GitHub repository.

<br />

The sister networks I used for the MNIST dataset are three layers of FNN. All the implementaion of the network are nothing special compared to the implementaions of other networks in TensorFlow, except for three caveats.

#### Share Weights Between Networks

Use ```scope.reuse_variables()``` to tell TensorFlow the variables used in the scope for ```output_1``` needs to be reused for ```output_2```. Although I have not tested, the variables in the scope could be reused as many times as possible as long as ```scope.reuse_variables()``` is stated after the useage of the variables.

```python
    def network_initializer(self):
        # Initialze neural network
        with tf.variable_scope("siamese") as scope:
            output_1 = self.network(self.tf_input_1)
            # Share weights
            scope.reuse_variables()
            output_2 = self.network(self.tf_input_2)
        return output_1, output_2
```

#### Implementation of the Contrastive Loss




#### Choice of the Optimizers


