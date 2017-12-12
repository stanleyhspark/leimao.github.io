---
layout: post
title: Comprehensive Proof of Perceptron Convergence Theorem
excerpt: "Perceptron learning algorithm always converges."
modified: 2017-05-15T14:17:25-04:00
categories: blog
tags: [Machine Learning]
comments: true
share: true
---

### Preface

I was reading the perceptron convergence theorem, which is a proof for the convergence of perceptron learning algorithm, in the book "Machine Learning - An Algorithmic Perspective" 2nd Ed. I found the authors made some error in the mathmatical derivation by introducing some unstated assumptions. Obviously, the author was looking at the materials from multiple different sources but did not generalize it very well to match his proceeding writings in the book. I then tried to look up the right derivation on the internet, and I found that most of the materials includes too many assumptions that did not generalize the theorem very well. I finally found one from the MIT opencourse and I think this is the best one I was looking for.

### Mathematical Proof and Caveats

In case you forget the perceptron learning algorithm, you may find it [here](/downloads/blog/2017-05-15-Perceptron-Convergence-Theorem/perceptron_learning_algorithm.pdf).

<br />

The perceptron convergence theorem basically states that the perceptron learning algorithm converges in finite number of steps, given a linearly separable dataset. More precisely, if for each data point x, \\( \\|\mathbf{x}\\| < R \\) where \\( R \\) is certain constant number,  \\( \gamma = (\theta^{\ast})^{T} \mathbf{x_c} \\) where \\( \mathbf{x_c} \\) is the data point that is the closest to the linear separate hyperplane. It should be noted that mathematically \\(\frac{\gamma}{\\|\theta^{\ast}\\|^2}\\) is the distance \\(d\\) of the closest datapoint to the linear separate hyperplane (it could be negative). The number of steps is bounded by \\(\frac{R^{2}\\|\theta^{\ast}\\|^{2}}{\gamma^2}\\) or \\(\frac{R^{2}}{d^2}\\).

<br />

In some materials, for simplicity, someone added assumption without generality that the weight of separate hyperplane is a unit vector (\\( \\|\theta^{\ast}\\|^{2} = 1 \\)) and one could claim that the physical meaning of \\( \gamma \\) is the the distance of the closest datapoint to the linear separate hyperplane. However, sometimes people ignored this assumption and claim \\( \gamma \\) is the the distance of the closest datapoint to the linear separate hyperplane. That was wrong.

<br />

The comprehensive correct proof could be found [here]({{ site.url }}/downloads/blog/2017-05-15-Perceptron-Convergence-Theorem/perceptron_convergence_theorem.pdf).

<br />

PS: "MathJax is against humanity." and "Happy Mother's Day."
![]({{ site.url }}/images/blog/2017-05-15-Perceptron-Convergence-Theorem/mothers-day.gif)

### Updates

6/16/2017

<br />

I happened to find an interesting non-mathematical informal proof in Hinton's "Neural Networks for Machine Learning" course. Unlike the previous mathematical proofs I provided, this proof discussed the problems in the weight space. The whole informal proof is very simple and easy to understand. The informal proof could be downloaded [here]({{ site.url }}/downloads/blog/2017-05-15-Perceptron-Convergence-Theorem/Hinton_lec2.pdf).
