import sys
from os import path
sys.path.append(path.dirname(path.dirname(path.abspath(__file__))))

from src.lib.webresources import WebResources


res = WebResources()

res.download('https://worldvectorlogo.com/download/nintendo-switch.svg','src/assets/switch.svg')
res.download('https://upload.wikimedia.org/wikipedia/de/7/7c/Foobar2000_Icon.svg','src/assets/foobar2000.svg')
res.download('https://upload.wikimedia.org/wikipedia/commons/4/4c/Antu_kodi.svg','src/assets/kodi.svg')

