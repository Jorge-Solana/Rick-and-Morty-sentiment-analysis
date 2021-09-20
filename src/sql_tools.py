from Config.config import engine
import pandas as pd
import ast
import src.nosql_tools as nosql

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
    #print("Hola")
    query = f"""
    SELECT episode.Episode_name, `phrase`.phrase
    FROM episode
    INNER JOIN `phrase`
    ON episode.idEpisode = `phrase`.Episode_idEpisode
    WHERE Episode_name = "{episode}";
    
    """
    datos = pd.read_sql_query(query,engine)
    print(datos)
    str_ = datos.to_json(orient='records')
    return str_

# no estoy muy seguro de esta funcion
def insert_data(data):
    engine.execute(f"""
    INSERT INTO `character` (Chracter_name)
    VALUES ({data['character']});
    INSERT INTO `phrase` (Phrase)
    VALUES ({data['phrase']});
    INSERT INTO episode (Episode_name)
    VALUES ({data['episode']});
    """)
    return 'The data was inserted correctly'
# puede que esta funcione mejor
# ojo con las llamadas a las funciones de check, hay que especificar de que carpeta esta viniendo
def insert(dictionary):
    for k,v in dictionary.items():
        if k == 'character':
            if nosql.check2('character', string):
                return 'This character already exists'
            else:
                engine.execute(f"""
                INSERT INTO `character` (Character_name) VALUES ('{string}');
                """)
        
        elif k == 'phrase':
            if nosql.check2('phrase', string):
                return 'This phrase already exists'
            else:
                engine.execute(f"""
                INSERT INTO `phrase` (Phrase) VALUES ('{string}');
                """)
        
        elif k == 'episode':
            if nosql.check2('episode', string):
                return 'This episode already exists'
            else:
                engine.execute(f"""
                INSERT INTO episode (Episode_name) VALUES ('{string}');
                """)
