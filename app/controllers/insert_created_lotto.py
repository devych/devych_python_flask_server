from app.controllers import get_last_draw


def insert_created_lotto(lists):
    from app.controllers import connect_db

    cur_draw = get_last_draw() + 1

    conn = connect_db()
    curs = conn.cursor()

    try:
        for arr in lists:
            user = 'unknown'
            drwNo = cur_draw
            drwtNo1 = arr[0]
            drwtNo2 = arr[1]
            drwtNo3 = arr[2]
            drwtNo4 = arr[3]
            drwtNo5 = arr[4]
            drwtNo6 = arr[5]

            sql = """insert user_created_lotto(user, drwNo, drwtNo1, drwtNo2, drwtNo3, drwtNo4, drwtNo5, drwtNo6) values(
            %s, %s, %s, %s, %s, %s, %s, %s) """

            curs.execute(sql, (user, drwNo, drwtNo1, drwtNo2, drwtNo3, drwtNo4, drwtNo5, drwtNo6))
            conn.commit()
            print('Lotto balls are Succesfully created')
    except ValueError:
        print(ValueError)

    curs.close()
    conn.close()

