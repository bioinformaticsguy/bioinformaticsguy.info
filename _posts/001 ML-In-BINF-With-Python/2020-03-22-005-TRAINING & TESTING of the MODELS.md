---
date: 2020-03-22 12:26:40
layout: post
title: TRAINING & TESTING of the MODELS
subtitle: We need to train and test the models and finding out the model with best accuracy.


series: A Beginner's Guide to AI in Bioinformatics with Python
series_sing: true
video_number: 5
video_id: dhBvm3whRUE
description: In order to make predicitons we need to train a few models and then to test them to see which one performs the best.
optimized_image: https://res.cloudinary.com/bioinformaticsguy/image/upload/c_scale,h_380/v1596696392/Machine%20Learning%20For%20Bioinformatics/MLINBINF-005.png

category: Machine Learning
tags:
  - Python
  - Machine Learning
  - Beginner
author: aliHassan
paginate: true
---

{% include youtube_embed.html %}

This post will be updated soon.

<!-- Let's get started with part 5 of the series [__Machine Learning in Bioinformatics With Python__](/001-Machine-Learning-in-Bioinformatics-With-Python). Previously videos we have downloaded the data from [__UCI Repository__](http://archive.ics.uci.edu/ml/datasets/breast+cancer+wisconsin+%28diagnostic%29) and we are also preprocessed our data.

> In this video we will be doing the training and testing of the models. We will split the data into the training dataset and the testing dataset. Eventually we will train our models by using two classifiers SVC and logistic regression.


First of all let's import a few things we will be needing  `train_test_split` , `LogisticRegression` and `SVC` . See the code block below.

{% highlight python %}
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.svm import SVC
{% endhighlight %}

Let's move on to splitting our datasets into training and testing. So we need `X_train` `X_test` `y_train` and `y_test` ( by convention y variable for the labels is kept small).


 now we are going to use the train and test blade we are
supposed to give the x and y our test size is going to be 0.1 0.1 means that the 10% of the data will be used as test and the remaining 90% will be used to
train the data and then we can also set the random stay random stay equals to 0 that's how we are going to split the data let's run this and see that there
is no errors okay fine so let's start the training we will first go for the SVC classifier so defining a classifier is very easy we just have to slide down
the name of her classifier say it las afire equals to SVC and close brackets that's how easy it is the next is we have to define our model models equals
to classifier dot fit and then we have to give the data it will be X trains comma Y train so the first line of code will define the models and the second
line of code will train the model over here we have to check the accuracy so we can say it accuracy equals to model our core core we are going to check the
accuracy on the test data so X test comma Y test and let's print the accuracy brain accuracy of as we see is AC thank you let's run this so we got
98% accuracy that's very darn good as you know in the first video I mentioned that we will get much more accuracy than the previous
studies which was I guess around 93 so it is also giving us warning and it so it's saying that you you need to set the gamma value so we can do this by
defining the kernel so we can say that kernel equals to linear let's run this again and see if the warning is going oh oh I messed up the linear spelling Li
near-60 creased and with the linear kernel we are not getting good accuracy we are getting 95% accuracy so let's try another classifier logistic regression
now you might get confused that this is logistic progression and regression is mostly when you are trying to predict the continuous values but here we are
doing binary classification but the thing is the name of this is a bit confusing and it is going to do the same classification so we will do the same
thing classifier equals to logistic regression and then model equals to classifier dot fit and in the brackets we are going to we are going to give it
a training data by train and then a QA C equals to model dot score and X test comma Y test now let's place the accuracy let's copy it okay
and we are gonna do it I'll just take regression alright let's see what's accuracy of logistic regression oh the accuracy of logistic regression is 97
percent and we are also getting some warnings over here it's saying that the default order will be change so we need to specify the solver and we can do that
in the bracket over here and let's so lver solver equals 2 let's use linear now you might be wondering from where I know that this we can keep the kernel as
linear or live linear now the thing is let me show you that you can go to the website you can simply google it logistic regression sq learn and you can
see that what are the different kernels and solvers available for this logistic regression classifier and you can use according to your needs now you want to
go deep into it then you can start to learn what is the basic difference between the solvers and what is the different between the kernels and what
is kernel basically so this is the basic tutorial and I'm not going to explain everything this is just to implement the machine learning classifiers and model
for a very simple data here are different solvers right we can use any of the solvers but live linear works best with this so we will use this
solver Wow we got 97% accuracy an that's pretty good now that's all for today we are done with training our models and in the next video we will be
making some prediction so don't forget to subscribe my channel to watch the next video which is going to be really interesting thank you very much for
watching and I will see you around in the next video  -->