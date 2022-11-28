# Take 2 user input and print the length nad count a specfic character 
name, char = input("Enter Name and Charater seperated with commas: ").split(",")
print(f"The Length of your name is {len(name)}")
print(f"Charater count: {name.lower().count(char.lower())}")  #case sensitive

# H-h complex to lowercase
# name.lower().count(char.lower)

# To remove spaces use replace
# print(name.replce(" ","")+ dots)

string = "She is beautiful and she is good de=ancer"
print(string.replace("", "_"))