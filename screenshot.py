#!/usr/bin/env python
from selenium import webdriver
from pyvirtualdisplay import Display
import atexit
import tabcomplete


wd = webdriver.Firefox(firefox_binary='/opt/firefox/firefox')
atexit.register(wd.quit)
wd.implicitly_wait(30)

wd.get("http://localhost:8000")
wd.get_screenshot_as_file('wiki.png')
