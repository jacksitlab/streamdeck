from enum import Enum
from ..client.samsungtv import SamsungTVClient
from .baseExecutor import BaseExecuter

class TVExecuter(BaseExecuter):

    def __init__(self, client):
        super().__init__()
        self.client = client

    def setSource(self, src):
        enumSrc = TVSource[src]
        self.client.selectByIndex(enumSrc.value)

class TVSource(Enum):
    PC="1"
    HOMETHEATER="2"
    KODI="3"
    
