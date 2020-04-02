from env.env import dbconfig
import pymysql
from app.controllers.crawl_lotto import insert_all_lottos, get_last_draw
from app.controllers.insert_created_lotto import insert_created_lotto
from app.controllers.rank_lotto import get_rank_lotto
from app.controllers.select_drw_lotto import select_drw_lotto


def connect_db():
    conn = pymysql.connect(host=dbconfig['host'], user=dbconfig['user'], password=dbconfig['password'],
                           db=dbconfig['db'], charset='utf8')
    return conn
