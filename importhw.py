#!/usr/bin/env python 3

import random

z = [1, 2, 3, 4, 5, 6]

x= random.randint(1,7)
a= random.choice(z)
   
print(f"{x},{a}which is the winner")
if x > a:
    print(f"the winner is {x}")
elif x < a:
    print(f"the winner is {a}")

    
