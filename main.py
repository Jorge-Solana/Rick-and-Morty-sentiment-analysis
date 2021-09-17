from flask import Flask, request
from flask import json
from flask.json import jsonify, load
from sqlalchemy.util.langhelpers import method_is_overridden
import src.sql_tools as sql

app = Flask(__name__)



@app.route('/')
def inicio():
    return 'Que pasa con tu rollo repollo'

@app.route("/characters")
def character():
    character = sql.character()
    return character

@app.route("/phrases")
def phrase():
    phrase = sql.phrase()
    return phrase

@app.route("/episodes")
def episode():
    episode = sql.episode()
    return episode

@app.route("/phrases/<name>")
def character_phrases(name):
    phrases = sql.character_phrases(name)
    return phrases

@app.route("/phrases/<episode>")
def phrases_episode(episode):
    phr_ep = sql.phrases_episode(episode)
    return phr_ep

@app.route("/newphrase", methods=['POST'])
def newphrase():
    #dict_ = {
        ''


    



app.run(debug=True)