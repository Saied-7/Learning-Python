
# Vowel Counter 

s = input("Enter a string: ").lower()
count = 0

for i in s:
    if i in ("aeiou"):
        count += 1

print(f"Output: {count}")