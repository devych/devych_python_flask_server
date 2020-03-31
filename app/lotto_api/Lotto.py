from env.env import dbconfig
from flask import jsonify
import requests
import random
from app.controllers.insert_created_lotto import insert_created_lotto
import pdb


class Lotto:
    @staticmethod
    def create_lotto_num(num=1):
        lists = []
        for i in range(0, int(num)):
            lotto = random.sample(range(1, 46), 6)
            lotto.sort()
            lists.append(lotto)
        insert_created_lotto(lists)
        return lists

    @staticmethod
    def ranking_lotto_num():
        pass


