import string
import spacy
from nltk.corpus import stopwords
from textblob import TextBlob
import pandas as pd
import requests
import sql_tools as sql
import sqlalchemy as alch
import os
from dotenv import load_dotenv

sql_pass = os.getenv('pass_sql')


# NLP FUNTIONS

def character_sentiment(name):
    '''
    Calls the API for all the phrases of an specified character and returns its polarity
    Args:
        name(str): the name of the character
    Returns:
        float: the polarity
    
    '''
    data = requests.get(f'http://127.0.0.1:5000/phrases/{name}')
    df = pd.DataFrame(data.json())
    lista = []
    for i,row in df.iterrows():
        blob = TextBlob(f"{row['phrase']}")
        polarity = blob.sentiment[0]
        lista.append(polarity)
    return sum(lista)/len(lista)


def sentiment_episode(episode):
    '''
     Calls the API for all the phrases of an specified episode and returns its polarity
    Args:
        episode(str): the name of the episode
    Returns:
        float: the polarity
    
    '''
    #query = sql.phrases_episode(f'{episode}')
    data = requests.get(f'http://127.0.0.1:5000/phrases_ep?episode={episode}')
    df = pd.DataFrame(data.json())
    all_ = []
    for i, row in df.iterrows():
        blob = TextBlob(f"{row['phrase']}")
        pol = blob.sentiment[0]
        all_.append(pol)
    return sum(all_)/len(all_)


def general_sentiment():
    '''
    Calls the API for all the phrases in season 1 and returs its polarity
    Args:
        none
    Returns:
        float: the polarity
    
    '''
    data_ = requests.get('http://127.0.0.1:5000/phrases')
    df = pd.DataFrame(data_.json())
    list_ = []
    for i, row in df.iterrows():
        blob = TextBlob(f'{row["Phrase"]}')
        polarity_ = blob.sentiment[0]
        list_.append(polarity_)
    return sum(list_)/len(list_)

# CHECK FUNTIONS & LOOPS

dbName="rick_morty"
connectionData=f"mysql+pymysql://root:{sql_pass}@localhost/{dbName}"
engine = alch.create_engine(connectionData)

def check (something, string):
    '''
    Checks if the value exists in the table.
    Args:
        something(str): the table from where we are checking
        string(str): a singular value of (something), the actual column
    Returns:
        bool: Ture if exists False if not exists
      
    '''
    if something == 'character':
        query = list(engine.execute(f"SELECT Character_name FROM `Character` WHERE Character_name = '{string}'" ))
        if len(query) > 0:
            return True
        else:
            return False
    elif something == 'phrase':
        query = list(engine.execute(f"SELECT Phrase FROM `Phrase` WHERE Phrase = '{string}'" ))
        if len(query) > 0:
            return True
        else:
            return False
    elif something == 'episode':
        query = list(engine.execute(f"SELECT Episode_name FROM Episode WHERE Episode_name = '{string}'" ))
        if len(query) > 0:
            return True
        else:
            return False

# dictionaries with our keys and values from our data
# this is for the insert when we have foreign keys

characters = {
    'Rick' : 1,
    'Morty' : 2,
    'Jerry' : 3,
    'Summer' : 4,
    'Beth' : 5
}

episodes = {
    'Pilot' : 1,
    'Lawnmower Dog' : 2,
    'Rick Potion 9' : 3,
    'A Rickle in Time' : 4,
    'The Wedding Squanchers' : 5,
    'Get Schwifty' : 6,
    'Interdimensional Cable 2  Tempting Fate' : 7,
    'The Rickshank Rickdemption' : 8,
    'Pickle Rick' : 9,
    'Vindicators 3  The Return of Worldender' : 10,
    'Tales From the Citadel' : 11
}


# loops for inserting our data

rick_morty = pd.read_csv('./RickAndMortyScripts.csv')
rick_morty.drop(['index'], axis = 1, inplace=True)
rick_morty = rick_morty[(rick_morty['name'] == 'Rick') | (rick_morty['name'] == 'Morty') | (rick_morty['name'] == 'Jerry') | (rick_morty['name'] == 'Summer') | (rick_morty['name'] == 'Beth')]




rick_morty.line = rick_morty.line.str.replace("'", ' ')
rick_morty.line = rick_morty.line.str.replace('"', ' ')
rick_morty.line = rick_morty.line.str.replace('%', '%%')



# this part is mentioned because is just for the insertion of the data whih is already loaded
'''
for i, fila in rick_morty.iterrows():
    if check('character', f"{fila['name']}"):
        print('This already exists')
    else:
        engine.execute(
            f"""
            INSERT INTO `character` (Character_name) VALUES
            ("{fila['name']}");
           """
        )

#for i, fila in rick_morty.iterrows():
    if check ('episode', f"{fila['episode name']}"):
        print('This already exists')
    else:
        engine.execute(
            f"""
            INSERT INTO `episode` (Episode_name) VALUES
            ("{fila['episode name']}");
           """
        )

#for ii, (i, fila) in enumerate(rick_morty.iterrows()):
    if ii % 100 == 0:
        print(f"voy por el {ii}")
    
    if check('phrase', f"{fila['line']}"):
        continue
    else:
        try:
            q = f"""
                INSERT INTO phrase (Phrase, Character_idCharacter, Episode_idEpisode) VALUES ("{fila['line']}", {characters[fila['name']]}, {episodes[fila['episode name']]});
                """
            engine.execute(q)            
        except:
            raise 'Couldn`t insert this phrase'
'''
