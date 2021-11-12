from fighting.creature import Creature
from fighting.weapon import Weapon
from pyspark.sql import SparkSession
from pyspark import SparkContext, SparkConf


creatures = [
    Creature("Solar Angel", 0, 363, 50, 44, [Weapon("Dancing Greatsword", [3, 6, 18], [35, 30, 25, 20], 10),
                                                 Weapon("Bow", [2, 6, 14], [31, 26, 21, 16], 110)], [0, 200, 0]),
    Creature("Worg Rider", 1, 13, 20, 18, [Weapon("mwk Battleaxe", [1, 8, 2], [6, 6, 6], 10)], [200, 160, 0]),
    Creature("Worg Rider", 1, 13, 20, 18, [Weapon("mwk Battleaxe", [1, 8, 2], [6, 6, 6], 10)], [200, 170, 0]),
    Creature("Worg Rider", 1, 13, 20, 18, [Weapon("mwk Battleaxe", [1, 8, 2], [6, 6, 6], 10)], [200, 180, 0]),
    Creature("Worg Rider", 1, 13, 20, 18, [Weapon("mwk Battleaxe", [1, 8, 2], [6, 6, 6], 10)], [200, 190, 0]),
    Creature("Worg Rider", 1, 13, 20, 18, [Weapon("mwk Battleaxe", [1, 8, 2], [6, 6, 6], 10)], [200, 200, 0]),
    Creature("Worg Rider", 1, 13, 20, 18, [Weapon("mwk Battleaxe", [1, 8, 2], [6, 6, 6], 10)], [200, 210, 0]),
    Creature("Worg Rider", 1, 13, 20, 18, [Weapon("mwk Battleaxe", [1, 8, 2], [6, 6, 6], 10)], [200, 220, 0]),
    Creature("Worg Rider", 1, 13, 20, 18, [Weapon("mwk Battleaxe", [1, 8, 2], [6, 6, 6], 10)], [200, 230, 0]),
    Creature("Worg Rider", 1, 13, 20, 18, [Weapon("mwk Battleaxe", [1, 8, 2], [6, 6, 6], 10)], [200, 240, 0]),
    Creature("Warlord", 1, 141, 30, 27,
             [Weapon("Vicious Flail", [1, 8, 10], [20, 15, 10], 10), Weapon("Throwing Axe", [1, 6, 5], [19], 40)],
             [250, 200, 0])
    ]

# --- Initialisation de spark ---
conf = SparkConf().setAppName('Fight1')
sc = SparkContext(conf=conf)
sc.setLogLevel("ERROR")
spark = SparkSession(sc)

rdd = sc.parallelize(creatures).flatMap(lambda creature: creature.play_turn(creatures))
