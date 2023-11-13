#  Lucky Number with the 3 tries
# 1 to 10

import random

lucky_no=random.randint(1,10)
guess_no=None
while guess_no != lucky_no:
    guess_no=int(input("enter no from 1 to 10"))
    if guess_no<lucky_no:
        print("too low")
    elif guess_no>lucky_no:
        print("too high")
print("found the lucky no:"+ str(lucky_no))
