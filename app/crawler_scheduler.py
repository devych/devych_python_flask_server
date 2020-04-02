import schedule
import time
from app.controllers import insert_all_lottos

schedule.every().saturday.at("20:50").do(insert_all_lottos)
schedule.every().saturday.at("20:51").do(insert_all_lottos)
schedule.every().saturday.at("20:52").do(insert_all_lottos)
schedule.every().saturday.at("20:53").do(insert_all_lottos)
schedule.every().saturday.at("20:54").do(insert_all_lottos)
schedule.every().saturday.at("20:55").do(insert_all_lottos)
schedule.every().saturday.at("21:00").do(insert_all_lottos)
schedule.every().saturday.at("21:30").do(insert_all_lottos)
schedule.every().saturday.at("22:00").do(insert_all_lottos)

while True:
    schedule.run_pending()
    time.sleep(1)
