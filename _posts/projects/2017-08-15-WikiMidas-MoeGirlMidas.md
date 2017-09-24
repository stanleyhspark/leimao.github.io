---
layout: post
title: WikiMidas and MoeGirlMidas
excerpt: "MediaWiki Webpage Crawler"
modified: 2017-08-15T14:17:25-04:00
categories: project
tags: [Data Crawling]
image:
  teaser: /images/projects/2017-08-15-WikiMidas-MoeGirlMidas/moegirl_teaser.png
comments: true
share: true
---

### Introduction

[WikiMidas](https://github.com/leimao/WikiMidas) is a Python spidering API wrapper program specifically designed for data crawling from [MediaWiki APIs](https://www.mediawiki.org/). It could be used to retrieve information from [Wikipedia](https://en.wikipedia.org/wiki/Main_Page) and [MoeGirl](https://zh.moegirl.org/Mainpage) which uses MediaWiki as their APIs. MoeGirl is more focused on the articles in the finctional characters' in anime. [MoeGirlMidas](https://github.com/leimao/MoeGirlMidas), developed based on WikiMidas, are designed specifically to retrieve characters' data from MoeGirl.

<br />

I named the two programs after "midas". Because I like the "feel" that you touch something and something becomes useful.

<div class = "titled-image">
<figure>
  <img src="{{ site.url }}/images/projects/2017-08-15-WikiMidas-MoeGirlMidas/midas.gif"/>
</figure>
</div>

### Learning Experience

I have little experience in writing a program to retrieve data from internet by myself. So, In addition to some practice program experience in MOOC courses ([Using Python to Access Web Data](https://www.coursera.org/learn/python-network-data)), this is the first time I formally write a data crawler by myself, and I did suffer a lot of problems in order to make it work.

<br />

To achieve the goal of data crawler, there are several aspects that one need to be at least familiar with:
* html language
* website API usage
* regular expression
* some third-party data crawler helper libraries

However, I have little prior knowledge about html language, except the basic concept that the html language wraps information in brackets, and have little experience in communicating with the website APIs. I also learned that I would need to use regular expression, a important practical concept in which I only have little knowlege without too much practice, to extract useful informations. The whole process is a little bit painful. But I think I have at least gained some practical experience in data crawling.

### Useful Materials and Tools

#### [wiki-api](https://github.com/richardasaurus/wiki-api)
This is a very good data crawler learning material for me. It had a small problem in getting the summary from Wikipedia articles, which was fixed in my own program.

#### [re](https://docs.python.org/2/library/re.html)
This libray allows user to use regular expression to do matching operations to extract useful information from texts. The usage of this library might be easy. But the key is to understand regular expression and use the correct regular expression to match the thing you are looking for.

{% highlight python %}
# To compile a message to regular expression
empty_regex = re.compile(message)
# To remove a string that matches certain regular expression
text = re.sub(regex, '', text, flags)
{% endhighlight %}

#### [pyquery](https://pythonhosted.org/pyquery/)
This library is a very power tool find certain nodes containing information of interests in the html file.

{% highlight python %}
# Make PyQuery object from a html file
# 'response_content' is a html file
html = pq(response_content)
# Query certain node
html('body')
# Query certain class
html('.mw-content-ltr')
# Query certain id
html('#firstHeading')
# Find all the subnodes
html('body').find('h2')
html('body').find('h2, p')
# Get attributs
html('body').find('.image').find('img').attr('src')
# Get text
html('#firstHeading').text()
{% endhighlight %}

#### [requests](http://docs.python-requests.org/en/master/)

This is a libray which is used to communicate with website APIs in the Python program.

{% highlight python %}
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
{% endhighlight %}

### Choices during Development

How to retrieve webpage content? API or Webpage Html?
The MediaWiki provides API to retrieve webpage content using its internal parser tools, such as [MediaWiki TextExtracts](https://www.mediawiki.org/wiki/Extension:TextExtracts). So this raises a question. Should we use the API internal tools or parse the content by ourselves?

<br />

I think my answer might be the latter one, parsing the content by ourselves. For websites using MediaWiki API, the optional parser tools might not be installed. Even if it is installed, from my preliminary test of the tool, I found it not flexible enough to achieve my relatively more sophisticated purposes, such as getting image urls, getting data from tables, etc.

<br />

Parsing by ourselves, although might be labor entensive, could be flexible to extract almost any data of interest using a combination of tools.

### MoeGirlMidas Demo


MoeGirlMidas was wrapped into a class object called "MoeGirlAPI". To use MoeGirlMidas in your Python program:

{% highlight python %}
from moegirlmidas import MoeGirlAPI
moegirl = MoeGirlAPI()
# To search for certain query in MoeGirl
# term is the keyword you are interested in; limit is the maximum number of returns
# the return is a list of relavant article titles found
search_result = moegirl.search(term = '神裂火织', limit = 50)
for item in search_result:
    print(item)
{% endhighlight %}
{% highlight shell %}
>>>
神裂火织
{% endhighlight %}
{% highlight python %}
# To retrieve article from MoeGirl
# title is the title of the article you want to retrieve from MoeGirl
# the return is article-class object containing 'heading', 'summary', 'content', 'properties', 'image', 'references' and 'url'
article = moegirl.retrieve(title = '神裂火织')
# To view the article content
print article.heading
{% endhighlight %}
{% highlight shell %}
>>>
神裂火织
{% endhighlight %}
{% highlight python %}
print article.image
{% endhighlight %}
{% highlight shell %}
>>> 
https://img.moegirl.org/common/thumb/f/fd/Kanzaki_Kaori.jpg/250px-Kanzaki_Kaori.jpg
{% endhighlight %}
{% highlight python %}
print article.summary
{% endhighlight %}
{% highlight shell %}
>>>
神裂火织是轻小说《魔法禁书目录》及其衍生的漫画、动画、游戏等作品的登场角色。
{% endhighlight %}
{% highlight python %}
print article.content
{% endhighlight %}
{% highlight shell %}
>>>
神裂火织

神裂火织 是轻小说《魔法禁书目录》及其衍生的漫画、动画、游戏等作品的登场角色。

目录

人物名片

职业：魔导师（伦敦排行前5）

魔法名：Salvere000（寄托意：对无法拯救之人伸出援手）

人物简介

英国清教必要之恶教会的魔法师。18岁，伦敦排行前五的魔导师，世界上不到20位的圣人之一。天草式十字凄教的 女教皇 。身穿T-shirt与牛仔裤的高窕 巨乳 少女。必杀技是 七千元 「七闪」和「唯闪」。

因为害怕自己强大的力量，会将无辜的他人卷入，一度选择离开天草式。拥有着「对受遗弃者伸出救赎之手」的博爱精神，从不杀人，也绝对无法允许有人在自己眼前被杀。

束成 马尾 的 黑色长发 垂至腰际、身材高窕皮肤白皙的美女。对人很有礼貌，口调犹如体现着古代 大和抚子 的精神。性格认真注重义理，将感情全都压在沉着冷静的表情之下。

身上穿着在腰部扎起的T恤，有时也会披着牛仔布质外套，下身总是穿着牛仔裤。但外套右手臂的部分连肩膀一起被切断，相反地，牛仔裤则是从左腿根部开始整条裤管切掉。 上条当麻子 曾 娇羞地 觉得神裂的服装很「色情」。实际上，左右不对称是因为神裂术式组成上的需要，神裂并不是故意要暴露身体曲线。 曾经因为七千元将上条当麻打伤，事后表示要用身体补偿。 在打死编者之前请查看魔法禁书目录的特典

幸运之处

与上条当麻的不幸相对立，神裂是一个从出生开始就相当幸运的人。出生前就被指定为“天草式十字凄教”的女教皇，拥有即使不用努力也可以获得成功的才能；什么都不用做就可以得到位居群众中心点的人望；每天都在发生连她自己都意料不到的惊喜；就算遭到暗杀，她也可以侥幸存活，子弹会毫无理由地射偏，就算炸弹在身边爆炸，也可以奇迹似地毫发无伤。

但是，神裂无法原谅自己这种为周围带来“不幸”的“幸运”人生。因为害怕自己强大的力量，会将无辜的他人卷入，一度选择离开天草式。为了保护身边的人，神裂只能压抑住想跟他们在一起的心情，自己选择了孤独。

魔法招式

七闪

神裂操纵七条钢丝所施展出的斩击，以看不见的速度撕裂对手，让眼前的一切全都如黏土般迸裂，可以说是非常恐怖的招式。攻击时神裂的拔刀动作为的是掩饰操纵钢丝的手，而实际上神裂根本没有拔刀，只是将刀从刀鞘中稍微拔出，然后又推回去罢了。其速度可以在一瞬间杀人七次，故被称做“瞬杀”。
利用“七闪”的钢丝，将其最大限度地展开，通过割裂空气还可以进行高空下落时的减速。

唯闪

神裂使用“七天七刀”的拔刀术。“十字教的术式不行的话就用佛教术式，佛教术式不行的话就用神道术式，神道术式不行的话就用十字教术式  ”，像这样借由适当互补彼此的弱点，发挥出完全破坏力的独一无二攻击术式便是“唯闪”。对特定宗教迂回使出其他教义的术式攻击，这样的一击就连天使也能切断。
“唯闪”是在瞬间使用“神之子”力量的招式，身为“圣人”神裂可以使用部分的“神之子”的力量。“唯闪”发动时，神裂被强行引出的威力，会超过肉体能操纵的运动量，所以不可能在这种状态下长时间进行战斗。正因如此，神裂的“唯闪”才要淬炼成一发就能决胜负的拔刀术。在面对大天使“神之力”加百列和后方之水的时候，都因为长时间使用身为“圣人”的力量而使身体濒临崩溃边缘  。

外部链接与注释

（日文） 官方人物介绍： http://www.project-index.net/contents/hp0006/index00840000.html

导航菜单

{% endhighlight %}
{% highlight python %}
for key in article.properties.keys():
    print key, ':', article.properties[key], '\n'
{% endhighlight %}
{% highlight shell %}
>>>
发色 : 黑发 

活动范围 : 世界各地 

瞳色 : 紫瞳 

声优 : 伊藤静 

所属团体 : 英国清教必要之恶教会，天草式十字凄教 

relatives : 上条当麻 ， 茵蒂克丝 ， 萝拉·斯图亚特 ， 史提尔·马格努斯 

出身地区 : 日本 

别号 : 大姐头 

姓名 : 神裂 （ かんざき ） 火織 （ かおり ） （Kanzaki Kaori） 

年龄 : 18岁 

身高 : 175cm以上 

萌点 : 单马尾 、 御姐 、 巨乳 、圣人、女武者、 大和抚子 、单裤腿 
{% endhighlight %}

The Python script could also be run directly in the shell (the shell might have conflicts with Chinese characters):

To search article
{% highlight shell %}
python moegirlmidas.py -s "神裂火织"
{% endhighlight %}

To retrieve article
{% highlight shell %}
python moegirlmidas.py -r "神裂火织"
{% endhighlight %}
The sample codes above could also be run in a Jupyter Notebook. See the run results [here](https://github.com/leimao/MoeGirlMidas/blob/master/sample_code.ipynb).

