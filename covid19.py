'''
Modified: Awok ID
'''
# Import lib
import os, sys, json
from time import sleep
try:
  import requests
  from urllib import request
except ImportError:
  os.system("pip install --upgrade pip")
  os.system("pip install requests")
  os.system("pip install urllib")

# Url
url = "https://indonesia-covid-19.mathdro.id/api/provinsi"
url_open = request.urlopen(url)
data = json.loads(url_open.read())

# Looping
for korona in data['data']:
  print(f"[ {korona['provinsi']} ]")
  print(f"\033[1;33mPositif   > {korona['kasusPosi']}")
  print(f"\033[1;32mSembuh    > {korona['kasusSemb']}")
  print(f"\033[1;31mMeninggal > {korona['kasusMeni']}\n")
  sleep(1.0)
  print("\033[0m")
