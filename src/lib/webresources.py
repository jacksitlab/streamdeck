
import urllib3
import shutil

class WebResources:

    def __init__(self):
        self.http = urllib3.PoolManager()

    def download(self, url, dstFilename):
        with self.http.request('GET', url, preload_content=False) as r, open(dstFilename, 'wb') as out_file:
            shutil.copyfileobj(r, out_file)
