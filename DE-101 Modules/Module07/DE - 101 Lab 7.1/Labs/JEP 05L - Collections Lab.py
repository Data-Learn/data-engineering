# Databricks notebook source
# MAGIC %md-sandbox
# MAGIC 
# MAGIC <div style="text-align: center; line-height: 0; padding-top: 9px;">
# MAGIC   <img src="https://databricks.com/wp-content/uploads/2018/03/db-academy-rgb-1200px.png" alt="Databricks Learning" style="width: 600px">
# MAGIC </div>

# COMMAND ----------

# MAGIC %md
# MAGIC # Collections Lab - Word Count
# MAGIC 
# MAGIC Write a function that accepts a list of values and returns a dictionary with a count of the number of times each unique value appeared in the list.
# MAGIC 0. The name of the function should be **`item_count`**
# MAGIC 0. The function should have one parameter that is a list of values.
# MAGIC 0. The function should return a diction where:
# MAGIC   * The dictionary-key is the original value from the list
# MAGIC   * The dictionary-value is the number of times the corresponding value appeared in the list.
# MAGIC 
# MAGIC For example, **`item_count(["a", "b", "a"])`** should return the dictionary **`{"a": 2, "b": 1}`**
# MAGIC 
# MAGIC Hint: For every value, you will need to first test the dictionary to see if you already have a count for that value or not.

# COMMAND ----------

# TODO
def FILL_IN(parameter)
    output = {}          # Initialize an empty dictionary
  
    for item in input:   # Iterate over the list of values
        FILL_IN            # Update the dictionary
      
    return output        # Return the dictionary

# COMMAND ----------

# MAGIC %md
# MAGIC ##![Spark Logo Tiny](https://s3-us-west-2.amazonaws.com/curriculum-release/images/105/logo_spark_tiny.png) Validate Your Answer
# MAGIC 
# MAGIC Once you have implemented and executed your solution, run the following cell to confirm that it produces correct results.
# MAGIC 
# MAGIC It should not raise any errors if you implemented the function correctly.

# COMMAND ----------

empty_list = []
empty_count_result = {}
assert item_count(empty_list) == empty_count_result

breakfast_list = ["pancake", "egg", "egg", "pancake", "coffee", "pancake"]
breakfast_count_result = {"pancake": 3, "egg": 2, "coffee": 1, }
assert item_count(breakfast_list) == breakfast_count_result

print("Congratulations! All tests passed.")

# COMMAND ----------

# MAGIC %md-sandbox
# MAGIC &copy; 2022 Databricks, Inc. All rights reserved.<br/>
# MAGIC Apache, Apache Spark, Spark and the Spark logo are trademarks of the <a href="https://www.apache.org/">Apache Software Foundation</a>.<br/>
# MAGIC <br/>
# MAGIC <a href="https://databricks.com/privacy-policy">Privacy Policy</a> | <a href="https://databricks.com/terms-of-use">Terms of Use</a> | <a href="https://help.databricks.com/">Support</a>
