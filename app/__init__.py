from flask import Flask, jsonify
from app.lotto_api.Lotto import Lotto
from app.controllers.select_drw_lotto import select_drw_lotto
from app import routes

print('app.init')

app = Flask(__name__, instance_relative_config=True)


@app.route('/hello')
def hello():
    return jsonify(hello='world')


@app.route('/dbtest')
def db_test():
    pass


@app.route('/lotto/<num>')
def get_lotto(num):
    data = select_drw_lotto(num)
    return jsonify(data=data)


@app.route('/lotto/create/<num>')
def create_lotto(num):
    data = Lotto.create_lotto_num(num)
    return jsonify(data=data)