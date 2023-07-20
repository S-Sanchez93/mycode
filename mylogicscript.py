#!/usr/bin/env python3
print("I see you chose to accept the invitation, welcome to our illustrious city, the city of the nine. Now, despite being acknowledged as worthy of being one of its citizens, that acknowledgement only goes towards your skills not you character, you must answer a brief series of questions, to see which part of the city you will...belong to.")


print("While enjoying a morning refreshment, you notice a aristocrat from another territory walking past you, how do you act?" )

print("A.challenge them to a duel.\nB.assassinate them.")

answer= input(">").lower()

if answer == "a":
   a= "The proper way we do things here."

else:
   a= "Is that how they do things in the west? cowards arent welcome."
   
print(a)

print("Next question,You find a wounded sliver dog in the street,how do you respond?")
print("A.carry it to a church of the furred marty.")
print("B.draw your own blood and gift it freely to its narrow maw.")
print("C.Ignore it, they unsettle you with all their eyes.")

answer= input(">").lower()

if answer == "a":
    b= "Kindness. What she asks of all her followers, loyalty's worth more then gold."

elif answer == "b":
    b= "sacrifice for the sake of others,seldom rewarded but remembered certainly."

else:
    b= "Its eyes scare you? Theirs worse things in the city then dogs with a few too many eyes."

print(b)

print("third question, which do you prefer to use in conflict")
print("A. diplomacy")
print("B. spearsaber")
print("C. fire")
print("D. my hands")

answer= input(">").lower()

if answer == "a":
    d= "the most dangerous weapon"

elif answer == "b":
    d="flexible range, and durable. Used by those best described as adaptable."

elif answer == "c":
    d= "Are you a burner? For the record the city is mostly fireproof, so dont worry about destroying the place if you get into a fight."

else:
    d= "a brawler, well you wont find the city lacking for those to test yourself against."

print(d)

print("im starting to see you for who you are, a one more question")

print("why did you accept the invitation, what is your reason for wanting to be a part of this city")

print("A.for wealth")
print("B.for knowledge")
print("C.for revenge")
print("D.For the prophecy")

answer= input(">").lower()

if answer == "a":
    d= "theirs plenty of entrepeneurs here, I mean con men. tomato, tomaato"
 
    
elif answer == "b":
    d= "the library in the main district has information on anything you want, you just have to find it in those labrynthine shelves"

    
elif answer == "c":
    d= "if I had a piece for every individual who came here seeking revenge on someone who wronged them, id be rich"


else:
    d= "many nowadays are born the seventh child of a seventh daugther, and many die trying to fulfill that destiny"

print(d)

print("Alright, we're done, now go on ahead down the main road till you get to the central tower and they'll decide which territory you belong to.")

print("Me, oh I dont decide, im just the gate guard.")
print("   ")
print("Look, if you had been doing this job for a few hundred years youd look for ways to kill time.")
print("   ")
print("I dont want to talk about how I ended up in this job, go to the tower and try not to die while your here.")

print("A.why")

answer= input(">").lower()
why = 0
while why < 3:
    print("I dont want to talk about it")
    why = why + 1
print("Your annoying me, look, I pissed off the wrong person and this was the result,now go.")
    






