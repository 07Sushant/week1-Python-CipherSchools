#  ask a user for name 
# Example - Sushant Kumar
# print count of each word 
# output:
#  S:1
#  U:2
#  S:3
#  H:4
#  A:5
#  N:6
#  T:7

# Using count through while loop

name = input("Please enetr your name: ")
x = ""
i = 0
while i < len(name):
    if name[i] not in x:
        x += name[i]
        print(f"{name[i]} : {name.count(name[i])}")
    i += 1
