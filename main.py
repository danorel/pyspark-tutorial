from pyspark.sql import SparkSession
from pyspark.sql.functions import explode, split

spark = SparkSession.builder \
    .master("local[1]") \
    .appName("SparkByExamples.com") \
    .getOrCreate()

spark.sparkContext.setLogLevel("ERROR")

df = spark.readStream \
    .format("socket") \
    .option("host", "localhost") \
    .option("port", "65432") \
    .load()

df.printSchema()

words_df = df.select(explode(split(df["value"], " ")).alias("word"))
count_df = words_df.groupBy("word").count()

query = count_df.writeStream \
    .format("console") \
    .outputMode("complete") \
    .start() \
    .awaitTermination()
