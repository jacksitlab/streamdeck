from ..client.kodiClient import KodiClient
from .baseExecutor import BaseExecuter

class KodiExecuter(BaseExecuter):

    def __init__(self, client):
        super().__init__()
        self.client = client
    
