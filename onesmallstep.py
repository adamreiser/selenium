#!/usr/bin/env python
from selenium import webdriver
import atexit
import tabcomplete

# A simple script to demonstrate WebDriver functionality
# Run with python -i for an interpreter with tab
# completion to explore the webdriver object.

wd = webdriver.Firefox(firefox_binary='/opt/firefox/firefox')

atexit.register(wd.quit)

wd.implicitly_wait(30)
wd.get("http://localhost:8000")
