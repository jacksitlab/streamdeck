import urllib3


class BaseHttpClient:

    def __init__(self, host):
        self.host = host

    def __init__(self, host):
        self.host = host
        self.http = urllib3.PoolManager()

    def sendGetCommand(self, uri):
        print('sending get command '+uri)
        resp = self.http.request('GET', self.host+uri)
        print(resp.status)
        return resp.data.decode('utf-8') if resp.status == 200 else None
