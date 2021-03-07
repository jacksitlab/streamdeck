from ..samsungtv import SamsungTVClient
from .baseExecutor import BaseExecuter

class TVExecuter(BaseExecuter):

    def __init__(self, client):
        super().__init__()
        self.client = client
    
