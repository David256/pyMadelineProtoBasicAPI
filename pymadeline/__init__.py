#!/usr/bin/python3
# -*- coding: utf-8 -*-

import requests
import json

# The main module :D
from pymadeline import worker

class pyMadeline(object):
	"""This class defines to a MadelineProto API methods
	for Python.
	"""
	def __init__(self, token=None):
		self.token = token

	def push(self, method, **kwargs):
		"""This method is who has to send the query was
		sent by the user. For more information, you
		have to read the MadelineProto documentation in
		https://pwrtelegram.xyz/
		"""
		jresult = worker.send_query(
			token=self.token,
			method=method,
			mode='get',
			params=kwargs
		)

		return jresult

	def login(self, step, **kwargs):
		"""With this method, you can login in Telegram.

		The step parameter indicate the process to do, It
		can be 1, 2, 3 or 0. It will be 0 when you need to
		create a new account. The step 1 is always required and
		you must pass the parameter `phone` and Telegram will be
		available to send you a verification code. The step 2
		is normalty the last step, here you must pass the
		parameter `code` to get the *permanent access token*.
		But, if you have a password, then you must too use the
		step 3 and pass the password with the parameter `password`.


		step 1:
		:param phone: you telephone number.

		step 2:
		:param code: a code sent to your telephone.


		step 3:
		:param password: the password.

		step 0:
		:param first_name: your first name.
		:param last_name: (optional) your last name.
		"""
		if step == 1:
			jresult = worker.request_login(kwargs['phone'])
			self.token = jresult
			return True

		if step == 2:
			jresult = self.push(
				'completephonelogin',
				code=kwargs['code']
			)
			self.token = jresult
			return True

		if step == 3:
			jresult = self.push(
				'complete2FALogin',
				password=kwargs['password']
			)
			self.token = jresult
			return True

		if step == 0:
			jresult = self.push(
				'completesignup',
				first_name=kwargs['first_name'],
				last_name=kwargs['last_name'] if 'last_name' in kwargs else ''
			)
			self.token = jresult
			return True

	@staticmethod
	def subobject(*args, **kwargs):
		"""Converts the parameters in a JSON-Object or a List-Object.
		"""
		if len(args) == 0:
			return json.dumps(kwargs)
		else:
			return str(list(args))