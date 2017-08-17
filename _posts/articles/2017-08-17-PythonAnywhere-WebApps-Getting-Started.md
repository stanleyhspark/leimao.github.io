---
layout: post
title: Getting Started to Build Web Applications on PythonAnywhere
excerpt: "The first step to learn host applications on website."
modified: 2017-08-17T14:17:25-04:00
categories: article
tags: [web applications]
comments: true
share: true
image:
  teaser: /images/articles/2017-08-17-PythonAnywhere-WebApps-Getting-Started/pythonanywhere_teaser.png
---

### Motivations

I was mainly focusing on applying machine learning algorithms to solve real-world problems. But the blossom of machine learning applications from IT tech giants quickly reminded me the importance of turning local programs to web applications. I have also seen the high school student [KvFrans](http://www.kvfrans.com/) hosting his machine learning applications on his own website, which makes me become more determined to learn how to do so. 

### Quick Research

I have to spend most of my time to deal with a discrete mathematics exam in the next month. So I need to get started as fast as possible.

<br />

My programs are mostly written in Python. So one of my ultimate goal is to host a Python program on the website. It could be simple such a image resizer, or more complicated such as a digit recognizer.

<br />

I did a quick google, I found there are multiple such service providers from IT tech giants, such as [Amazon EC2](https://aws.amazon.com/ec2/) and [Google AppEngine](https://cloud.google.com/appengine/). These services looked a little bit daunting at the first glance from a newbie. Somehow I found another service provider called [PythonAnywhere](https://www.pythonanywhere.com/), which I decided to use it for my beginner's trial. I like its name because it does not look intimating. In addition, it provides beginner's account, which is absolutely free. It is not like free-trial of full services for certain period of time from IT tech giants, which is definited not useful for a newbie who knows almost nothing. 

### Tutorial

There is a beginner's tutorial titled ["A beginner's guide to building a simple database-backed Flask website on PythonAnywhere"](https://blog.pythonanywhere.com/121/) on PythonAnywhere, assuming some preknowledge of Python and HTML (luckily I think I know them to some extent).

<br />

I wondered what hell the "Flask" is. [Wikipedia]((https://en.wikipedia.org/wiki/Flask_(web_framework))) told me that [Flask](http://flask.pocoo.org/) is basically a web framework that helps you to build web applications. There are similar tools, such as [Django](https://www.djangoproject.com/). Whatever, let us keep on moving.

<figure class="half">
    <img src = "{{ site.url }}/images/articles/2017-08-17-PythonAnywhere-WebApps-Getting-Started/Flask_logo.svg">
    <img src = "{{ site.url }}/images/articles/2017-08-17-PythonAnywhere-WebApps-Getting-Started/Django_logo.svg">
</figure>

<br />

In the firt part of the tutorial, it taught you how to manage your source code files on PythonAnywhere. I was surprised that they even have a source code control system, just like GitHub, in their system. You will have to do all these "git" things in their console (I got too used to do "git" things in "clickable" GitHub Destop). For editing or submitting your source code, you can edit the file in the text editor in the broswer or just submit from your own local machine. Everything is easy and straightforward. Here is the first web-hosted application I made. It should be noted that the application might be expired because of the limit of the free account.

<br />

Go to [http://leimao.pythonanywhere.com/](http://leimao.pythonanywhere.com/), it will show a "hello world" message.
Go to [http://leimao.pythonanywhere.com/foo](http://leimao.pythonanywhere.com/foo), it will show another "hello world" message.

<br />

Those two are simple webpages. However, what's different to ordinary HTML webpages is that there are no HTML files. The text messages are the returns from certain Python functions when you go to the urls specified.