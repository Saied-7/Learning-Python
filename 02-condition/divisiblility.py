#Divisibility Checker
x = int(input("Enter a number: "))

if x % 3 == 0 and x % 5 == 0:
    print("Divisible by both 3 and 5")
else:
    print("Not Divisible by both 3 and 5")