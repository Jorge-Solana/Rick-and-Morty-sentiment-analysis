from Config.config import engine
import pandas as pd

def character():
    query = f"""
    SELECT * FROM `Character`
    """
    datos = pd.read_sql_query(query,engine)
    return datos.to_json(orient='records')

def phrase():
    query = f"""
    SELECT * FROM `Phrase`
    """
    datos = pd.read_sql_query(query,engine)
    return datos.to_json(orient='records')

def episode():
    query = f"""
    SELECT * FROM `Episode`
    """
    datos = pd.read_sql_query(query,engine)
    return datos.to_json(orient='records')


def character_phrases(name):
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
    query = f"""
    SELECT episode.Episode_name, `phrase`.phrase
    FROM episode
    INNER JOIN `phrase`
    ON episode.idEpisode = `phrase`.Episode_idEpisode
    WHERE Episode_name = "{episode}""
    
    """
    datos = pd.read_sql_query(query,engine)
    return datos.to_json(orient='records')

    
