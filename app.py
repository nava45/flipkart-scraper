from flask import Flask, request, render_template, send_from_directory, flash, redirect, url_for
from redis import Redis

from models import fetch_by_name
from main import crawler_machine
from config import REDIS_CRAWLER_KEY,REDIS_RECENT_SEARCHES,MAX_RECENT_SEARCH_ITEMS

import os
import json

app = Flask(__name__)
app.config["SECRET_KEY"] = os.environ.get('SECRET_KEY') or 't0p s3cr3t'
redis = Redis()

if app.debug:
    import logging
    from logging.handlers import RotatingFileHandler
    file_handler = RotatingFileHandler('app.log', 'a', 1 * 1024 * 1024, 10)
    file_handler.setFormatter(logging.Formatter('%(asctime)s %(levelname)s: %(message)s [in %(pathname)s:%(lineno)d]'))
    app.logger.setLevel(logging.DEBUG)
    file_handler.setLevel(logging.DEBUG)
    app.logger.addHandler(file_handler)
    #app.logger.info('microblog startup')

@app.route('/', methods=('GET', 'POST'))
def index():
    return redirect(url_for('.view_search'))
    
@app.route('/search', methods=('GET', 'POST'))
def view_search():
    keyword = request.form.get('Search',None)
    search_results = ''
    #print "Input:",keyword
    if keyword:
        redis.lpush(REDIS_RECENT_SEARCHES,keyword)
        search_results = fetch_by_name(keyword)
    return render_template('index.html', search_results=search_results, keyword=keyword)

@app.route('/recrawl', methods=('GET', 'POST'))
def recrawl():
    kw = request.args.get('search',None)
    if kw is not None:
        redis.sadd(REDIS_CRAWLER_KEY,kw)
        #crawler_machine(kw)
        flash("you have rescheduled the crawler for '%s'.It will happen sooner or later." %kw)
    return redirect(url_for('.view_search'))


@app.route('/get', methods=('GET', 'POST'))
def service():
    name = request.args.get('name',None)
    if name:
        return fetch_by_name(name, _as='json')
    return []


@app.route('/recent', methods=('GET', 'POST'))
def recent():
    result = redis.lrange(REDIS_RECENT_SEARCHES, 0, MAX_RECENT_SEARCH_ITEMS)
    return json.dumps({'recent':result})


if __name__ == '__main__':
    
    app.run(port=8802, debug=True)
