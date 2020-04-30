from flask import Flask, render_template
import requests
import gunicorn
import json
import xml.etree.ElementTree as ET

app = Flask(__name__)

@app.route("/")
def home_view():
    return render_template("index.html")