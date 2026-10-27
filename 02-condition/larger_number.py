#Find the Larger Number
a = int(input("Enter the first number:"))
b = int(input("Enter the second number:"))

if a > b :
    print(f"{a} is largest")
elif a == b:
    print("Equal")
else:
    print(f"{b} is largest")