
from ..kodiClient import KodiClient

class KodiExecuter:

    def __init__(self, client):
        self.client = client
    
    def execute(self, command):
        print("execute kodi command "+command)