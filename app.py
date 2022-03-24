from functools import wraps
import json
import threading
import uuid
from flask import Flask, current_app, jsonify, render_template, request
from setuptools import Extension
from speechtotext import generate_keywords
import twitter, asyncio
from flask_cors import CORS

global usertoken

app = Flask(__name__)

@app.route("/")
def home():
    return "hello world"

@app.route('/api/login', methods =['POST'])
def login():
    return "success"

@app.route('/api/keywords/<user_token>')
def user(user_token):
    threading.Thread(target=send_keyword_request(user_token)).start()
    return "success"
def send_keyword_request(user_token):
    generate_keywords(user_token)
    
# twitter.scrape_twitter("cyclone", "tauktae")