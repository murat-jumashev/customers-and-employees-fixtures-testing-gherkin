import os
from django.conf import settings
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.chrome.options import Options


def before_all(context):
    chrome_options = Options()
    if os.environ[settings.TEST_MODE] == settings.HEADLESS:
        chrome_options.add_argument("--headless")
    context.browser = webdriver.Chrome(
        executable_path=r'/usr/local/bin/chromedriver',
        chrome_options=chrome_options
    )
    context.browser.implicitly_wait(3)
    context.server_url = 'http://localhost:8000'

def after_all(context):
    context.browser.quit()
