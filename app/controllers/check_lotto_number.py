def check_lotto_number(page=1, content_amounts=20000):
    from app.controllers import connect_db, get_last_draw
    import pymysql

    last_draw = get_last_draw()
    first_idx = content_amounts * (page - 1)

    conn = connect_db()
    curs = conn.cursor(pymysql.cursors.DictCursor)

    lotto_result_list = []

    try:
        sql = """select * from user_created_lotto where drwNo <= %s order by id desc limit %s, %s """

        curs.execute(sql, (last_draw, first_idx, content_amounts))

        user_create_num_dict = curs.fetchall()

        high_drw = user_create_num_dict[0]["drwNo"]
        low_drw = user_create_num_dict[len(user_create_num_dict) - 1]["drwNo"]

        sql = """select drwNo, drwNoDate, drwtNo1, drwtNo2, drwtNo3, drwtNo4, drwtNo5, drwtNo6, bnusNo from lotto_draw_info 
        where drwNo between %s and %s """

        curs.execute(sql, (low_drw, high_drw))

        lotto = curs.fetchall()

        for answer in lotto:
            for target in user_create_num_dict:
                if answer["drwNo"] == target["drwNo"] and check_lotto_count(answer, target) is not None:
                    lotto_result_list.append(check_lotto_count(answer, target))

        lotto_result_list = sorted(lotto_result_list, key=lambda lotto_result_list:lotto_result_list[0])
    except ValueError:
        print(ValueError)

    finally:
        curs.close()
        conn.close()

    lotto_result_list.reverse()

    return lotto_result_list


def check_lotto_count(answer, target):
    count = 0

    answer_list = [answer["drwtNo1"], answer["drwtNo2"], answer["drwtNo3"], answer["drwtNo4"], answer["drwtNo5"],
                   answer["drwtNo6"], answer["bnusNo"]]

    target_list = [target["drwtNo1"], target["drwtNo2"], target["drwtNo3"], target["drwtNo4"], target["drwtNo5"],
                   target["drwtNo6"]]

    result = [target["id"], answer['drwNo'], target['user'], target['created_date'], target_list, []]

    for answer in answer_list:
        if answer in target_list:
            result[5].append(answer)
            count += 1

    if count >= 3 and answer_list[6] not in result[5] or count == 6 and answer_list[6] in result[5]:
        return check_lotto_rank(result, answer_list[6], count)


def check_lotto_rank(list, bnusNo, count):
    if count == 3 and bnusNo not in list:
         list.append('5')
    elif count == 4 and bnusNo not in list:
         list.append('4')
    elif count == 5 and bnusNo not in list:
         list.append('3')
    elif count == 6 and bnusNo in list[5]:
         list.append('2')
    elif count == 6 and bnusNo not in list[5]:
         list.append('1')

    return list
