#!/usr/bin/env python3
import requests, os

url = "http://localhost/fruits/"
path = os.getcwd() + "/supplier_data/descriptions"
fruit = {}
for file in os.listdir(path):
  with open(os.path.join(path, file), 'r') as opened:
    f = opened.readlines()
    fruit['name'] = f[0].rstrip("\n")
    weight = f[1].rstrip("\n")
    fruit['weight'] = int(weight[:len(weight)-4])
    fruit['description'] = f[2].rstrip("\n")
    fruit['image_name'] = file[:len(file)-4] + ".jpeg"
    r = requests.post(url, json=fruit)

    if r.ok:
      print("Fruit successfully uploaded")