import string
import spacy
from nltk.corpus import stopwords
from textblob import TextBlob
import pandas as pd
import requests
import sql_tools as sql



def character_sentiment(name):
    data = requests.get(f'http://127.0.0.1:5000/phrases/{name}')
    df = pd.DataFrame(data.json())
    lista = []
    for i,row in df.iterrows():
        blob = TextBlob(f"{row['phrase']}")
        polarity = blob.sentiment[0]
        lista.append(polarity)
    return sum(lista)/len(lista)


def sentiment_episode(episode):
    query = sql.phrases_episode(f'{episode}')
    df = pd.DataFrame(query)
    all_ = []
    for i, row in df.iterrows():
        blob = TextBlob(f"{row['phrase']}")
        pol = blob.sentiment[0]
        all_.append(pol)
    return sum(all_)/len(all_)


def general_sentiment():
    data_ = requests.get('http://127.0.0.1:5000/phrases')
    df = pd.DataFrame(data_.json())
    list_ = []
    for i, row in df.iterrows():
        blob = TextBlob(f'{row["Phrase"]}')
        polarity_ = blob.sentiment[0]
        list_.append(polarity_)
    return sum(list_)/len(list_)