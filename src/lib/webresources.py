
import urllib3
import shutil
import sys
import subprocess

class WebResources:

    def __init__(self):
        self.http = urllib3.PoolManager()

    def download(self, url, dstFilename):
        with self.http.request('GET', url, preload_content=False) as r, open(dstFilename, 'wb') as out_file:
            shutil.copyfileobj(r, out_file)

    def svg2png(self, svgFilename, pngFilename, size=(72,72)):
        execCommand = "inkscape --without-gui "+svgFilename+" -w "+str(size[0])+" -h "+str(size[1])+" --export-png="+pngFilename
        self.execute(execCommand)

    def execute(self, command):
        output = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE).stdout.read()
        return output