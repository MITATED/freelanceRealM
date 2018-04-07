from selenium.webdriver import Chrome, ChromeOptions
from selenium.webdriver.remote.command import Command
from selenium.webdriver.common.by import By
from time import sleep, time

def UA():#Список User-Agent'ов
	with open("UAs.txt", "r") as file:
		lUA = file.read().split("\n")[:-1]
	return random.choice(lUA)


class Driver(Chrome):
	"""This Driver its modification chromedriver
	Attributes:
		executable_path - Path to driver
		UserAgent - useragent, can use UA(), but file UAs.txt has been
		proxy - proxy, (http|socks4|socks5)://000.000.000.000:8080
		wait - time period for wait element
	Modified functions:
		click(elem)
		maximize()
		js([script | path to js file])

		xpath(self, xpath, is_displayed = 1, start_wait = .5, wait = None)
		cxpath(self, xpath, is_displayed = 1, start_wait = .5, wait = None)
		xpathes(self, xpath, is_displayed = 1, start_wait = .5, wait = None)
		cxpathes(self, xpath, is_displayed = 1, start_wait = .5, wait = None)
		xpath_u(self, xpath, is_one = 1, is_displayed = 1, is_click = 1, clickAll = 0, start_wait = 0.5, wait = None)

		css(self, css, is_displayed = 1, start_wait = .5, wait = None)
		ccss(self, css, is_displayed = 1, start_wait = .5, wait = None)
		csses(self, css, is_displayed = 1, start_wait = .5, wait = None)
		ccsses(self, css, is_displayed = 1, start_wait = .5, wait = None)
		css_u(self, css, is_one = 1, is_displayed = 1, is_click = 1, clickAll = 0, start_wait = 0.5, wait = None)
	"""
	def __init__(self, 
				executable_path="chromedriver.exe",
				UserAgent = None, 
				proxy = None,
				wait = 5):
		self.wait = wait
		self.chrome_options = ChromeOptions()
		if UserAgent:
			self.chrome_options.add_argument('--user-agent=%s'%self.UserAgent)
		if proxy:
			self.chrome_options.add_argument('--proxy-server=%s'%self.proxy)# "(http|socks4|socks5)://000.000.000.000:8080"
		Chrome.__init__(self, executable_path="chromedriver.exe",chrome_options=self.chrome_options)
		self.maximize()
	def get(self, url):
		self.execute(Command.GET, {'url': url})
	def click(self, elem):
		try:
			self.execute(Command.CLICK_ELEMENT, {'id': elem._id})
		except:
			self.execute_script("arguments[0].click();", elem)
			
	def xpath(self, xpath, is_displayed = 1, start_wait = .5, wait = None):
		"""
			def xpath(self, xpath, is_displayed = 1, start_wait = .5, wait = None):
				sleep(start_wait)
				thisWait = wait if wait != None else self.wait
				for waitOne in range(thisWait + 1):
					elems = self.execute(Command.FIND_ELEMENTS, {'using': By.XPATH, 'value': xpath})['value'] or []
					if elems and ((not is_displayed) or (is_displayed and elems[0].is_displayed())):
						return elems[0]
					sleep(1)
				return None
		"""
		sleep(start_wait)
		thisWait = wait if wait != None else self.wait
		for waitOne in range(thisWait + 1):
			elems = self.execute(Command.FIND_ELEMENTS, {'using': By.XPATH, 'value': xpath})['value'] or []
			if elems and ((not is_displayed) or (is_displayed and elems[0].is_displayed())):
				return elems[0]
			sleep(1)
		return None
	def cxpath(self, xpath, is_displayed = 1, start_wait = .5, wait = None):
		"""
			def cxpath(self, xpath, is_displayed = 1, start_wait = .5, wait = None):
				sleep(start_wait)
				thisWait = wait if wait != None else self.wait
				for waitOne in range(thisWait + 1):
					elems = self.execute(Command.FIND_ELEMENTS, {'using': By.XPATH, 'value': xpath})['value'] or []
					if elems and ((not is_displayed) or (is_displayed and elems[0].is_displayed())):
						return self.click(elems[0]), elems[0]
					sleep(1)
				return (False, None)
		"""
		sleep(start_wait)
		thisWait = wait if wait != None else self.wait
		for waitOne in range(thisWait + 1):
			elems = self.execute(Command.FIND_ELEMENTS, {'using': By.XPATH, 'value': xpath})['value'] or []
			if elems and ((not is_displayed) or (is_displayed and elems[0].is_displayed())):
				return self.click(elems[0]), elems[0]
			sleep(1)
		return (False, None)
	def xpathes(self, xpath, is_displayed = 1, start_wait = .5, wait = None):
		"""
			def xpathes(self, xpath, is_displayed = 1, start_wait = .5, wait = None):
				sleep(start_wait)
				thisWait = wait if wait != None else self.wait
				for waitOne in range(thisWait + 1):
					elems = self.execute(Command.FIND_ELEMENTS, {'using': By.XPATH, 'value': xpath})['value'] or []
					if elems:
						retElems = []
						for elem in elems:
							if is_displayed and not elem.is_displayed():
								continue
							retElems += [elem]
						return retElems
					sleep(1)
				return []
		"""
		sleep(start_wait)
		thisWait = wait if wait != None else self.wait
		for waitOne in range(thisWait + 1):
			elems = self.execute(Command.FIND_ELEMENTS, {'using': By.XPATH, 'value': xpath})['value'] or []
			if elems:
				retElems = []
				for elem in elems:
					if is_displayed and not elem.is_displayed():
						continue
					retElems += [elem]
				return retElems
			sleep(1)
		return []
	def cxpathes(self, xpath, is_displayed = 1, start_wait = .5, wait = None):
		"""
			def cxpathes(self, xpath, is_displayed = 1, start_wait = .5, wait = None):
				sleep(start_wait)
				thisWait = wait if wait != None else self.wait
				for waitOne in range(thisWait + 1):
					elems = self.execute(Command.FIND_ELEMENTS, {'using': By.XPATH, 'value': xpath})['value'] or []
					if elems:
						retElems = []
						for elem in elems:
							if is_displayed and not elem.is_displayed():
								continue
							retElems += [(elem, self.click(elem))]
						return retElems
					sleep(1)
				return []
		"""
		sleep(start_wait)
		thisWait = wait if wait != None else self.wait
		for waitOne in range(thisWait + 1):
			elems = self.execute(Command.FIND_ELEMENTS, {'using': By.XPATH, 'value': xpath})['value'] or []
			if elems:
				retElems = []
				for elem in elems:
					if is_displayed and not elem.is_displayed():
						continue
					retElems += [(elem, self.click(elem))]
				return retElems
			sleep(1)
		return []

	def xpath_u(self, xpath, is_one = 1, is_displayed = 1, is_click = 1, clickAll = 0, start_wait = 0.5, wait = None):
		"""
			def xpath_u(self, xpath, is_one = 1, is_displayed = 1, is_click = 1, clickAll = 0, start_wait = 0.5, wait = None):
				sleep(start_wait)
				thisWait = wait if wait != None else self.wait
				for waitOne in range(thisWait + 1):
					elems = self.execute(Command.FIND_ELEMENTS, {'using': By.XPATH, 'value': xpath})['value'] or []
					if is_one and elems and ((not is_displayed) or (is_displayed and elems[0].is_displayed())):
						if is_click:
							return self.click(elems[0]), elems[0]
						else:
							return elems[0]
					elif not is_one and elems:
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
		"""
		sleep(start_wait)
		thisWait = wait if wait != None else self.wait
		for waitOne in range(thisWait + 1):
			elems = self.execute(Command.FIND_ELEMENTS, {'using': By.XPATH, 'value': xpath})['value'] or []
			if is_one and elems and ((not is_displayed) or (is_displayed and elems[0].is_displayed())):
				if is_click:
					return self.click(elems[0]), elems[0]
				else:
					return elems[0]
			elif not is_one and elems:
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
	def css(self, css, is_displayed = 1, start_wait = .5, wait = None):
		"""
			def css(self, css, is_displayed = 1, start_wait = .5, wait = None):
				sleep(start_wait)
				thisWait = wait if wait != None else self.wait
				for waitOne in range(thisWait + 1):
					elems = self.execute(Command.FIND_ELEMENTS, {'using': By.CSS_SELECTOR, 'value': css})['value'] or []
					if elems and ((not is_displayed) or (is_displayed and elems[0].is_displayed())):
						return elems[0]
					sleep(1)
				return None
		"""
		sleep(start_wait)
		thisWait = wait if wait != None else self.wait
		for waitOne in range(thisWait + 1):
			elems = self.execute(Command.FIND_ELEMENTS, {'using': By.CSS_SELECTOR, 'value': css})['value'] or []
			if elems and ((not is_displayed) or (is_displayed and elems[0].is_displayed())):
				return elems[0]
			sleep(1)
		return None
	def ccss(self, css, is_displayed = 1, start_wait = .5, wait = None):
		"""
			def ccss(self, css, is_displayed = 1, start_wait = .5, wait = None):
				sleep(start_wait)
				thisWait = wait if wait != None else self.wait
				for waitOne in range(thisWait + 1):
					elems = self.execute(Command.FIND_ELEMENTS, {'using': By.CSS_SELECTOR, 'value': css})['value'] or []
					if elems and ((not is_displayed) or (is_displayed and elems[0].is_displayed())):
						return self.click(elems[0]), elems[0]
					sleep(1)
				return (False, None)
		"""
		sleep(start_wait)
		thisWait = wait if wait != None else self.wait
		for waitOne in range(thisWait + 1):
			elems = self.execute(Command.FIND_ELEMENTS, {'using': By.CSS_SELECTOR, 'value': css})['value'] or []
			if elems and ((not is_displayed) or (is_displayed and elems[0].is_displayed())):
				return self.click(elems[0]), elems[0]
			sleep(1)
		return (False, None)
	def csses(self, css, is_displayed = 1, start_wait = .5, wait = None):
		"""
			def csses(self, css, is_displayed = 1, start_wait = .5, wait = None):
				sleep(start_wait)
				thisWait = wait if wait != None else self.wait
				for waitOne in range(thisWait + 1):
					elems = self.execute(Command.FIND_ELEMENTS, {'using': By.CSS_SELECTOR, 'value': css})['value'] or []
					if elems:
						retElems = []
						for elem in elems:
							if is_displayed and not elem.is_displayed():
								continue
							retElems += [elem]
						return retElems
					sleep(1)
				return []
		"""
		sleep(start_wait)
		thisWait = wait if wait != None else self.wait
		for waitOne in range(thisWait + 1):
			elems = self.execute(Command.FIND_ELEMENTS, {'using': By.CSS_SELECTOR, 'value': css})['value'] or []
			if elems:
				retElems = []
				for elem in elems:
					if is_displayed and not elem.is_displayed():
						continue
					retElems += [elem]
				return retElems
			sleep(1)
		return []
	def ccsses(self, css, is_displayed = 1, start_wait = .5, wait = None):
		"""
			def ccsses(self, css, is_displayed = 1, start_wait = .5, wait = None):
				sleep(start_wait)
				thisWait = wait if wait != None else self.wait
				for waitOne in range(thisWait + 1):
					elems = self.execute(Command.FIND_ELEMENTS, {'using': By.CSS_SELECTOR, 'value': css})['value'] or []
					if elems:
						retElems = []
						for elem in elems:
							if is_displayed and not elem.is_displayed():
								continue
							retElems += [(elem, self.click(elem))]
						return retElems
					sleep(1)
				return []
		"""
		sleep(start_wait)
		thisWait = wait if wait != None else self.wait
		for waitOne in range(thisWait + 1):
			elems = self.execute(Command.FIND_ELEMENTS, {'using': By.CSS_SELECTOR, 'value': css})['value'] or []
			if elems:
				retElems = []
				for elem in elems:
					if is_displayed and not elem.is_displayed():
						continue
					retElems += [(elem, self.click(elem))]
				return retElems
			sleep(1)
		return []

	def css_u(self, css, is_one = 1, is_displayed = 1, is_click = 1, clickAll = 0, start_wait = 0.5, wait = None):
		"""
			def css_u(self, css, is_one = 1, is_displayed = 1, is_click = 1, clickAll = 0, start_wait = 0.5, wait = None):
				sleep(start_wait)
				thisWait = wait if wait != None else self.wait
				for waitOne in range(thisWait + 1):
					elems = self.execute(Command.FIND_ELEMENTS, {'using': By.css, 'value': css})['value'] or []
					if is_one and elems and ((not is_displayed) or (is_displayed and elems[0].is_displayed())):
						if is_click:
							return self.click(elems[0]), elems[0]
						else:
							return elems[0]
					elif not is_one and elems:
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
		"""
		sleep(start_wait)
		thisWait = wait if wait != None else self.wait
		for waitOne in range(thisWait + 1):
			elems = self.execute(Command.FIND_ELEMENTS, {'using': By.css, 'value': css})['value'] or []
			if is_one and elems and ((not is_displayed) or (is_displayed and elems[0].is_displayed())):
				if is_click:
					return self.click(elems[0]), elems[0]
				else:
					return elems[0]
			elif not is_one and elems:
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
	def maximize(self):
		self.execute(Command.MAXIMIZE_WINDOW, {"windowHandle": "current"})
	def js(self, script = None, path = None):
		if script:
			self.execute_script(script)
		elif path:
			with open(path, "r") as file:
				self.execute_script(file.read())
		else:
			print("ERROR: Not js for running!!!")

# driver = Driver(executable_path="chromedriver.exe")
# driver.get("http://google.com")
# print(Driver.__doc__)
# print(Driver.xpath.__doc__)

# t = time()
# driver.ccss(".gb_b.gb_hc")
# t1 = time() - t

# sleep(10)
# driver.quit()
