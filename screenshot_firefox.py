#!/usr/bin/env python
from selenium import webdriver


options = webdriver.firefox.options.Options()
options.add_argument("--headless")

wd = webdriver.Firefox(firefox_options=options)

wd.implicitly_wait(30)
wd.get("http://localhost:8000")
wd.get_screenshot_as_file("wiki.png")
