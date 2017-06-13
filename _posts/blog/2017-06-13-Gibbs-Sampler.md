---
layout: post
title: Implementation of the Gibbs Sampler
excerpt: "Understand Gibbs Sampling."
modified: 2017-06-13T14:17:25-04:00
categories: blog
tags: [Math, Statistics, Machine Learning]
image:
  feature: site_logos/Logo Umbrella_Corporation.png
  credit: 
  creditlink: 
comments: true
share: true
---

### Introduction

The basic algorithm for Gibbs Sampler is as follows.
<center><img width="600" height="600" src="/images/blog/2017-06-13-Gibbs-Sampler/gibbs_sampler_algorithm.png"/></center>

From my understanding, there are two applications of Gibbs sampler as well as general Monte Carlo Markov Chain (MCMC) samplers.

The first application is to sample multivariable data point from a certain distributions, which is relatively easy. 
<center><img width="600" height="600" src="/images/blog/2017-06-13-Gibbs-Sampler/gibbs_sampling.jpg"/></center>

If you want to sample data from a bivariate normal distribtution, here is what you can do using Gibbs sampler.
<center><img width="600" height="600" src="/images/blog/2017-06-13-Gibbs-Sampler/gibbs_sampler_bivariate_normal.jpg"/></center>

The second application is to do Bayesian Inference of the parameters behind a certain dataset, which is relatively difficult to some extent, and requires more expertise in math. This is what I am going to emphasize on in this blog article.

### Gibbs Sampler Inference

[Here](/downloads/blog/2017-06-13-Gibbs-Sampler/GibbsSampling.pdf) is a very good problem example of Gibbs Sampler Bayesian Inference. The author also provided the implementation [code](http://www2.bcs.rochester.edu/sites/jacobslab/cheat_sheets.html) for solving the problem using Gibbs Sampler, which you could also download it [here](/downloads/blog/2017-06-13-Gibbs-Sampler/GibbsSampling.code.py).


```python
# Gibbs sampler for the change-point model described in a Cognition cheat sheet titled "Gibbs sampling."
# This is a Python implementation of the procedure at http://www.cmpe.boun.edu.tr/courses/cmpe58n/fall2009/
# Written by Ilker Yildirim, September 2012.

from scipy.stats import uniform, gamma, poisson
import matplotlib.pyplot as plt
import numpy
from numpy import log,exp
from numpy.random import multinomial

# fix the random seed for replicability.
numpy.random.seed(123456789)

# Generate data

# Hyperparameters
N=50
a=2
b=1

# Change-point: where the intensity parameter changes.
n=int(round(uniform.rvs()*N))
print str(n)

# Intensity values
lambda1=gamma.rvs(a,scale=1./b) # We use 1/b instead of b because of the way Gamma distribution is parametrized in the package random.
lambda2=gamma.rvs(a,scale=1./b)

lambdas=[lambda1]*n
lambdas[n:N-1]=[lambda2]*(N-n)

# Observations, x_1 ... x_N
x=poisson.rvs(lambdas)

# make one big subplots and put everything in it.
f, (ax1,ax2,ax3,ax4,ax5)=plt.subplots(5,1)
# Plot the data
ax1.stem(range(N),x,linefmt='b-', markerfmt='bo')
ax1.plot(range(N),lambdas,'r--')
ax1.set_ylabel('Counts')

# Gibbs sampler
E=5200
BURN_IN=200

# Initialize the chain
n=int(round(uniform.rvs()*N))
lambda1=gamma.rvs(a,scale=1./b)
lambda2=gamma.rvs(a,scale=1./b)

# Store the samples
chain_n=numpy.array([0.]*(E-BURN_IN))
chain_lambda1=numpy.array([0.]*(E-BURN_IN))
chain_lambda2=numpy.array([0.]*(E-BURN_IN))

for e in range(E):
	print "At iteration "+str(e)
	# sample lambda1 and lambda2 from their posterior conditionals, Equation 8 and Equation 9, respectively.
	lambda1=gamma.rvs(a+sum(x[0:n]), scale=1./(n+b))
	lambda2=gamma.rvs(a+sum(x[n:N]), scale=1./(N-n+b))
	
	# sample n, Equation 10
	mult_n=numpy.array([0]*N)
	for i in range(N):
		mult_n[i]=sum(x[0:i])*log(lambda1)-i*lambda1+sum(x[i:N])*log(lambda2)-(N-i)*lambda2
	mult_n=exp(mult_n-max(mult_n))
	n=numpy.where(multinomial(1,mult_n/sum(mult_n),size=1)==1)[1][0]
	
	# store
	if e>=BURN_IN:
		chain_n[e-BURN_IN]=n
		chain_lambda1[e-BURN_IN]=lambda1
		chain_lambda2[e-BURN_IN]=lambda2
		

ax2.plot(chain_lambda1,'b',chain_lambda2,'g')
ax2.set_ylabel('$\lambda$')
ax3.hist(chain_lambda1,20)
ax3.set_xlabel('$\lambda_1$')
ax3.set_xlim([0,12])
ax4.hist(chain_lambda2,20,color='g')
ax4.set_xlim([0,12])
ax4.set_xlabel('$\lambda_2$')
ax5.hist(chain_n,50)
ax5.set_xlabel('n')
ax5.set_xlim([1,50])
plt.show()

```








Confusion

[Self-Organizing Map (SOM)](https://en.wikipedia.org/wiki/Self-organizing_map) is an unsupervised neural network that is used to cluster multi-dimensional data. When the number of nodes in the neural network is small, it behaves very similar to k-Means algorithm. When the number of nodes in the neural network is large, it rerranges the data and keeps the original data topology (I haven't totally understood what data topology is for now, but it does not affect our understanding of the algorithm).

Regrading the SOM algorithm, I understood the node position (in the weight space) is trying to move closer to each of the data point during the training (update the node weights closer to the data point). However, I had difficulties in understanding why the algorithm will finally converge. Say, if the weights of two nodes happened to be initialized to almost the same with very slight difference, and they are very far apart in the 2D neural network (Not weight space. In the weight space, their positions are extremely close.). 1) How does the model finally achieves that the node in the neural network and its neighbor nodes have similar weights (The nodes far apart have very different weights)? 2) If so, what happens to the two nodes with similar initialized weights I mentioned above during the learning iteration?

### Intuition

I finally found a figure from the Wikipedia that totally explain all of my questions in an intuitive way. I would like to thank the author of the figure very much.

In an ordinary introduction material of self-organizing map, you will often see such kind of figure illustrating the SOM neural network. I personally think this is not helpful for readers to understand the algorithm, although it is correct.
<center><img width="300" height="300" src="/images/blog/2017-06-05-Self-Organizing-Map/som_representation.jpg"/></center>

The great figure from the Wikipedia is this:
![](/images/blog/2017-06-05-Self-Organizing-Map/Somtraining.svg)
<font size="2.5">An illustration of the training of a self-organizing map. The blue blob is the distribution of the training data, and the small white disc is the current training datum drawn from that distribution. At first (left) the SOM nodes are arbitrarily positioned in the data space. The node (highlighted in yellow) which is nearest to the training datum is selected. It is moved towards the training datum, as (to a lesser extent) are its neighbors on the grid. After many iterations the grid tends to approximate the data distribution (right).</font>

I could add more comments to this figure. If you put the whole initialized neural network in the higer-dimensional weight space, it could "look" like "folded", "wrapped", meaning that any two nodes in neural network in the weight space could be very close to each other depending on the weight initialization. Your job, or what learning is going to do, is to "unfold" the initialized neural network, and use it to cover the whole data point set. So the answer to question 1 is automatically answered. The answer to question 2 is also very obvious. Although the two nodes initially sit very close to each other in the weight space, they might be separated apart because the whole neural network has to cover the whole data point set.
