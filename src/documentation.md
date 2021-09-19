# Welcome to Rick and Morty 's API

![portada](https://github.com/Jorge-Solana/Rick-and-Morty-sentiment-analysis/blob/main/images/Rick-y-Morty-800x400.jpg)



Here you can either access to the information of the season 1, you add new data or even you can receive the analysis of the polarity of the characters and the episodes.

## For the correct responses, follow the documentation as it says.

Before any endpoint, the url you must have is the following:
http://127.0.0.1:5000

For the sake of saving space, in the following documentation, when mentioning the endpoints, we are goint to omit the url, but for every response you must have it before any endpoint.


## ENDPOINTS
Here you are going to find the 3 different type of endpints you can use with this API.

### - GET Method endpoints
    
- /characters
        
    This endpoint gives you a response in a json format    containing all the main characters in Rick and Morty's season 1.

- /episodes
        
    This endpoint gives you a response in a json format containing all the episodes in the season 1.
    
- /phrases
        
    This endpoint gives you a response in a json format 
        containing all the phrases, the dialogues, from season 1.
    
- /phrases/name
        
    This endpoint gives you a response in a json format containing all the phrases of a certain character, (name), of your choice.
    
- /phrases/episode
        
    This endopint gives you a response in a json format containing all the phrases of a certain episode of your choice. The episode must be the name of the episode, NOT THE NUMBER.

##  POST Method enpoint

- /newdata
        
    This endpoint is for you to insert new data in this API.
    The format you have to present the data is the following:
            
            dictionary = {
                'character' : 'name of the character'
                'episode' : 'name of the episode'
                'phrase' : 'phrase'
            }

##  Sentimient analysis enpoints

- /phrases/character/sentiment
        
    This endpoint gives you a string as a response. This string is a value between -1 and 1, where -1 is the most negative it can be and 1 is the most positive it can be. In this case it will return the polarity of a desired character, (character), of the season 1.

- /phrases/episode/sentiment
        
    This endpoint gives you a string as a response. This string is a value between -1 and 1, where -1 is the most negative it can be and 1 is the most positive it can be. In this case it will return the polarity of a desired episode, (episode), of the season 1. You must indicate the episode name, not the number.
    
- /sentiment
        
    This endpoint gives you a string as a response. This string is a value between -1 and 1, where -1 is the most negative it can be and 1 is the most positive it can be. In this cade, this evaluates the general polarity of the whole season.