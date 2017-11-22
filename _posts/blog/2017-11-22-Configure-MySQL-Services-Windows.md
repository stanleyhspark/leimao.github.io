---
layout: post
title: "Configure MySQL Services on Windows"
excerpt: "My first touch to the Windows services"
modified: 2017-11-22T14:17:25-04:00
categories: blog
tags: [Windows Services, MySQL]
comments: true
share: true
---

### Introduction

I am learning PHP recently so I wanted to install MAMP on my laptop. The installation was successful. However, when I started to run MAMP, it raised the warning "mysql needs open port 3306 ..." because MAMP uses MySQL. This reminded me that I have already installed MySQL on my laptop and the service was always running. Since I do not want to delete MySQL, I need to find a way to get MAMP and MySQL stay peacefully together. One way to solve the problem is to use another port, other than port 3306, for MAMP. But I don't like it. I want to assign the port to MAMP or MySQL whenever I want to use either one. Running MySQL constantly from Windows startup does not make sense to me, since it is only a laptop for local test but not service host.

### Solution

I did some Google searches and found the solutions. To manipulate the Windows services, one have to run commands as **administrator** in the terminal (Right click the terminal and run as administrator).

<br />

The MySQL service name might be different to "MySQL". To find out the MySQL service name, run the following command to find MySQL services among all the services.

```shell
sc query type= service
```

My MySQL service name is "Thinkpad-Mysql" (I configured it and later I forgot). To stop the service, run the following command.

```shell
net stop Thinkpad-Mysql
```

However, it is still not enough. Next time you start the computer, the "Thinkpad-Mysql" service will automatically run since startup. To prevent his, run the following command.

```shell
sc config Thinkpad-Mysql start= disabled
```

To restart "Thinkpad-Mysql" service, basically reverse the command we have run.

```shell
sc config Thinkpad-Mysql start= auto
net start Thinkpad-Mysql
```

### Notes

I also tried to set the "Thinkpad-Mysql" service "manual" by running the following command.
```shell
sc config Thinkpad-Mysql start= manual
```

However, I failed. But the following command seems to work for "mannual" (Check [Microsoft Documentation](https://technet.microsoft.com/en-us/library/cc990290(v=ws.11).aspx)). 

```shell
sc config Thinkpad-Mysql start= demand
```

If the service becomes "demand", it could be turned on or off by running single commands.

```shell
net start Thinkpad-Mysql
```

or

```shell
net stop Thinkpad-Mysql
```
