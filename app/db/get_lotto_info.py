import requests
import pymysql
from env.env import dbconfig


def connect_db():
    conn = pymysql.connect(host=dbconfig['host'], user=dbconfig['user'], password=dbconfig['password'],
                           db=dbconfig['db'], charset='utf8')
    return conn


def get_last_draw():
    lastDraw = 0
    conn = connect_db()
    curs = conn.cursor(pymysql.cursors.DictCursor)
    try:
        sql = """select * from lottoDrawInfo order by drwNoDate desc limit 1 """
        curs.execute(sql)
        row = curs.fetchone()
        if row is not None:
            lastDraw = row["drwNo"]

        print('lastDraw is', lastDraw)
    except:
        print('error!')

    conn.close()
    return lastDraw


def insert_all_lottos():
    curDraw = get_last_draw() + 1
    while 1:
        data = requests.get("http://www.nlotto.co.kr/common.do?method=getLottoNumber&drwNo=" + str(curDraw))
        if data.json()["returnValue"] == "success":
            insert_one_lotto(curDraw)
            curDraw += 1
        else:
            print(curDraw, '회 로또는 아직 진행중입니다.')
            break


def insert_one_lotto(num):
    conn = connect_db()

    curs = conn.cursor(pymysql.cursors.DictCursor)
    sql = """select * from lottoDrawInfo where drwNo = %s """
    curs.execute(sql, (str(num)))
    rows = curs.fetchall()
    if len(rows) == 0:
        try:
            data = requests.get("http://www.nlotto.co.kr/common.do?method=getLottoNumber&drwNo=" + str(num))
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

            sql = """insert lottoDrawInfo(drwNo, drwNoDate, firstAccumamnt, firstPrzwnerCo, firstWinamnt, totSellamnt, 
            drwtNo1, drwtNo2, drwtNo3, drwtNo4, drwtNo5, drwtNo6, bnusNo) values(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, 
            %s, %s, %s) """

            curs.execute(sql, (
                drwNo, drwNoDate, firstAccumamnt, firstPrzwnerCo, firstWinamnt, totSellamnt, drwtNo1, drwtNo2, drwtNo3,
                drwtNo4, drwtNo5, drwtNo6, bnusNo))
            conn.commit()
            print(num, 'draw Lotto Information is Succesfully inserted')
        except:
            print(num, "draw Lotto isn't finished yet")
    else:
        print(num, 'draw Lotto Information already exist')

    conn.close()


