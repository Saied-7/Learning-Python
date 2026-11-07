#Character Checker

char = input("Enter a character: ")

if len(char) != 1 or not char.isalpha():
    print("Invalid character")
elif char.lower() in "aeiou":
    print("Vowel")
else:
    print("Consonant")