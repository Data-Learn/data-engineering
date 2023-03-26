from pyspark.sql.types import *
import pyspark.sql.functions as F

# Programmatic way to define a schema 
fire_schema = StructType([StructField('CallNumber', IntegerType(), True),
                     StructField('UnitID', StringType(), True),
                     StructField('IncidentNumber', IntegerType(), True),
                     StructField('CallType', StringType(), True),                  
                     StructField('CallDate', StringType(), True),      
                     StructField('WatchDate', StringType(), True),
                     StructField('CallFinalDisposition', StringType(), True),
                     StructField('AvailableDtTm', StringType(), True),
                     StructField('Address', StringType(), True),       
                     StructField('City', StringType(), True),       
                     StructField('Zipcode', IntegerType(), True),       
                     StructField('Battalion', StringType(), True),                 
                     StructField('StationArea', StringType(), True),       
                     StructField('Box', StringType(), True),       
                     StructField('OriginalPriority', StringType(), True),       
                     StructField('Priority', StringType(), True),       
                     StructField('FinalPriority', IntegerType(), True),       
                     StructField('ALSUnit', BooleanType(), True),       
                     StructField('CallTypeGroup', StringType(), True),
                     StructField('NumAlarms', IntegerType(), True),
                     StructField('UnitType', StringType(), True),
                     StructField('UnitSequenceInCallDispatch', IntegerType(), True),
                     StructField('FirePreventionDistrict', StringType(), True),
                     StructField('SupervisorDistrict', StringType(), True),
                     StructField('Neighborhood', StringType(), True),
                     StructField('Location', StringType(), True),
                     StructField('RowID', StringType(), True),
                     StructField('Delay', FloatType(), True)])

# Use the DataFrameReader interface to read a CSV file
sf_fire_file = "sf-fire-calls.csv"
fire_df = spark.read.csv(sf_fire_file, header=True, schema=fire_schema)

# Cache the DataFrame since we will be performing some operations on it.
fire_df.cache()
fire_df.count()

fire_df.printSchema()


#display(fire_df.limit(5))
fire_df.show(5, False)

# Filter out "Medical Incident" call types

# Note that filter() and where() methods on the DataFrame are similar. Check relevant documentation for their respective argument types.

few_fire_df = (fire_df
               .select("IncidentNumber", "AvailableDtTm", "CallType")
               .where(F.col("CallType") != "Medical Incident"))

few_fire_df.show(5, truncate=False)

# return number of distinct types of calls using countDistinct()
from pyspark.sql.functions import *
(fire_df
  .select("CallType")
  .where(F.col("CallType").isNotNull())
  .agg(F.countDistinct("CallType").alias("DistinctCallTypes"))
  .show())

(fire_df
  .select("CallType")
  .where(F.col("CallType").isNotNull())
  .distinct()
  .count())

# Example
few_fire_df = (fire_df
  .select("IncidentNumber", "AvailableDtTm", "CallType") 
  .where(col("CallType") != "Medical Incident"))
few_fire_df.show(5, truncate=False)

# filter for only distinct non-null CallTypes from all the rows
(fire_df
  .select("CallType")
  .where(col("CallType").isNotNull())
  .distinct()
  .show(10, False))

# Rename column
new_fire_df = fire_df.withColumnRenamed("Delay", "ResponseDelayedinMins")
(new_fire_df
  .select("ResponseDelayedinMins")
  .where(F.col("ResponseDelayedinMins") > 5)
  .show(5, False))

# date operations
fire_ts_df = (new_fire_df
  .withColumn("IncidentDate", F.to_timestamp(F.col("CallDate"), "MM/dd/yyyy"))
  .drop("CallDate") 
  .withColumn("OnWatchDate", F.to_timestamp(F.col("WatchDate"), "MM/dd/yyyy"))
  .drop("WatchDate") 
  .withColumn("AvailableDtTS", F.to_timestamp(F.col("AvailableDtTm"), 
  "MM/dd/yyyy hh:mm:ss a"))
  .drop("AvailableDtTm"))

# Select the converted columns
(fire_ts_df
  .select("IncidentDate", "OnWatchDate", "AvailableDtTS")
  .show(5, False))

# what were the most common types of fire calls?
(fire_ts_df
  .select("CallType")
  .where(F.col("CallType").isNotNull())
  .groupBy("CallType")
  .count()
  .orderBy("count", ascending=False)
  .show(n=10, truncate=False))

# min,max, avg
(fire_ts_df
  .select(F.sum("NumAlarms"), F.avg("ResponseDelayedinMins"),
    F.min("ResponseDelayedinMins"), F.max("ResponseDelayedinMins"))
  .show())

#ASSIGNEMTN

# Q-1) How many distinct types of calls were made to the Fire Department?
# To be sure, let's not count "null" strings in that column.

# Q-2) What are distinct types of calls were made to the Fire Department?
# These are all the distinct type of call to the SF Fire Department

# Q-3) Find out all response or delayed times greater than 5 mins?
# Rename the column Delay - > ReponseDelayedinMins
# Returns a new DataFrame
# Find out all calls where the response time to the fire site was delayed for more than 5 mins


# Q-3) Find out all response or delayed times greater than 5 mins?
# Rename the column Delay - > ReponseDelayedinMins
# Returns a new DataFrame
# Find out all calls where the response time to the fire site was delayed for more than 5 mins

# Q-4a) What zip codes accounted for most common calls?
# Let's investigate what zip codes in San Francisco accounted for most fire calls and what type where they.
# Filter out by CallType
# Group them by CallType and Zip code
# Count them and display them in descending order
# It seems like the most common calls were all related to Medical Incident, and the two zip codes are 94102 and 94103.

# Q-4b) What San Francisco neighborhoods are in the zip codes 94102 and 94103
# Let's find out the neighborhoods associated with these two zip codes. In all likelihood, these are some of the contested neighborhood with high reported crimes.

# Q-5) What was the sum of all calls, average, min and max of the response times for calls?
# Let's use the built-in Spark SQL functions to compute the sum, avg, min, and max of few columns:
# Number of Total Alarms
# What were the min and max the delay in response time before the Fire Dept arrived at the scene of the call

# ** Q-6b) What week of the year in 2018 had the most fire calls?**
# Note: Week 1 is the New Years' week and week 25 is the July 4 the week. Loads of fireworks, so it makes sense the higher number of calls.

# ** Q-7) What neighborhoods in San Francisco had the worst response time in 2018?**
# It appears that if you living in Presidio Heights, the Fire Dept arrived in less than 3 mins, while Mission Bay took more than 6 mins.

# ** Q-8a) How can we use Parquet files or SQL table to store data and read it back?**

# ** Q-8c) How can read data from Parquet file?**
# Note we don't have to specify the schema here since it's stored as part of the Parquet metadata