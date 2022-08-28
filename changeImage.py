#!/usr/bin/env python3
from PIL import Image
import os

path = os.getcwd() + "/supplier-data/images"
for file in os.listdir(path):
  if file == "README" or file == "LICENSE":
    continue
  outfile = os.path.splitext(file)[0] + ".jpeg"
  with Image.open(os.path.join(path, file)) as im:
    im.convert("RGB").resize((600, 400)).save(os.path.join(path, outfile))
