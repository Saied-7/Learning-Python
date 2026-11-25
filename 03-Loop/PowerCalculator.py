
# Power Calculator

Base = int(input("Enter Base: "))
Exponent = int(input("Enter Exponent"))
Output = 1

for i in range(Exponent):
    Output *= Base

print(f"OUTPUT: {Output}")