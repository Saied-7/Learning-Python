#Find the Largest of Three Numbers
x = int(input("Enter your marks: "))

if 80 <= x and x <= 100:
    print("A+")
elif 70 <= x < 80:
    print("A")
elif 60 <= x < 70:
    print("A-")
elif 50 <= x < 60:
    print("B")
elif 40 <= x < 50:
    print("C")
elif 0 <= x < 40:
    print("F")
else:
    print("Invalid marks.")