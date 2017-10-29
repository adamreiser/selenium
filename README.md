# Selenium

Repository for *Selenium: dark side of the moon* demo and examples.


## Requirements

- Firefox
    - Use Firefox 56+ (not esr). Assumed to be in /opt/firefox.

- geckodriver - add binary to your PATH
    - https://github.com/mozilla/geckodriver/releases

- Selenium Python bindings[1]
    - pip install selenium

- Docker, Docker Compose
    - The demo environment is a local MediaWiki instance running under Docker.

## Optional

- Selenium IDE / Selenium Builder
    - No longer recommended. IDE incompatible with current versions except esr[2].

- PhantomJS
    - Alternative, can also be used with WebDriver.

- xvfb
    - Option for headless mode when not natively supported by the browser.
    xvfb-run and pyvirtualdisplay are two ways to use it.


## References

[1] http://selenium-python.readthedocs.io/installation.html

[2] https://seleniumhq.wordpress.com/2017/08/09/firefox-55-and-selenium-ide/
