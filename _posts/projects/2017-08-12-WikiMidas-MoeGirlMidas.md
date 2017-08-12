---
layout: post
title: WikiMidas and MoeGirlMidas
excerpt: "MediaWiki Webpage Crawler"
modified: 2017-08-12T14:17:25-04:00
categories: project
tags: [Data Crawling]
image:
  feature: site_logos/Logo Umbrella_Corporation.png
  credit: 
  creditlink: 
comments: true
share: true
---

### Introduction

[WikiMidas](https://github.com/leimao/WikiMidas) is a Python spidering API wrapper program specifically designed for data crawling from MediaWiki APIs (https://www.mediawiki.org/). It could be used to retrieve information from Wikipedia (https://en.wikipedia.org/wiki/Main_Page) and MoeGirl (https://zh.moegirl.org/Mainpage) which uses MediaWiki as their APIs. MoeGirl is more focused on the articles in the finctional characters' in anime. [MoeGirlMidas], developed based on WikiMidas, are designed specifically to retrieve characters' data from MoeGirl.

I named the two programs after "midas". Because I like the "feel" that you touch something and something becomes useful.

[midas image]

### Learning Experience

I have little experience in writing a program to retrieve data from internet by myself. So, In addition to some practice program experience in MOOC courses ([Using Python to Access Web Data](https://www.coursera.org/learn/python-network-data)), this is the first time I formally write a data crawler by myself, and I did suffer a lot of problems in order to make it work.

To achieve the goal of data crawler, there are several aspects that one need to be at least familiar with:
* html language
* website API usage
* regular expression
* some third-party data crawler helper libraries

However, I have little prior knowledge about html language, except the basic concept that the html language wraps information in brackets, and have little experience in communicating with the website APIs. I also learned that I would need to use regular expression, a important practical concept in which I only have little knowlege without too much practice, to extract useful informations. The whole process is a little bit painful. But I think I have at least gained some practical experience in data crawling.

### Useful Materials and Tools

* wiki-api (https://github.com/richardasaurus/wiki-api)
This is a very good data crawler learning material for me. It had a small problem in getting the summary from Wikipedia articles, which was fixed in my own program.

* re (https://docs.python.org/2/library/re.html)
This libray allows user to use regular expression to do matching operations to extract useful information from texts.

* pyquery (https://pythonhosted.org/pyquery/)
This library is a very power tool find certain nodes containing information of interests in the html file.

* requests (http://docs.python-requests.org/en/master/)
This is a libray which is used to communicate with website APIs in the Python program.

```python
# To work with website API
# 'url' is the website API url and 'params' is the parameters for certain API function
response = requests.get(url, params)
# the response might be in different formats that the user specified
# the response is in json format
response_json = response.json()

# To get the html content of the webpage
# 'url' is the webpage url
response = requests.get(url)
response_content = response.content
```

### Choices during Development

* How to retrieve webpage content? API or Webpage Html?
The MediaWiki provides API to retrieve webpage content using its internal parser tools, such as MediaWiki TextExtracts (https://www.mediawiki.org/wiki/Extension:TextExtracts). So this raises a question. Should we use the API internal tools or parse the content by ourselves?

I think my answer might be the latter one, parsing the content by ourselves. For websites using MediaWiki API, the optional parser tools might not be installed. Even if it is installed, from my preliminary test of the tool, I found it not flexible enough to achieve my relatively more sophisticated purposes, such as getting image urls, getting data from tables, etc.

Parsing by ourselves, although might be labor entensive, could be flexible to extract almost any data of interest using a combination of tools.
