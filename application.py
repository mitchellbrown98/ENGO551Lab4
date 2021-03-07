import os

from flask import Flask, session, render_template, request, flash, json, jsonify
from flask_session import Session
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker

import requests

app = Flask(__name__)

# Check for environment variable
#if not os.getenv("DATABASE_URL"):
#    raise RuntimeError("DATABASE_URL is not set")

# Configure session to use filesystem
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

# Set up database
#engine = create_engine(os.getenv("DATABASE_URL"))
#db = scoped_session(sessionmaker(bind=engine))


@app.route("/")
def home():
    #mapbox info
    username = 'mitchellbrown98'
    style_id = 'ckkcvultf02pt17o521x7072r'
    style_id2 = 'cklwsiu2911ov17nsiiywum05'
    accessToken = 'pk.eyJ1IjoibWl0Y2hlbGxicm93bjk4IiwiYSI6ImNra2N2cjB5NTAwYnQybm91OHFpanQ2b2sifQ.sWLC8sV-m3qg2cvANpey0w'

    info=[]
    info.append(username)
    info.append(style_id)
    info.append(style_id2)
    info.append(accessToken)

    return render_template("index.html", info=info)
