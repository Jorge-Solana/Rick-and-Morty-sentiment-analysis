from flask import Flask, request
from flask import json
from flask.json import jsonify, load
from sqlalchemy.util.langhelpers import method_is_overridden
import src.sql_tools as sql
import src.nosql_tools as nosql
import markdown.extensions.fenced_code 


app = Flask(__name__)



@app.route('/')
def index():
    readme_file = open("documentation.md", "r")
    md_template = markdown.markdown(readme_file.read(), extensions = ["fenced_code"])
    return md_template


@app.route("/characters")
def character():
    '''
    Calls the character function and returns is json
    Args:
        none
    Returns:
        json
    '''
    character = sql.character()
    return character

@app.route("/phrases")
def phrase():
    '''
    Calls the phrase function and returns its json
    Args:
        none
    Returns:
        json
    '''
    phrase = sql.phrase()
    return phrase

@app.route("/episodes")
def episode():
    '''
    Calls the episode function and returns its json
    Args:
        none
    Returns:
        json
    '''
    episode = sql.episode()
    return episode

@app.route("/phrases/<name>")
def character_phrases(name):
    '''
    Calls the character_phrases function and returs its json
    Args:
        name(str): the name of the character
    Returns:
        json
    '''
    phrases = sql.character_phrases(name)
    return phrases

@app.route("/phrases?episode")
def phrases_episode(episode):
    '''
    Calls the phrases_episode function and returns its json
    Args:
        episode(str): the name of the episode
    Returns:
        json
    '''
    ep = request.args(episode) ### SOLUCIONALO CON ARGS
    phrases = sql.phrases_episode(ep)
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
    '''
    Calls the character_sentiment function and returns its polarity
    Args:
        name(str): the name of the character
    Returns:
        str: the polarity value
    '''
    char_sent = nosql.character_sentiment(name)
    return str(char_sent)

# this doesnt work
@app.route("/phrases/<episode>/sentiment")
def ep_sentiment(episode):
    '''
    Calls the sentiment_episode function and returns its polarity
    Args:
        episode(str): the name of the episode
    Returns:
        str: the polarity value
    '''
    ep_sent = nosql.sentiment_episode(episode)
    return str(ep_sent)

@app.route("/sentiment")
def general_sentiment():
    '''
    Calls the general_sentiment funciotn and returns its polarity
    Args:
        none
    Returns:
        str: the polarity value
    '''
    gen_sent = nosql.general_sentiment()
    return str(gen_sent)    



app.run(debug=True)