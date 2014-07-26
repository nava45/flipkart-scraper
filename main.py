from selenium import webdriver
from selenium.webdriver.common.keys import Keys

import signal
import sys
import time

url = "http://www.flipkart.com/search?q=%s&as=off&as-show=on&otracker=start"
driver = webdriver.Firefox()
fo = open('out.txt', 'w')


def close(signal, frame):
    global driver
    print('You pressed Ctrl+C!')
    driver.close()
    signal.pause()
    fo.close()
    sys.exit(0)
    

def get_page(url, keyword="moto g"):
    global driver
    driver.get(url % keyword)
    return driver.page_source

def parser(input):
    print "html recorded"
    print >> fo, 'data',input.encode('utf-8',errors='ignore')

def start():
    html_data = get_page(url)
    result = parser(html_data)
    time.sleep(20)

if __name__ == '__main__':
    try:
        signal.signal(signal.SIGINT, close)
        start()
    finally:
        driver.close()
