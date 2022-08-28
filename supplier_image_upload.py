#!/usr/bin/env python3
import requests, os

url = "http://localhost/upload/"
path = os.getcwd() + "/supplier-data/images"
for file in os.listdir(path):
  if file == "README" or file == "LICENSE":
    continue
  with open(os.path.join(path, file), 'rb') as opened:
    r = requests.post(url, files={'file': opened})
  