import pymysql


def select_drw_lotto(num):
    from app.controllers import connect_db

    conn = connect_db()
    curs = conn.cursor(pymysql.cursors.DictCursor)
    try:
        sql = """select * from lotto_draw_info where drwNo=%s"""
        curs.execute(sql, (num,))
        rows = curs.fetchone()

    except ValueError:
        print(ValueError)

    curs.close()
    conn.close()

    # print(rows)
    return rows

