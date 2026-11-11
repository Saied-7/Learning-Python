#Electricity Bill Calculator

unit = float(input("Enter your using units: "))

if unit <= 100:
    print(f"{unit} unit costs {unit*5}")
elif unit <= 200:
    print(f"{unit} unit costs {(unit-100)*7 + (100*5)}")
else:
    print(f"{unit} unit costs {(100*5) + (100*7) + (unit-200)*10}" ) 