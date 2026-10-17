#Swap Two Variables

x = int(input("Enter x:"))
y = int(input("Enter y:"))

print(f"Before: x = {x} , y = {y}")

temp = x
x = y
y = temp

print(f"After : x = {x}, y = {y}")
