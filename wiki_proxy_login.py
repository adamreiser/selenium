#!/usr/bin/env python
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
import atexit
import tabcomplete
import credentials
from seleniumprofile import SeleniumProxy


proxy = SeleniumProxy(firefox_binary='/opt/firefox/firefox',
                      ca_file='/root/credentials/cert8.db')

(u, p) = credentials.load("/root/credentials/mediawiki.txt")

wd = proxy.wd
atexit.register(wd.quit)
wd.implicitly_wait(30)

wd.get("http://localhost:8000")

wd.maximize_window()

wd.find_element_by_link_text("Log in").click()

wd.find_element_by_id("wpName1").send_keys(u)

wd.find_element_by_id('wpPassword1').send_keys(p)

wd.find_element_by_id('wpLoginAttempt').click()
