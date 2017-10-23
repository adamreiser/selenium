#!/usr/bin/env python
from selenium import webdriver
import atexit
import tabcomplete
from seleniumprofile import SeleniumProxy


# A simple script to demonstrate WebDriver functionality
# with an application proxy.

# Run with python -i for an interpreter with tab
# completion to explore the webdriver object.

proxy = SeleniumProxy(firefox_binary='/opt/firefox/firefox',
                      ca_file='/root/credentials/cert8.db')

wd = proxy.wd

atexit.register(wd.quit)

wd.implicitly_wait(30)
wd.get("https://wikipedia.org")
