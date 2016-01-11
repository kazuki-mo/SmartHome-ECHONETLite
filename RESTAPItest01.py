#!/usr/bin/env python
# -*- coding: utf-8 -*-

import json
from functools import wraps
import subprocess

from flask import Flask, jsonify, request, url_for, abort, Response

app = Flask(__name__)

# ダミーデータ (DB の代わり)
id_index = 3
users = {1: {'id': 1, 'name': 'foo'},
         2: {'id': 2, 'name': 'bar'}}


def consumes(content_type):
    def _consumes(function):
        @wraps(function)
        def __consumes(*argv, **keywords):
            if request.headers['Content-Type'] != content_type:
                abort(400)
            return function(*argv, **keywords)
        return __consumes
    return _consumes

AirconBR_IP = "192.168.126.104"
AirconLR_IP = "192.168.126.103"

############################ Aircon_BR #######################################
@app.route('/Aircon_BR/Power/<value>')
def AirconBR_Power(value):
    if value == "On":
        value = "30"
    elif value == "Off":
        value = "31"
    cmd = "./OneShotSender " + AirconBR_IP + " 0 0001 0ef001 013001 61 80 " + value
    subprocess.call(cmd.split(" "))
    cmd = "./OneShotSender -r " + AirconBR_IP + " 0 0001 0ef001 013001 62 80 ."
    check = subprocess.check_output(cmd.split(" "))
    return str(check)

@app.route('/Aircon_BR/DriveMode/<value>')
def AirconBR_DriveMode(value):
    if value == "Auto":
        value = "41"
    elif value == "Cool":
        value = "42"
    elif value == "Heat":
        value = "43"
    elif value == "Dehum":
        value = "44"
    elif value == "Blast":
        value = "45"
    elif value == "Other":
        value = "40"
    cmd = "./OneShotSender " + AirconBR_IP + " 0 0001 0ef001 013001 61 B0 " + value
    subprocess.call(cmd.split(" "))
    cmd = "./OneShotSender -r " + AirconBR_IP + " 0 0001 0ef001 013001 62 B0 ."
    check = subprocess.check_output(cmd.split(" "))
    return str(check)

@app.route('/Aircon_BR/SetTemp/<value>')
def AirconBR_SetTemp(value):
    value = format(int(value), 'x')
    cmd = "./OneShotSender " + AirconBR_IP + " 0 0001 0ef001 013001 61 B3 " + value
    subprocess.call(cmd.split(" "))
    cmd = "./OneShotSender -r " + AirconBR_IP + " 0 0001 0ef001 013001 62 B3 ."
    check = subprocess.check_output(cmd.split(" "))
    return str(check)

@app.route('/Aircon_BR/AirFlow/<value>')
def AirconBR_AirFlow(value):
    if value == "Auto":
        value = "41"
    else:
        value = format(int(value)+48, 'x')
    cmd = "./OneShotSender " + AirconBR_IP + " 0 0001 0ef001 013001 61 A0 " + value
    subprocess.call(cmd.split(" "))
    cmd = "./OneShotSender -r " + AirconBR_IP + " 0 0001 0ef001 013001 62 A0 ."
    check = subprocess.check_output(cmd.split(" "))
    return str(check)


############################ Aircon_LR #######################################
@app.route('/Aircon_LR/Power/<value>')
def AirconLR_Power(value):
    if value == "On":
        value = "30"
    elif value == "Off":
        value = "31"
    cmd = "./OneShotSender " + AirconLR_IP + " 0 0001 0ef001 013001 61 80 " + value
    subprocess.call(cmd.split(" "))
    cmd = "./OneShotSender -r " + AirconLR_IP + " 0 0001 0ef001 013001 62 80 ."
    check = subprocess.check_output(cmd.split(" "))
    return str(check)

@app.route('/Aircon_LR/DriveMode/<value>')
def AirconLR_DriveMode(value):
    if value == "Auto":
        value = "41"
    elif value == "Cool":
        value = "42"
    elif value == "Heat":
        value = "43"
    elif value == "Dehum":
        value = "44"
    elif value == "Blast":
        value = "45"
    elif value == "Other":
        value = "40"
    cmd = "./OneShotSender " + AirconLR_IP + " 0 0001 0ef001 013001 61 B0 " + value
    subprocess.call(cmd.split(" "))
    cmd = "./OneShotSender -r " + AirconLR_IP + " 0 0001 0ef001 013001 62 B0 ."
    check = subprocess.check_output(cmd.split(" "))
    return str(check)

@app.route('/Aircon_LR/SetTemp/<value>')
def AirconLR_SetTemp(value):
    value = format(int(value), 'x')
    cmd = "./OneShotSender " + AirconLR_IP + " 0 0001 0ef001 013001 61 B3 " + value
    subprocess.call(cmd.split(" "))
    cmd = "./OneShotSender -r " + AirconLR_IP + " 0 0001 0ef001 013001 62 B3 ."
    check = subprocess.check_output(cmd.split(" "))
    return str(check)

@app.route('/Aircon_LR/AirFlow/<value>')
def AirconLR_AirFlow(value):
    if value == "Auto":
        value = "41"
    else:
        value = format(int(value)+48, 'x')
    cmd = "./OneShotSender " + AirconLR_IP + " 0 0001 0ef001 013001 61 A0 " + value
    subprocess.call(cmd.split(" "))
    cmd = "./OneShotSender -r " + AirconLR_IP + " 0 0001 0ef001 013001 62 A0 ."
    check = subprocess.check_output(cmd.split(" "))
    return str(check)

@app.route('/')
def hello():
    global users
    print(users)
    return str(users)

@app.route('/users', methods=['GET'])
def index():
    # ユーザ一覧からレスポンスを作る
    response = jsonify({'results': users.values()})
    # ステータスコードは OK (200)
    response.status_code = 200
    return response


@app.route('/users', methods=['POST'])
@consumes('application/json')
def create():
    global id_index
    # Content-Body を JSON 形式として辞書に変換する
    content_body_dict = json.loads(request.data)
    # ID を付与する
    content_body_dict['id'] = id_index
    # ID をインクリメントする
    id_index += 1
    # ユーザ一覧に追加する
    users[content_body_dict['id']] = (content_body_dict)
    # レスポンスオブジェクトを作る
    response = jsonify(content_body_dict)
    # ステータスコードは Created (201)
    response.status_code = 201
    # 作成したリソースを Location ヘッダを設定する
    response.headers['Location'] = url_for('read',
                                           user_id=content_body_dict['id'])
    return response


def _get_user(user_id):
    user = users.get(user_id)
    if user is None:
        abort(404)
    return user


@app.route('/users/<user_id>', methods=['GET'])
def read(user_id):
    # リクエストされたパスと ID を持つユーザを探す
    found_user = _get_user(user_id)
    # レスポンスオブジェクトを作る
    response = jsonify(found_user)
    # ステータスコードは Created (201)
    response.status_code = 200
    return response


@app.route('/users/<user_id>', methods=['PUT'])
@consumes('application/json')
def update(user_id):
    # Content-Body を JSON 形式として辞書に変換する
    content_body_dict = json.loads(request.data)
    # リクエストされたパスと ID を持つユーザを探す
    found_user = _get_user(user_id)
    # ユーザ名を書き換える
    found_user['name'] = content_body_dict['name']
    # レスポンスオブジェクトを作る
    response = jsonify(found_user)
    # ステータスコードは Created (201)
    response.status_code = 200
    return response


@app.route('/users/<user_id>', methods=['DELETE'])
def delete(user_id):
    # リクエストされたパスと ID を持つユーザを探す
    _get_user(user_id)
    # ユーザがいれば削除する
    users.pop(user_id)
    # レスポンスオブジェクトを作る
    response = Response()
    # ステータスコードは NoContent (204)
    response.status_code = 204
    return response

if __name__ == '__main__':
    app.run(host='0.0.0.0')
