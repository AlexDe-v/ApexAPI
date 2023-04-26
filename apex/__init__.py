"""
## Apex legends API wrapper  

Uses modern async/await syntax!


Using this requires a token wich can be setup like this:  

`apex.token = <TOKEN>`  

If you don't have one you can visit the website: https://portal.apexlegendsapi.com/  


Need help? You can visit the github of this wrapper for some code examples:  
https://github.com/AlexDe-v/ApexAPI  

"""

import requests



class TokenError(Exception):
    """
    Will be raised if there is something wrong with the token or if none is present.
    """
    def __init__(self, message):
        self.message = message
        self.error_code = 1


class Switch(Exception):
    """
    Will be raised if you didn't read the text and used Switch as the platform :P
    """
    def __init__(self):
        self.message = "Switch isn't supported by the API!"
        self.error_code = 1

token = None
"""This token will be used by future requests. If you don't have one visit https://portal.apexlegendsapi.com/  

Not having a token will raise a `TokenError`.
"""

class Result:
    def __init__(self, banner, uri):
        self.banner = banner
        self.uri = uri

def test():
    r = "rr"
    s = "ss"
    return Result(r, s)

    


def get_maps():
    """
    Returns current map rotation in JSON format.
    Note that this does not require a token!
    """
    r = requests.get('https://lil2-gateway.apexlegendsstatus.com/gateway.php?qt=map')
    json = r.json()
    return json


def get_user(username: str, platform: str):
    """
    Returns player data in JSON format.
    This does require a token!

    
    #### Arguments:
    `username`: name of the player
    `platform`: PC | Xbox | PS4

    
    Note that switch is not supported by the apexstatus API!
    """
    if token == None:
        raise TokenError("No token is provided! Provide one with `apex.token`")
    if platform.lower() == 'switch':
        raise Switch()
    r = requests.get(f'https://api.mozambiquehe.re/bridge?auth={token}&player={username}&platform={platform}')
    json = r.json()
    return json