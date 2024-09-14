from dublib.Methods.JSON import ReadJSON
from Source.Browser import Browser
from selenium import webdriver
from netscape_cookies import save_cookies_to_file
from netscape_cookies import to_netscape_string

Settings = ReadJSON("Settings.json")

browser = Browser()

cookies = browser.authorization(Settings["login"], Settings["password"])

file_path = "cookies.txt"

save_cookies_to_file(cookies, file_path)

to_netscape_string(cookies)