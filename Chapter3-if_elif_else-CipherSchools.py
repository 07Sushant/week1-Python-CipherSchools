# # if elif else statement

# show ticket Pricing
# 1 to 3 (Free)
# 4 to 10 (150)
# 11 to 60 (250)
# avobe 60 (200)


age = int(input("Please enter your age :"))
if age == 0 or age < 0:
    print("You cannot watch")
elif 0<age<=3:
    print("Ticket are Free")
elif 3<age<=10:
    print("Ticket price: 150")
elif 10<age<=60:
    print("Ticket price: 250")
else:
    print("Ticket price: 200")
