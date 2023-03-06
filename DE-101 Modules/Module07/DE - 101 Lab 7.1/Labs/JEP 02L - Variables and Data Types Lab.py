# Databricks notebook source
# MAGIC %md-sandbox
# MAGIC 
# MAGIC <div style="text-align: center; line-height: 0; padding-top: 9px;">
# MAGIC   <img src="https://databricks.com/wp-content/uploads/2018/03/db-academy-rgb-1200px.png" alt="Databricks Learning" style="width: 600px">
# MAGIC </div>

# COMMAND ----------

# MAGIC %md
# MAGIC ## Variables and Data Types Lab
# MAGIC 
# MAGIC Let's convert EUR to USD and prints the results.
# MAGIC 
# MAGIC To aid you in this, we have identified the cells you need to update with the **TODO** comment and provided a **FILL_IN** place-holder for your own code where appropriate.

# COMMAND ----------

# MAGIC %md
# MAGIC The current exchange rate as of Oct 17, 2021 is **1 EUR** to **1.16 USD**.
# MAGIC 0. Create a variable called **`conversion_rate`** and initialize it to the value of **`1.16`**.
# MAGIC 
# MAGIC This way, if the rate ever changes, we would only need to modify this single line of code and have everything else still work properly!

# COMMAND ----------

# TODO
FILL_IN = FILL_IN # Create the variable conversion_rate and assign it the value of 1.16

# COMMAND ----------

# MAGIC %md
# MAGIC Write an assertion that verifies **`conversion_rate`** is of type **`float`**.

# COMMAND ----------

# TODO
# Assert that your variable is of the correct type
assert FILL_IN == FILL_IN, FILL_IN

# COMMAND ----------

# MAGIC %md
# MAGIC Given that we have 566 EUR, compute what the corresponding amount should be in USD.
# MAGIC 0. Create the variable **`euro_amount`** and assign it the value **`566`**.
# MAGIC 0. Assign the result of the computation to the variable **`usd_amount`**.
# MAGIC 
# MAGIC Make sure you to use the variable **`conversion_rate`** in your computation and not the hard coded value **`1.16`**.

# COMMAND ----------

# TODO
FILL_IN = FILL_IN # Create the variable euro_amount and assign it the value of 566
FILL_IN = FILL_IN # Assign the result of the computation to usd_amount

# Test your solution
assert usd_amount == 656.56, "Incorrect amount." 

# COMMAND ----------

# MAGIC %md
# MAGIC Using **`euro_amount`** and **`usd_amount`**, print your results.
# MAGIC 0. Create a new f-string using this template: **`{} Euros is equal to ${} USD`**
# MAGIC 1. Print that new string to the console
# MAGIC 
# MAGIC Hint: This can be completed in one or two lines of code

# COMMAND ----------

# TODO
print(FILL_IN)

# COMMAND ----------

# MAGIC %md-sandbox
# MAGIC &copy; 2022 Databricks, Inc. All rights reserved.<br/>
# MAGIC Apache, Apache Spark, Spark and the Spark logo are trademarks of the <a href="https://www.apache.org/">Apache Software Foundation</a>.<br/>
# MAGIC <br/>
# MAGIC <a href="https://databricks.com/privacy-policy">Privacy Policy</a> | <a href="https://databricks.com/terms-of-use">Terms of Use</a> | <a href="https://help.databricks.com/">Support</a>
