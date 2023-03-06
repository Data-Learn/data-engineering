# Databricks notebook source
# MAGIC %md-sandbox
# MAGIC 
# MAGIC <div style="text-align: center; line-height: 0; padding-top: 9px;">
# MAGIC   <img src="https://databricks.com/wp-content/uploads/2018/03/db-academy-rgb-1200px.png" alt="Databricks Learning" style="width: 600px">
# MAGIC </div>

# COMMAND ----------

# MAGIC %md
# MAGIC # Functions Lab
# MAGIC 
# MAGIC Building on the previous lab, the FizzBuzz Test, we are going to refactor that code into a function.
# MAGIC 0. Declare a function.
# MAGIC   0. The name of the function should be **`fizz_buzz`**
# MAGIC   0. The function has one parameter, presumably an integer (**`int`**).
# MAGIC   0. The function should return a string (**`str`**)
# MAGIC 0. Add a guard, or pre-condition, that asserts that the one specified parameter is of type **`int`**.
# MAGIC 
# MAGIC Bonus: Update your function to use type hints.

# COMMAND ----------

# MAGIC %md To help you get started, we have included one possible solution to the Fizz Buzz Test here. 
# MAGIC 
# MAGIC NOTE: You will not want to include the for loop when you make your function.

# COMMAND ----------

for num in range(1, 101):
    if (num % 5 == 0) and (num % 3 == 0):
        print("FizzBuzz")
    elif num % 5 == 0:
        print("Buzz")
    elif num % 3 == 0:
        print("Fizz")
    else:
        print(num)

# COMMAND ----------

# TODO
def FILL_IN
    assert FILL_IN

    if FILL_IN

# COMMAND ----------

# MAGIC %md Use the code below to test your function.

# COMMAND ----------

expected = "Fizz"
result = fizz_buzz(3)
assert result == expected, f"Expected {expected}, but found {result}."

expected = "Buzz"
result = fizz_buzz(5)
assert result == expected, f"Expected {expected}, but found {result}."

expected = "FizzBuzz"
result = fizz_buzz(15)
assert result == expected, f"Expected {expected}, but found {result}."

expected = "7"
result = fizz_buzz(7)
assert result == expected, f"Expected {expected}, but found {result}."

# COMMAND ----------

# MAGIC %md-sandbox
# MAGIC &copy; 2022 Databricks, Inc. All rights reserved.<br/>
# MAGIC Apache, Apache Spark, Spark and the Spark logo are trademarks of the <a href="https://www.apache.org/">Apache Software Foundation</a>.<br/>
# MAGIC <br/>
# MAGIC <a href="https://databricks.com/privacy-policy">Privacy Policy</a> | <a href="https://databricks.com/terms-of-use">Terms of Use</a> | <a href="https://help.databricks.com/">Support</a>
