# -*- coding: utf-8 -*-

#######################
NAME = "RealMadrid"
VERSION = "1.0.0"
PASSWORD = "freelance"
#######################

import sys
from time import sleep, strftime

f = open('%s.log' % NAME, 'a')
f.write("%s %s\n"%(strftime("%d.%m.%Y"), strftime("%H:%M:%S")))
f.close()
f = open('%s.log' % NAME, 'a')
sys.stderr = f

##################------Основные
# import os
# from os.path import split, splitext, join, exists, basename
# from os import listdir
# import shutil
import random

##################------Системные
# import psutil
# import pyperclip
# import traceback

##################------Строки
# from base64 import b64encode as base64
# from string import ascii_uppercase, ascii_lowercase, digits
# import cPickle as pickle

##################------Интернет
# import urllib2
# import urlparse
# import requests
# import subprocess
# import json

##################------selenium
from selenium import webdriver
# from selenium.webdriver.firefox.firefox_profile import FirefoxProfile
# from selenium.webdriver.firefox.firefox_binary import FirefoxBinary

##################------Автоматизация
# from pywinauto.application import Application
# import pyautogui
# from pyautogui import keyDown, keyUp


def UA():#Список User-Agent'ов
	with open("UAs.txt", "r") as file:
		lUA = file.read().split("\n")[:-1]
	return random.choice(lUA)

class Driver:#Работа с драйвером
	"""docstring for Driver"""
	def __init__(self, typeD = "Chrome", proxy = None, isTor = 0, UserAgent = 0):
		# super(Driver, self).__init__()
		self.typeD = typeD
		self.wait = 15
		self.isTor = isTor
		self.UserAgent = UserAgent
		self.proxy = proxy
		self.preference()
	def preference(self):
		if self.typeD == "Chrome":
			self.chrome_options = webdriver.ChromeOptions()
			if self.UserAgent:
				self.chrome_options.add_argument('--user-agent=%s'%self.UserAgent)
			if self.isTor:
				self.chrome_options.add_argument('--proxy-server=socks5://127.0.0.1:9150')
			if self.proxy:
				self.chrome_options.add_argument('--proxy-server=%s'%self.proxy)# "(http|socks4|socks5)://000.000.000.000:8080"
		elif self.typeD == "FF":
			self.ff_prof=webdriver.FirefoxProfile()
			if self.UserAgent:
				self.ff_prof.set_preference('general.useragent.override', self.UserAgent)
			if self.proxy:
				self.ff_prof.set_preference( "network.proxy.type", 1 )
				self.ff_prof.set_preference( "network.proxy.socks_version", 5 )
				self.ff_prof.set_preference( "network.proxy.socks", self.proxy.split(":")[0])
				self.ff_prof.set_preference( "network.proxy.socks_port", int(self.proxy.split(":")[1]) )
				self.ff_prof.set_preference( "network.proxy.socks_remote_dns", True )
			if self.isTor:
				tor_path = "%sTor Browser\\Browser\\firefox.exe"%dic["pathTor"]
				# Настройки приватности
				self.ff_prof.set_preference( "places.history.enabled", True )
				self.ff_prof.set_preference( "privacy.clearOnShutdown.offlineApps", True )
				self.ff_prof.set_preference( "privacy.clearOnShutdown.passwords", True )
				self.ff_prof.set_preference( "privacy.clearOnShutdown.siteSettings", True )
				self.ff_prof.set_preference( "privacy.sanitize.sanitizeOnShutdown", True )
				self.ff_prof.set_preference( "signon.rememberSignons", False )
				self.ff_prof.set_preference( "network.cookie.lifetimePolicy", 2 )
				self.ff_prof.set_preference( "network.dns.disablePrefetch", False )
				self.ff_prof.set_preference( "network.http.sendRefererHeader", 2 )		
				# Настраиваем Прокси
				self.ff_prof.set_preference( "network.proxy.type", 1 )
				self.ff_prof.set_preference( "network.proxy.socks_version", 5 )
				self.ff_prof.set_preference( "network.proxy.socks", '127.0.0.1' )
				self.ff_prof.set_preference( "network.proxy.socks_port", 9150 )
				self.ff_prof.set_preference( "network.proxy.socks_remote_dns", True )
				# Отключаем загрузку изображений через Tor - для ускорения соединений
				self.ff_prof.set_preference('general.useragent.override', self.UA())
				self.binary = FirefoxBinary(tor_path)
	def open(self):
		if self.typeD == "Chrome":
			self.driver = webdriver.Chrome(executable_path="/usr/lib/chromium-browser/chromedriver",chrome_options=self.chrome_options)
		elif self.typeD == "FF":
			if not self.isTor:
				self.driver = webdriver.Firefox()
			else:
				self.driver = webdriver.Firefox(self.ff_prof, self.binary)
		return self.driver
	def close(self):
		self.driver.quit()
	def click(self, elem):
		try:
			try:
				elem.click()
			except:
				self.driver.execute_script("arguments[0].click(); ", elem)
			return 1
		except:
			return 0
	def xpath(self, xpath, is_one = 1, is_displayed = 1, is_click = 1, clickAll = 0, start_wait = 1.5, wait = None):
		sleep(start_wait)
		thisWait = wait if wait != None else self.wait
		for waitOne in xrange(thisWait + 1):
			elems = self.driver.find_elements_by_xpath(xpath)
			if is_one and len(elems) >= 1 and ((not is_displayed) or (is_displayed and elems[0].is_displayed())):
				if is_click:
					return self.click(elems[0]), elems[0]
				else:
					return elems[0]
			elif not is_one and len(elems) >= 1:
				retElems = []
				for elem in elems:
					if is_displayed and not elem.is_displayed():
						continue
					if clickAll:
						x = self.click(elem)
					retElems += [elem]
				return retElems
			sleep(1)
		return [0, 0] if not is_one else []
	def max_win(self):#Размер браузера - на все окно
		self.driver.maximize_window()
	def get(self, path):
		self.driver.get(path)
	def js(self, script = None, path = None):
		if script:
			self.driver.execute_script(script)
		elif path:
			with open(path, "r") as file:
				self.driver.execute_script(file.read())
		else:
			print("ERROR: Not js for running!!!")

###################################################




try:# Настройки
	with open("settings.ini", "r") as file:
		dic = {}
		for i in file.read().split("\n")[:-1]:
			dic[i.split(":::")[0]] = i.split(":::")[1]
except:
	pass




print( "TEST")

ua = UA()
driver = Driver(UserAgent = ua, typeD = "Chrome")
print(1)

driver.open()
print(1)
driver.max_win()
print(1)
driver.get("https://www.realmadrid.com/en/tickets")
print(1)
print(driver.getTitle())
print(1)


sleep(500)

driver.close()

################################################
print( "end(5)")
sleep(5)