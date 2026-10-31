#Find the Largest of Three Numbers

a = int(input("Enter the first number: "))
b = int(input("Enter the second number: "))
c = int(input("Enter the third number: "))

if a >= b and a >= c:
   print(f"{a} largest")
elif b >= a and b >= c:
    print(f"{b} largest")
else:
    print(f"{c} largest")