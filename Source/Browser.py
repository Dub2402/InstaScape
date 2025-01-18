from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
from selenium_authenticated_proxy import SeleniumAuthenticatedProxy
from dublib.Methods.Filesystem import ReadJSON

class Browser:

	def __init__(self):

		Settings = ReadJSON("Settings.json")
		options = Options()
		proxy_helper = SeleniumAuthenticatedProxy(proxy_url=Settings["proxy"])
		proxy_helper.enrich_chrome_options(options)
		options.add_argument("--disable-gpu")
		options.add_argument("--no-sandbox")
		options.add_argument("--disable-software-rasterizer")
		options.add_argument("--headless=new")
		self.__browser = webdriver.Chrome(options = options)
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

			except Exception as ExceptionData: print(ExceptionData)

	def authorization(self, login, password)-> list:
		
		self.__Get("https://www.instagram.com/")
		element = WebDriverWait(self.__browser, 10).until(
			EC.presence_of_element_located((By.NAME, "username"))
		)

		self.__browser.find_element(By.NAME, "username").send_keys(login)
		self.__browser.find_element(By.NAME, "password").send_keys(password)

		elements = self.__browser.find_elements(By.TAG_NAME, "button")
		for Index in range(len(elements)):
			if elements[Index].text in ["Войти", "Log in"]: elements[Index].click()
			else: pass

		url = self.__browser.current_url
		try:
			element = WebDriverWait(self.__browser, 15).until(
				EC.presence_of_element_located((By.XPATH, "/html/body/div[2]/div/div/div/div[2]/div/div/div[1]/section/main/div[2]/div/div/div/div/div[1]/div/div/div[2]/div[2]/div"))
			)
			
			if "challenge" in url:
				
				element = self.__browser.find_element(By.XPATH, "/html/body/div[2]/div/div/div/div[2]/div/div/div[1]/section/main/div[2]/div/div/div/div/div[1]/div/div/div[2]/div[2]/div")
				element.click()
				print("Доступ к сайту был заблокирован. Доступ сейчас разрешён.")

		except: print("Доступ к сайту не был заблокирован.")
			
		cookies = self.__browser.get_cookies()

		return cookies
