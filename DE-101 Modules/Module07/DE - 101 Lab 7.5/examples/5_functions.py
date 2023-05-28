# Create dummy dataset
from pyspark.sql.types import *
schema = StructType([StructField("celsius", ArrayType(IntegerType()))])

t_list = [[35, 36, 32, 30, 40, 42, 38]], [[31, 32, 34, 55, 56]]
t_c = spark.createDataFrame(t_list, schema)
t_c.createOrReplaceTempView("tC")

# Show the DataFrame
t_c.show()

# transform()
spark.sql("""
SELECT celsius, 
 transform(celsius, t -> ((t * 9) div 5) + 32) as fahrenheit 
  FROM tC
""").show()

# +--------------------+--------------------+
# |             celsius|          fahrenheit|
# +--------------------+--------------------+
# |[35, 36, 32, 30, ...|[95, 96, 89, 86, ...|
# |[31, 32, 34, 55, 56]|[87, 89, 93, 131,...|
# +--------------------+--------------------+

# filter()
spark.sql("""
SELECT celsius, 
 filter(celsius, t -> t > 38) as high 
  FROM tC
""").show()

# +--------------------+--------+
# |             celsius|    high|
# +--------------------+--------+
# |[35, 36, 32, 30, ...|[40, 42]|
# |[31, 32, 34, 55, 56]|[55, 56]|
# +--------------------+--------+

#exists()
spark.sql("""
SELECT celsius, 
       exists(celsius, t -> t = 38) as threshold
  FROM tC
""").show()

# +--------------------+---------+
# |             celsius|threshold|
# +--------------------+---------+
# |[35, 36, 32, 30, ...|     true|
# |[31, 32, 34, 55, 56]|    false|
# +--------------------+---------+

# reduce()
spark.sql("""
SELECT celsius, 
       reduce(
          celsius, 
          0, 
          (t, acc) -> t + acc, 
          acc -> (acc div size(celsius) * 9 div 5) + 32
        ) as avgFahrenheit 
  FROM tC
""").show()

# +--------------------+-------------+
# |             celsius|avgFahrenheit|
# +--------------------+-------------+
# |[35, 36, 32, 30, ...|           96|
# |[31, 32, 34, 55, 56]|          105|
# +--------------------+-------------+