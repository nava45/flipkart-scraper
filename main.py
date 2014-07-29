from selenium import webdriver
from selenium.webdriver.common.keys import Keys

from config import URL_FORMAT, SCROLL_TIMES
from parser import FParser

import signal
import sys
import time

driver = None


def close(signal, frame):
    '''
    When you press Ctrl-C the browser closes
    '''
    global driver
    print('You pressed Ctrl+C!')
    driver.close()
    signal.pause()
    sys.exit(0)

    
def scroll_down(driver):
    '''
    This helps you to scroll the search results page to load more results
    '''
    for i in range(SCROLL_TIMES):
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(0.3)


def get_page(driver, url):
    driver.get(url)
    return driver.page_source


def press_the_button_2_crawl(driver, keyword):
    """
    Main function handles everything 
    """
    html_data = get_page(driver, URL_FORMAT % keyword)
    scroll_down(driver)
    parser = FParser(html_data)
    parser.store() #store into db
    time.sleep(2)


if __name__ == '__main__':
    try:
        driver = webdriver.Firefox()
        signal.signal(signal.SIGINT, close)
        press_the_button_2_crawl(driver,'moto g')
    finally:
        driver.close()
