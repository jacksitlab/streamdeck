import re
from ..client.denonClient import DenonClient,DenonSource
from .baseExecutor import BaseExecuter

class DenonExecuter(BaseExecuter):

    def __init__(self, client):
        super().__init__()
        self.client = client

    def setVolume(self, dBValue):
        print("set volume to "+str(dBValue))
        self.client.setVolume(dBValue)
    
    def setSource(self, src):
        print("set source to "+src)
        enumSrc = DenonSource[src]
        self.client.setSource(enumSrc)