from flask import Flask, render_template, request
from flask_mysqldb import MySQL

app = Flask(__name__)
app.config['SECRET_KEY'] = ""
app.config['MYSQL_DB'] = ""
app.config['MYSQL_PASSWORD'] = ""
app.config['MYSQL_USER'] = "root"
app.config['MYSQL_HOST'] = "localhost"
app.config['MYSQL_CURSORCLASS'] = "DictCursor"
mysql = MySQL(app)


@app.route('/')
def index():
    pass


@app.route('/create', methods=['GET', 'POST'])
def create():
    pass


@app.route('/<int:post_id>')
def post(post_id):
    pass


@app.route('/<int:post_id>/edit', methods=['GET', 'POST'])
def edit(post_id):
    pass


@app.route('/<int:post_id/delete>')
def delete(post_id):
    pass


if __name__ == '__main__':
    app.run(debug=True)
