import re
from ..denonClient import DenonClient

class DenonExecuter:

    def __init__(self, client):
        self.client = client
    
    def execute(self, command):
        regex = r"^([^\(]+)\(([^\)]*)\)$"
        match = re.findall(regex, command, re.M|re.I)
        if len(match)>0:
            cmd = match[0][0]
            args = match[0][1] if len(match[0])>1 else ""

            return self.resolveExecution(cmd, args)

        
        raise Exception("unable to resolve "+command)

    def resolveExecution(self, cmd, args):
        print("execute denon command "+cmd +" with args "+str(args))
        return None