import pymysql
from pymysql.cursors import DictCursor

# Ajusta estos datos segun tu instalacion de MySQL
DB_CONFIG = {
    "host": "interchange.proxy.rlwy.net",
    "user": "root",
    "password": "TtBGjcWEKxncFyHplxzbayHbbhtGextx",
    "database": "railway",
    "port": 19602,
    "cursorclass": DictCursor,
}


def get_connection():
    return pymysql.connect(**DB_CONFIG)
