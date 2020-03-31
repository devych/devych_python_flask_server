from env.env import dbconfig
from flask import jsonify
import requests
import random
from app.controllers.insert_created_lotto import insert_created_lotto
import pdb


class Lotto:
    @staticmethod
    def set_all_lottos(num):
        data = requests.get("http://www.nlotto.co.kr/common.do?method=getLottoNumber&drwNo=" + num)
        print(data.text)
        return data.text

    @staticmethod
    def store_db_lotto():
        pass

    @staticmethod
    def create_lotto_num(num=1):
        lists = []
        for i in range(0, int(num)):
            lotto = random.sample(range(1, 46), 6)
            lotto.sort()
            lists.append(lotto)

        print(lists)
        return insert_created_lotto(lists)

    @staticmethod
    def ranking_lotto_num():
        pass


Lotto.create_lotto_num(10)
