#!/usr/bin/python3
# -*- coding: utf-8 -*-

import sys
import time

sys.path.append('../')

import pymadeline

TOKEN = '' # here the bot token.

TOKEN = input('give the token: ')
group_name = input('group name: ')

bot = pymadeline.pyMadeline(TOKEN)

info = bot.push(
	'messages.createChat',
	users='[555666555, 777888777, 999000999]', # users' id.
	title=group_name
)

print(info)