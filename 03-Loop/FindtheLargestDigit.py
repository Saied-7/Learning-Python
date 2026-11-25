
# Find the Largest Digit

number = int(input("Enter a number: "))
dig = 0

for i in range(len(str(number))):
    digit = number % 10

    if digit > dig:
        dig = digit

    number //= 10

print(f"Output: {dig}")