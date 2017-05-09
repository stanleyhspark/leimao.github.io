---
layout: post
title: "Making Reinforcement Learning Agent Library"
categories: journal
tags: [documentation,sample]
image:
  feature: blog_images/2017-05-09-Reinforcement-Learning-Agent-Library/rl_teaser.jpg
  teaser: blog_images/2017-05-09-Reinforcement-Learning-Agent-Library/rl_teaser.jpg
  credit: 
  creditlink: ""
---

<script type="text/x-mathjax-config">
 MathJax.Hub.Config({tex2jax: {inlineMath: [['$','$'], ['\\(','\\)']]}});
</script>

### Ideas

When I was developing learning agents using different reinforcement learning algorithms, somehow I made these learning agents into class. All these learning agents take the current environment state, the action for the current environment state, the reward got after taking the action, the next environment state, and also possible the next action for the next environment state, as input. They all output actions when given the environment state. So all these learning agents could be employed and tested in different learning enviroments, especially the OpenAI Gym environment.

I have already implemented several learning agents and prepared the corresponding enviroment running script in my [GitHub](https://github.com/leimao/OpenAI). One could simply change the enviroment name and the learning agent to import in the environment running script to test.

I just came up with this idea. So there is still no documentation of how to use these learning agents on your own computer. The Python expert might find easy to use it because you only have to change a little bit in the raw code in order to make it work. However, the Python beginners might have to wait me to get some time to arrange these learning agents to more formal classes and write official documentations.


### Talk About Algorithms

### Actor-Critic Policy Gradient

In the [REINFORCE Policy Gradient reinforcement learning algorithm](https://leimao.github.io/journal/REINFORCE-Policy-Gradient.html), we calculate the value of the next state after taking the action $G_t$ ($v_t$) from the rewards in the whole episode and use it to guide our gradient descent. So it is a statistically sampled value. One could actually construct another neural network to represent the value of the state and update it routinely until we get the a good estimate of the true value of the state. 

The policy network output the action and use the value of the next state to guide its future actions. So the policy network is just like an actor learning how to perform. The value network use the reward after the actor taking the action to estimate the value of the state, and provide this information to the actor. So the value network is just like an critic informing whether the actor did good or bad. This circus is called "Actor-Critic" Policy Gradient method.

The [Sutton Book draft](http://incompleteideas.net/sutton/book/the-book-2nd.html) provided the pseudocode for one-step Actor-Critic method. However it is episodic (see below).

![](/images/blog_images/2017-05-09-Reinforcement-Learning-Agent-Library/actor-critic_episodic.png)

I did not find a pseudocode continuing case in this draft. However, we just have to modify this pseudocode a little bit to get the pseudocode for the continuing case. To do this, simply remove everything that is related to I (see below). 

![](/images/blog_images/2017-05-09-Reinforcement-Learning-Agent-Library/actor-critic_continuing.jpg)

I should also mention that the value we used to guide our gradient descent is different to what we used in REINFORCE. This value is called time-dependent error (td_error). It will not affect the direction of our gradient descent mathematically but tune the step width to make our training have less variance (in principal). Please see "REINFORCE with Baseline" in the Sutton Book draft for more details.

Despite the update for the critic value network, everything is very similar to the REINFORCE Policy Gradient method.

I tested the algorithm in the CartPole environment and uploaded to my GitHub:

<https://github.com/leimao/OpenAI/tree/master/OpenAI_Gym_Solutions/CartPole-v0/Actor-Critic/2017-05-08-v1>

The learning performance of the algorithm was submitted to OpenAI Gym:

<https://gym.openai.com/evaluations/eval_T51WU12pRlWydRLLI9bdg>

### Sarsa Actor-Critic Policy Gradient

Sarsa Actor-Critic Policy Gradient is a variant of the Actor-Critic Policy Gradient I talked above. It uses Q-network instead of the value network. You may remember the Q-network is a network to represent the value of state-action pairs. To update the Q-network, instead of using DQN that I used for [Flappy Bird](https://leimao.github.io/journal/Flappy-Bird-AI.html), people tend to use Sarsa (?), a variant method to update Q-network. I should have introduced Sarsa before I introduce Sarsa Actor-Critic Policy Gradient. But when I was doing the implementation, I implemented Sarsa from the Sarsa Actor-Critic Policy Gradient template. I got used to present things in a time-dependent manner, because it is time-saving and easy to tell a story.

The [Silver Courseware](http://www0.cs.ucl.ac.uk/staff/D.Silver/web/Teaching.html) provided the pseudocode for one-step Sarsa Actor-Critic method. It is weird that he called it QAC though it does Sarsa.

![](/images/blog_images/2017-05-09-Reinforcement-Learning-Agent-Library/Sarsa_AC.png)

It should also be noted that there is slight gradient descent detail that is different to the Actor-Critic Policy Gradient method I mentioned above. It might be tricky to understand, but it is correct. I have not thought of a straightforward way to explain this to you. So I just skipped it for now.

I tested the algorithm in the CartPole environment and uploaded to my GitHub:

<https://github.com/leimao/OpenAI/tree/master/OpenAI_Gym_Solutions/CartPole-v0/Sarsa_Actor-Critic/2017-05-09-v1>

The learning performance of the algorithm was submitted to OpenAI Gym:

<https://gym.openai.com/evaluations/eval_fiRpY1pESl2KJCq9nsRq3w>

### Sarsa

The basic concept of Sarsa is almost the same to the critic value network I mentioned above, except for the sampling of action. Sarsa Actor-Critic Policy Gradient uses softmax to sample action, Sarsa here use $/epsilon$-greedy to sample action.

The [Sutton Book draft](http://incompleteideas.net/sutton/book/the-book-2nd.html) provided the pseudocode for one-step episodic Sarsa method (see below).

![](/images/blog_images/2017-05-09-Reinforcement-Learning-Agent-Library/Sarsa_episodic.png)

I tested the algorithm in the CartPole environment and uploaded to my GitHub:

<https://github.com/leimao/OpenAI/tree/master/OpenAI_Gym_Solutions/CartPole-v0/Sarsa/2017-05-09-v1>

The learning performance of the algorithm was submitted to OpenAI Gym:

<https://gym.openai.com/evaluations/eval_7VNiHaATsCn9JYXVfjPQ>
