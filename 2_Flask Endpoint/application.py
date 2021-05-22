from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
	return "Great!!"

@app.route('/home')
def home():
	return "<h1>Hello Everyone!!</h1>"


if __name__ == "__main__":
	app.run(debug = True, port=5001)