from flask import Flask, render_template
import datetime
from datetime import date

app = Flask(__name__, template_folder="templates")

@app.route("/")
def index():
  headline = "This was a placeholder!"
  now = datetime.datetime.now()
  new_yr = now.month == 8 and now.day == 10
  return render_template("hello.html", new_yr=new_yr)
