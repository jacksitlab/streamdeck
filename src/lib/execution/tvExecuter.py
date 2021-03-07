
from ..samsungtv import SamsungTVClient

class TVExecuter:

    def __init__(self, client):
        self.client = client
    
    def execute(self, command):
        print("execute tv command "+command)