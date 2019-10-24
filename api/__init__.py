# -*- coding: utf-8 -*-
"""
Onyx Project
https://onyxlabs.fr
Software under licence Creative Commons 3.0 France
http://creativecommons.org/licenses/by-nc-sa/3.0/fr/
You may not use this software for commercial purposes.
@author :: Cassim Khouani
"""
from onyx.util.log import getLogger
from onyx.api.assets import Json
from onyx.api.exceptions import *
try:
	import urllib.request
except ImportError:
	import urllib

logger = getLogger('Transport')
json = Json()

"""
	Get information of RATP service

	Informations sur les différents services de la RATP
"""
class Ratp:

	def __init__(self):
		self.url = None
		self.line = None
		self.station = None
		self.direction = None

	def get_metro_schedule(self):
		try:
			return 'https://api-ratp.pierre-grimaud.fr/v4/schedules/metros/{}/{}/{}/'.format(self.line, self.station, self.direction)
		except Exception as e:
			logger.error('Metro error : ' + str(e))
			raise TransportException(str(e))


	def get_rer_schedule(self):
		try:
			return 'https://api-ratp.pierre-grimaud.fr/v4/schedules/rers/{}/{}/{}/'.format(self.line, self.station, self.direction)
		except Exception as e:
			logger.error('Rer error : ' + str(e))
			raise TransportException(str(e))
