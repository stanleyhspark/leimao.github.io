# Gibbs sampler for the change-point model described in a Cognition cheat sheet titled "Gibbs sampling."
# This is a Python implementation of the procedure at http://www.cmpe.boun.edu.tr/courses/cmpe58n/fall2009/
# Written by Ilker Yildirim, September 2012.
# Revised and Annotated by Lei Mao, June 2017.
# dukeleimao@gmail.com

from scipy.stats import uniform, gamma, poisson
import matplotlib.pyplot as plt
import numpy
from numpy import log,exp
from numpy.random import multinomial

# fix the random seed for replicability.
numpy.random.seed(0)

# Generate data

# Hyperparameters
# Number of total data points
N=50

# Change-point: where the intensity parameter changes.
# The threhold point of two sets of data points
# n <= N
# Here we set n = 23
n=23
print str(n)

# Intensity values
# lambda1 for generating the first set of data from Poisson distribution
# Here we set lambda1 = 2
lambda1=2
# lambda2 for generating the second set of data from Poisson distribution
# Here we set lambda1 = 8
lambda2=8

# Generating observations x, consisting x_1 ... x_N
lambdas=[lambda1]*n
lambdas[n:N-1]=[lambda2]*(N-n)

x=poisson.rvs(lambdas)

# Make one big subplots and put everything in it.
f, (ax1,ax2,ax3,ax4,ax5)=plt.subplots(5,1)
# Plot the data
ax1.stem(range(N),x,linefmt='b-', markerfmt='bo')
ax1.plot(range(N),lambdas,'r--')
ax1.set_ylabel('Counts')

# Given the dataset, our mission is to model this dataset
# Our hypothesis is that the dataset consists two set of data, each set of the
# data satisfies Poisson distribution (You can also model the data using other 
# distributions, say, Normal distribution, to see whether it works).
# We need to infer three parameters in the model using the dataset we have. 
# 1. The threhold point of two sets of data points n
# 2. lambda1 for the first Poisson distribution dataset
# 3. lambda2 for the second Poisson distribution dataset

# Gibbs sampler
# Number of parameter sets we are going to sample
E=5200
# Number of parameter sets at the beginning of sampling we need to remove
# This is called "BURN-IN"
BURN_IN=200

# Initialize the chain
# Model n to be uniformly distributed from 0 to N
n=int(round(uniform.rvs()*N))
# Model lambda to satisfy gamma distribution
# We mannually set the gamma distribution parameter
a=2
b=0.2
lambda1=gamma.rvs(a,scale=1./b)
lambda2=gamma.rvs(a,scale=1./b)

# My understanding is that the model of these three variables should at least 
# sample the true values of the variables with probablities larger than 0 (here
# the uniform distribution could sample variables from 0 to N, gamma
# distribution could sample variables greater or equal to 0), and the posterior
# conditionals of these three could be calculated easily using Bayesian 
# Equations. Finally, this posterior probability distribution should be easy to # use for sampling.

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
