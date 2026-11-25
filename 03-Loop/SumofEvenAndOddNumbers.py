
# Sum of Even & Odd Numbers

number = int(input("Enter a number: "))
even = 0 
odd = 0 

for i in range(number):
    if (i+1) % 2 == 0:
        even += i+1
    else:
        odd += i+1

print(f"Even sum: {even}\nOdd sum: {odd}")