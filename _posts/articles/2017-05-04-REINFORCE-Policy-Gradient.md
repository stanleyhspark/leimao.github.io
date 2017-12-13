---
layout: post
title: Monte Carlo Policy Gradient in OpenAI-Gym LunarLander
excerpt: "Implementation of Deep Monte Carlo Policy Gradient learning algorithm in OpenAI Gym environments."
modified: 2017-05-04T14:17:25-04:00
categories: article
tags: [artificial intelligence, deep learning, reinforcement learning]
comments: true
share: true
image:
  teaser: /images/articles/2017-05-04-REINFORCE-Policy-Gradient/lunarlander.png
---

### Introduction

[LunarLander](https://gym.openai.com/envs/LunarLander-v2) is one of the learning environment in OpenAI Gym. I have actually tried to solve this learning problem using Deep Q-Learning which I have successfully used to train the CartPole environment in OpenAI Gym and the Flappy Bird game. However, I was not able to get good training performance in a reasonable amount of episodes. The lunarlander controlled by AI only learned how to steadily float in the air but was not able to successfully land within the time requested.

<br />

Here I am going to tackle this LunarLander problem using a new alogirthm called "REINFORCE" or "Monte Carlo Policy Gradient".

<br />

![]({{ site.url }}/images/articles/2017-05-04-REINFORCE-Policy-Gradient/lunarlander.png)

### Touch the Algorithm

Algorithm from [Sutton Book draft](http://incompleteideas.net/sutton/book/the-book-2nd.html)

<br />

![]({{ site.url }}/images/articles/2017-05-04-REINFORCE-Policy-Gradient/Sutton_REINFORCE.png)

<br />

Algorithm from [Silver Courseware](http://www0.cs.ucl.ac.uk/staff/D.Silver/web/Teaching.html)

<br />

![]({{ site.url }}/images/articles/2017-05-04-REINFORCE-Policy-Gradient/Silver_REINFORCE.png)

<br />

Note that the \\(G_t\\) item in Sutton's REINFORCE algorithm and the \\(v_t\\) item in Silver's REINFORCE algorithm are the same thing.

$$ G_t = R_{t+1} + \gamma \times R_{t+2} + \gamma^2 \times R_{t+3} + ... + \gamma^{T-t+1} \times R_{T} $$

However, Silver's REINFORCE algorithm lacked a \\( \gamma^t \\) item than Sutton's algorithm. It turned out that both of the algorithms are correct. Sutton's algorithm worked for the episodic case maximizing the value of start state, while Silver's algorithm worked for the continuing case maximizing the averaged value. The lunarlander problem is a continuing case, so I am going to implement Silver's REINFORCE algorithm without including the \\( \gamma^t \\) item.

### Make OpenAI Deep REINFORCE Class

The main neural network in Deep REINFORCE Class, which is called policy network, taks the observation as input and outputs the softmaxed probability for all actions available.

<br />

This algorithm is very conceptually simple. However, I got stuck for a while when I firstly tried to implement it on my computer. We have got used to use deep learning libraries, such as tensorflow, to calculate derivatives for convenience. The tensorflow allows us to optimize the parameters in the neural network by minimizing some loss functions. However, from the REINFORCE algorithm, it seems that we have to manually calculate the derivatives and optimize the parameters through iterations. 

<br />

One of way to overcome this is to construct a loss function whose minimization derivative udpate is exactly the same to the one in the algorithm. One simple loss function could be \\( -\log{\pi}(A_t \mid S_t,\theta) \times v_t \\). Note that \\( -\log{\pi}(A_t \mid S_t,\theta) \\) is the cross entropy of softmaxed action prediction and labeled action.

### Test OpenAI Deep REINFORCE Class in OpenAI Gym LunarLander Environment

#### Key Parameters

FC-16 -> FC-32

```python
GAMMA = 0.99 # decay rate of past observations
LEARNING_RATE = 0.005 # learning rate in deep learning
RAND_SEED = 0 # random seed
```
#### Algorithm Performance

Before Training:

![]({{ site.url }}/images/articles/2017-05-04-REINFORCE-Policy-Gradient/episode_0.gif)

After Training:

![]({{ site.url }}/images/articles/2017-05-04-REINFORCE-Policy-Gradient/episode_3000.gif)

#### OpenAI Gym Evaluation

Solved after 1476 episodes. Best 100-episode average reward was 203.29 ± 4.98.

<https://gym.openai.com/evaluations/eval_6QdRxa5TuOD6GbmpbpsCw>

This algorithm did solve the problem as OpenAI Gym requested. However, it suffered from high vairance problem. I tried to tune the hyperparameters and change the size of neural network. But this did not help significantly.

<br />

![]({{ site.url }}/images/articles/2017-05-04-REINFORCE-Policy-Gradient/training_record_lunarlander.jpeg)

### Links to Github

<https://github.com/leimao/OpenAI_Gym_AI/tree/master/LunarLander-v2/REINFORCE/2017-05-24-v1>


### Conclusions

REINFORCE Monte Carlo Policy Gradient solved the LunarLander problem which Deep Q-Learning did not solve. However, it suffered from high variance problem. One may try REINFORCE with baseline Policy Gradient or actor-critic method to reduce variance during the training. I will write a blog once I implemented these new algorithm to solve the LunarLander problem.

### Notes

#### 2017-5-4

To implement Policy Gradients Reinforcement Learning, I recommended to use Tensorflow but not Keras, because you may have to introduce a lot of user-defined loss functions. Some of the customized loss functions could be easily defined in Keras, some of them are not. If you are comfortable with doing gradient descent by yourself, you do not even have to use tensorflow.

<br />

I also tried REINFORCE to solve CartPole and MountainCar Problem in OpenAI Gym. 

<br />

REINFORCE successfully solved CartPole in a very shot period of time. However, it still suffered from high variance problem ([example](https://gym.openai.com/evaluations/eval_juc7UYABTFmahgF80oBIA)). After tuning the model, one may get reasonable learning performance without too much variance([example](https://gym.openai.com/evaluations/eval_KINLU2HNSHiI331ecc6F8A)). The code example could be found [here](https://github.com/leimao/OpenAI_Gym_AI/tree/master/CartPole-v0/REINFORCE/2017-05-03-v1).

<br />

REINFORCE never solved MountainCar problem unless I cheated. This is because it is extremely difficult (probability is extremely low) to get the top of the mountain without learning thoroughly. The learning agent always get -200 reward in each episode. Therefore, the learning algorithm is useless. However, if the MountainCar problem is unwrapped, which means the game lasts forever unless the car goes to the top of the mountain, there could be appropriate gradient descent to solve the problem. Alternatively, one could engineer the reward that the API returns. By rewarding differently, say the higher the car goes the more reward it received, the car could easily learn how to climb. However, these are considered cheating because these does not provide any proof of the goodness of the learning algorithm itself.




