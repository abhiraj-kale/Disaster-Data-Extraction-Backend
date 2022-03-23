import json
import uuid
from flask import Flask, jsonify, render_template, request
import twitter

app = Flask(__name__)

@app.route("/")
def home():
    return "hello world"

@app.route('/api/login', methods =['POST'])
def login():
    return "sdf"

# twitter.scrape_twitter("cyclone", "tauktae")