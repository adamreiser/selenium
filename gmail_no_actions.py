#!/usr/bin/env python

from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
import atexit
import tabcomplete
import credentials
from seleniumprofile import SeleniumProxy


# This script is intended to show Selenium interacting with a
# complex web service. It's not recommended to actually use it
# except as a teaching example. Use gmail's API for any kind of real
# automation.

proxy = SeleniumProxy(firefox_binary='/opt/firefox/firefox',
                      ca_file='/root/credentials/cert8.db')

(u, p) = credentials.load('/root/credentials/gmail.txt')

wd = proxy.wd

atexit.register(wd.quit)

wd.implicitly_wait(30)

wd.get("https://accounts.google.com/ServiceLogin?service=mail&passive=true&"
       "rm=false&continue=https://mail.google.com/mail/&ss=1&scc=1&"
       "ltmpl=default&ltmplcache=2&emr=1&osid=1")

wd.find_element_by_id("identifierId").send_keys("{}\n".format(u))

# Element exists but may not yet be 'visible'
# This hinders interaction with it, but implicitly_wait doesn't know that

WebDriverWait(wd, 30).until(EC.element_to_be_clickable((By.ID, "password")))

wd.find_element_by_id("password").send_keys("{}\n".format(p))
