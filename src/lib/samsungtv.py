
import websocket
import ssl
import time
from threading import Thread
import json

class SamsungTV:

    def __init__(self, host):
        config = {
            "name": "test",
            "description": "PC",
            "id": "",
            "host": host,
            "port": 8002,
            "method": "websocket",
            "timeout": 0,
        }
        self.connected = False
        url = "wss://"+config["host"]+":"+str(
            config["port"])+"/api/v2/channels/samsung.remote.control?name="+config["name"]
        #self.ws = websocket.Websocket(sslopt={"cert_reqs": ssl.CERT_NONE})
        # self.ws.connect("wss://"+config["host"]+":"+str(config["port"])+"/api/v2/channels/samsung.remote.control?name="+config["name"],
        #                on_message=self.onMessage,
        #                on_error=self.onError,
        #                on_close=self.onClose,
        #                on_open=self.onOpen)
        print("connect to "+url)
        websocket.enableTrace(True)
        self.ws = websocket.WebSocketApp(url,
                                         on_message=self.onMessage,
                                         on_error=self.onError,
                                         on_close=self.onClose)
        #self.ws.on_open=self.onOpen
        self.thread = Thread(target=self.start, args=())
        self.thread.start()

    def start(self):
        self.ws.run_forever(sslopt={"cert_reqs": ssl.CERT_NONE})

    def sendControlKey(self, keyCode):
        print("sending code "+keyCode)
        self.ws.send(json.dumps({
            "method": "ms.remote.control",
            "params": {
                "Cmd": "Click",
                "DataOfCmd": keyCode,
                "Option": "false",
                "TypeOfRemote": "SendRemoteKey"
            }
        }))
        time.sleep(0.1)

    def isConnected(self):
        return self.connected

    def onMessage(self, ws, message):
        print(message)

    def onError(self, ws, error):
        print("onError:"+str(error))
        print(error)

    def onClose(self, ws):
        print("### closed ###")

    def onOpen(self, ws):
        print("onOpen")
        self.connected = True

    def selectKodi(self):
        self.selectByIndex(2)
    def selectHomeTheater(self):
        self.selectByIndex(1)
    def selectPC(self):
        self.selectByIndex(0)
    
    def selectByIndex(self, idxFromRight=0):
        self.sendControlKey("KEY_SOURCE")
        self.sendControlKey("KEY_DOWN")
        self.sendControlKey("KEY_RIGHT")
        self.sendControlKey("KEY_RIGHT")
        self.sendControlKey("KEY_RIGHT")
        self.sendControlKey("KEY_RIGHT")
        self.sendControlKey("KEY_RIGHT")
        self.sendControlKey("KEY_RIGHT")
        self.sendControlKey("KEY_RIGHT")
        while idxFromRight>0:
            self.sendControlKey("KEY_LEFT")
            idxFromRight-=1
        self.sendControlKey("KEY_ENTER")


#tv = SamsungTV("10.20.0.222")
#time.sleep(3)
#while not tv.isConnected():
#    time.sleep(1)

#tv.selectKodi()

#while True:
#    time.sleep(1)
