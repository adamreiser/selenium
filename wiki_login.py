#!/usr/bin/env python
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
import atexit
import tabcomplete
import credentials


wd = webdriver.Firefox(firefox_binary='/opt/firefox/firefox')

(u, p) = credentials.load("/root/credentials/mediawiki.txt")

atexit.register(wd.quit)
wd.implicitly_wait(30)

wd.get("http://localhost:8000")

wd.maximize_window()

wd.find_element_by_id("pt-login").click()

wd.find_element_by_id("wpName1").send_keys(u)

wd.find_element_by_id('wpPassword1').send_keys(p)

wd.find_element_by_id('wpLoginAttempt').click()
