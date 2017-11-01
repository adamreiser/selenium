#!/usr/bin/env python
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
import atexit
import tabcomplete


wd = webdriver.Firefox(firefox_binary='/opt/firefox/firefox')

atexit.register(wd.quit)

wd.implicitly_wait(30)

wd.get("http://localhost/click.html")


click_me = wd.find_element_by_link_text("Click me!")

action = ActionChains(wd)
action.move_to_element(click_me)
action.click(click_me)
action.perform()
