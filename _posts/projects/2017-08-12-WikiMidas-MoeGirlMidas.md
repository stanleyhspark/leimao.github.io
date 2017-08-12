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
The MediaWiki provides API to retrieve webpage content using its internal parser tools, such as MediaWiki TextExtracts (https://www.mediawiki.org/wiki/Extension:TextExtracts).





        search_params = {
            'action': 'opensearch', # use 'opensearch' API
            'search': term, # search term that the user provided
            'format': 'json', # retrieved data format
            'limit': limit # maximum number of results to return (default:10, maximum: 500 or 5000?)
        }
        # Specify API url
        url = u"{scheme}://{locale_sub}.{hostname_path}".format(
            scheme = uri_scheme,
            locale_sub = self.options['locale'],
            hostname_path = api_uri
        )
        # Retrieve data from API url
        # The data retrieved from Opensearch API is an array
        # Here is a sample return from Opensearch API: https://en.wikipedia.org/w/api.php?action=opensearch&search=api&limit=10&namespace=0&format=jsonfm
        response = requests.get(url, params = search_params)



response = requests.get(url)
        response_content = response.content


* MediaWiki API mannual (https://www.mediawiki.org/wiki/API:Main_page)
Wikipedia and MoeGirl both uses MediaWiki API. One can find detailed instructions and sample codes about certain API parameters from it.
















[Micromouse](https://en.wikipedia.org/wiki/Micromouse) is a contest where small robot mice (micromouse) solve a maze. It is very popular in US, UK and Japan among the young juniors who are interested in designing robots and programming artificial intelligence. In Micromouse contest, the players are going to test their micromouse to solve the maze. 
The project goal is to design a micromouse that could explore and find destination efficiently in the virtual maze.

Here is a demo of a real micromouse contest.
<iframe width="560" height="315" src="https://www.youtube.com/embed/CLwICJKV4dw" frameborder="0" allowfullscreen></iframe>

A maze solver algorithm and a maze explorer algorithm were developed for micromouse using real-time dynamic programming. Equipped with such algorithms, the micromouse shows extremely potent ability in maze exploration optimal route planning。

### Source Codes

All the Python source codes could be downloaded from my [GitHub](https://github.com/leimao/Intelligent_Mouse).

The codes for the project includes the following files:
- maze.py   
  This script contains functions for constructing the maze objects.
- mouse.py  
  This script establishes the micromouse class controlling the actions of miromouse.
- observer.py
  This script contains some functions for micromouse movement visualization.
- planner.py
  This script contains the functions that decide micromouse's actions.
- showmaze.py
  This script can be used to create a visual demonstration of what a maze looks like.
  To run showmaze.py, run the following command in the shell:
  ```shell
  python showmaze.py test_maze_01.txt
  ```
- showmouse.py
  This script can be used to create a visual demonstration of how micromouse is exploring and solving the maze.
  To run showmouse.py, run the following command in the shell:
  ```shell
  python showmouse.py test_maze_01.txt complete

  python showmouse.py test_maze_01.txt incomplete
  ```
  where "complete" and "incomplete" designate the strategy of micromouse.
  Please also remember to hit "Enter" once in the shell to start the micromouse
- showplanner.py
  This script can be used to create a visual demonstration of the optimal actions of micromouse in the maze.
  To run showplanner.py, run the following command in the shell:
  ```shell
  python showplanner.py test_maze_01.txt
  ```
- test.py
  This script allows you to test your micromouse in different modes on different mazes.
  To run test.py, run the following command in the shell:
  ```shell
  python test.py test_maze_01.txt
  ```
  
The script uses the turtle module to visualize the maze; you can click on the window with the visualization after drawing is complete to close the window. 
To allow more changes to the micromouse, the scripts can be modified accordingly.

## Simulation Results

Watch the micromouse exploring and solving the maze on [YouTube](https://www.youtube.com/playlist?list=PLVLJFoX8B37F6t81x2bK_Pe86TU2txIFn).

Here is one of the demos showing the virtual micromouse explores and solves the virtual maze.
<iframe width="560" height="315" src="https://www.youtube.com/embed/8DZaQ8hyT10?list=PLVLJFoX8B37F6t81x2bK_Pe86TU2txIFn" frameborder="0" allowfullscreen></iframe>