#!/usr/bin/env python3

import json
import yaml
file_1 = "favs.json"
file_2 = "favs.yaml"

with open(file_1,"r") as file:
    data_object = json.load(file)

new_dict= {
        "name": "Salvo",
        "movie": "Lilo and Stitch",
        "ice cream": "Rocky Road",
        "color": "Forest Green"
          }

data_object.append(new_dict)

for data in data_object:
    print("Name:", data["name"])
    print("Movie:", data["movie"])
    print("Ice cream:", data["ice cream"])
    print("Color:", data["color"])

with open (file_2,"w") as favs:
    yaml.dump(data_object, favs)
