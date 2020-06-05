import random
from app.controllers \
    import insert_created_lotto, get_rank_lotto, select_drw_lotto, check_lotto_number, generated_lotto, fully_auto_generate_lottos


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
    def generate_lotto(num=1, fix=[], remove=[]):
        lists = []

        def pick_ball(balls, inner_fix, inner_remove):
            ball = random.sample(range(1, 46), 1)
            if ball[0] not in inner_remove and ball[0] not in balls:
                balls.append(ball[0])

            if len(balls) == 6:
                balls.sort()
                lists.append(balls)
            else:
                pick_ball(balls, inner_fix, inner_remove)

        while len(lists) < int(num):
            lotto = fix[:]
            pick_ball(lotto, fix, remove)
        insert_created_lotto(lists)
        return lists

    @staticmethod
    def get_drw_lotto(num):
        data = select_drw_lotto(num)
        return data

    @staticmethod
    def get_ranking_lotto_num(bool):
        data = get_rank_lotto(bool)
        return data

    @staticmethod
    def get_creted_lotto_result():
        data = check_lotto_number()
        return data

    @staticmethod
    def get_genrerated_lottos():
        data = generated_lotto()
        return data

    @staticmethod
    def get_fully_auto_genrerated_lottos(num):
        data = fully_auto_generate_lottos(num)
        return data
