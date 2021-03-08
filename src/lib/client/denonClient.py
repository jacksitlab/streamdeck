from enum import Enum
import math
from .baseHttpClient import BaseHttpClient
from ..denon.status import DenonStatus


class DenonClient(BaseHttpClient):

    def __init__(self, url):
        super().__init__(url)

    def volumeUp(self, inc=1):
        while inc > 0:
            self.sendGetCommand('/goform/formiPhoneAppDirect.xml?MVUP')
            inc = inc-1

    def volumeDown(self, dec=1):
        while dec > 0:
            self.sendGetCommand('/goform/formiPhoneAppDirect.xml?MVDOWN')
            dec = dec-1

    def setVolume(self, dBValue):
#        status = self.readStatus()
#        curdbValue = status.masterVolume
#        diff = math.ceil(curdbValue - dBValue)
#        print("diff="+str(diff))
#        if diff > 0:
#            self.volumeUp(diff)
#        elif diff < 0:
#            self.volumeDown(-1*diff)
        self.sendGetCommand('/goform/formiPhoneAppVolume.xml?1+'+str(dBValue))

    def setSource(self, src):
        self.sendGetCommand('/goform/formiPhoneAppDirect.xml?'+src.value)

    def readStatus(self):
        xmlResponse = self.sendGetCommand(
            '/goform/formMainZone_MainZoneXml.xml')
        if xmlResponse is None:
            return None
        return DenonStatus(xmlResponse)


class DenonSource(Enum):
    CBLSAT = "SISAT"
    DVD = "SIDVD"
    BLURAY = "SIBD"
    GAME = "SIGAME"
    AUX = "SIAUX1"
    MEDIA_PLAYER = "SIMPLAY"
    IPOD_USB = "SIIPOD"
    CD = "SICD"
    TUNER = "SITUNER"
    NETWORK = "SINETWORK"
    TV = "SITV"
    INTERNET_RADIO = "SIINTERNET"
