import sys
from os import path
sys.path.append(path.dirname(path.dirname(path.abspath(__file__))))

from src.lib.denonClient import DenonClient,DenonSource

denon = DenonClient('http://10.20.0.221')
denon.setSource(DenonSource.CBLSAT)
#denon.volumeUp(10)
#denon.volumeDown(10)

#print(denon.readStatus())

#denon.setVolume(-30)