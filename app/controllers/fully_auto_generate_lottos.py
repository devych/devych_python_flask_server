def fully_auto_generate_lottos(num, user_ip):
    from app.controllers import get_rank_lotto, insert_created_lotto
    from app.api.Lotto import Lotto
    import random

    lotto_rank = get_rank_lotto(0)
    lotto_rank = list(map(lambda x: x[0], lotto_rank))

    autoFixLottos = random.sample(lotto_rank[:14], 2)
    autoRemoveLottos = random.sample(lotto_rank[-12:], 8)

    data = Lotto.generate_lotto(num, autoFixLottos, autoRemoveLottos, user_ip)

    return data
