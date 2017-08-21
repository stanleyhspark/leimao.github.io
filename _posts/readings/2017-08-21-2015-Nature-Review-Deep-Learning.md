---
layout: post
title: "2015 Nature Review: Deep Learning"
excerpt: "Deep Learning Authority Review"
modified: 2017-08-21T14:17:25-04:00
categories: reading
tags: [Deep Learning]
comments: true
share: true
---

In 2015, Yann LeCun, Yoshua Bengio & Geoffrey Hinton, the three distinguished scientists in the field of machine learning published a review titled "Deep Learning" in Nature journal. Although it is year 2017 right now, it is still a very good starting point for deep learning beginners, like me, who wanted to be devoted and kept updated in the field of deep learning and has some levels of knowledge of deep learning from ordinary class courses or MOOC.

<br />

The original paper could be downloaded [here](https://github.com/leimao/Deep_Learning_Papers/raw/master/Reviews/Nature_Deep_Learning_Review_2015/Nature_Deep_Learning_Review_2015.pdf), and my annotated paper could be download [here](https://github.com/leimao/Deep_Learning_Papers/raw/master/Reviews/Nature_Deep_Learning_Review_2015/Nature_Deep_Learning_Review_2015_annotated.pdf).

<br />

In general, it is a very well summarized review on deep learning, in particular convolutional neural network (CNN) and resursive neural network (RNN). The authors gave relative detailed application examples on object recognition and machine translation. Anyone who has some fundamental knowledge about deep learning should be able to understand without too much difficulties. This paper could also serve to refresh your mind on several key deep learning aspects.

<br />

The authors introduced in the paper that there has been theoretical studies suggesting that local minima is not the main problem of deep learning because almost all the "saddle points" have very similar values of object functions. This is very suprising to me. I swear I could not think of it beforehand.

<br />

The authors also claimed that "pre-training" is only needed for small datasets, (but not required for big datasets in deep learning). I assume the "pre-training" technique is the "Restricted Boltzmann Machine" which is developed by Geoffery Hinton, one of the authors in this paper. I admire Restricted Boltzmann Machine very much, both theoretically and practically, although I have actually never implemented it by myself. I will see if this statement is true in my new career life soon.

<br />

The "image to text" application, with a combination of CNN and RNN, is extremely interesting. I would like to know what their training dataset is and how exactly the CNN and RNN are integrated together.

<br />

The machine translation using a combination of "English-encoder" and "French-decoder" is interesting. I sought have some idea about how it works. **Build a English auto-encoder and a French auto-encoder using RNN, and combine the English encoder with the French decoder**. Is it overall correct?