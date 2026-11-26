
# Take a string and a character from the user
s = input("Enter a string: ").lower()
ch = input("Enter a character: ").lower()
fre = 0

for i in s:
    if i == ch:
        fre += 1

print(f"The frequency of {ch} is: {fre}")