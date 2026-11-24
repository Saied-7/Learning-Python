# Sum of Digits

num = int(input("Enter a number: "))
total = 0

while num != 0:
    total += num % 10 # sum of last digits
    num = num // 10 # update number 

print(total)