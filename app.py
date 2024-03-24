from flask import *

app = Flask(__name__)

@app.route('/')
def main_page():
    return render_template('index.html')

app.run(port=5200)
