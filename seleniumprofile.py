from selenium import webdriver
import shutil
import os


class SeleniumProxy():
    """Base class to set up Selenium with a proxy."""

    def __init__(self, firefox_binary, ca_file):

        fp = webdriver.FirefoxProfile()
        fp.set_preference("network.proxy.http", "127.0.0.1")
        fp.set_preference("network.proxy.http_port", 8080)
        fp.set_preference("network.proxy.ssl", "127.0.0.1")
        fp.set_preference("network.proxy.ssl_port", 8080)
        fp.set_preference("network.proxy.type", 1)
        fp.set_preference("network.proxy.no_proxies_on", "")

        # Install the proxy CA
        shutil.copy(ca_file, fp.path)

        self.wd = webdriver.Firefox(firefox_binary=firefox_binary,
                                    firefox_profile=fp)
