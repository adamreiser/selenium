#!/usr/bin/env python

from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
import atexit
import tabcomplete
import credentials
from seleniumprofile import SeleniumProxy


proxy = SeleniumProxy(firefox_binary='/opt/firefox/firefox',
                      ca_file='/root/credentials/cert8.db')

wd = proxy.wd

atexit.register(wd.quit)

wd.implicitly_wait(30)

wd.get("https://www.google.com")

wd.find_element_by_class_name('gsfi').send_keys("wikipedia\n")

