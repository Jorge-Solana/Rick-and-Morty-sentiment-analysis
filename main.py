from flask import Flask, request
from flask import json
from flask.json import jsonify, load
from sqlalchemy.util.langhelpers import method_is_overridden
import src.sql_tools as sql
import src.nosql_tools as nosql


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
    phrases = sql.phrases_episode(episode)
    return phrases

@app.route("/newdata", methods=['POST'])
def newdata():
    character = request.form.get('character')
    phrase = request.form.get('phrase')
    episode = request.form.get('episode')

    return sql.insert_data(character, phrase, episode)


# now we create the endpoints for the sentiment analysis

@app.route("/phrases/<name>/sentiment")
def char_sentiment(name):
    char_sent = nosql.character_sentiment(name)
    return str(char_sent)

# this doesnt work
@app.route("/phrases/<episode>/sentiment")
def ep_sentiment(episode):
    ep_sent = nosql.sentiment_episode(episode)
    return str(ep_sent)

@app.route("/sentiment")
def general_sentiment():
    gen_sent = nosql.general_sentiment()
    return str(gen_sent)    



app.run(debug=True)