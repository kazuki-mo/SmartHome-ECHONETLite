# -*- coding: utf-8 -*-

import commands
import time
import threading
import httplib, urllib
import json

def sendCats():
	t = threading.Timer(3600, sendCats)
	t.start()	

	send80 = ""
	send8F = ""
	sendB0 = ""
	sendB3 = ""
	sendBB = ""
	sendA0 = ""

	check = commands.getoutput("./OneShotSender -r 192.168.126.104 0 0001 0ef001 013001 62 80 . 8F . B0 . B3 . BB . A0 . ")
	print check
	for line in check.splitlines():
		#print line + "\n"
		if line.find('epc') > -1:
			lineSplit = line.split(':')
			if lineSplit[2] == '80':
				send80 = lineSplit[3]
			elif lineSplit[2] == '8f':
				send8F = lineSplit[3]
			elif lineSplit[2] == 'b0':
				sendB0 = lineSplit[3]
			elif lineSplit[2] == 'b3':
				sendB3 = lineSplit[3]
			elif lineSplit[2] == 'bb':
				sendBB = lineSplit[3]
			elif lineSplit[2] == 'a0':
				sendA0 = lineSplit[3]
		

	params = '''[{"dt":null,"pw":null,"dat": ["'''+ send80 + '''","''' + send8F + '''","''' + sendB0 + '''","''' + sendB3 + '''","''' + sendBB + '''","''' + sendA0 + '''"]}]'''
	headers = {"Content-type": "application/JSON","charset": "UTF-8"}
	conn = httplib.HTTPConnection("192.168.10.67")
	conn.request("POST", "/Cats/api/dataadd/echonet/Aircon_BR", params, headers)
	response = conn.getresponse()
	print response.status, response.reason
	data = response.read()
	conn.close()
	print data

t = threading.Timer(3600, sendCats)
t.start()

try:
	while True:
		time.sleep(1)
except KeyboardInterrupt:
	print("end\n")
