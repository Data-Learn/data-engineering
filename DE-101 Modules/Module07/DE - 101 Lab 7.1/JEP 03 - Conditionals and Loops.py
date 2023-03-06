# Databricks notebook source
# MAGIC %md-sandbox
# MAGIC 
# MAGIC <div style="text-align: center; line-height: 0; padding-top: 9px;">
# MAGIC   <img src="https://databricks.com/wp-content/uploads/2018/03/db-academy-rgb-1200px.png" alt="Databricks Learning" style="width: 600px">
# MAGIC </div>

# COMMAND ----------

# MAGIC %md
# MAGIC # Conditionals and Loops
# MAGIC 
# MAGIC ## ![Spark Logo Tiny](https://files.training.databricks.com/images/105/logo_spark_tiny.png) In this lesson you:<br><br>
# MAGIC 
# MAGIC  - Define syntax for writing lists and accessing their elements
# MAGIC  - Apply basic control flow statements to write programs that:
# MAGIC      - Repeat an action
# MAGIC      - Apply a function to any item on a list
# MAGIC      - Use conditional statements to how a program will execute 

# COMMAND ----------

# MAGIC %md
# MAGIC ### 1) List
# MAGIC 
# MAGIC Let's make a <a href="https://www.w3schools.com/python/python_lists.asp" target="_blank">list</a> of what everyone ate for breakfast this morning.
# MAGIC 
# MAGIC <img src="https://upload.wikimedia.org/wikipedia/commons/thumb/2/20/Scrambed_eggs.jpg/1280px-Scrambed_eggs.jpg" width="20%" height="10%">

# COMMAND ----------

breakfast_list = ["pancakes", "eggs", "waffles"]

# COMMAND ----------

# MAGIC %md
# MAGIC Let's get the first breakfast element from this list.
# MAGIC 
# MAGIC **Note:** Everything in Python is 0-indexed, so the first element is at position 0.

# COMMAND ----------

breakfast_list[0]

# COMMAND ----------

# MAGIC %md
# MAGIC Let's get the last breakfast item from this list.

# COMMAND ----------

breakfast_list[-1]

# COMMAND ----------

# MAGIC %md
# MAGIC What if I want the second breakfast item and onwards?

# COMMAND ----------

breakfast_list[1:]

# COMMAND ----------

# MAGIC %md
# MAGIC Let's add an element to our list.

# COMMAND ----------

breakfast_list += ["apple"]

# The += is a short cut for
# breakfast_list = breakfast_list + ["apple"]

# COMMAND ----------

# MAGIC %md
# MAGIC ### 2) For Loops
# MAGIC 
# MAGIC What if we wanted to print every breakfast we had this morning?
# MAGIC 
# MAGIC Loops are a way to repeat a block of code while iterating over a sequence (<a href="https://www.w3schools.com/python/python_for_loops.asp" target="_blank">"for-loop"</a>). 
# MAGIC   
# MAGIC Notice how in the code below the syntax is:
# MAGIC 
# MAGIC <code><b>
# MAGIC for element in list:<br/>
# MAGIC &nbsp; &nbsp; do-something
# MAGIC </b></code>
# MAGIC 
# MAGIC Anything you want executed multiple times needs to be indented inside the for loop. 
# MAGIC 
# MAGIC **`food`** is a temporary variable we define below, but you can call it anything you like.

# COMMAND ----------

for food in breakfast_list:
    print(food)

print("This is executed once because it is outside the for loop")

# COMMAND ----------

# MAGIC %md
# MAGIC You can also get it to print out the index of the element in the list too, by using **`enumerate`**.

# COMMAND ----------

for i, food in enumerate(breakfast_list):
    print(i, food)

# COMMAND ----------

# MAGIC %md
# MAGIC ### 3) Conditionals
# MAGIC 
# MAGIC Sometimes, depending on certain conditions, we don't always want to execute every line of code. We can control this through using the **`if`**, **`elif`**, and **`else`** <a href="https://www.w3schools.com/python/python_conditions.asp" target="_blank">conditionals</a>.
# MAGIC 
# MAGIC You are not required to have elif/else statements following an if statement.

# COMMAND ----------

if food == "eggs":
    print("Make scrambled eggs")
elif food == "waffles":
    print("I want maple syrup on my waffles")
else:
    print(food)

# COMMAND ----------

# MAGIC %md
# MAGIC You can also nest these if/elif/else statements, or combine them with **`or`** & **`and`**

# COMMAND ----------

if food != "eggs":
    if (food == "waffles") or (food == "pancakes"):
        print("I want maple syrup on my waffles")
    else:
        print("It must be an apple")
else:
    print(food)

# COMMAND ----------

# MAGIC %md
# MAGIC We can put these if/elif/else statements inside of a for loop.

# COMMAND ----------

for food in breakfast_list:
    if food != "eggs":
        if (food == "waffles") or (food == "pancakes"):
            print("I want maple syrup on my waffles")
        else:
            print("It must be an apple")
    else:
        print(food)

# COMMAND ----------

# MAGIC %md
# MAGIC ### 4) Ranges
# MAGIC 
# MAGIC A _range_ represents an _immutable_ sequence of numbers, and is commonly used for looping a specific number of times in **`for`** loops.

# COMMAND ----------

# Note that a range includes the start value and excludes the stop value
print("A range from 1 up to but not including 5")
for i in range(1, 5):
    print(i)

# A start value of 0 is used if you don't specify a value
print("\nA range from 0 up to but not including 5")
for i in range(5):
    print(i)

# COMMAND ----------

# MAGIC %md
# MAGIC A difference between lists and ranges is that a range is a _generator_, which generates the values when they are accessed rather than storing all of the values in memory. If necessary, you can use the **`list()`** built-in function to create a list by materializing all of the elements of a range.

# COMMAND ----------

values_range = range(5)
print(f"The original range: {values_range}")

values_list = list(values_range)
print(f"The materialized range as a list: {values_list}")

# COMMAND ----------

# MAGIC %md-sandbox
# MAGIC &copy; 2022 Databricks, Inc. All rights reserved.<br/>
# MAGIC Apache, Apache Spark, Spark and the Spark logo are trademarks of the <a href="https://www.apache.org/">Apache Software Foundation</a>.<br/>
# MAGIC <br/>
# MAGIC <a href="https://databricks.com/privacy-policy">Privacy Policy</a> | <a href="https://databricks.com/terms-of-use">Terms of Use</a> | <a href="https://help.databricks.com/">Support</a>
