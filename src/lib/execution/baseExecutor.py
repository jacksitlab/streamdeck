import re

class BaseExecuter:

    def __init__(self):
        pass

    def execute(self, command):
        regex = r"^([^\(]+)\(([^\)]*)\)$"
        match = re.findall(regex, command, re.M|re.I)
        if len(match)>0:
            cmd = match[0][0]
            args = match[0][1] if len(match[0])>1 else ""

            return self.resolveExecution(cmd, args)

        
        raise Exception("unable to resolve "+command)

    def resolveExecution(self, cmd, args):
        method_to_call = getattr(self, cmd)
        if method_to_call:
            return method_to_call(args)
    
        raise Exception("unable to resolve "+command)
    