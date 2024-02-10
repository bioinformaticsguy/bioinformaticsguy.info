---
date: 2020-07-15 12:26:40
layout: post
title: SIMPLE VALUES
subtitle: The building Blocks.

series: PYTHON FOR BIOINFORMATICS
series_sing: true
video_number: 2
video_id: KUXgAjSz4ro
description: If you have never learned programing language and you are from the field of Biology. You can learn python with examples from the realm of Biology. 

optimized_image: https://res.cloudinary.com/bioinformaticsguy/image/upload/c_scale,h_380/v1596701389/002%20Python-for-Bioinformatics/Python-for-Bioinformatics-002.png


category: Python Basics
tags:
  - Python
  - Basics
  - Bioinformatics
author: alihassan
paginate: true
---

{% include youtube_embed.html %}


Hey there, bioinformatics enthusiasts! Welcome back to another installment of our Python for Bioinformatics series. 
Today we'll delve into the fundamentals of simple values in Python, including booleans, integers,
floats, special values, and the ever-important strings.

# Booleans
The boolean value (True or False), also known as logical values, forms the foundation of conditional statements in Python. 
As you may recall from exams, boolean values can be either `True` or `False`. You can just type `True` in the python shell and
you will see that python recognises it. You can also check the type of this by using the type function.

Let's take a closer look:

~~~ {.bash}
Python 3.11.7 (main, Dec  4 2023, 18:10:11) ß
Type "help", "copyright", "credits" or "license" for more information.
>>> True 
~~~
~~~ {.output}
True
~~~

Then you can check the type of the bool.




~~~ {.bash}
>>> type(True)
~~~
~~~ {.output}
<class 'bool'>
~~~



Remember, boolean values are case-sensitive in Python, so ensure correct spellings when using them in your code.

# Integers
Integers represent whole numbers like 1,2,3,4,5...., including both positive and negative values. 
They are used extensively in various computations. Here's how you can work with integers:

~~~ {.bash}
>>> 1
~~~
~~~ {.output}
1
~~~


You can also check the class of the integers.

~~~ {.bash}
>>> type(1)
~~~
~~~ {.output}
<class 'int'>
~~~

You can also enter a very huge integer like this:

~~~ {.bash}
>>> 1234531244038974908237
~~~
~~~ {.output}
1234531244038974908237
~~~

You might have noted that commas and seprators (which are there to make the huge numbers more readable) 
are not used in python for integers.




# Floats
Floats, short for floating point numbers (also known as Decimal Numbers), are used to represent 
decimal values or numbers in scientific notation. In Python, the term "float" refers to a data type used to represent decimal numbers (numbers with a fractional part). 

Here's a glimpse:


~~~ {.bash}
>>> 2.5
~~~
~~~ {.output}
2.5
~~~

You can also check the type by using the type function:

~~~ {.bash}
>>> type(2.5)
~~~
~~~ {.output}
<class 'float'>
~~~

Python automatically switches to scientific notation for extremely large float values.
~~~ {.bash}
>>> 123213123123123123123.12321329
~~~
~~~ {.output}
1.2321312312312313e+20
~~~


# Special Values
The special value `None` denotes the absence of a value, often used to indicate missing data in datasets. If you will 
type None in the python shell and hit enter you will not get back any thing like you used to get with other types.
See the code example below:

~~~ {.bash}
>>> None
~~~
~~~ {.output}
>>>
~~~

We will see how and where None can be used in later videos.


# Strings
Strings play a crucial role in bioinformatics, especially when dealing with DNA, RNA, or protein sequences. 
They are enclosed within single quotes, double quotes, or triple quotes for multiline strings:


~~~ {.bash}
>>> "Python for Bioinformatics"
~~~
~~~ {.output}
'Python for Bioinformatics'
~~~

Lets take a look at the protein sequence:
~~~ {.bash}
>>> 'MKMDLMK'
~~~
~~~ {.output}
'MKMDLMK'
~~~


Lets take a look at the DNA sequence:
~~~ {.bash}
>>> "ATGCTCTCGTCGACGACDAT"
~~~
~~~ {.output}
'ATGCTCTCGTCGACGACDAT'
~~~

Strings enable us to represent and manipulate textual data efficiently, 
making them indispensable in bioinformatics workflows.

Next we will be talking about [Expressions](/003-EXPRESSIONS-python-for-Bioinformatics/).