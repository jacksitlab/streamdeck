import xml.etree.ElementTree as ET

# GET /goform/formMainZone_MainZoneXml.xml


class DenonStatus:

    def __init__(self, xmlString):
        root = ET.fromstring(xmlString)
        self.friendlyName = root.find('FriendlyName/value').text
        self.power = root.find('Power/value').text
        self.zonePower = root.find('ZonePower/value').text
        self.renameZone = root.find('RenameZone/value').text
        self.topMenuLink = root.find('TopMenuLink/value').text
        self.videoSelectDisp = root.find('VideoSelectDisp/value').text
        self.videoSelect = root.find('VideoSelect/value').text
        self.videoSelectOnOff = root.find('VideoSelectOnOff/value').text
        self.videoSelectLists = DenonStatusVideoSelectList(
            root.find('VideoSelectLists'))
        self.modelId = int(root.find('ModelId/value').text)
        self.brandId = root.find('BrandId/value').text
        self.salesArea = int(root.find('SalesArea/value').text)
        self.inputFuncSelect = root.find('InputFuncSelect/value').text
        self.netFuncSelect = root.find('NetFuncSelect/value').text
        self.selectSurround = root.find('selectSurround/value').text
        self.volumeDisplay = root.find('VolumeDisplay/value').text
        self.masterVolume = float(root.find('MasterVolume/value').text)
        self.mute = root.find('Mute/value').text
        self.remoteMaintenance = root.find('RemoteMaintenance/value').text
        self.subwooferDisplay = root.find('SubwooferDisplay/value').text
        self.zone2VolDisp = root.find('Zone2VolDisp/value').text

    def __str__(self):
        return "friendlyName="+str(self.friendlyName) + " power="+self.power + "masterVolume" + str(self.masterVolume)


class DenonStatusVideoSelectList:

    def __init__(self, xmlEle):
        self.items = []
        for child in xmlEle:
            e = DenonStatusVideoSelectItem(child)
            self.items.append(e)


class DenonStatusVideoSelectItem:

    def __init__(self, xmlEle):
        self.index = xmlEle.attrib["index"]
        self.table = xmlEle.attrib["table"]
        self.param = xmlEle.attrib["param"]

    def __str__(self):
        return "index="+str(self.index) + " table="+str(self.table) + " param="+str(self.param)
