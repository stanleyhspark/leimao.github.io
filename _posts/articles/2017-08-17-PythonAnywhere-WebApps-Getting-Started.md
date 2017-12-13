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

#### An Extremely Simple "Hello World" Web App

In the firt part of the tutorial, it taught you how to manage your source code files on PythonAnywhere. I was surprised that they even have a source code control system, just like GitHub, in their system. You will have to do all these "git" things in their console (I got too used to do "git" things in "clickable" GitHub Destop). For editing or submitting your source code, you can edit the file in the text editor in the broswer or just submit from your own local machine. Everything is easy and straightforward. Here is the first web-hosted application I made. It should be noted that the application might be expired because of the limit of the free account.

```python
# A very simple Flask Hello World app for you to get started with...
from flask import Flask

app = Flask(__name__)

# Return at the root page
@app.route('/')
def hello_world():
    return 'Hello from Flask!'

# Return at the foo folder
@app.route('/foo')
def hello_world_2():
    return 'Welcome to the foo inside Flask!'
```

Go to [http://leimao.pythonanywhere.com/](http://leimao.pythonanywhere.com/), it will show a "hello world" message.
Go to [http://leimao.pythonanywhere.com/foo](http://leimao.pythonanywhere.com/foo), it will show another "hello world" message.

<br />

Those two are simple webpages. However, what's different to ordinary HTML webpages is that there are no HTML files. The text messages are the returns from certain Python functions when you go to the urls specified.

#### A More Advanced "Comment" Web App

In the second part of the tutorial, it taught us how to make a database backended comment application.

```python
# A very simple Flask Hello World app for you to get started with...
from flask import Flask, render_template

app = Flask(__name__)

# To help debug the code
app.config["DEBUG"] = True

@app.route("/")
def index():
    return render_template("main_page.html")
```

```html
<!DOCTYPE html>
<--!main_page.html-->
<html>
    <head>
        <title>My scratchboard page</title>
    </head>

    <body>
        <div>
            This is the first dummy comment.
        </div>

        <div>
            This is the the second dummy comment.  It's no more interesting than the first.
        </div>

        <div>
            This is the third dummy comment.  It's actually quite exciting!
        </div>

        <div>
            <form action="." method="POST">
                <textarea name="contents" placeholder="Enter a comment"></textarea>
                <input type="submit" value="Post comment">
            </form>
        </div>
    </body>
</html>
```

Go to [http://leimao.pythonanywhere.com/](http://leimao.pythonanywhere.com/). The main_page.html will be presented. 

<figure>
    <img src = "{{ site.url }}/images/articles/2017-08-17-PythonAnywhere-WebApps-Getting-Started/post_comment.png">
</figure>

Let us add some elements to make the site fancier.

```html
<!DOCTYPE html>
<--!main_page.html-->
<html>
    <head>
        <meta charset="utf-8">
        <meta http-equiv="X-UA-Compatible" content="IE=edge">
        <meta name="viewport" content="width=device-width, initial-scale=1">

        <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.5/css/bootstrap.min.css" integrity="sha512-dTfge/zgoMYpP7QbHy4gWMEGsbsdZeCXz7irItjcC3sPUFtf0kuFbDz/ixG7ArTxmDjLXDmezHubeNikyKGVyQ==" crossorigin="anonymous">

        <title>My scratchboard page</title>
    </head>

    <body>
        <nav class="navbar navbar-inverse">
          <div class="container">
            <div class="navbar-header">
              <button type="button" class="navbar-toggle collapsed" data-toggle="collapse" data-target="#navbar" aria-expanded="false" aria-controls="navbar">
                <span class="sr-only">Toggle navigation</span>
                <span class="icon-bar"></span>
                <span class="icon-bar"></span>
                <span class="icon-bar"></span>
              </button>
              <a class="navbar-brand" href="#">My scratchpad</a>
            </div>
          </div>
        </nav>

        <div class="container">

            <div class="row">
                This is the first dummy comment.
            </div>

            <div class="row">
                This is the the second dummy comment.  It's no more interesting
                than the first.
            </div>

            <div class="row">
                This is the third dummy comment.  It's actually quite exciting!
            </div>

            <div class="row">
                <form action="." method="POST">
                    <textarea class="form-control" name="contents" placeholder="Enter a comment"></textarea>
                    <input type="submit" value="Post comment">
                </form>
            </div>

        </div>

    </body>
</html>

```

The interface now looks like this:

<figure>
    <img src = "{{ site.url }}/images/articles/2017-08-17-PythonAnywhere-WebApps-Getting-Started/post_comment_2.png">
</figure>

So far, we have finished making the web application interface. However, the application is not functional because it is not able to receive message from the user. What we are going to do next is to add this feature. For the moment, we use temporary list to show the comments.


```python
from flask import Flask, redirect, render_template, request, url_for

app = Flask(__name__)
app.config["DEBUG"] = True

comments = []

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "GET":
        return render_template("main_page.html", comments=comments)

    comments.append(request.form["contents"])
    return redirect(url_for('index'))
```


```html
<!DOCTYPE html>
<--!main_page.html-->
<html>
    <head>
        <meta charset="utf-8">
        <meta http-equiv="X-UA-Compatible" content="IE=edge">
        <meta name="viewport" content="width=device-width, initial-scale=1">

        <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.5/css/bootstrap.min.css" integrity="sha512-dTfge/zgoMYpP7QbHy4gWMEGsbsdZeCXz7irItjcC3sPUFtf0kuFbDz/ixG7ArTxmDjLXDmezHubeNikyKGVyQ==" crossorigin="anonymous">

        <title>My scratchboard page</title>
    </head>

    <body>
        <nav class="navbar navbar-inverse">
          <div class="container">
            <div class="navbar-header">
              <button type="button" class="navbar-toggle collapsed" data-toggle="collapse" data-target="#navbar" aria-expanded="false" aria-controls="navbar">
                <span class="sr-only">Toggle navigation</span>
                <span class="icon-bar"></span>
                <span class="icon-bar"></span>
                <span class="icon-bar"></span>
              </button>
              <a class="navbar-brand" href="#">My scratchpad</a>
            </div>
          </div>
        </nav>

        <div class="container">

            {% for comment in comments %}
                <div class="row">
                    {{ comment }}
                </div>
            {% endfor %}

            <div class="row">
                <form action="." method="POST">
                    <textarea class="form-control" name="contents" placeholder="Enter a comment"></textarea>
                    <input type="submit" value="Post comment">
                </form>
            </div>

        </div>

    </body>
</html>
```

<figure>
    <img src = "{{ site.url }}/images/articles/2017-08-17-PythonAnywhere-WebApps-Getting-Started/post_comment_3.png">
</figure>

#### Add Back-Ended Database to "Comment" Web App

As is mentioned in the PythonAnywhere documentation, "SQLite is pretty slow on PythonAnywhere, and doesn't scale well for larger sites anyway. Postgres is a paid feature on PythonAnywhere because of its larger server power requirements, and we don't have built-in support for MongoDB. So we're going to use MySQL, which you can use from a free PythonAnywhere account." So probably the best choice is to go with MySQL.

```python
from flask import Flask, redirect, render_template, request, url_for
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

# To help debug the code
app.config["DEBUG"] = True

# Connection configurations to database
SQLALCHEMY_DATABASE_URI = "mysql+mysqlconnector://{username}:{password}@{hostname}/{databasename}".format(
    username="leimao",
    password="********", # database passowrd hidden
    hostname="leimao.mysql.pythonanywhere-services.com",
    databasename="leimao$comments",
)
app.config["SQLALCHEMY_DATABASE_URI"] = SQLALCHEMY_DATABASE_URI
app.config["SQLALCHEMY_POOL_RECYCLE"] = 299 # connection timeouts
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False # no warning disruptions

db = SQLAlchemy(app)

class Comment(db.Model):

    __tablename__ = "comments"

    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.String(4096))

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "GET":
        return render_template("main_page.html", comments=Comment.query.all())

    comment = Comment(content=request.form["contents"])
    db.session.add(comment)
    db.session.commit()
    return redirect(url_for('index'))
```

The final web application looks like this:
<figure>
    <img src = "{{ site.url }}/images/articles/2017-08-17-PythonAnywhere-WebApps-Getting-Started/post_comment_4.png">
</figure>

One can visit this web application at [http://leimao.pythonanywhere.com/](http://leimao.pythonanywhere.com/). The "user name" is "leimao", and the password is "123456".

### Conclusions

We have implemented a simple web application on PythonAnywhere. To host a more complicated web application in the future, I need to become more efficient in database coding (I have not used database for a very long time)and get familiar with the usage of Flask or Django.

### Supplementations

Concept of model inheritence:
[https://docs.djangoproject.com/en/1.11/topics/db/models/](https://docs.djangoproject.com/en/1.11/topics/db/models/)