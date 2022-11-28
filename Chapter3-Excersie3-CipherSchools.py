# Sum of n natural number using while loop
x = int(input("Enter the range:"))
sum = 0
i = 1
while i <= x:
    sum += i
    i += 1
print(sum)