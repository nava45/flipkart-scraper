flipkart-scraper
================


> Python is going to bite the flipkart soon... :)

execute the crawler only in this way:

`python main.py --search=django book`

Description:
------------

This is a simple python based project which is used to scrape the flipkart search results page. Also it does the scrolling to navigate into next page to crawl the data.This project has been implemented with mighty technologies like mongodb, redis, python, flask. It will be helpful to collect some historical data from flipkart.If you keep this crawler running in your server, this automatically scrapes the data for the user's keyword from flipkart website. Once you started gathering the data, you could do run many analysis like price range variation, offers, review analysis etc..

in `screenshots` directory we have uploaded our first version screenshots. you can take a look and give us the feedback.

Tools:
------

- We love python(2.7).
- phantomjs is phenomenon
- xpath is amazing.
- redis always rocks
- mongodb is sweet, if you are apetite 
- flask simply flashes as usual
- selenium is damn serious

> Upon all the above, Ubuntu is our living earth.

:)

> lxml, mongodb, redis are the required system packages to be installed to execute it, after just run `pip install -r requirements.txt`.

How to execute this project?
----------------------------

`$ ./start.sh` in your shell will do the job.It runs the `redis_worker.py` and `flask` app.
you can even customize for your case.


Features:
---------
- Simple interface
- Re-Crawl option available to the user
- Case-insensitive search 
- easy expandable

we have been working for further releases for the extensive use of customers.

Screenshots:
------------
###Demo:


![Flipkart Scraper Demo](https://raw.githubusercontent.com/nava45/flipkart-scraper/master/screenshots/A%20Snake's%20Flipkart%20Scraper%20Demo.png)

###Re-Crawl:

![CrawlReschedule](https://raw.githubusercontent.com/nava45/flipkart-scraper/master/screenshots/Crawlschedule.png)


Thanks for your time.
