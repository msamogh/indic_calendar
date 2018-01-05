from flask import *
from cal import *

app = Flask(__name__)

@app.route('/')
def main():
	c = Calendar(5118)
	
	return render_template('index.html')

app.run(host='0.0.0.0', port=8000, debug=True)