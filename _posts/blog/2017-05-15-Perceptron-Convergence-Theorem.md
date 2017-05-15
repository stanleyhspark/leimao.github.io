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

The perceptron convergence theorem basically states that the perceptron learning algorithm converges in finite number of steps, given a linearly separable dataset. More precisely, if for each data point x, \\(\|\|{\bf{x}}\|\| < R\\) where \\(R\\) is certain constant number, \\(\gamma = {\theta}^{*T}x_{\text{closest}}\\) where \\(x_{\text{closest}}\\) is the data point that is the closest to the linear separate hyperplane.



\\(\frac{1}{1+x}\\)

\\(\frac{1}{1+x^2}\\)

\\(\frac{1}{(1+x)^2}\\)

\\(\frac{1}{\theta^2}\\)

\\(\frac{1}{\|\|\theta\|\|^2}\\)


aaa\\(\gamma = {\theta}^{*T}x_{closest}\\)

\\(\gamma = {\theta}^{T}\\)

\\(\gamma = {{\theta}}^{T}\\)

\\(\gamma = \theta^T\\)

\\(\gamma = {\theta}^{*}x_{closest}\\)

\\(\gamma = {\theta}^{*T}x_{closest}\\)

\\(\gamma = {\theta}^{*}x_{closest}\\)

\\(\gamma = {\theta}^{*T}x_{closest}\\)

\\(\gamma = {\theta}^{*}^{T}x_{closest}\\) where \\(x_{closest}\\) is the data point that is the closest to the linear separate hyperplane, and \\({\theta}^{*}\\) is the weights of the hyperplane.



\\(\gamma = \{\theta}^{*}^{T}x_{closest}\\) where \\(x_{closest}\\) is the data point that is the closest to the linear separate hyperplane, and \\({\theta}^{*}\\) is the weights of the hyperplane.

x_{\text{closest}}
