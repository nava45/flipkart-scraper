from flask import Flask, request, render_template, send_from_directory

from models import fetch_by_name
from main import crawler_machine

app = Flask(__name__)


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
        crawler_machine(kw)
        flash("you have rescheduled it")
    redirect(url_for('app.view_search'))

if __name__ == '__main__':
    app.run(port=8802)