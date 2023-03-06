# Databricks notebook source
# MAGIC %md-sandbox
# MAGIC 
# MAGIC <div style="text-align: center; line-height: 0; padding-top: 9px;">
# MAGIC   <img src="https://databricks.com/wp-content/uploads/2018/03/db-academy-rgb-1200px.png" alt="Databricks Learning" style="width: 600px">
# MAGIC </div>

# COMMAND ----------

# MAGIC %md
# MAGIC # Methods, Functions, Packages
# MAGIC 
# MAGIC ## ![Spark Logo Tiny](https://files.training.databricks.com/images/105/logo_spark_tiny.png) In this lesson you:<br><br>
# MAGIC * Define and use functions to reuse, not repeat code
# MAGIC   * with and without arguments
# MAGIC   * with and without type hints
# MAGIC * Use assert() statements to "unit test" functions
# MAGIC * Call the **`help()`** function to learn about modules, functions, classes, and keywords
# MAGIC * Identify differences between functions and methods
# MAGIC * Import libraries
# MAGIC    

# COMMAND ----------

# MAGIC %md
# MAGIC ### Functions
# MAGIC 
# MAGIC In this lesson, we're going to see how we can use functions to make code reusable.
# MAGIC 
# MAGIC Let's start with a simple example:<br>
# MAGIC We know that we can use Python to do math. The modulo operator returns the remainder of a division. The code below returns 0 because 42 is even, so this division has no remainder.

# COMMAND ----------

42 % 2

# COMMAND ----------

# MAGIC %md
# MAGIC The code below will return 1 because it is odd. 

# COMMAND ----------

41 % 2

# COMMAND ----------

# MAGIC %md
# MAGIC If we want to determine whether a whole bunch of numbers are even or odd, we can package this same code into a **function**. 
# MAGIC 
# MAGIC A <a href="https://www.w3schools.com/python/python_functions.asp" target="_blank">function</a> is created with the **`def`** keyword, followed by the name of the function, any parameters in parentheses, and a colon.

# COMMAND ----------

# General syntax
# def function_name(parameter_name):
#     block of code that is run every time function is called

# defining the function
def even_or_odd(num):
    """Optional doc string explaining the function"""
    if num % 2 == 0:
        print("even")
    elif num % 2 == 1:
        print("odd")
    else:
        print("UNKNOWN")

# execute the function by passing it a number
even_or_odd(42)

# COMMAND ----------

# MAGIC %md
# MAGIC The one problem with printing the result is that if you assign it back to a variable, the variable is a None datatype (the output of print, versus the output of the function).
# MAGIC 
# MAGIC Instead, use the **`return`** keyword.

# COMMAND ----------

def even_or_odd(num):
    """Returns the string even, odd, or unknown"""
    if num % 2 == 0:
        return "even"
    elif num % 2 == 1:
        return "odd"
    else:
        return "UNKNOWN"

# execute the function by passing it a number
even_or_odd(42)

# COMMAND ----------

# MAGIC %md
# MAGIC A best practice is to create a "unit" test to verify our function.
# MAGIC 
# MAGIC An "AssertionError:" will only display if the function returns something that is not expected.

# COMMAND ----------

assert "odd" == even_or_odd(101)
assert "even" == even_or_odd(400)
assert "odd" == even_or_odd(5)
assert "even" == even_or_odd(2)
assert "even" == even_or_odd(3780)
assert "odd" == even_or_odd(78963)
assert "UNKNOWN" == even_or_odd(1/3)

# COMMAND ----------

# MAGIC %md
# MAGIC ###Help Function
# MAGIC 
# MAGIC The python **`help()`** function can display the additional information on modules, functions, classes, and keywords.

# COMMAND ----------

help(even_or_odd)

# COMMAND ----------

# MAGIC %md
# MAGIC ### Passing in Multiple Arguments<br>
# MAGIC Functions can accept more than one argument. Let's modify our function to accept an extra argument - a string that prints out when the number is not even or odd.

# COMMAND ----------

def even_or_odd(num, error_string):
    if num % 2 == 0:
        return "even"
    elif num % 2 == 1:
        return "odd"
    else:
        return error_string

# execute the function by passing it a number
error_string = "This isn't an even or odd number!"
even_or_odd(42.1, error_string)

# COMMAND ----------

# MAGIC %md
# MAGIC A new "unit" test can verify our function.

# COMMAND ----------

assert "odd" == even_or_odd(101, error_string) 
assert error_string == even_or_odd(1/3, error_string)

# COMMAND ----------

# MAGIC %md
# MAGIC ###Type Hints<br>
# MAGIC Functions can be more strongly typed. Type hinting allows us to indicate the argument and return type.<br>
# MAGIC This is done by adding a colon space and data type to the parameter like below. <br>
# MAGIC `num: int`<br>
# MAGIC The return type is indicated with a hyphen, greater than and data type before the colon at the end of the signature line.<br>
# MAGIC `-> str:`
# MAGIC 
# MAGIC <img src="https://files.training.databricks.com/images/icon_note_24.png"/> Types are not enforced, but merely provide hints to the user of a function, are used when generating docs and for validation in some IDEs.

# COMMAND ----------

def even_or_odd(num: int, error_string: str) -> str:
    if num % 2 == 0:
        return "even"
    elif num % 2 == 1:
        return "odd"
    else:
        return error_string

# execute the function by passing it a number
even_or_odd(42, error_string)

# COMMAND ----------

# MAGIC %md
# MAGIC We can improve our function further by adding default values.

# COMMAND ----------

def even_or_odd(num: int, error_string: str = "This isn't an even or odd number!") -> str:
    if num % 2 == 0:
        return "even"
    elif num % 2 == 1:
        return "odd"
    else:
        return error_string

# execute the function by passing it a number
even_or_odd(42)

# COMMAND ----------

# MAGIC %md
# MAGIC ### Methods
# MAGIC 
# MAGIC In Python a Method refers to a special kind of function that is applied to an object. <br>
# MAGIC Below we create a string object called name and print it.

# COMMAND ----------

name = "Databricks"
print(name)

# COMMAND ----------

# MAGIC %md
# MAGIC Next we apply the upper() method to name.

# COMMAND ----------

print(name.upper())

# COMMAND ----------

# MAGIC %md
# MAGIC Certain methods expect an argument.
# MAGIC 
# MAGIC Below we pass in **`a`** as an argument to the **`count()`** method and it returns the count of number of times **`a`** is found in the string 

# COMMAND ----------

print(name.count("a"))

# COMMAND ----------

# MAGIC %md
# MAGIC ### Libraries
# MAGIC 
# MAGIC You can also use additional libraries when working with Python, such as <a href="https://numpy.org/doc/stable/". 
# MAGIC 
# MAGIC Numpy is pre-installed on the Databricks runtime.
# MAGIC                                                                            
# MAGIC You will need to first **`import`** numpy.

# COMMAND ----------

import numpy

numpy.sqrt(9)

# COMMAND ----------

help(numpy.sqrt)

# COMMAND ----------

# MAGIC %md
# MAGIC You can also change the name of the library when you import it, such as:

# COMMAND ----------

import numpy as np

np.sqrt(12)

# COMMAND ----------

# MAGIC %md
# MAGIC Or if you want to import every function from numpy, you can use the wildcard **`*`**.
# MAGIC 
# MAGIC However, while this is simpler, it is generally not preferred.

# COMMAND ----------

from numpy import *

sqrt(12)

# COMMAND ----------

# MAGIC %md-sandbox
# MAGIC &copy; 2022 Databricks, Inc. All rights reserved.<br/>
# MAGIC Apache, Apache Spark, Spark and the Spark logo are trademarks of the <a href="https://www.apache.org/">Apache Software Foundation</a>.<br/>
# MAGIC <br/>
# MAGIC <a href="https://databricks.com/privacy-policy">Privacy Policy</a> | <a href="https://databricks.com/terms-of-use">Terms of Use</a> | <a href="https://help.databricks.com/">Support</a>
