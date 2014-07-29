from selenium import webdriver
from selenium.webdriver.common.keys import Keys

from config import URL_FORMAT
from parser import FParser

import signal
import sys
import time

driver = webdriver.Firefox()

def close(signal, frame):
    global driver
    print('You pressed Ctrl+C!')
    driver.close()
    signal.pause()
    sys.exit(0)
    

def get_page(url):
    global driver
    driver.get(url)
    return driver.page_source

def start(keyword):
    html_data = get_page(URL_FORMAT % keyword)
    parser = FParser(html_data)
    parser.store() #store into db
    time.sleep(2)

if __name__ == '__main__':
    try:
        signal.signal(signal.SIGINT, close)
        start('moto g')
    finally:
        driver.close()
