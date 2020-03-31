import pymysql
from env.env import dbconfig
from app.controllers.get_lotto_info import get_last_draw


def connect_db():
    conn = pymysql.connect(host=dbconfig['host'], user=dbconfig['user'], password=dbconfig['password'],
                           db=dbconfig['db'], charset='utf8')
    return conn


def insert_created_lotto(lists):
    cur_draw = get_last_draw() + 1

    conn = connect_db()
    curs = conn.cursor()

    try:
        for list in lists:
            user = 'unknown'
            drwNo = cur_draw
            drwtNo1 = list[0]
            drwtNo2 = list[1]
            drwtNo3 = list[2]
            drwtNo4 = list[3]
            drwtNo5 = list[4]
            drwtNo6 = list[5]

            sql = """insert user_created_lotto(user, drwNo, drwtNo1, drwtNo2, drwtNo3, drwtNo4, drwtNo5, drwtNo6) values(
            %s, %s, %s, %s, %s, %s, %s, %s) """

            curs.execute(sql, (user, drwNo, drwtNo1, drwtNo2, drwtNo3, drwtNo4, drwtNo5, drwtNo6))
            conn.commit()
            print('Lotto balls are Succesfully created')
    except ValueError:
        print(ValueError)

    curs.close()
    conn.close()

    return


