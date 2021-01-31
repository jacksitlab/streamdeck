import json


class StreamDeckConfig:

    def __init__(self, configFilename):
        file = open(configFilename,'r')
        o = json.load(file)
        file.close()
        self.remote = dict()
        self.remote["foobar"] = getOrDefault(o["remote"],"foobar")
        self.remote["denon"] = getOrDefault(o["remote"],"denon")
        self.items = self.loadItems(o["items"])

    def loadItems(self, itemsMap):
        m = dict()
        keys = itemsMap.keys()
        for key in keys:
            m[key] = ItemConfig(itemsMap[key])
        return m


class ItemConfig:

    def __init__(self, obj):
        self.type = obj["type"]
        self.image = getOrDefault(obj, "image")
        self.imagePressed = getOrDefault(obj, "imagePressed")
        self.executions = getOrDefault(obj, "exec")
        tmp = getOrDefault(obj, "refreshRate")
        self.refreshRate = int(tmp) if not tmp is None else None
        


def getOrDefault(dictObj, key, defaultValue=None):
    if key in dictObj:
        return dictObj[key]
    return defaultValue
