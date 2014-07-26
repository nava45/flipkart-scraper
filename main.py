from selenium import webdriver
from selenium.webdriver.common.keys import Keys

import signal
import sys
import time

url = "http://www.flipkart.com/search?q=%s&as=off&as-show=on&otracker=start"
driver = webdriver.Firefox()

def close(signal, frame):
    global driver
    print('You pressed Ctrl+C!')
    driver.close()
    signal.pause()
    sys.exit(0)
 

def get_page(url, keyword="moto g"):
    global driver
    driver.get(url % keyword)
    return driver.page_source

def parser(input):
    pass

def start():
    html_data = get_page(url)
    result = parser(html_data)
    time.sleep(20)

if __name__ == '__main__':
    signal.signal(signal.SIGINT, close)
    start()
  
