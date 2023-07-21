
# can you loop over this list and print "<hero name> is great!"
heroes= ["Batman","Spiderman","Catwoman","Alfred Pennyworth"]

# can you loop over this list of dictionaries are print: "<hero name>'s power is <power>"
hero_dict= [{"name": "Batman", "powers": "being the world's greatest detective"},
            {"name": "Spiderman", "powers": "web shooting"},
            {"name": "Catwoman", "powers": "burglary"},
            {"name": "Alfred Pennyworth", "powers": "being super butler"}
           ]
#for x in heroes:
   # print(x,"is great!")






for y in hero_dict:
    name = y["name"]
    print(name)
for v in hero_dict:
    powers = v["powers"]
    print(f"{name} powers is {powers}")
