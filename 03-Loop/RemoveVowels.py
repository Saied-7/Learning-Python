
# Remove Vowels

s = input("Enter a string: ")
p = ""

for i in s:
    if i  not in ("aeiou"): # remove vowels
        p += i


print(p)