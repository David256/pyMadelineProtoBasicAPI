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
	def __init__(self, token):
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

	@staticmethod
	def subobjet(**kwargs):
		"""Converts the parameters in a JSON-Object.
		"""
		return json.dumps(kwargs)