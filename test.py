# -*- coding: utf-8 -*-

import commands

check = commands.getoutput("./OneShotSender -r 192.168.10.77 0 0001 0ef001 013001 62 80 . BB .")

print check
