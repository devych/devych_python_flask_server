import requests
import pymysql


def get_last_draw():
    from app.controllers import connect_db

    lastDraw = 0

    conn = connect_db()
    curs = conn.cursor(pymysql.cursors.DictCursor)
    try:
        sql = """select * from lotto_draw_info order by drwNoDate desc limit 1 """
        curs.execute(sql)
        row = curs.fetchone()
        if row is not None:
            lastDraw = row["drwNo"]
    except ValueError:
        print(ValueError)

    finally:
        curs.close()
        conn.close()
    return lastDraw


def insert_all_lottos():
    curDraw = get_last_draw() + 1
    print(curDraw, '회 로또 정보 업데이트를 시도합니다.')
    while 1:
        try:
            data = requests.get("https://dhlottery.co.kr/common.do?method=getLottoNumber&drwNo=" + str(curDraw))
            if data.json()["returnValue"] == "success" and data.json()["totSellamnt"] != 0:
                insert_one_lotto(curDraw)
                print(curDraw, '회 로또 정보가 업데이트되었습니다.')
                curDraw += 1
            else:
                print(curDraw, '회 로또는 아직 진행중입니다.')
                break
        except:
            print('insert_all_lottos error')


def insert_one_lotto(num):
    from app.controllers import connect_db

    conn = connect_db()
    curs = conn.cursor()
    sql = """select * from lotto_draw_info where drwNo = %s """
    curs.execute(sql, (str(num),))
    rows = curs.fetchall()
    try:
        if len(rows) == 0:
            data = requests.get("https://dhlottery.co.kr/common.do?method=getLottoNumber&drwNo=" + str(num))
            data = data.json()
            drwNo = data['drwNo']
            drwNoDate = data['drwNoDate']
            firstAccumamnt = data['firstAccumamnt']
            firstPrzwnerCo = data['firstPrzwnerCo']
            firstWinamnt = data['firstWinamnt']
            totSellamnt = data['totSellamnt']
            drwtNo1 = data['drwtNo1']
            drwtNo2 = data['drwtNo2']
            drwtNo3 = data['drwtNo3']
            drwtNo4 = data['drwtNo4']
            drwtNo5 = data['drwtNo5']
            drwtNo6 = data['drwtNo6']
            bnusNo = data['bnusNo']

            sql = """insert lotto_draw_info(drwNo, drwNoDate, firstAccumamnt, firstPrzwnerCo, firstWinamnt, totSellamnt, 
            drwtNo1, drwtNo2, drwtNo3, drwtNo4, drwtNo5, drwtNo6, bnusNo) values(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, 
            %s, %s, %s) """

            curs.execute(sql, (
                drwNo, drwNoDate, firstAccumamnt, firstPrzwnerCo, firstWinamnt, totSellamnt, drwtNo1, drwtNo2, drwtNo3,
                drwtNo4, drwtNo5, drwtNo6, bnusNo,))

            conn.commit()
            print(num, 'draw Lotto Information is Succesfully inserted')
        else:
            print(num, 'draw Lotto Information already exist')

    except :
        print(num, "draw Lotto isn't finished yet")

    finally:
        curs.close()
        conn.close()


