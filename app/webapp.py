from apscheduler.schedulers.background import BackgroundScheduler
from flask import Flask, jsonify, request
from waitress import serve
from app.api.Lotto import Lotto
from app.controllers import insert_all_lottos

app = Flask(__name__, instance_relative_config=True)


@app.route('/lotto/<num>', methods=['GET'])
def get_lotto(num):
    data = Lotto.get_drw_lotto(num)
    print('get_lotto', jsonify(request.json))
    return jsonify(data=data)


@app.route('/lotto/create/<num>', methods=['GET'])
def create_lotto(num):
    data = Lotto.create_lotto_num(num)
    print('create_lotto', jsonify(request.json))
    return jsonify(data=data)


@app.route('/lotto/rank/<boolean>', methods=['GET'])
def get_lotto_ranking(boolean):
    data = Lotto.ranking_lotto_num(boolean)
    print('get_lotto_ranking', jsonify(request.json))
    return jsonify(data=data)


scheduler = BackgroundScheduler()
scheduler.add_job(insert_all_lottos, 'cron', day_of_week='sat', hour='21', minute='5-30')
scheduler.start()

if __name__ == "__main__":
    app.debug = True
    serve(app, host='0.0.0.0', port=5000)
