from env.env import dbconfig
import pymysql
print('controllers __init__')


def connect_db():
    conn = pymysql.connect(host=dbconfig['host'], user=dbconfig['user'], password=dbconfig['password'],
                           db=dbconfig['db'], charset='utf8')
    return conn