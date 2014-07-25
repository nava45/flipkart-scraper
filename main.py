from selenium import webdriver
from selenium.webdriver.common.keys import Keys

url = "http://www.flipkart.com/search?q=%s&as=off&as-show=on&otracker=start"
driver = webdriver.Firefox()

def get_page(url):
    global driver
    driver.get(url)
    return d.page_source

def parser(input):
    pass

def start():
    html_data = get_page(url)
    result = parser(html_data)


if __name__ == '__main__':
    start()
