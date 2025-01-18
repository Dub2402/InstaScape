from dublib.Methods.Filesystem import ReadJSON, MakeRootDirectories
from Source.Browser import Browser
from netscape_cookies import to_netscape_string
from dublib.Methods.Filesystem import WriteTextFile

import os

Settings = ReadJSON("Settings.json")

browser = Browser()
cookies = browser.authorization(Settings["login"], Settings["password"])

file_path = Settings["path"]

try: 
    if not os.path.exists(file_path) and '/' in file_path:
        folder = '/'.join(file_path.split("/")[:-1])
        MakeRootDirectories([folder])
except: print("Неправильно задан путь к папку cookies")                             

NetStr = to_netscape_string(cookies)
NetStr = "# Netscape HTTP Cookie File\n" + NetStr

WriteTextFile(file_path, NetStr)