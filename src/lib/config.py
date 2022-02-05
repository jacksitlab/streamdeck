import json


class StreamDeckConfig:

    def __init__(self, configFilename):
        file = open(configFilename, 'r')
        o = json.load(file)
        file.close()
        self.defaultMargin = int(getOrDefault(o,"defaultMargin","0"))
        self.remote = dict()
        tmp = getOrDefault(o["remote"], "foobar")
        if tmp:
            self.remote["foobar"] = FoobarConfig(tmp)
        tmp = getOrDefault(o["remote"], "denon")
        if tmp:
            self.remote["denon"] = DenonConfig(tmp)
        tmp = getOrDefault(o["remote"], "kodi")
        if tmp:
            self.remote["kodi"] = KodiConfig(tmp)
        tmp = getOrDefault(o["remote"], "tv")
        if tmp:
            self.remote["tv"] = TVConfig(tmp)
        self.items = self.loadItems(o["items"])
        self.profiles = getOrDefault(o,"profiles",dict())

    def loadItems(self, itemsMap):
        m = dict()
        keys = itemsMap.keys()
        for key in keys:
            m[key] = ItemConfig(itemsMap[key])
        return m

    def getRemoteConfigs(self):
        return self.remote

    def getProfileConfigs(self):
        return self.profiles

    def getItemConfig(self, key):
        if str(key) in self.items:
            return self.items[str(key)]
        return None


class DenonConfig:
    def __init__(self, obj):
        self.url = obj["url"]
        self.type = obj["type"]


class FoobarConfig:
    def __init__(self, obj):
        self.url = obj["url"]
        self.type = obj["type"]


class KodiConfig:
    def __init__(self, obj):
        self.url = obj["url"]
        self.type = obj["type"]
        self.username = obj["username"]
        self.password = obj["password"]

class TVConfig:
    def __init__(self, obj):
        self.host = obj["host"]
        self.type = obj["type"]

class ItemConfig:

    def __init__(self, obj):
        self.type = obj["type"]
        self.image = getOrDefault(obj, "image")
        self.imagePressed = getOrDefault(obj, "imagePressed")
        self.executions = getOrDefault(obj, "exec",())
        tmp = getOrDefault(obj, "refreshRate")
        self.refreshRate = int(tmp) if not tmp is None else None


def getOrDefault(dictObj, key, defaultValue=None):
    if key in dictObj:
        return dictObj[key]
    return defaultValue
