#!/usr/bin/env python3
import requests
import pprint


print("Antlion", "Behemoth", "Chocobo")
monstertolookup = input ("Pick between the monsters above to search for attack and description:")

URL= "https://www.moogleapi.com/api/v1/monsters/search?name=" + monstertolookup

information = requests.get(URL).json()



for each_monster_dict in information:
    violence = each_monster_dict["attack"]
    desc = each_monster_dict["description"]
   # print(each_monster_dict["attack"],each_monster_dict["description"])
    print(f"the attack value is: {violence}\nits description is: {desc}\n")

   # print(each_monster_dict)


