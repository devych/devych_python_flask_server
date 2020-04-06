def get_rank_lotto(is_including_bnusNo):
    from app.controllers import connect_db
    is_including_bnusNo = int(is_including_bnusNo)
    rank = {}
    conn = connect_db()
    curs = conn.cursor()
    try:
        if is_including_bnusNo:
            sql = """select drwtNo1,drwtNo2,drwtNo3,drwtNo4,drwtNo5,drwtNo6,bnusNo from lotto_draw_info"""
        else:
            sql = """select drwtNo1,drwtNo2,drwtNo3,drwtNo4,drwtNo5,drwtNo6 from lotto_draw_info"""

        curs.execute(sql)
        rows = curs.fetchall()

        for t in rows:
            for i in t:
                if i in rank:
                    rank[i] += 1
                else:
                    rank[i] = 1

        # sort by desc
        rank = sorted(rank.items(), reverse=True, key=lambda item: item[1])

        # print(rank)
    except ValueError:
        print(ValueError)
    finally:
        curs.close()
        conn.close()
    return rank
