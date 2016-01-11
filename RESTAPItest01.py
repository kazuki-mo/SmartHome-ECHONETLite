#!/usr/bin/env python
# -*- coding: utf-8 -*-

import json
from functools import wraps
import subprocess

from flask import Flask, jsonify, request, url_for, abort, Response

app = Flask(__name__)

AirconBR_IP = "192.168.126.104"
AirconLR_IP = "192.168.126.103"
TV_IP = "192.168.126.105"
IH_IP = "192.168.126.106"
Refrige_IP = "192.168.126.107"
Light_IP = "192.168.126.101"


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
    value = format(int(value), '02x')
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
        value = format(int(value)+48, '02x')
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
    value = format(int(value), '02x')
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
        value = format(int(value)+48, '02x')
    cmd = "./OneShotSender " + AirconLR_IP + " 0 0001 0ef001 013001 61 A0 " + value
    subprocess.call(cmd.split(" "))
    cmd = "./OneShotSender -r " + AirconLR_IP + " 0 0001 0ef001 013001 62 A0 ."
    check = subprocess.check_output(cmd.split(" "))
    return str(check)


############################ TV #######################################
@app.route('/TV/Power/<value>')
def TV_Power(value):
    if value == "On":
        value = "30"
    elif value == "Off":
        value = "31"
    cmd = "./OneShotSender " + TV_IP + " 0 0001 0ef001 060201 61 80 " + value
    subprocess.call(cmd.split(" "))
    cmd = "./OneShotSender -r " + TV_IP + " 0 0001 0ef001 060201 62 80 ."
    check = subprocess.check_output(cmd.split(" "))
    return str(check)


############################ IH #######################################
@app.route('/IH/Power/<value>')
def IH_Power(value):
    if value == "On":
        value = "30"
    elif value == "Off":
        value = "31"
    cmd = "./OneShotSender " + IH_IP + " 0 0001 0ef001 03B901 61 80 " + value
    subprocess.call(cmd.split(" "))
    cmd = "./OneShotSender -r " + IH_IP + " 0 0001 0ef001 03B901 62 80 ."
    check = subprocess.check_output(cmd.split(" "))
    return str(check)

@app.route('/IH/AllStop')
def IH_AllStop():
    cmd = "./OneShotSender " + IH_IP + " 0 0001 0ef001 03B901 61 B3 40"
    subprocess.call(cmd.split(" "))
    return "Success"


############################ Light #######################################
@app.route('/Light/Power/<value>')
def Light_Power(value):
    if value == "On":
        value = "30"
    elif value == "Off":
        value = "31"
    cmd = "./OneShotSender " + Light_IP + " 0 0001 0ef001 029001 61 80 " + value
    subprocess.call(cmd.split(" "))
    cmd = "./OneShotSender -r " + Light_IP + " 0 0001 0ef001 029001 62 80 ."
    check = subprocess.check_output(cmd.split(" "))
    return str(check)

@app.route('/Light/LightLevel/<value>')
def Light_LightLevel(value):
    value = format(int(value), '02x')
    cmd = "./OneShotSender " + Light_IP + " 0 0001 0ef001 029001 61 B0 " + value
    subprocess.call(cmd.split(" "))
    cmd = "./OneShotSender -r " + Light_IP + " 0 0001 0ef001 029001 62 B0 ."
    check = subprocess.check_output(cmd.split(" "))
    return str(check)

@app.route('/Light/LightColor/<value>')
def Light_LightColor(value):
    if value == "LightBulb":
        value = "41"
    elif value == "White":
        value = "42"
    elif value == "NaturalWhite":
        value = "43"
    elif value == "Daylight":
        value = "44"
    elif value == "Other":
        value = "40"
    cmd = "./OneShotSender " + Light_IP + " 0 0001 0ef001 029001 61 B1 " + value
    subprocess.call(cmd.split(" "))
    cmd = "./OneShotSender -r " + Light_IP + " 0 0001 0ef001 029001 62 B1 ."
    check = subprocess.check_output(cmd.split(" "))
    return str(check)

@app.route('/Light/LightLevelStage/<value>')
def Light_LightLevelStage(value):
    value = format(int(value), '02x')
    cmd = "./OneShotSender " + Light_IP + " 0 0001 0ef001 029001 61 B2 " + value
    subprocess.call(cmd.split(" "))
    cmd = "./OneShotSender -r " + Light_IP + " 0 0001 0ef001 029001 62 B2 ."
    check = subprocess.check_output(cmd.split(" "))
    return str(check)

@app.route('/Light/LightColorStage/<value>')
def Light_LightColorStage(value):
    value = format(int(value), '02x')
    cmd = "./OneShotSender " + Light_IP + " 0 0001 0ef001 029001 61 B3 " + value
    subprocess.call(cmd.split(" "))
    cmd = "./OneShotSender -r " + Light_IP + " 0 0001 0ef001 029001 62 B3 ."
    check = subprocess.check_output(cmd.split(" "))
    return str(check)

@app.route('/Light/LightingMode/<value>')
def Light_LightingMode(value):
    if value == "Auto":
        value = "41"
    elif value == "Normal":
        value = "42"
    elif value == "Night":
        value = "43"
    elif value == "Color":
        value = "45"
    cmd = "./OneShotSender " + Light_IP + " 0 0001 0ef001 029001 61 B6 " + value
    subprocess.call(cmd.split(" "))
    cmd = "./OneShotSender -r " + Light_IP + " 0 0001 0ef001 029001 62 B6 ."
    check = subprocess.check_output(cmd.split(" "))
    return str(check)

@app.route('/Light/LightLevel_Normal/<value>')
def Light_LightLevelNormal(value):
    value = format(int(value), '02x')
    cmd = "./OneShotSender " + Light_IP + " 0 0001 0ef001 029001 61 B7 " + value
    subprocess.call(cmd.split(" "))
    cmd = "./OneShotSender -r " + Light_IP + " 0 0001 0ef001 029001 62 B7 ."
    check = subprocess.check_output(cmd.split(" "))
    return str(check)

@app.route('/Light/LightLevelStage_Normal/<value>')
def Light_LightLevelStageNormal(value):
    value = format(int(value), '02x')
    cmd = "./OneShotSender " + Light_IP + " 0 0001 0ef001 029001 61 B8 " + value
    subprocess.call(cmd.split(" "))
    cmd = "./OneShotSender -r " + Light_IP + " 0 0001 0ef001 029001 62 B8 ."
    check = subprocess.check_output(cmd.split(" "))
    return str(check)

@app.route('/Light/LightLevel_Night/<value>')
def Light_LightLevelNight(value):
    value = format(int(value), '02x')
    cmd = "./OneShotSender " + Light_IP + " 0 0001 0ef001 029001 61 B9 " + value
    subprocess.call(cmd.split(" "))
    cmd = "./OneShotSender -r " + Light_IP + " 0 0001 0ef001 029001 62 B9 ."
    check = subprocess.check_output(cmd.split(" "))
    return str(check)

@app.route('/Light/LightLevelStage_Night/<value>')
def Light_LightLevelStageNight(value):
    value = format(int(value), '02x')
    cmd = "./OneShotSender " + Light_IP + " 0 0001 0ef001 029001 61 BA " + value
    subprocess.call(cmd.split(" "))
    cmd = "./OneShotSender -r " + Light_IP + " 0 0001 0ef001 029001 62 BA ."
    check = subprocess.check_output(cmd.split(" "))
    return str(check)

@app.route('/Light/LightColor_Normal/<value>')
def Light_LightColor_Normal(value):
    if value == "LightBulb":
        value = "41"
    elif value == "White":
        value = "42"
    elif value == "NaturalWhite":
        value = "43"
    elif value == "Daylight":
        value = "44"
    elif value == "Other":
        value = "40"
    cmd = "./OneShotSender " + Light_IP + " 0 0001 0ef001 029001 61 BB " + value
    subprocess.call(cmd.split(" "))
    cmd = "./OneShotSender -r " + Light_IP + " 0 0001 0ef001 029001 62 BB ."
    check = subprocess.check_output(cmd.split(" "))
    return str(check)

@app.route('/Light/LightColorStage_Normal/<value>')
def Light_LightColorStage_Normal(value):
    value = format(int(value), '02x')
    cmd = "./OneShotSender " + Light_IP + " 0 0001 0ef001 029001 61 BC " + value
    subprocess.call(cmd.split(" "))
    cmd = "./OneShotSender -r " + Light_IP + " 0 0001 0ef001 029001 62 BC ."
    check = subprocess.check_output(cmd.split(" "))
    return str(check)


if __name__ == '__main__':
    app.run(host='0.0.0.0')
