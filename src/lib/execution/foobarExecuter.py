
from ..foobarClient import FoobarClient

class FoobarExecuter:

    def __init__(self, client):
        self.client = client
    
    def execute(self, command):
        print("execute foobar command "+command)