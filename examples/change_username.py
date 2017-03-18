#!/usr/bin/python3
# -*- coding: utf-8 -*-

import sys
import time

sys.path.append('../')

import pymadeline

TOKEN = '' # here the bot token.

TOKEN = input('give the token: ')
new_username = input('new username: ')

print('I am going to change the username to %s' % new_username)

bot = pymadeline.pyMadeline(TOKEN)

info = bot.push(
	'account.updateUsername',
	username=new_username
)
print('I did it :%s' % str(info))