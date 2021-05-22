from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
	return "Great!!"

@app.route('/home')
def home():
	return render_template('example.html')


if __name__ == "__main__":
	app.run(debug = True, port=5002)