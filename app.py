from flask import Flask, request, render_template, send_from_directory

from models import fetch_by_name

app = Flask(__name__)


@app.route('/search', methods=('GET', 'POST'))
def view_search():
    keyword = request.form.get('Search',None)
    if keyword:
        search_results = fetch_by_name(keyword)
    return render_template('index.html')

if __name__ == '__main__':
    app.run(port=8802)