---
layout: post
title: Image Resizer Python Web App
excerpt: "Host a Simple Image Resizer Web App using Python on Web Server"
modified: 2017-08-26T14:17:25-04:00
categories: project
tags: [Web App]
image:
  teaser: /images/projects/2017-08-26-Image-Resizer-Web-App/image_resizer_teaser.png
comments: true
share: true
---

### Introduction

Since I am hosting my own websites, I sometimes have to prepare some png-formatted images with the right size for my website. So I developed this [Image Resizer](http://imageresizer.pythonanywhere.com/) web application using Python in two days, and hosted it on PythonAnywhere. This is formally my first experience of developing web applications, and I think I have learned a lot.

### Mannual

This is the Image Resizer Web Application Interface. It is extremely simple and advertisement free. You will just have to select your image file, select the resizing mode (use width and height / use ratio), and input your parameter. The Image Resizer could enlarge or shrink the images. But the performance of shrinking images is the best. After submitting the image and parameters, you will be allowed to download the image resized in png format.

<figure>
    <img src = "{{ site.url }}/images/projects/2017-08-26-Image-Resizer-Web-App/image_resizer_index.png">
    <figcaption>Image Resizer Web Application Interface</figcaption>
</figure>

### Development Experience

I have never developed my own web applicaton before, and I have only tried a simple web application tutorial provided by Python Anywhere (see my [article](https://leimao.github.io/article/PythonAnywhere-WebApps-Getting-Started/)).

#### Resizing Functions
The image resizing function is simple because I used OpenCV to resize the images. The most important part of this project is to learn how to use Flask to build your Python web applications. 

{% highlight python %}
# Resize a image using user-defined parameters
def resizer_ratio(img, fx = 1, fy = 1):
    res = cv2.resize(src = img, dsize = None, fx = fx, fy = fy, interpolation = cv2.INTER_AREA)
    return res

def resizer_defined(img, width = None, height = None):
    res = cv2.resize(src = img, dsize = (width, height), fx = 0, fy = 0, interpolation = cv2.INTER_AREA)
    return res
{% endhighlight %}

#### Choice of Web App Framework

I was hesitating whether I have to use Flask or Dejango. The feedback from Google and Quora is that Flask is more simple, user-friendly, and more convenient for simple applications, while Dejango, though more powerful and structured for large and complicated applications, might be hauting for new users without too much web app development experience. So my choice became Flask.

#### Choice of Hosting Server

I have a little bit experience of using PythonAnywhere to host Python programs. It is very user-friendly. You do not even have to know how to use vim because it provides a text editor on the web control end. The more important thing is that its basic account is free. Every basic account could host one web application. So my choice is no doubt PythonAnywhere.

#### Web Application Organization

The index() route render the Image Resizer Interface. Once the image and parameters were submitted, it directed to upload() to upload the image to the server, and cache the parameter. After successful upload, the image was resized in resize_image(). The file sizes before and after resize were calculated, and the filename of resized image was also cached.. When resizing image is finished, the user will be directed to a 'download' webpage, where there is a buttom for click to download. Once the buttom is clicked, the download() was activated and the resized image will be send to your computer from the server.

{% highlight python %}
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/upload', methods=['GET', 'POST'])
def upload():
    ...
    return redirect(url_for('resize_image'))

@app.route('/resize')
def resize_image():
    ...
    return render_template('download.html', filesize_original = filesize_original, filesize_resized = filesize_resized)

@app.route('/download', methods=['GET', 'POST'])
def download():
    ...
    return send_from_directory(directory = app.config['DOWNLOAD_FOLDER'], filename = filename_resized)
{% endhighlight %}

There might be some rendering issue due to browser cache for the resized image. It was resized but the browser rendered a cached image. I tried hard to solve this. Although I have no idea about the mechanism, the following code seems to help.

{% highlight python %}
app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 300

@app.after_request
def add_header(r):
    """
    Add headers to both force latest IE rendering engine or Chrome Frame,
    and also to cache the rendered page for 10 minutes.
    """
    r.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    r.headers["Pragma"] = "no-cache"
    r.headers["Expires"] = "0"
    r.headers['Cache-Control'] = 'public, max-age=0'
{% endhighlight %}

#### Caveats on PythonAnywhere

After preparing all the python application code and html files, the test of the application was successful on my local machine. However, when I tested the application on PythonAnywhere, some error poped up. 

* Absolute Path
PythonAnywhere does not support file operations using relative path. You will have to use absolute path instead. To do this, first find out the absolute path of current folder and concatenate the folder absolute path to your file/folder name.

{% highlight python %}
# This folder path
THIS_FOLDER = os.path.dirname(os.path.abspath(__file__))

# This is the path to the upload directory
app.config['UPLOAD_FOLDER'] = os.path.join(THIS_FOLDER, 'uploads/')
app.config['DOWNLOAD_FOLDER'] = os.path.join(THIS_FOLDER, 'downloads/')
{% endhighlight %}

* OpenCV3 Installation
There was OpenCV2 (for Python 2.7) pre-installed on the server. However, I need OpenCV3 (for Python 3.6) because I developed the application in Python 3.6 and Flask 0.12 was also for Python 3.6. Unlike usual pip install, to install new packages on PythonAnywhere server:

{% highlight shell %}
# Pip install package
pip install --user package
# Pip install OpenCV3
pip3.6 install --user opencv-python
{% endhighlight %}

#### Some Features

* Examine the format of image for submission.
* Restrict the image size for submission to prevent blowing the server.
* Clear the images stored on the server routinely to prevent hitting the server hard disk limit.
* Show the size of images before and after resizing.

### User Feedback

Thank Guotu Li, Jianhai Zhang and Di Wang for initial testings and feedbacks.

* Ugly interface

The interface was written in pure html. I have no knowledge about how to make a good web UI interface.

* Image sizer became larger after shrinking

For some original small-sized image, after shrinking, the size became a little bit bigger. I think it due to the resize function and image-save function in OpenCV. I tested some compression parameters of OpenCV image-save functions. But they do not make too much difference. I will study OpenCV in depth in the future if I get chance.

### Source Code

To view source code, please visit my [GitHub](https://github.com/leimao/Image_Resizer).