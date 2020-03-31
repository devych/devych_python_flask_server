from app.controllers import connect_db
import pymysql


def select_drw_lotto(num):
    conn = connect_db()
    curs = conn.cursor(pymysql.cursors.DictCursor)
    try:
        sql = """select * from lottoDrawInfo where drwNo=%s"""
        curs.execute(sql, (num,))
        rows = curs.fetchone()

    except ValueError:
        print(ValueError)

    curs.close()
    conn.close()

    print(rows)
    return rows

