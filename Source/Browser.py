from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep

class Browser():

	def __init__(self):
		self.__browser = webdriver.Chrome()
		self.__browser.set_window_size(1920, 1080)

	def __Get(self, url: str):

		# Состояние: выполнен ли переход.
		IsSuccess = False

		# Пока переход не выполнен.
		while not IsSuccess:

			try:
				# Переход по ссылке.
				self.__browser.get(url)
				# Остановка цикла.
				IsSuccess = True

			except Exception as ExceptionData: pass

	def __GetBody(self):
		html = self.__ExecuteJavaScript("return document.body.outerHTML;")
		soup = BeautifulSoup(html, "html.parser")

		return soup
	
	def __Refresh(self):
		"""Обновляет текущую страницу."""

		# Состояние: выполнен ли переход.
		IsSuccess = False

		# Пока переход не выполнен.
		while not IsSuccess:

			try:
				# Обновление страницы.
				self.__browser.refresh()
				# Остановка цикла.
				IsSuccess = True

			except Exception as ExceptionData: pass

	
	def authorization(self, login, password)-> list:
		
		self.__Get("https://www.instagram.com/")
		sleep(3)

		self.__browser.find_element(By.NAME, "username").send_keys(login)
		self.__browser.find_element(By.NAME, "password").send_keys(password)
		sleep(1)

		elements = self.__browser.find_elements(By.TAG_NAME, "button")
		elements[1].click()
		sleep(3)
		url = self.__browser.currnt_url()
		if "challenge" in url:
			

		cookies = self.__browser.get_cookies()
		
		return cookies


