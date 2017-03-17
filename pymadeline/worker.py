#!/usr/bin/python3
# -*- coding: utf-8 -*-

import requests
import json

url_base = 'https://api.pwrtelegram.xyz/user{0}/{1}'
url_login = 'https://api.pwrtelegram.xyz/phonelogin'

def send_query(token, method, mode='get', params=None, url_base=url_base):
	"""Recive the parameters value and create the full URL. After,
	it make a query to that. Returns dict object with the API's result

	:param token: the user token.
	:param method: the telegram method, see https://daniil.it/MadelineProto/API_docs/
	:param mode: the HTTP method: GET or POST
	:param params: A dict object with all params for the API of pwrtelegram
	:param url_base: optional, the API url.
	"""
	the_url = url_base.format(token, method)
	result = requests.request(mode, the_url, params=params, timeout=(4, 30))
	return check_result(mode, result)['result']

def request_login(telephone, url_login=url_login):
	result = requests.get(
		url_login,
		params={
			'phone': telephone
		}
	)
	return check_result('get', result)['result']

def check_result(mode, result):
	"""Check if we got an error :P
	"""
	if result.status_code != 200:
		error_msg = 'Error HTTP [{0}] {1} {2}, message: {2}'.format(
			mode, result.status_code, result.reason, result.text)
		raise GeneralApiException(error_msg)

	try:
		jresult = result.json()
	except Exception as e:
		error_msg = 'The server returned an weird thing: {0}: {1}'.format(str(e), result.text.decode('utf-8'))
		raise GeneralApiException(error_msg)

	if not jresult['ok']:
		raise ApiRequestException(jresult['error_code'], jresult['description'])

	return jresult

class GeneralApiException(Exception):
	"""When check_result finds an error.
	"""

	def __init__(self, text):
		super(GeneralApiException, self).__init__('General Api Exception. {0}'.format(text))

class ApiRequestException(Exception):
	"""When the requests was unsuccessful.
	"""

	def __init__(self, code, description):
		super(ApiRequestException, self).__init__('A request was unsuccessful. [{0}] {1}'.format(code, description))
		self.code = code
		self.description = description