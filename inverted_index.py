import json
from pyspark.sql import SparkSession
from pyspark import SparkContext, SparkConf

# --- Initialisation de spark ---
conf = SparkConf().setAppName('Inverted Index')
sc = SparkContext(conf=conf)
sc.setLogLevel("ERROR")
spark = SparkSession(sc)

# --- Lecture du fichier json et création du DataFrame ---
data = json.load(open("results/result.json"))
rdd = sc.parallelize(data)
df = rdd.toDF()

# --- Informations sur le DataFrame ---
"""
print(f"Total number of rows: {rdd.count()}")
df.show(20)
"""

# --- Inversion ---
result = rdd.flatMap(lambda row: [(spell, row['name']) for spell in row["spells"]])\
            .reduceByKey(lambda a,b: a+b)\
            .collect()
df2 = sc.parallelize(result).toDF(("spell", "names"))

#--- sauvegarde au format .json ---
df2.toPandas().to_json('results/inverted_result.json', orient='records', force_ascii=False, lines=True)