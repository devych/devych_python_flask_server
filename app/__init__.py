from flask import Flask, jsonify
from app.lotto_api.Lotto import Lotto
from app.controllers import select_drw_lotto

print('app.init')

app = Flask(__name__, instance_relative_config=True)


@app.route('/lotto/<num>')
def get_lotto(num):
    data = Lotto.get_drw_lotto(num)
    return jsonify(data=data)


@app.route('/lotto/create/<num>')
def create_lotto(num):
    data = Lotto.create_lotto_num(num)
    return jsonify(data=data)


@app.route('/lotto/rank/<boolean>')
def get_lotto_ranking(boolean):
    data = Lotto.ranking_lotto_num(boolean)
    return jsonify(data=data)
