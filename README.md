# Selenium

Repository for *Selenium: dark side of the moon* demo and examples.


## Requirements

- Firefox
 - Use Firefox 56+ (not esr). Assumed to be in /opt/firefox.

- geckodriver - add binary to your PATH
    - https://github.com/mozilla/geckodriver/releases

- [Selenium Python bindings](https://selenium-python.readthedocs.io/installation.html)
    - pip install selenium

- Docker, Docker Compose
    The demo environment is a local MediaWiki instance running under Docker.

- Burp Suite
 - We will be conntecting selenium sessions to an intercepting proxy. The free
    version is fine.


## Optional

- Selenium IDE / Selenium Builder
 - No longer recommended. IDE incompatible with current versions except esr[1](https://seleniumhq.wordpress.com/2017/08/09/firefox-55-and-selenium-ide/).

- PhantomJS
 - Alternative, can also be used with WebDriver.

- Chrome, chromedriver
 - Used for speed test comparisons.

- xvfb
    - Fallback option when headless mode is not natively supported by the browser.
    xvfb-run and pyvirtualdisplay are two ways to use it.

## Demo setup

- Burp (or another application proxy) should be listening on port 8080. For the Firefox demos, add your proxy's certificate authority to it. This trust will be stored in the cert8.db file in the corresponding profile, which you can add to the new Firefox profiles created by Selenium. At present, the demo scripts are hardcoded to look for it in `/root/credentials/cert8.db`.

- The MediaWiki demo uses a compose file based on [the official repository](https://hub.docker.com/_/mediawiki/). See that link or the slides for setup instructions to obtain a local MediaWiki instance on port 8000.
- Both the MediaWiki and demo files use a simple module to load credentials from outside the repository. These are stored in the clear as text files with the username on the first line and the password on the second. You will of course need your own gmail credentials.
- Some of the demos expect content from the srv directory to be served on localhost port 80 - the Python SimpleHTTPServer module will do this, although it listens on all interfaces by default.


## Running the demo

This is mostly documented in [selenium.pdf](selenium.pdf). Assuming you kept the default locations, your credentials directory should like
```
root@kali:~# ls /root/credentials/
cert8.db  gmail.txt  mediawiki.txt
```

You should now be able to run the demo scripts such as `python -i gmail.py`. Tab completion should be enabled. This is very handy for interactive Selenium sessions when building out a script. Try tab completion on the webdriver object and element objects, as well as the selenium modules themselves!
