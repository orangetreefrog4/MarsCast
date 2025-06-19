## Made by Liam Owen
## for the hack club TerminalCraft event
## using NASA Mars weather API
## with <3.

from . import requests

weather = requests.get('https://api.nasa.gov/insight_weather/?api_key=DEMO_KEY&feedtype=json&ver=1.0')

print(weather.text)