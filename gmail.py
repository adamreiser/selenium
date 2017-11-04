#!/usr/bin/env python

from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
import atexit
import tabcomplete
import credentials
from seleniumprofile import SeleniumProxy


# This script is intended to show Selenium interacting with a
# complex web service. It's not recommended to actually use it
# except as a teaching example. Use gmail's API for any kind of real
# automation.

(u, p) = credentials.load('/root/credentials/credentials.txt')

wd = webdriver.Firefox(firefox_binary='/opt/firefox/firefox')

atexit.register(wd.quit)

wd.implicitly_wait(30)

wd.get("https://accounts.google.com/ServiceLogin?service=mail&passive=true&"
       "rm=false&continue=https://mail.google.com/mail/&ss=1&scc=1&"
       "ltmpl=default&ltmplcache=2&emr=1&osid=1")

login_el = wd.find_element_by_id("identifierId")

enter_username = ActionChains(wd)
enter_username.move_to_element(login_el)
enter_username.click(login_el)
enter_username.send_keys("{}\n".format(u))
enter_username.perform()

WebDriverWait(wd, 30).until(EC.element_to_be_clickable((By.ID, "password")))

pass_el = wd.find_element_by_id("password")

enter_password = ActionChains(wd)
enter_password.move_to_element(pass_el)
enter_password.click(pass_el)
enter_password.send_keys("{}\n".format(p))
enter_password.perform()

wd.find_element_by_xpath("//span[.='open me']").click()
wd.find_element_by_partial_link_text("127.0.0.1").click()
