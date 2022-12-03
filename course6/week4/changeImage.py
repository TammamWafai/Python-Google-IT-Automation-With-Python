#!/usr/bin/env python3

import os
from PIL import Image

path = 'supplier-data/images/'

for file in os.listdir(path):
    if '.tiff' in file:
        img = Image.open(path + file).convert("RGB")
        dir, filename = os.path.split(file)
        filename = os.path.splitext(filename)[0]  #filename without .tiff
        img.resize((600, 400)).save(path + filename + '.jpeg' , 'jpeg')
