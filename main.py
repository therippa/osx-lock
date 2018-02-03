import subprocess
import time
from flask import Flask
from flask import render_template

app = Flask(__name__)

@app.route("/")
def main():
	subprocess.call('/usr/bin/pmset displaysleepnow', shell=True)
	refresh_time = time.strftime('%x %X')
	return render_template('index.html', refresh_time=refresh_time)
