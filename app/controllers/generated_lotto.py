def generated_lotto():
    from app.controllers import connect_db
    import pymysql
    conn = connect_db()
    curs = conn.cursor(pymysql.cursors.DictCursor)
    try:
        sql = """select * from user_created_lotto order by id desc"""

        curs.execute(sql)
        lotto_generated_list = curs.fetchall()
    finally:
        curs.close()
        conn.close()

    return lotto_generated_list
