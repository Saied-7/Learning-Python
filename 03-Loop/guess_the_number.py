# Guess the number 

num = int(input("Guess A Number: "))
correct = 223

while num != correct:
    if num < correct:
        print("Too Low")
    elif num > correct:
        print("Too high")
    num = int(input("Guess A Number: "))

print("Correct!")