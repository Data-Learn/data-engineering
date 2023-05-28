# Set file paths
from pyspark.sql.functions import expr
tripdelaysFilePath = "departuredelays.csv"
airportsFilePath = "airport-codes-na.txt"
  
# Obtain airports data set
airports = (spark.read 
  .format("csv")
  .options(header="true", inferSchema="true", sep="\t")
  .load(airportsFilePath))

airports.createOrReplaceTempView("airports")

# Obtain departure delays data set
departureDelays = (spark.read 
  .format("csv") 
  .options(header="true") 
  .load(tripdelaysFilePath))

departureDelays = (departureDelays 
  .withColumn("delay", expr("CAST(delay as INT) as delay")) 
  .withColumn("distance", expr("CAST(distance as INT) as distance")))

departureDelays.createOrReplaceTempView("departureDelays")

# Create temporary small table
foo = (departureDelays 
  .filter(expr("""origin == 'SEA' and destination == 'SFO' and 
    date like '01010%' and delay > 0"""))) 

foo.createOrReplaceTempView("foo")

spark.sql("SELECT * FROM airports LIMIT 10").show()

# +-----------+-----+-------+----+
# |       City|State|Country|IATA|
# +-----------+-----+-------+----+
# | Abbotsford|   BC| Canada| YXX|
# |   Aberdeen|   SD|    USA| ABR|
# |    Abilene|   TX|    USA| ABI|
# |      Akron|   OH|    USA| CAK|
# |    Alamosa|   CO|    USA| ALS|
# |     Albany|   GA|    USA| ABY|
# |     Albany|   NY|    USA| ALB|
# |Albuquerque|   NM|    USA| ABQ|
# | Alexandria|   LA|    USA| AEX|
# |  Allentown|   PA|    USA| ABE|
# +-----------+-----+-------+----+

spark.sql("SELECT * FROM departureDelays LIMIT 10").show()

# +--------+-----+--------+------+-----------+
# |    date|delay|distance|origin|destination|
# +--------+-----+--------+------+-----------+
# |01011245|    6|     602|   ABE|        ATL|
# |01020600|   -8|     369|   ABE|        DTW|
# |01021245|   -2|     602|   ABE|        ATL|
# |01020605|   -4|     602|   ABE|        ATL|
# |01031245|   -4|     602|   ABE|        ATL|
# |01030605|    0|     602|   ABE|        ATL|
# |01041243|   10|     602|   ABE|        ATL|
# |01040605|   28|     602|   ABE|        ATL|
# |01051245|   88|     602|   ABE|        ATL|
# |01050605|    9|     602|   ABE|        ATL|
# +--------+-----+--------+------+-----------+

spark.sql("SELECT * FROM foo").show()

# +--------+-----+--------+------+-----------+
# |    date|delay|distance|origin|destination|
# +--------+-----+--------+------+-----------+
# |01010710|   31|     590|   SEA|        SFO|
# |01010955|  104|     590|   SEA|        SFO|
# |01010730|    5|     590|   SEA|        SFO|
# +--------+-----+--------+------+-----------+

# Union
# Union two tables
bar = departureDelays.union(foo)
bar.createOrReplaceTempView("bar")

# Show the union (filtering for SEA and SFO in a specific time range)
bar.filter(expr("""origin == 'SEA' AND destination == 'SFO'
AND date LIKE '01010%' AND delay > 0""")).show()

spark.sql("""
SELECT * 
  FROM bar 
 WHERE origin = 'SEA' 
   AND destination = 'SFO' 
   AND date LIKE '01010%' 
   AND delay > 0
""").show()

# +--------+-----+--------+------+-----------+
# |    date|delay|distance|origin|destination|
# +--------+-----+--------+------+-----------+
# |01010710|   31|     590|   SEA|        SFO|
# |01010955|  104|     590|   SEA|        SFO|
# |01010730|    5|     590|   SEA|        SFO|
# |01010710|   31|     590|   SEA|        SFO|
# |01010955|  104|     590|   SEA|        SFO|
# |01010730|    5|     590|   SEA|        SFO|
# +--------+-----+--------+------+-----------+

# Joins
foo.join(
  airports, 
  airports.IATA == foo.origin
).select("City", "State", "date", "delay", "distance", "destination").show()

spark.sql("""
SELECT a.City, a.State, f.date, f.delay, f.distance, f.destination 
  FROM foo f
  JOIN airports a
    ON a.IATA = f.origin
""").show()

# +-------+-----+--------+-----+--------+-----------+
# |   City|State|    date|delay|distance|destination|
# +-------+-----+--------+-----+--------+-----------+
# |Seattle|   WA|01010710|   31|     590|        SFO|
# |Seattle|   WA|01010955|  104|     590|        SFO|
# |Seattle|   WA|01010730|    5|     590|        SFO|
# +-------+-----+--------+-----+--------+-----------+

# Windows functions
spark.sql("""
SELECT origin, destination, TotalDelays, rank 
  FROM ( 
     SELECT origin, destination, TotalDelays, dense_rank() 
       OVER (PARTITION BY origin ORDER BY TotalDelays DESC) as rank 
       FROM departureDelaysWindow
  ) t 
 WHERE rank <= 3
""").show()

# +------+-----------+-----------+----+
# |origin|destination|TotalDelays|rank|
# +------+-----------+-----------+----+
# |   SEA|        SFO|      22293|   1|
# |   SEA|        DEN|      13645|   2|
# |   SEA|        ORD|      10041|   3|
# |   SFO|        LAX|      40798|   1|
# |   SFO|        ORD|      27412|   2|
# |   SFO|        JFK|      24100|   3|
# |   JFK|        LAX|      35755|   1|
# |   JFK|        SFO|      35619|   2|
# |   JFK|        ATL|      12141|   3|
# +------+-----------+-----------+----+

# Modifications
from pyspark.sql.functions import expr
foo2 = (foo.withColumn(
          "status", 
          expr("CASE WHEN delay <= 10 THEN 'On-time' ELSE 'Delayed' END")
        ))

foo2.show()

# +--------+-----+--------+------+-----------+-------+
# |    date|delay|distance|origin|destination| status|
# +--------+-----+--------+------+-----------+-------+
# |01010710|   31|     590|   SEA|        SFO|Delayed|
# |01010955|  104|     590|   SEA|        SFO|Delayed|
# |01010730|    5|     590|   SEA|        SFO|On-time|
# +--------+-----+--------+------+-----------+-------+

foo3 = foo2.drop("delay")
foo3.show()

# Renamning columns
foo4 = foo3.withColumnRenamed("status", "flight_status")
foo4.show()

# +--------+--------+------+-----------+-------------+
# |    date|distance|origin|destination|flight_status|
# +--------+--------+------+-----------+-------------+
# |01010710|     590|   SEA|        SFO|      Delayed|
# |01010955|     590|   SEA|        SFO|      Delayed|
# |01010730|     590|   SEA|        SFO|      On-time|
# +--------+--------+------+-----------+-------------+

# +--------+--------+------+-----------+-------+
# |    date|distance|origin|destination| status|
# +--------+--------+------+-----------+-------+
# |01010710|     590|   SEA|        SFO|Delayed|
# |01010955|     590|   SEA|        SFO|Delayed|
# |01010730|     590|   SEA|        SFO|On-time|
# +--------+--------+------+-----------+-------+

# Pivoting in SQL
spark.sql(SELECT * FROM (
SELECT destination, CAST(SUBSTRING(date, 0, 2) AS int) AS month, delay 
  FROM departureDelays WHERE origin = 'SEA' 
) 
PIVOT (
  CAST(AVG(delay) AS DECIMAL(4, 2)) AS AvgDelay, MAX(delay) AS MaxDelay
  FOR month IN (1 JAN, 2 FEB)
)
ORDER BY destination)

# +-----------+------------+------------+------------+------------+
# |destination|JAN_AvgDelay|JAN_MaxDelay|FEB_AvgDelay|FEB_MaxDelay|
# +-----------+------------+------------+------------+------------+
# |        ABQ|       19.86|         316|       11.42|          69|
# |        ANC|        4.44|         149|        7.90|         141|
# |        ATL|       11.98|         397|        7.73|         145|
# |        AUS|        3.48|          50|       -0.21|          18|
# |        BOS|        7.84|         110|       14.58|         152|
# |        BUR|       -2.03|          56|       -1.89|          78|
# |        CLE|       16.00|          27|        null|        null|
# |        CLT|        2.53|          41|       12.96|         228|
# |        COS|        5.32|          82|       12.18|         203|
# |        CVG|       -0.50|           4|        null|        null|
# |        DCA|       -1.15|          50|        0.07|          34|
# |        DEN|       13.13|         425|       12.95|         625|
# |        DFW|        7.95|         247|       12.57|         356|
# |        DTW|        9.18|         107|        3.47|          77|
# |        EWR|        9.63|         236|        5.20|         212|
# |        FAI|        1.84|         160|        4.21|          60|
# |        FAT|        1.36|         119|        5.22|         232|
# |        FLL|        2.94|          54|        3.50|          40|
# |        GEG|        2.28|          63|        2.87|          60|
# |        HDN|       -0.44|          27|       -6.50|           0|
# +-----------+------------+------------+------------+------------+