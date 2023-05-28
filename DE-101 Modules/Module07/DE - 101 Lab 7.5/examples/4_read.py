#Use Parquet 
# read
file = "/summary-data/parquet/2010-summary.parquet/"
df = spark.read.format("parquet").load(file)

# write
(df.write.format("parquet")
  .mode("overwrite")
  .option("compression", "snappy")
  .save("/tmp/data/parquet/df_parquet"))

#Use CSV
# read
file = "/summary-data/csv/*"
schema = "DEST_COUNTRY_NAME STRING, ORIGIN_COUNTRY_NAME STRING, count INT"
df = (spark.read.format("csv") 
  .option("header", "true")  
  .schema(schema) 
  .option("mode", "FAILFAST")  # Exit if any errors 
  .option("nullValue", "")     # Replace any null data field with quotes 
  .load(file))

# write
df.write.format("csv").mode("overwrite").save("/data/csv/df_csv")

#Use JSON
# read
file = "/databricks-datasets/learning-spark-v2/flights/summary-data/json/*"
df = spark.read.format("json").load(file) 

# write
df.write.format("json") \
  .mode("overwrite") \
  .option("compression", "snappy") \
  .save("/tmp/data/json/df_json") 

# Avro
# read 
df = (spark.read.format("avro")
  .load("/databricks-datasets/learning-spark-v2/flights/summary-data/avro/*"))
df.show(truncate=False)

#write
(df.write
  .format("avro")
  .mode("overwrite")
  .save("/tmp/data/avro/df_avro"))

# ORC
# read
file = "/databricks-datasets/learning-spark-v2/flights/summary-data/orc/*"
df = spark.read.format("orc").option("path", file).load()
df.show(10, False)

# write
file = "/databricks-datasets/learning-spark-v2/flights/summary-data/orc/*"
df = spark.read.format("orc").option("path", file).load()
df.show(10, False)

# Images
from pyspark.ml import image

image_dir = "/cctvVideos/train_images/"
images_df = spark.read.format("image").load(image_dir)
images_df.printSchema()

images_df.select("image.height", "image.width", "image.nChannels", "image.mode", \
  "label").show(5, truncate=False)

# Binary
path = "/databricks-datasets/learning-spark-v2/cctvVideos/train_images/"
binary_files_df = (spark.read.format("binaryFile")
  .option("pathGlobFilter", "*.jpg")
  .load(path))
binary_files_df.show(5)

#To ignore partitioning data discovery in a directory, you can set recursiveFileLookup to "true":
# In Python
binary_files_df = (spark.read.format("binaryFile")
  .option("pathGlobFilter", "*.jpg")
  .option("recursiveFileLookup", "true")
  .load(path))
binary_files_df.show(5)