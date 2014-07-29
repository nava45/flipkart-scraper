from flask import Flask, request, render_template, send_from_directory


app = Flask(__name__)


@app.route('/', methods=('GET', 'POST'))
def view_search():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(port=5001)