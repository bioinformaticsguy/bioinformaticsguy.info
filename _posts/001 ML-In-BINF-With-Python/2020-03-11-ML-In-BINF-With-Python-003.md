---
date: 2020-03-11 12:26:40
layout: post
title: PREPROCESSING OF THE DATA
subtitle: In this video we will be learning about the preprocessing of the data!

series: A Beginner's Guide to AI in Bioinformatics with Python
series_sing: true
video_number: 3
description: Most of the times the data is not in tidy form and is not in the usable shape this is when preprocessing comes in handy.
optimized_image: https://res.cloudinary.com/bioinformaticsguy/image/upload/c_scale,h_380/v1596696392/Machine%20Learning%20For%20Bioinformatics/MLINBINF-003.png

category: Machine Learning
tags:
  - Python
  - Machine Learning
  - Beginner
author: alihassan
paginate: true
---

{% include youtube_embed.html id="V8zwd42gDNk" %}

> Website is under developement written material will be added soon!


<!-- 

hating guys bioinformatics guy here and
welcome to another video of the series
machine learning in bioinformatics in
this video we will be talking about the
pre-processing of their era so what is
pre-processing just like in the previous
video you have seen that that era on its
own but not making any sense to us so we
use the name soil and created a CSV file
and open it in Excel to see what is this
data trying to tell us by the same token
the machine learning models cannot
understand and they cannot process the
data on its own so we have to follow a
few rules and we have to make that data
understandable by that machine learning
model so pre-processing mostly includes
removing the unwanted values removing
those values which are going to confuse
a machine learning model and sometimes
following the conventions is also a part
of pre-processing so let's get started
as you can see that this is the ID
column and this the purpose of this ID
column is just to recognize the sample
it is not adding the information to the
definition of this class right over here
so we have to remove it before feeding
it to our machine learning model the
next thing is the missing values most of
the times in the data the missing values
are represented by question marks or n a
n in this era we can see that the
missing values are represented by the
question mark so question mark is not a
numeric value and if we will feed these
this data right away the program is
going to consider it as a string so we
have to change it to a numeric value
most of the times the missing values are
converted into minus 9 9 9 so we have to
change this question mark to minus nine
nine nine all the question marks in the
data so next thing is more of a
convention so it's not compulsory to do
this but it's a good idea to follow that
you can see that in this class column
there are only twos and fours we have
also read this in the names file
the last video it was written over there
that Tori's to represents the benign and
poor represents the malignant tumors
this is a binary data there are only two
conditions like the tumor is either
benign or it's malignant the convention
of the binary data is that it is
supposed to be in zeros and one so we
will change this to two zero and four to
one so then the zero will be
representing benign and poor will be
representing malignant so let's start
writing our code now we can directly
read our CSV file that we created in the
last video so we will comment this out
and reading the file is similar so we
just have to change the name of the file
over here there are our CSV so we have
imported our file now we have to drop
the ID column if you want to see how
Dera looks in Python you can write print
data dot head rather than printing the
whole data data dot had just print the
few of the columns and it just gives the
rough idea of the data how the develops
so let's run this and see how it looks
so as you can see that there are five
rows and eleven columns and ID column is
included right now so we have to remove
this ID column and removing the ID
column is also very simple
there are dot drop we are going to drop
a column now we have to mention the name
of our column which is ID since we don't
want to replace it with any other thing
so we will keep in place equal to true
since we want to remove a column so we
we have to specify that access equal to
one so this is going to drop the ID
column now let's print at after the ID
column is drawn you can see that the ID
column is drop and now there are only
ten columns now we have to place the
missing values okay and in order to
replace the missing values we there is a
replace function so data dot replace now
we have to tell this function but what
do we want to replace so we want to
replace question marks with minus nine
nine nine nine nine five nines and we
also don't want to we also not want to
replace with anything so we will keep in
place equals to true so this line of
course we will change the missing values
now the next thing is we have to change
the force in this class to one and the
twos into zero so we will be using the
map function and the map functions
requires and other functions to follow
so we will have to define our function
which will return one if the value is
four and zero if the value is two today
we are going to learn how to define a
function in Python so dei f this is the
keyword to define a function and next is
the name of the function return ten
binary and in the parenthesis we have to
mention the arguments or the inputs that
we are going to
to the function so we will check that if
x equals two for return 1 else return
zero all right so we have created our
function the next thing is to use this
function so we have to use this function
or this on this class column so we will
write down data in the parent issues we
will write the name of the name of our
column class and next dot now we are
going to use the map function map and in
the parenthesis we have to write down
the name of the function that we just
defined return bin so let's run this
code and see if the class is now in the
binary oh there is an error so the tea
is supposed to be Cavanaugh we also have
to write the print statement again tarah
dot head all right so now you can see
that all the tools are changed to 0 and
the 4 is change 1 so that's all we are
going to do but I also want to share a
track with you you can see that we have
to write down four to five lines of code
to change the classes to ones and zeros
let me tell you that you can do the same
thing in just one line you can do that
by using the lambda functions lambda is
an anonymous function and it is only
created when it's needed we are going to
use the same line so we just have to
define our lambda function over here so
L am BD a lambda and this is our input
so it will return 1 if x equals 2 for
else 0
so this these five lines and this last
line is going to do the same thing let's
print the header again you can see that
we got the same result so this is a very
basic kind of data there are only two
classes so that's all the pre-processing
we are going to need for this data so
that's all for today in the next video
we will be talking about defining the
features and the label do subscribe if
you haven't already so that you don't
miss my videos I will see you around in
my next videos  -->