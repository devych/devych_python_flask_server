import pymysql
from env.env import db


def test():
    conn = pymysql.connect(host=db['host'], user=db['user'], password=db['password'], db='devych_server',
                           charset='utf8')

    curs = conn.cursor(pymysql.cursors.DictCursor)
    sql = """select * from test"""
    curs.execute(sql)
    rows = curs.fetchall()

    num = len(rows) + 1

    sql = """insert test(testname, testcontent) values(%s, %s)"""
    curs.execute(sql, ('test' + str(num), 'test' + str(num)))
    conn.commit()

    sql = """select * from test"""
    curs.execute(sql)
    rows = curs.fetchall()

    conn.close()
    return rows
