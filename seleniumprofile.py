from selenium import webdriver
import shutil
import shlex
import os


class SeleniumProxy():
    """Base class to set up a Firefox Selenium profile with a proxy.
    Keyword arguments are passed to webdriver.Firefox, except for
    ca_file and args."""

    def __init__(self, **kwargs):

        fp = webdriver.FirefoxProfile()
        fp.set_preference("network.proxy.http", "127.0.0.1")
        fp.set_preference("network.proxy.http_port", 8080)
        fp.set_preference("network.proxy.ssl", "127.0.0.1")
        fp.set_preference("network.proxy.ssl_port", 8080)
        fp.set_preference("network.proxy.type", 1)
        fp.set_preference("network.proxy.no_proxies_on", "")

        # Install the proxy CA from path
        shutil.copy(kwargs["ca_file"], fp.path)

        # Set the profile options
        kwargs["firefox_profile"] = fp

        # Remove custom keyword keyword
        kwargs.pop("ca_file")

        # Set the CLI options to invoke firefox with
        if 'args' in kwargs:
            options = webdriver.firefox.options.Options()

            for opt in shlex.split(kwargs['args']):
                options.add_argument(opt)
            kwargs.pop("args")
            kwargs['firefox_options'] = options

        # Create webdriver object using remaining keyword options
        self.wd = webdriver.Firefox(**kwargs)
