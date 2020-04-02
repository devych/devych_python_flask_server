from apscheduler.schedulers.background import BackgroundScheduler
from flask import Flask, jsonify
from app.api.Lotto import Lotto
from app.controllers import insert_all_lottos


app = Flask(__name__, instance_relative_config=True)


@app.route('/lotto/<num>', methods=['GET'])
def get_lotto(num):
    data = Lotto.get_drw_lotto(num)
    return jsonify(data=data)


@app.route('/lotto/create/<num>', methods=['GET'])
def create_lotto(num):
    data = Lotto.create_lotto_num(num)
    return jsonify(data=data)


@app.route('/lotto/rank/<boolean>', methods=['GET'])
def get_lotto_ranking(boolean):
    data = Lotto.ranking_lotto_num(boolean)
    return jsonify(data=data)


scheduler = BackgroundScheduler()
scheduler.add_job(insert_all_lottos, 'cron', day_of_week='sat', hour='20-21', minute='50-60')
scheduler.start()
