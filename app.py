from flask import Flask, render_template, url_for

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/two')
def second():
    return render_template('two.html')


@app.route('/user/<string:name>/<int:id>')
def AB(name, id):
    return 'ABC' + name + '-' + str(id)


if __name__ == '__main__':
    app.run(debug=True)
