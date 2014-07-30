flipkart-scraper
================

Scrape it..come on

> Python is going to bite the flipkart soon... :)

execute the crawler only in this way:

`python main.py --search=django book`

Description:
------------

This is a simple python based project which is used to scrape the flipkart search results by scrolling flipkart official pages.This project will contain some historical data.If you keep this crawler running in your server, this automatically scrapes the data from flipkart website. Once you started gathering the data, you could do run many analysis like price range variation, offers, review analysis etc..

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

How to execute this project?
----------------------------

`$ ./start.sh` in your shell will do the job.It runs the `redis_worker.py` and `flask` app.
you can even customize for your case.


Features:
---------
1. Simple interface
2 .Re-Crawl option available to the user
3 .Case-insensitive search 
4 .easy expandable

Screenshots:
------------
###Demo:


![Flipkart Scraper Demo](https://raw.githubusercontent.com/nava45/flipkart-scraper/master/screenshots/A%20Snake's%20Flipkart%20Scraper%20Demo.png)

###Re-Crawl:

![CrawlReschedule](https://raw.githubusercontent.com/nava45/flipkart-scraper/master/screenshots/Crawlschedule.png)


Thanks for your time.
