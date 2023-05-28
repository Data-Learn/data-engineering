#create a database called learn_spark_db and tell Spark we want to use that database
spark.sql("CREATE DATABASE learn_spark_db")
spark.sql("USE learn_spark_db")

#Creating a managed table
# option 1
spark.sql("CREATE TABLE managed_us_delay_flights_tbl (date STRING, delay INT,  \
  distance INT, origin STRING, destination STRING)")

# option 2
# Path to our US flight delays CSV file 
csv_file = "departuredelays.csv"
# Schema as defined in the preceding example
schema="date STRING, delay INT, distance INT, origin STRING, destination STRING"
flights_df = spark.read.csv(csv_file, schema=schema)
flights_df.write.saveAsTable("managed_us_delay_flights_tbl")


#Creating an unmanaged table
# option 1
spark.sql("""CREATE TABLE us_delay_flights_tbl(date STRING, delay INT, 
  distance INT, origin STRING, destination STRING) 
  USING csv OPTIONS (PATH 
  'departuredelays.csv')""")

# option 2
(flights_df
  .write
  .option("path", "/tmp/data/us_flights_delay")
  .saveAsTable("us_delay_flights_tbl"))

#Creating Views
# In Python
df_sfo = spark.sql("SELECT date, delay, origin, destination FROM \
  us_delay_flights_tbl WHERE origin = 'SFO'")
df_jfk = spark.sql("SELECT date, delay, origin, destination FROM \
  us_delay_flights_tbl WHERE origin = 'JFK'")

# Create a temporary and global temporary view
df_sfo.createOrReplaceGlobalTempView("us_origin_airport_SFO_global_tmp_view")
df_jfk.createOrReplaceTempView("us_origin_airport_JFK_tmp_view")

# Drop views
spark.catalog.dropGlobalTempView("us_origin_airport_SFO_global_tmp_view")
spark.catalog.dropTempView("us_origin_airport_JFK_tmp_view")