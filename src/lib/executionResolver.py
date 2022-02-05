import os
import re
from .execution.denonExecuter import DenonExecuter
from .execution.foobarExecuter import FoobarExecuter
from .execution.kodiExecuter import KodiExecuter
from .execution.tvExecuter import TVExecuter
from .execution.profileExecuter import ProfileExecuter
from .client.denonClient import DenonClient
from .client.foobarClient import FoobarClient
from .client.kodiClient import KodiClient
from .client.samsungtv import SamsungTVClient

class ExecutionResolver:

    def __init__(self, config):
        self.resolvers = dict()
        self.config = config
        # remoteConfigs
        rc = self.config.getRemoteConfigs()
        for k in rc.keys():
            e = self.findExecutor(rc[k])
            if e:
                self.register(k,e)
            else:
                print("unable to find executor for "+k)
        # profile confis
        pc = self.config.getProfileConfigs()
        for k in pc.keys():
            self.register("profile."+k+"()",ProfileExecuter(pc[k],self.resolvers))


    def register(self, k, executer):
        print("register executer for key "+k+" "+ str(type(executer)))
        self.resolvers[k] = executer

    # run execution
    # e.g. profile.nintendoSwitch()
    def execute(self, execution):
        print("try to execute: "+ str(execution))
        regex = r"^([^\.]+)\.(.*)$"
        match = re.findall(regex, execution, re.M|re.I)
        if len(match)>0:
            k = match[0][0]
            e = match[0][1]
            if k == "profile":
                k = k+"."+e
                if k in self.resolvers:
                    return self.resolvers[k].execute()
                else:
                    raise Exception("unable to find executor for "+k)
            else:
                print("try to resolve executor "+k+ " with fn="+e)
                if k in self.resolvers:
                    return self.resolvers[k].execute(e)
                else:
                    raise Exception("unable to find executor for "+k)
        else:
            raise Exception("unable to detect command")


    # instantiate executor and belonging client
    def findExecutor(self, remoteConfig):
        t = remoteConfig.type
        if t == "DENON":
            return DenonExecuter(DenonClient(remoteConfig.url))
        elif t == "FOOBAR":
            return FoobarExecuter(FoobarClient(remoteConfig.url))
        elif t == "KODI":
            return KodiExecuter(KodiClient(remoteConfig.url,
                remoteConfig.username,
                remoteConfig.password))
        elif t == "SAMSUNG_SMARTTV":
            return TVExecuter(SamsungTVClient(remoteConfig.host))
        return None
