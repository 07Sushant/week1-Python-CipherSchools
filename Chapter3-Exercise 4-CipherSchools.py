# calculate the sum of diditis in user input
number  = input("Enetr a number: ")
sum = 0
i = 0
while i < len(number):
    sum += int(number[i])
    i += 1
print(sum)