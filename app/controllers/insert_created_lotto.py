from app.controllers import connect_db
from app.controllers.crawl_lotto import get_last_draw


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

