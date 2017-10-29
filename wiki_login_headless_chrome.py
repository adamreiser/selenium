#!/usr/bin/env python
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
import atexit
import tabcomplete
import credentials

options = webdriver.chrome.options.Options()
options.add_argument("--headless")

wd = webdriver.Chrome(chrome_options=options)

(u, p) = credentials.load("/root/credentials/mediawiki.txt")

atexit.register(wd.quit)
wd.implicitly_wait(30)

wd.get("http://localhost:8000")

wd.maximize_window()

wd.find_element_by_link_text("Log in").click()

wd.find_element_by_id("wpName1").send_keys(u)

wd.find_element_by_id('wpPassword1').send_keys(p)

wd.find_element_by_id('wpLoginAttempt').click()
