import sys
import os
import re
from .webresources import WebResources
from PIL import Image

class ImageCache:

    def __init__(self, folder, convertSvgs=False, dstSize=(72,72)):
        self.baseFolder = folder
        self.convertSvgs = convertSvgs
        self.dstSize = dstSize
        self.res = WebResources()
        if not os.path.exists(self.baseFolder):
            os.makedirs(self.baseFolder)

    def clear(self):
        for root, dirs, files in os.walk(self.baseFolder):
            for file in files:
                os.remove(os.path.join(root, file))

    def get(self, filenameOrUrl):
        if filenameOrUrl.startswith("http"):
            return self.download(filenameOrUrl)
        else:
            return self.load(filenameOrUrl)

    def load(self, filename, interal=False):
        if not interal:
            filename = self.baseFolder+"/"+filename
        
        if not os.path.isfile(filename):
            raise Exception("unable to find file "+filename)
  
        return Image.open(filename)

    def convertToPng(self, src, dst, size):
        self.res.svg2png(src, dst, size)

    def download(self, url, dstFilename=None):
        if dstFilename is None:
            regex = r'\/([^\/]+)$'
            match = re.findall(regex, url, re.M|re.I)
            if len(match)>0:
                dstFilename = match[0]
            else:
                print("no match")
        if dstFilename is None:
            raise Exception("unable to detect dst filename out of url")
        dstPath=self.baseFolder+"/"+dstFilename
        if not os.path.isfile(dstPath):
            self.res.download(url,dstPath)
        
        if self.convertSvgs and dstPath.endswith('.svg'):
            print("have to convert svg to png")
            dstPathPng = dstPath[:len(dstPath)-4]+".png"
            if not os.path.isfile(dstPathPng):
                self.convertToPng(dstPath,dstPathPng, self.dstSize)
            dstPath = dstPathPng
        return self.load(dstPath, True)


        
