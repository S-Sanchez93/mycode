#!/usr/bin/env python3
print("I see you chose to accept the invitation, welcome to our illustrious city, the city of the nine. Now, despite being acknowledged as worthy of being one of its citizens, you must fill out a brief questionaire, to see which part of the city you will...belong to")

poors= 0
richies= 0

print("While enjoying a morning refreshment, you notice a rival aristocrat walking past you, how do you act?")
print("A. Challenge them to a duel\nB. Assassinate them")

answer= input(">").lower()

if answer == "a":
    poors += 1

else:
    richies += 1

print(poors)
print(richies)
