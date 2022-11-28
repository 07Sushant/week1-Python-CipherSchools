# #  WATCH COCO
# #  ASk user name and age 
# #  if user name start with ('a' or 'A') and aahe is above 10 the 
# print("You are eligible")
# Else sorry

user_name = input("Enter your name: ")
age = int(input("Enter your age: "))
if age >= 10 and (user_name[0]=='a' or user_name[0] == 'A'):
    print("You are eligible")
else:
    print("You cannot watch")
