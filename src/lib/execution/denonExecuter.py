import re
from ..denonClient import DenonClient
from .baseExecutor import BaseExecuter

class DenonExecuter(BaseExecuter):

    def __init__(self, client):
        super().__init__()
        self.client = client

    def setVolume(self, dBValue):
        print("set volume to "+str(dBValue))
    
    def setSource(self, src):
        print("set source to "+src)