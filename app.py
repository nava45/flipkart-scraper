from flask import Flask, request, render_template, send_from_directory, flash, redirect, url_for
from redis import Redis

from models import fetch_by_name
from main import crawler_machine

import os

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
    print "Input:",keyword
    if keyword:
        search_results = fetch_by_name(keyword)
    return render_template('index.html', search_results=search_results, keyword=keyword)

@app.route('/recrawl', methods=('GET', 'POST'))
def recrawl():
    kw = request.args.get('search',None)
    if kw:
        redis.lpush('crawling_keywords',kw)
        #crawler_machine(kw)
        flash("you have rescheduled it for '%s'.It will happen sooner or later" %kw)
    return redirect(url_for('.view_search'))



if __name__ == '__main__':
    
    app.run(port=8802, debug=True)