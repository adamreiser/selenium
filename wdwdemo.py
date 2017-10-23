#!/usr/bin/env python
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
import atexit
import tabcomplete


wd = webdriver.Firefox(firefox_binary='/opt/firefox/firefox')
atexit.register(wd.quit)
wd.implicitly_wait(30)

wd.get("https://wikipedia.org")

wd.find_element_by_id("js-link-box-en").click()

# Wait until the new page loads
WebDriverWait(wd, 30).until(
    lambda wd: wd.current_url == "https://en.wikipedia.org/wiki/Main_Page")

wd.maximize_window()
wd.get_screenshot_as_file('en_wikipedia.png')
