import re

class ProfileExecuter:

    def __init__(self, commands, executors):
        self.commands = commands
        self.executors = executors
    
    def execute(self):
        for cmd in self.commands:
            regex = r"^([^\.]+)\.(.*)$"
            match = re.findall(regex, cmd, re.M|re.I)
            if len(match)>0:
                k = match[0][0]
                e = match[0][1]
                if k in self.executors:
                    self.executors[k].execute(e)
                else:
                    raise Exception("unable to find executor for "+k)



        