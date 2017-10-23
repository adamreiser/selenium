#!/usr/bin/env python
from selenium import webdriver
from pyvirtualdisplay import Display
import atexit
import tabcomplete


Display(visible=0, size=(1440, 900)).start()

wd = webdriver.Firefox(firefox_binary='/opt/firefox/firefox')
atexit.register(wd.quit)
wd.implicitly_wait(30)

wd.get("https://wikipedia.org")
wd.get_screenshot_as_file('wikipedia.png')
