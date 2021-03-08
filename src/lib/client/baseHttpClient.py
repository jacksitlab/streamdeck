import urllib3


class BaseHttpClient:

    def __init__(self, url):
        self.baseUrl = url
        self.http = urllib3.PoolManager()

    def sendGetCommand(self, uri):
        print('sending get command '+uri)
        resp = self.http.request('GET', self.baseUrl+uri)
        print(resp.status)
        return resp.data.decode('utf-8') if resp.status == 200 else None
