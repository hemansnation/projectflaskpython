from flask import Flask, render_template, request, redirect, url_for
from flask_mysqldb import MySQL

app = Flask(__name__)


app.config['MYSQL_HOST'] = 'sql6.freemysqlhosting.net'
app.config['MYSQL_USER'] = 'sql6413722'
app.config['MYSQL_PASSWORD'] = 'y4TSmi55tb'
app.config['MYSQL_DB'] = 'sql6413722'
app.config['MYSQL_CURSORCLASS'] = 'DictCursor'

mysql = MySQL(app)

@app.route('/')
def index():
	cur = mysql.connection.cursor()
	#cur.execute('''CREATE TABLE indore (name VARCHAR(20), comment VARCHAR(20))''')
	cur.execute('''SELECT * FROM indore''')
	results = cur.fetchall()
	print(results)
	return render_template('index.html', result=results)

@app.route('/sign')
def sign():
	return render_template('sign.html')

@app.route('/process', methods=['POST'])
def process():
	name = request.form['name']
	comment = request.form['comment']
	cur = mysql.connection.cursor()
	cur.execute("INSERT INTO indore(name, comment) VALUES (%s,%s)",(name, comment))
	mysql.connection.commit()
	cur.close()
	return redirect(url_for('index'))

if __name__ == '__main__':
	app.run(debug=True, port=5006)