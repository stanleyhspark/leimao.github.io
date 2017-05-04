---
layout: post
title: "Monte Carlo Policy Gradient in OpenAI-Gym LunarLander"
categories: journal
tags: [documentation,sample]
image:
  feature: blog_images/2017-05-04-REINFORCE-Policy-Gradient/lunarlander.png
  teaser: blog_images/2017-05-04-REINFORCE-Policy-Gradient/lunarlander.png
  credit: 
  creditlink: ""
---

### Introduction

[LunarLander](https://gym.openai.com/envs/LunarLander-v2) is one of the learning environment in OpenAI Gym. I have actually tried to solve this learning problem using Deep Q-Learning which I have successfully used to train the CartPole environment in OpenAI Gym and the Flappy Bird game. However, I was not able to get good training performance in a reasonable amount of episodes. The lunarlander controlled by AI only learned how to steadily float in the air but was not able to successfully land within the time requested.

Here I am going to tackle this LunarLander problem using a new alogirthm called "REINFORCE" or "Monte Carlo Policy Gradient".

### Touch the Algorithm

Algorithm from [Sutton Book draft]()

![](/images/blog_images/2017-05-04-REINFORCE-Policy-Gradient/Sutton_REINFORCE.png)

Algorithm from [Silver Courseware](http://www0.cs.ucl.ac.uk/staff/D.Silver/web/Teaching.html)

![](/images/blog_images/2017-05-04-REINFORCE-Policy-Gradient/Silver_REINFORCE.png)

Note that the Gt item in Sutton's REINFORCE algorithm and the vt item in Silver's REINFORCE algorithm are the same thing.

Gt = Rt+1 + gamma * Rt+2 + gamma^2 * Rt+3 + ... + gamma^(T-t+1)RT

However, Silver's REINFORCE algorithm lacked a gamma^t item than Sutton's algorithm. I personally believe that Silver was wrong and Sutton was correct. It may not have an significanty impact on the optimization of the algorithm. I will confirm this and explore the effect of lacking this item if I have chance in the future. For now, I am going to implement Silver's REINFORCE algorithm without including the gamma^t item.

### Make OpenAI Deep REINFORCE Class

The main neural network in Deep REINFORCE Class, which is called policy network, taks the observation as input and outputs the softmaxed probability for all actions available.

This algorithm is very conceptually simple. However, I got stuck for a while when I firstly tried to implement it on my computer. We have got used to use deep learning libraries, such as tensorflow, to calculate derivatives for convenience. The tensorflow allows us to optimize the parameters in the neural network by minimizing some loss functions. However, from the REINFORCE algorithm, it seems that we have to manually calculate the derivatives and optimize the parameters through iterations. 

One of way to overcome this is to construct a loss function whose minimization derivative udpate is exactly the same to the one in the algorithm. One simple loss function could be (-log_p * vt) note that -log_p is the cross entropy of softmaxed action prediction and labeled action.

### Test OpenAI Deep REINFORCE Class in OpenAI Gym LunarLander Environment

#### Key Parameters

FC-16 -> FC-32

```python

GAMMA = 0.99 # decay rate of past observations
LEARNING_RATE = 0.005 # learning rate in deep learning
RAND_SEED = 0 # random seed

```
#### Algorithm Performance

OpenAI Gym Evaluation

Solved after 1476 episodes. Best 100-episode average reward was 203.29 ± 4.98.

<https://gym.openai.com/evaluations/eval_6QdRxa5TuOD6GbmpbpsCw>

This algorithm did solve the problem as OpenAI Gym requested. However, it suffered from high vairance problem. I tried to tune the hyperparameters and change the size of neural network. But this did not help significantly.

![](/images/blog_images/2017-05-04-REINFORCE-Policy-Gradient/training_record_lunarlander.jpeg)

#### Links to Github

<https://github.com/leimao/OpenAI_Gym_AI/tree/master/LunarLander-v2/REINFORCE/2017-05-24-v1>


### Conclusions

REINFORCE Monte Carlo Policy Gradient solved the LunarLander problem which Deep Q-Learning did not solve. However, it suffered from high variance problem. One may try REINFORCE with baseline Policy Gradient or actor-critic method to reduce variance during the training. I will write a blog once I implemented these new algorithm to solve the LunarLander problem.

### Notes

#### 2017-5-4

I also tried REINFORCE to solve CartPole and MountainCar Problem in OpenAI Gym. 

REINFORCE successfully solved CartPole in a very shot period of time. However, it still suffered from high variance problem ([example](https://gym.openai.com/evaluations/eval_juc7UYABTFmahgF80oBIA)). After tuning the model, one may get reasonable learning performance without too much variance([example](https://gym.openai.com/evaluations/eval_KINLU2HNSHiI331ecc6F8A)). The code example could be found [here](https://github.com/leimao/OpenAI_Gym_AI/tree/master/CartPole-v0/REINFORCE/2017-05-03-v1).

REINFORCE never solved MountainCar problem unless I cheated. This is because it is extremely difficult (probability is extremely low) to get the top of the mountain without learning thoroughly. The learning agent always get -200 reward in each episode. Therefore, the learning algorithm is useless. However, if the MountainCar problem is unwrapped, which means the game lasts forever unless the car goes to the top of the mountain, there could be appropriate gradient descent to solve the problem. Alternatively, one could engineer the reward that the API returns. By rewarding differently, say the higher the car goes the more reward it received, the car could easily learn how to climb. However, these are considered cheating because these does not provide any proof of the goodness of the learning algorithm itself.




