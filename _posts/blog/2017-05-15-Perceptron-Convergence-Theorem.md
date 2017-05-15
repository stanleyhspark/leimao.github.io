---
layout: post
title: Comprehensive Proof of Perceptron Convergence Theorem
excerpt: "Mathematical derivation of bias-variance relationship"
modified: 2017-05-13T14:17:25-04:00
categories: blog
tags: [Machine Learning]
image:
  feature: site_logos/Logo Umbrella_Corporation.png
  credit: 
  creditlink: 
comments: true
share: true
---

### Preface

I was reading the perceptron convergence theorem, which is a proof for the convergence of perceptron learning algorithm, in the book "Machine Learning - An Algorithmic Perspective" 2nd Ed. I found the authors made some error in the mathmatical derivation by introducing some unstated assumptions. Obviously, the author was looking at the materials from multiple different sources but did not generalize it very well to match his proceeding writings in the book. I then tried to look up the right derivation on the internet, and I found that most of the materials includes too many assumptions that did not generalize the theorem very well. I finally found one from the MIT opencourse and I think this is the best one I was looking for.

In case you forget the perceptron learning algorithm, you may find it [here](/downloads/blog/2017-05-15-Perceptron-Convergence-Theorem/perceptron_learning_algorithm.pdf).


Note that the \\(G_t\\) item in Sutton's REINFORCE algorithm and the \\(v_t\\) item in Silver's REINFORCE algorithm are the same thing.
\\(\gamma\\)\\(\left|\frac{1}{2}\right|\\)

The perceptron convergence theorem basically states that the perceptron learning algorithm converges in finite number of steps, given a linearly separable dataset. More precisely, if for each data point x, 


sdfsafdasdf\\(left|left|xright|right| < R\\), 



and \\(\gamma = ({\theta}^*)^Tx_{closest}\\) where \\(x_{closest}\\) is the data point that is the closest to the linear separate hyperplane, and \\({\theta}^*\\) is the weights of the hyperplane. It should be noted that mathematically \\(\frac{\gamma}{left|left|{\theta}^*right|right|^2}\\) is the distance \\(d\\)of the closest datapoint to the linear separate hyperplane. The number of steps is bounded by