---
date: 2020-03-28 12:26:40
layout: post
title: PICKLING 
subtitle: After the model is trained we save them.
series: A Beginner's Guide to AI in Bioinformatics with Python
series_sing: true
video_number: 6
ideo_id: C2vAMliBt58
description: PICKLING is the process of saving something in python. Let's use it to save out trained models.

optimized_image: https://res.cloudinary.com/bioinformaticsguy/image/upload/c_scale,h_380/v1596696392/Machine%20Learning%20For%20Bioinformatics/MLINBINF-006.png

category: Machine Learning
tags:
  - Python
  - Machine Learning
  - Beginner
author: alihassan
paginate: true
---

{% include youtube_embed.html %}


> Website is under developement written material will be added soon!



<!-- 
hi guys
bye informatics guy here and welcome to
another video of the series machine
learning in bioinformatics in the last
video we trained the models and then
check the accuracy of the those models
before moving on to making the
protections from those models I would
like to share a very important thing and
that is saving and lowering the models
so this training is done on a very small
data so whenever we train our models it
only takes a few seconds but when you
will start to train your models on huge
tera so it is going to take a lot of
time so after training a model it is
always a good idea to save that model in
our hard desk so let's get started in
order to save the model we will be using
this library and its name is pickle it's
just like pickling in real life so we
will import pickle so saving the model
is very easy pickle dot dum then we have
to decide which model we have to save
since logistic regression is giving us
the highest accuracy we will save that
model and let's comment this out now we
have to write down the name of our model
which is model then we open a file and
the name of our file will be logistic
regression dot model or we can only
write M that will also be fine and we
just also have to define that this is
right about now that's all we have to do
to save the model and when we want to
load the model let's name this model
loaded model loaded model and it is
pickle dot load and then we have to open
our file and our filename is logistic
regression dot M and since we are going
to only read this we will write our B
let's run this no errors
now let's comment this out and now we
are going to print the accuracy by using
are loaded model and now we are using
loaded loaded model rather than using
the model and let's see Oh
model is not defined oh we don't have to
save our model again
so let's comment this out again and on
this grade we got the 97% accuracy so
that's all for this video and in the
next video we will be making our
predictions feel free to subscribe so
that you don't miss my next video thank
you very much for watching and I will
see you around in my next video  -->