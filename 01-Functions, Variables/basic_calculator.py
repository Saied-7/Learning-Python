
# Basic Calculator

x = float(input("What is x: "))
y = float(input("What is y: "))

add = x + y
sub = x - y
mul = x * y
div = x / y

#:.2f means displaying two digits after the decimel point
print(
    f"Addition: {add}\n"
    f"Subtraction: {sub:.2f}\n"
    f"Multiplication: {mul:.2f}\n"
    f"Division: {div:.2f}"
)
