import json


class StreamDeckConfig:

    def __init__(self, configFilename):
        file = open(configFilename, 'r')
        o = json.load(file)
        file.close()
        self.defaultMargin = int(getOrDefault(o,"defaultMargin","0"))
        self.remote = dict()
        tmp = getOrDefault(o["remote"], "foobar")
        self.remote["foobar"] = FoobarConfig(tmp) if not tmp is None else None
        tmp = getOrDefault(o["remote"], "denon")
        self.remote["denon"] = DenonConfig(tmp) if not tmp is None else None
        tmp = getOrDefault(o["remote"], "kodi")
        self.remote["kodi"] = KodiConfig(tmp) if not tmp is None else None
        self.items = self.loadItems(o["items"])

    def loadItems(self, itemsMap):
        m = dict()
        keys = itemsMap.keys()
        for key in keys:
            m[key] = ItemConfig(itemsMap[key])
        return m

    def getItemConfig(self, key):
        if str(key) in self.items:
            return self.items[str(key)]
        return None


class DenonConfig:
    def __init__(self, obj):
        self.host = obj["host"]


class FoobarConfig:
    def __init__(self, obj):
        self.host = obj["host"]


class KodiConfig:
    def __init__(self, obj):
        self.host = obj["host"]
        self.username = obj["username"]
        self.password = obj["password"]


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
