import sys
import time

sys.path.append('../')

import pymadeline

bot = pymadeline.pyMadeline()
phone = input('phone: ')

bot.login(1, phone=phone)
code = input('code: ')

try:
	bot.login(2, code=code)
except pymadeline.worker.ApiRequestException as e:
	# if it failed, maybe the account has a two step verification,
	# then you must send the password.
	print(str(e))
	password = input('password: ')
	bot.login(3, password=password)
else:
	print('the end.')

