from Config.config import engine
import pandas as pd
import ast
import src.nosql_tools as nosql
import requests 
from sqlalchemy.util.langhelpers import method_is_overridden

def character():
    '''
    Calls the database and returns all the characters
    Args:
        none
    Returns:
        json: all the chacarters in a json format
    
    '''
    query = f"""
    SELECT * FROM `Character`
    """
    datos = pd.read_sql_query(query,engine)
    return datos.to_json(orient='records')

def phrase():
    '''
    Calls the databse and returns all the phrases
    Args:   
        none
    Returs:
        json: all the phrases in a json format
    
    '''
    query = f"""
    SELECT * FROM `Phrase`
    """
    datos = pd.read_sql_query(query,engine)
    return datos.to_json(orient='records')

def episode():
    '''
    Calls the databse and returns all the episodes (names)
    Args:
        none
    Returns:
        json: all the episodes in a jsonn format
    
    '''
    query = f"""
    SELECT * FROM `Episode`
    """
    datos = pd.read_sql_query(query,engine)
    return datos.to_json(orient='records')


def character_phrases(name):
    '''
    Calls the database and returns all the phrases of the specified character
    Args:
        name(str): the name of the character
    Returns:
        json: all the phrases of a character in a json format
    
    '''
    query = f"""
    SELECT `character`.Character_name, `phrase`.phrase
    FROM `character`
    INNER JOIN `phrase`
    ON `character`.idCharacter = phrase.Character_idCharacter
    WHERE Character_name = "{name}";

    """
    datos = pd.read_sql_query(query,engine)
    return datos.to_json(orient='records')

def phrases_episode(episode):
    '''
    Calls the database and returns all the phrases of the specified episode
    Args:
        episode(str): the name of the episode
    Returns:
        json: all the phrases of an episode in a json format
        #I had do the ast.literal_eval because otherwise the return was a string
    '''
    
    query = f"""
    SELECT episode.Episode_name, `phrase`.phrase
    FROM episode
    INNER JOIN `phrase`
    ON episode.idEpisode = `phrase`.Episode_idEpisode
    WHERE Episode_name = "{episode}";
    
    """
    datos = pd.read_sql_query(query,engine)
    #print(datos)
    str_ = datos.to_json(orient='records')
    return str_

def get_character_id(character_name):
    '''
    Calls the DB to return the id of the character if exists or if it is inserted
    Args:
        character_name(str)
    Returns:
        int
    '''
    chars = list(engine.execute(f"SELECT Character_name, idCharacter FROM `Character` WHERE Character_name = '{character_name}'"))
    if len(chars) > 0:
        id_character = chars[0][1]
        return id_character
    else:
        cursor = engine.execute(f"INSERT INTO `Character` (Character_name) VALUES ('{character_name}')")
        id_character = cursor.lastrowid
        return id_character

def get_episode_id(episode_name):
    '''
      Calls the DB to return the id of the episode if exists or if it is inserted
    Args:
        character_name(str)
    Returns:
        int
    '''
    ep = list(engine.execute(f"SELECT Episode_name, idEpisode FROM `episode` WHERE Episode_name = '{episode_name}'"))
    if len(ep) > 0:
        id_episode = ep[0][1]
        return id_episode
    else:
        cursor = engine.execute(f"INSERT INTO `Episode` (Episode_name) VALUES ('{episode_name}')")
        id_episode = cursor.lastrowid
        return id_episode

#function to check if the data and insert if so
def insert_ifnew(dictionary):
    ''' 
    By calling get_characterid and get_episodeid checks if the data given by POST method exists, gives the ids of each value 
    and inserts the data if it does not exist
    Args:
        dictionary(dict): see documentation to see how write it
    Returns:
        str
    
    '''
    character_name = dictionary.get("character")
    episode_name = dictionary.get("episode")
    phrase = dictionary.get("phrase")
    

    char_id = get_character_id(character_name)
    ep_id = get_episode_id(episode_name)
    
    
    phras = list(engine.execute(f"SELECT Phrase FROM `phrase` WHERE Phrase = '{phrase}' AND Character_idCharacter = {char_id} AND Episode_idEpisode = {ep_id}"))
    if len(phras) > 0:
        return 'Your data already exists'
    else:
        engine.execute(f"INSERT INTO phrase (Phrase, Character_idCharacter, Episode_idEpisode) VALUES ('{phrase}', {char_id}, {ep_id})")
        return 'Inserted correctly'

