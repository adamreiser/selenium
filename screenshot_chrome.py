#!/usr/bin/env python
from selenium import webdriver


options = webdriver.chrome.options.Options()
options.add_argument("--headless")

wd = webdriver.Chrome(chrome_options=options)

wd.implicitly_wait(30)
wd.get("http://localhost:8000")
wd.get_screenshot_as_file("wiki.png")
