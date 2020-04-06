import pymysql


def select_drw_lotto(num):
    from app.controllers import connect_db

    conn = connect_db()
    curs = conn.cursor(pymysql.cursors.DictCursor)

    try:
        if num != 'all':
            sql = """select * from lotto_draw_info where drwNo=%s"""
            curs.execute(sql, (num,))
        else:
            sql = """select * from lotto_draw_info"""
            curs.execute(sql)

        rows = curs.fetchall()

    except ValueError:
        print(ValueError)

    finally:
        curs.close()
        conn.close()

    # print(rows)
    return rows

