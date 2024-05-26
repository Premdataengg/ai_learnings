
from pyspark.sql import SparkSession

# Initialize Spark session
spark = SparkSession.builder.appName("InferDataTypes").getOrCreate()

# Path to the CSV file
csv_file_path = "/users/prem/Documents/replaced_dataframe.txt"  # Change this to the actual path of your data.csv file

# Read the CSV file into a Spark DataFrame
df = spark.read.csv(csv_file_path, header=False, inferSchema=True)

# Show the DataFrame
df.show()

# Print the schema to see the inferred data types
df.printSchema()
