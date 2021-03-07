from ..foobarClient import FoobarClient
from .baseExecutor import BaseExecuter

class FoobarExecuter(BaseExecuter):

    def __init__(self, client):
        super().__init__()
        self.client = client
    
