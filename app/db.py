from flask import jsonify
import pymysql
from env import db

conn = pymysql.connect(host=db['host'], user=db['user'], password=db['password'], db='devych_server', charset='utf8')

curs = conn.cursor()
sql = """select * from users"""

curs.execute(sql)

rows = curs.fetchall()
print(rows)

conn.close()

