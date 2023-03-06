# Databricks notebook source
# MAGIC %md-sandbox
# MAGIC 
# MAGIC <div style="text-align: center; line-height: 0; padding-top: 9px;">
# MAGIC   <img src="https://databricks.com/wp-content/uploads/2018/03/db-academy-rgb-1200px.png" alt="Databricks Learning" style="width: 600px">
# MAGIC </div>

# COMMAND ----------

# MAGIC %md
# MAGIC # The Databricks Environment
# MAGIC 
# MAGIC ## ![Spark Logo Tiny](https://files.training.databricks.com/images/105/logo_spark_tiny.png) In this lesson you:<br>
# MAGIC * Use Databricks to: 
# MAGIC   * Run code in a notebook
# MAGIC   * Switch between languages in a single notebook
# MAGIC   * Export notebooks
# MAGIC   
# MAGIC References:
# MAGIC * Databricks documentation on
# MAGIC <a href="https://docs.databricks.com" target="_blank">AWS</a>,
# MAGIC <a href="https://docs.microsoft.com/en-us/azure/databricks" target="_blank">Azure</a> &
# MAGIC <a href="https://docs.gcp.databricks.com" target="_blank">GCP</a>

# COMMAND ----------

# MAGIC %md-sandbox
# MAGIC ##![Spark Logo Tiny](https://files.training.databricks.com/images/105/logo_spark_tiny.png) Scala, Python, R, SQL
# MAGIC 
# MAGIC * Each notebook is tied to a specific language: **Scala**, **Python**, **SQL** or **R**
# MAGIC * Run the cell below using one of the following options:
# MAGIC   * **CTRL+ENTER** or **CMD+RETURN**
# MAGIC   * **SHIFT+ENTER** or **SHIFT+RETURN** to run the cell and move to the next one
# MAGIC   * Using **Run Cell**, **Run All Above** or **Run All Below** as seen here<br/><img style="box-shadow: 5px 5px 5px 0px rgba(0,0,0,0.25); border: 1px solid rgba(0,0,0,0.25);" src="https://files.training.databricks.com/images/notebook-cell-run-cmd.png"/>
# MAGIC 
# MAGIC Feel free to tweak the code below if you like:

# COMMAND ----------

print("I'm running Python!")

# COMMAND ----------

# MAGIC %md
# MAGIC What happens if you define the same variable in Python & Scala?

# COMMAND ----------

comment = "This is python code."

# COMMAND ----------

# MAGIC %scala
# MAGIC val comment = "This is scala code."

# COMMAND ----------

# MAGIC %md
# MAGIC What is the value of x?

# COMMAND ----------

comment

# COMMAND ----------

# MAGIC %md
# MAGIC ### Magic Command: &percnt;md
# MAGIC 
# MAGIC Our favorite Magic Command **&percnt;md** allows us to render Markdown in a cell:
# MAGIC * Double click this cell to begin editing it
# MAGIC * Then hit **`Esc`** to stop editing
# MAGIC 
# MAGIC # Title One
# MAGIC ## Title Two
# MAGIC ### Title Three
# MAGIC 
# MAGIC This is a test of the emergency broadcast system. This is only a test.
# MAGIC 
# MAGIC This is text with a **bold** word in it.
# MAGIC 
# MAGIC This is text with an *italicized* word in it.
# MAGIC 
# MAGIC This is an ordered list
# MAGIC 0. once
# MAGIC 0. two
# MAGIC 0. three
# MAGIC 
# MAGIC This is an unordered list
# MAGIC * apples
# MAGIC * peaches
# MAGIC * bananas
# MAGIC 
# MAGIC Links/Embedded HTML: <a href="http://bfy.tw/19zq" target="_blank">What is Markdown?</a>
# MAGIC 
# MAGIC Images:  
# MAGIC ![Spark Engines](https://files.training.databricks.com/images/Apache-Spark-Logo_TM_200px.png)
# MAGIC 
# MAGIC And of course, tables:
# MAGIC 
# MAGIC | Name  | Age | Breed    |
# MAGIC |-------|-----|--------|
# MAGIC | Buddy   | 2  | Golden Retriever   |
# MAGIC | Bingo  | 10  | Border Collie |
# MAGIC | Momo  | 3  | Lab   |

# COMMAND ----------

# MAGIC %md
# MAGIC ### Try displaying your favorite image in a markdown cell and adding a title cell.

# COMMAND ----------

# TODO

# COMMAND ----------

# MAGIC %md
# MAGIC ### Exporting Notebooks
# MAGIC 
# MAGIC If you want to export this notebook and share it with someone else, select `File -> Export -> DBC Archive`.

# COMMAND ----------

# MAGIC %md
# MAGIC ### Databricks File System - DBFS
# MAGIC 
# MAGIC * DBFS is a layer over a cloud-based object store
# MAGIC * Files in DBFS are persisted to the object store
# MAGIC * The lifetime of files in the DBFS are **NOT** tied to the lifetime of our cluster
# MAGIC * Notebooks are **NOT** stored in DBFS, but in a relational database

# COMMAND ----------

# MAGIC %md
# MAGIC #![Spark Logo Tiny](https://files.training.databricks.com/images/105/logo_spark_tiny.png) Learning More
# MAGIC 
# MAGIC We like to encourage you to explore the documentation to learn more about the various features of the Databricks platform and notebooks.
# MAGIC * <a href="https://docs.azuredatabricks.net/user-guide/index.html" target="_blank">User Guide</a>
# MAGIC * <a href="https://docs.azuredatabricks.net/user-guide/notebooks/index.html" target="_blank">User Guide / Notebooks</a>
# MAGIC * <a href="https://docs.azuredatabricks.net/administration-guide/index.html" target="_blank">Administration Guide</a>
# MAGIC * <a href="https://docs.azuredatabricks.net/api/index.html" target="_blank">REST API</a>
# MAGIC * <a href="https://docs.azuredatabricks.net/release-notes/index.html" target="_blank">Release Notes</a>
# MAGIC * <a href="https://docs.azuredatabricks.net" target="_blank">And much more!</a>

# COMMAND ----------

# MAGIC %md-sandbox
# MAGIC &copy; 2022 Databricks, Inc. All rights reserved.<br/>
# MAGIC Apache, Apache Spark, Spark and the Spark logo are trademarks of the <a href="https://www.apache.org/">Apache Software Foundation</a>.<br/>
# MAGIC <br/>
# MAGIC <a href="https://databricks.com/privacy-policy">Privacy Policy</a> | <a href="https://databricks.com/terms-of-use">Terms of Use</a> | <a href="https://help.databricks.com/">Support</a>
