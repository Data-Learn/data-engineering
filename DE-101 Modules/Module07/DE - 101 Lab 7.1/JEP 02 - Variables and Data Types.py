# Databricks notebook source
# MAGIC %md-sandbox
# MAGIC 
# MAGIC <div style="text-align: center; line-height: 0; padding-top: 9px;">
# MAGIC   <img src="https://databricks.com/wp-content/uploads/2018/03/db-academy-rgb-1200px.png" alt="Databricks Learning" style="width: 600px">
# MAGIC </div>

# COMMAND ----------

# MAGIC %md
# MAGIC # Variables and Data Types
# MAGIC 
# MAGIC ## ![Spark Logo Tiny](https://files.training.databricks.com/images/105/logo_spark_tiny.png) In this lesson you:<br><br>
# MAGIC 
# MAGIC - Explore fundamental concepts in Python, such as: 
# MAGIC     * Data types
# MAGIC     * Variables
# MAGIC     * Print values
# MAGIC     * Assert statements
# MAGIC    
# MAGIC Recommended Resources:
# MAGIC * <a href="https://www.amazon.com/gp/product/1491957662/ref=as_li_qf_asin_il_tl?ie=UTF8&tag=quantpytho-20&creative=9325&linkCode=as2&creativeASIN=1491957662&linkId=ea8de4253cce96046e8ab0383ac71b33" target="_blank">Python for Data Analysis by Wes McKinney</a>
# MAGIC * <a href="https://www.pythoncheatsheet.org/" target="_blank">Python reference sheet</a>
# MAGIC * <a href="https://docs.python.org/3/tutorial/" target="_blank">Python official tutorial</a>
# MAGIC 
# MAGIC Here is some documentation to help with <a href="https://forums.databricks.com/static/markdown/help.html" target="_blank">markdown cells</a>.

# COMMAND ----------

# MAGIC %md
# MAGIC ### 1) Numbers: Using Python as your calculator!

# COMMAND ----------

# Hit the run button, or shift + enter
# The # is a comment, which means that whatever you write after the # will not be executed
1+1 

# COMMAND ----------

# MAGIC %md
# MAGIC ### 2) Strings
# MAGIC 
# MAGIC Strings in Python have **`''`** or **`""`** around the content. Generally it is preferred to use **`""`**. 
# MAGIC 
# MAGIC Notice how it performs differently when you add two strings together instead of two numbers.

# COMMAND ----------

"Ice cream"

# COMMAND ----------

"Ice cream" + "is paradise"

# COMMAND ----------

# MAGIC %md
# MAGIC If you are not sure what "type" something is, you can call the function **`type()`**.
# MAGIC 
# MAGIC We will discuss functions in detail later.

# COMMAND ----------

type("Ice cream")

# COMMAND ----------

# MAGIC %md
# MAGIC You'll notice that if you put quotes around a number, its type is a string.

# COMMAND ----------

type("1")

# COMMAND ----------

# MAGIC %md
# MAGIC Within numeric fields, there are two types: Integers and Floats. Integers are whole numbers, and floats contain a decimal place.

# COMMAND ----------

type(1)

# COMMAND ----------

type(1.0)

# COMMAND ----------

# MAGIC %md
# MAGIC ### 3) Variables
# MAGIC 
# MAGIC As Shakespeare famously wrote: **`A rose by any other name would smell as sweet`**. A variable in Python simply holds a value - you can call it any name you want (within reason...)!
# MAGIC 
# MAGIC If you plan to re-use the same value multiple times throughout your notebook, it is best to put it in a variable so you can change its value only once, it will be reflected throughout all uses in the notebook.
# MAGIC 
# MAGIC A few things to note on Python Variable Names from <a href="https://www.w3schools.com/python/gloss_python_variable_names.asp#:~:text=Rules%20for%20Python%20variables%3A,0%2D9%2C%20and%20_%20" target="_blank">W3 Schools</a>:
# MAGIC * A variable name must start with a letter or the underscore character
# MAGIC * A variable name cannot start with a number
# MAGIC * A variable name can only contain alpha-numeric characters and underscores (A-z, 0-9, and _ )
# MAGIC * Variable names are case-sensitive (**`age`**, **`Age`** and **`AGE`** are three different variables)

# COMMAND ----------

best_food = "Ice cream"

# COMMAND ----------

# MAGIC %md
# MAGIC ### 4) Print Statements
# MAGIC 
# MAGIC In Databricks or Jupyter notebooks, it will automatically print out the last line of the cell that it evaluates.

# COMMAND ----------

best_food

# COMMAND ----------

# MAGIC %md 
# MAGIC However, we can force it to print out other components by using a <a href="https://www.w3schools.com/python/ref_func_print.asp" target="_blank">print()</a> statement.

# COMMAND ----------

print("Hi there, tell me the best food.")
print(best_food)

# COMMAND ----------

# MAGIC %md
# MAGIC You can also be more explicit about what you are printing. You can add your variable within your print statement.
# MAGIC 
# MAGIC In Python 3.5, you'd have to print it like this:

# COMMAND ----------

print("{} is the best food on earth.".format(best_food))

# COMMAND ----------

# MAGIC %md
# MAGIC In Python 3.6+, you can use f-string formatting, e.g. **`f"{my_variable}"`**

# COMMAND ----------

print(f"{best_food} is the best food on earth.")

# COMMAND ----------

# MAGIC %md
# MAGIC <img src="https://files.training.databricks.com/images/icon_note_24.png"/> DBR 7.3 LTS uses Python 3.7 & DBR 9.1 uses Python 3.8

# COMMAND ----------

# MAGIC %md
# MAGIC ### 5) Assert Statements and Type Checking
# MAGIC 
# MAGIC We have been defining quite a number of variables. What if we forget what types are the variables? Don't worry -- we can always check using <a href="https://www.w3schools.com/python/ref_func_type.asp" target="_blank">type()</a>!

# COMMAND ----------

type(best_food)

# COMMAND ----------

# MAGIC %md
# MAGIC If you want to test if two things are equal, you can put them on either side of the **`==`**. 
# MAGIC 
# MAGIC Conversely, if you want to test if things are not equal, you can do **`!=`**.
# MAGIC 
# MAGIC This returns a **`Boolean`**, which is a type that only contains the values **`True`** or **`False`** (case-sensitive).

# COMMAND ----------

2 == 2

# COMMAND ----------

type(best_food) == str

# COMMAND ----------

type(best_food) != str

# COMMAND ----------

# MAGIC %md
# MAGIC If the equality test does not hold, you might want to throw an error message.
# MAGIC 
# MAGIC That's exactly what an <a href="https://www.w3schools.com/python/python_ref_keywords.asp" target="_blank">assert</a> statement allows you to do.
# MAGIC 
# MAGIC You assert that two things should be equal, and if they are not, it will throw an error and print out a message you provide.

# COMMAND ----------

assert type(best_food) == str, "If this fails, it will print this message"

# COMMAND ----------

# MAGIC %md
# MAGIC **`assert`** and **`type`** are reserved keywords in Python, so make sure you don't accidentally created any variables named **`assert`** or **`type`**!
# MAGIC 
# MAGIC **Question**: What other reserved keywords have you seen?

# COMMAND ----------

# MAGIC %md
# MAGIC Summary of types:
# MAGIC 0. An **`int`** is a numeric type in Python. It is an integer, so a whole number without decimals. 
# MAGIC 0. A **`float`** is a numeric type in Python. It is basically a number that has decimal places. 
# MAGIC 0. A **`String`** type is a sequence of characters, such as the food **`"ice cream"`**. It can be any sequence of characters too, not just words. **`"Hello123"`** or even **`"123"`** could also be a string. They are enclosed in quotes.
# MAGIC 0. A **`Boolean`** type is either True or False.

# COMMAND ----------

# MAGIC %md
# MAGIC ### ![Spark Logo Tiny](https://files.training.databricks.com/images/105/logo_spark_tiny.png) Congrats! You have finished your first lesson on Python!

# COMMAND ----------

# MAGIC %md-sandbox
# MAGIC &copy; 2022 Databricks, Inc. All rights reserved.<br/>
# MAGIC Apache, Apache Spark, Spark and the Spark logo are trademarks of the <a href="https://www.apache.org/">Apache Software Foundation</a>.<br/>
# MAGIC <br/>
# MAGIC <a href="https://databricks.com/privacy-policy">Privacy Policy</a> | <a href="https://databricks.com/terms-of-use">Terms of Use</a> | <a href="https://help.databricks.com/">Support</a>
