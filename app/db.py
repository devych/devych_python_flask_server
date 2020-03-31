import pymysql
from env.env import dbconfig


def test():
    conn = pymysql.connect(host=dbconfig['host'], user=dbconfig['user'], password=dbconfig['password'], db=dbconfig['db'],
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

    curs.close()
    conn.close()
    return rows
