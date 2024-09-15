from dublib.Methods.JSON import ReadJSON
from Source.Browser import Browser
from netscape_cookies import save_cookies_to_file
from netscape_cookies import to_netscape_string
from datetime import datetime
import os


Settings = ReadJSON("Settings.json")

browser = Browser()

cookies = browser.authorization(Settings["login"], Settings["password"])

now = datetime.now()

try:
    for file in os.listdir("Cookies"):
        if file.endswith(".txt"):
            os.remove(f"Cookies/{file}")
except: pass

file_path = f"Cookies/{now}_cookies.txt"

save_cookies_to_file(cookies, file_path)

to_netscape_string(cookies)