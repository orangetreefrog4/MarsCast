## Made by Liam Owen
## for the hack club TerminalCraft event
## using NASA Mars weather API
## with <3.

# Gets the modules/libraries ready.
def prepModules() :
print('Loading...')
import os
import sys
from pathlib import Path

listOfSrc = list(Path(os.path.realpath(sys.path[0])).glob('**/*.py'))

for src in listOfSrc :
    parent_dir = os.path.abspath(os.path.dirname(src))
    vendor_dir = os.path.join(parent_dir, 'vendor')
    sys.path.append(vendor_dir)
    
import requests
import urllib3
import certifi
import chardet
import idna
from time import sleep 
    print('Done!')

running = 1

while running == 1 :
    weather = requests.get('https://api.nasa.gov/insight_weather/?api_key=DEMO_KEY&feedtype=json&ver=1.0')
    sleep(1)

print(weather)