import flask import Flask
import render_template from flusk
app = Flask(__name__)

@app.route('/')
@app.route('/jobs')
def jobs():
    return render_template('index.html')
