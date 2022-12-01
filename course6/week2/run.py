#! /usr/bin/env python3

import os
import requests

path = "/data/feedback"

keys = ["title", "name", "date", "feedback"]

folder = os.listdir(path)
for file in folder:
    key_count = 0
    feedback = {}
    with open(path +"/"+ file) as txt:
        for line in txt:
            value = line.strip()
            feedback[keys[key_count]] = value
            key_count += 1
    response = requests.post("http://34.66.252.69/feedback/",json=feedback)
    if(response.status_code==201):
      print(file," feedback posted successfully!")

print("All feedbacks posted!")
