# -*- coding: utf-8 -*-

#######################
NAME = "RealMadrid"
VERSION = "1.0.0"
PASSWORD = "freelance"
#######################

import sys
from time import sleep, strftime

f = open('RealMadrid.log', 'a')
f.write("%s %s\n"%(strftime("%d.%m.%Y"), strftime("%H:%M:%S")))
f.close()
f = open('RealMadrid.log', 'a')
sys.stderr = f
##################------Основные
import os
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
from selenium.webdriver.support.ui import Select
# from selenium.webdriver.firefox.firefox_profile import FirefoxProfile
# from selenium.webdriver.firefox.firefox_binary import FirefoxBinary

##################------Автоматизация
# from pywinauto.application import Application
# import pyautogui
# from pyautogui import keyDown, keyUp

##################------Interface
from tkinter import *

#################-------Selenide(MITATED modyfycation)
from selenide import Driver

def UA():#Список User-Agent'ов
	with open("UAs.txt", "r") as file:
		lUA = file.read().split("\n")[:-1]
	return random.choice(lUA)


class Run:
	def __init__(self):
		root=Tk()
		label = Label(text=u"Сколько мест искать?")
		label.grid(row=0, column=0, columnspan=7)
		button1 = Button(command=lambda: self.real(1), text=u"1")
		button1.grid(row=1, column=1, ipadx=10, ipady=2)
		button2 = Button(command=lambda: self.real(2), text=u"2")
		button2.grid(row=1, column=2, ipadx=10, ipady=2)
		button3 = Button(command=lambda: self.real(3), text=u"3")
		button3.grid(row=1, column=3, ipadx=10, ipady=2)
		button4 = Button(command=lambda: self.real(4), text=u"4")
		button4.grid(row=1, column=4, ipadx=10, ipady=2)
		root.mainloop()

	def real(self, NUM):
		ua = UA() #Read useragents
		driver = Driver(UserAgent = ua, typeD = "Chrome") #Initialize driver/browser

		driver.open()#Open driver/browser
		print("Maximize and fixed current window")
		driver.max_win() #For full monitor

		self.goto(driver, NUM)


	def goto(self, driver, NUM):
		window = driver.driver.current_window_handle

		print("GoTo")
		driver.get("https://www.realmadrid.com/en/tickets")

		if not driver.xpath("//*[contains(@class, 'header_section')]", is_click=0):
			print("Not tickets-page")
			return 0


		print("Click full button")
		driver.xpath("//a[@class='btn btn_full']")

		print("Switch window")
		driver.driver.switch_to_window(window)
		driver.driver.close()
		windows = driver.driver.window_handles
		driver.driver.switch_to_window(windows[0])
		self.sel(driver, NUM)
		driver.close()


	def sel(self, driver, NUM, errs = []):
		if not driver.xpath("//*[@id='selectNumEntradas']", is_click=0):
			print("Not Number of tickets")
			return 0


		select = Select(driver.xpath('//select[@id="num-entradas"]', is_click = 0, start_wait = 2.5, wait = 5))
		select.select_by_value("%s" % NUM)
		driver.xpath("//*[@id='boton-seleccion-entradas']")

		if not driver.xpath("//*[@id='sectors-list']", is_click=0):
			print("Not SEAT SELECTION")
			return 0

		sectors = ("padredamian", "conchaespina", "castellana", "rafaelsalgado") #Sectors
		for sector in sectors:
			driver.xpath("//span[@data-sector='%s']" % sector)
			x = driver.xpath("//*[@data-available-seats][@data-zone-with-promo]", is_one=0, is_click=0)
			for i in x:
				if int(i.get_attribute("data-available-seats")) >= NUM:
					print("click1")
					id = i.get_attribute("id")
					if id in errs:
						continue
					driver.xpath("//*[@id='%s_t']" % id)
					if driver.xpath("//*[@id='message-alert']"):
						driver.xpath("//*[@id='alert-ok']")
						errs += [id]
						self.sel(driver, NUM)
					break
			else:
				driver.xpath("//a[@id='boton-compra-back']")
				continue
			break
		else:
			self.goto(driver, NUM)
		if driver.xpath("//*[@id='boton-compra']"):
			print("Congratulations")
			os.system("beep.mp3")



Run()


