# Databricks notebook source
# MAGIC %md-sandbox
# MAGIC 
# MAGIC <div style="text-align: center; line-height: 0; padding-top: 9px;">
# MAGIC   <img src="https://databricks.com/wp-content/uploads/2018/03/db-academy-rgb-1200px.png" alt="Databricks Learning" style="width: 600px">
# MAGIC </div>

# COMMAND ----------

# MAGIC %md
# MAGIC # Pandas
# MAGIC 
# MAGIC <a href="https://pandas.pydata.org/pandas-docs/stable/reference/index.html" target="_blank">Pandas</a> is a popular Python library among data scientists with high performing, easy-to-use data structures and data analysis tools.
# MAGIC 
# MAGIC ## ![Spark Logo Tiny](https://files.training.databricks.com/images/105/logo_spark_tiny.png) In this lesson you:<br><br>
# MAGIC * Explain what pandas is and why it's so popular
# MAGIC * Create and manipulate pandas DataFrames and Series
# MAGIC * Perform operations on pandas objects
# MAGIC 
# MAGIC First, let us import pandas with the alias **`pd`** so we can refer to the library without having to type Pandas out each time. 
# MAGIC 
# MAGIC Pandas is pre-installed on Databricks.   

# COMMAND ----------

import pandas as pd

pd.__version__

# COMMAND ----------

# MAGIC %md
# MAGIC ### Motivate why to use **`pandas`**
# MAGIC 
# MAGIC Let's start big picture...
# MAGIC 
# MAGIC * Humans are tool using animals 
# MAGIC * Computers are one of the most powerful tools we've created
# MAGIC * If you write code, you can unlock the full power of these tools

# COMMAND ----------

# MAGIC %md
# MAGIC Ok, cool. But why **`pandas`**?
# MAGIC 
# MAGIC * More and more, data is leading decision making
# MAGIC * Excel is great but what if...
# MAGIC   - You want to automate your analysis so it re-runs on new data each day?
# MAGIC   - You want to build a code base to share with your colleagues
# MAGIC   - You want more robust analyses to feed a business decision
# MAGIC   - You want to do machine learning
# MAGIC * One of the core libraries used by data analysts and data scientists in Python
# MAGIC 
# MAGIC Enter **`pandas`**...

# COMMAND ----------

# MAGIC %md
# MAGIC ### Introduce **`pandas`** and its history
# MAGIC 
# MAGIC **`pandas`** is a fast, powerful, flexible and easy to use open source data analysis and manipulation tool, built on top of the Python programming language.
# MAGIC 
# MAGIC Highlights:
# MAGIC 
# MAGIC - Built in 2008, open sourced in 2009
# MAGIC - A fast and efficient **DataFrame object** for data manipulation with integrated indexing;
# MAGIC - Tools for **reading and writing data** between in-memory data structures and different formats: CSV and text files, Microsoft Excel, SQL databases, and the fast HDF5 format;
# MAGIC - Intelligent **data alignment** and integrated handling of **missing data**: gain automatic label-based alignment in computations and easily manipulate messy data into an orderly form;
# MAGIC - Flexible **reshaping and pivoting** of data sets;
# MAGIC - Intelligent label-based **slicing, fancy indexing, and subsetting** of large data sets;
# MAGIC - Columns can be inserted and deleted from data structures for **size mutability**;
# MAGIC - Aggregating or transforming data with a powerful **group by** engine allowing split-apply-combine operations on data sets;
# MAGIC - High performance **merging and joining** of data sets;
# MAGIC - Hierarchical axis **indexing** provides an intuitive way of working with high-dimensional data in a lower-dimensional data structure;
# MAGIC - **Time series**-functionality: date range generation and frequency conversion, moving window statistics, date shifting and lagging. Even create domain-specific time offsets and join time series without losing data;
# MAGIC - Highly **optimized** for performance, with critical code paths written in Cython or C.
# MAGIC - Python with pandas is in use in a wide variety of **academic and commercial domains**, including Finance, Neuroscience, Economics, Statistics, Advertising, Web Analytics, and more.
# MAGIC 
# MAGIC 
# MAGIC <a href="https://www.amazon.com/gp/product/1491957662/ref=as_li_qf_asin_il_tl?ie=UTF8&tag=quantpytho-20&creative=9325&linkCode=as2&creativeASIN=1491957662&linkId=ea8de4253cce96046e8ab0383ac71b33" target="_blank">Check out the book</a>

# COMMAND ----------

# MAGIC %md
# MAGIC ## Pandas DataFrames
# MAGIC 
# MAGIC Let's see how we can create a simple <a href="https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.html" target="_blank">DataFrame</a> in Pandas.
# MAGIC 
# MAGIC We are going to create a list with 5 strings that we wish to store inside the DataFrame.

# COMMAND ----------

data = ["row one", "row two", "row three", "row four", "row five"]

pd.DataFrame(data=data)

# COMMAND ----------

# MAGIC %md
# MAGIC 
# MAGIC The **`0`** in the very first row is the name of the column with defaults to integers if not specified. 
# MAGIC 
# MAGIC What if we want to add in another column and name the columns?

# COMMAND ----------

data = [["row one", 1], ["row two", 2], ["row three", 3], ["row four", 4], ["row five", 5]]
column_names = ["Strings", "Integers"]

df = pd.DataFrame(data=data, columns=column_names)
df

# COMMAND ----------

# MAGIC %md
# MAGIC Now we have multiple columns in our DataFrame! We can check the types of columns in our df.

# COMMAND ----------

df.dtypes

# COMMAND ----------

# MAGIC %md
# MAGIC What if our DataFrame has many rows and we don't want to print out our entire DataFrame?
# MAGIC 
# MAGIC We can use the **`.head()`** and **`.tail()`** functions to limit the number of rows we see.

# COMMAND ----------

# look at the first 2 rows of df 
df.head(2)

# COMMAND ----------

# look at the last 2 rows of df 
df.tail(2)

# COMMAND ----------

# MAGIC %md
# MAGIC If we had many columns and we didn't want to see all of them? 
# MAGIC 
# MAGIC We can select specific columns to include by using brackets and "indexing" our DataFrame. 
# MAGIC 
# MAGIC This would return us another DataFrame which we can display.

# COMMAND ----------

cols_to_show = ["Integers"]
df[cols_to_show]

# COMMAND ----------

# MAGIC %md
# MAGIC ## Pandas Series

# COMMAND ----------

# MAGIC %md
# MAGIC If we only wanted to select out one column we can do the following.

# COMMAND ----------

df.Integers

# COMMAND ----------

df["Integers"]

# COMMAND ----------

# MAGIC %md
# MAGIC The 2 cells above returned Pandas <a href="https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.Series.html" target="_blank">Series</a> objects instead of Pandas DataFrame objects.
# MAGIC 
# MAGIC A Pandas Series is a single column of a Pandas DataFrame.

# COMMAND ----------

type(df), type(df["Integers"])

# COMMAND ----------

# MAGIC %md
# MAGIC We can index into a Series to get an entry in a specific row.
# MAGIC 
# MAGIC The index count starts at 0 by default.

# COMMAND ----------

df["Strings"][0]

# COMMAND ----------

# MAGIC %md
# MAGIC ## Operations
# MAGIC 
# MAGIC The benefit of having Pandas Series is the ability to easily perform mathematical operations on it.

# COMMAND ----------

df["Integers"] + df["Integers"]

# COMMAND ----------

df["Integers"] * df["Integers"]

# COMMAND ----------

# MAGIC %md
# MAGIC We can create a new column in our DataFrame **`df`**.

# COMMAND ----------

df["New Column"] = df["Integers"] * 100
df

# COMMAND ----------

# MAGIC %md-sandbox
# MAGIC &copy; 2022 Databricks, Inc. All rights reserved.<br/>
# MAGIC Apache, Apache Spark, Spark and the Spark logo are trademarks of the <a href="https://www.apache.org/">Apache Software Foundation</a>.<br/>
# MAGIC <br/>
# MAGIC <a href="https://databricks.com/privacy-policy">Privacy Policy</a> | <a href="https://databricks.com/terms-of-use">Terms of Use</a> | <a href="https://help.databricks.com/">Support</a>
