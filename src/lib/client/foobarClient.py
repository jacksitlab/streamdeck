from .baseHttpClient import BaseHttpClient

class FoobarClient(BaseHttpClient):
    
    def __init__(self, url, username=None, password=None):
        super().__init__(url)
        self.username = username
        self.password = password