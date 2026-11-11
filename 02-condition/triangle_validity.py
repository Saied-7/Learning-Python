#Triangle Validity

a = int(input("Enter the first side of a triangle: "))
b = int(input("Enter the second side of a triangle: "))
c = int(input("Enter the third side of a triangle: "))

if a > 0 and b > 0 and c > 0 and a+b > c and b+c > a and c+a > b:
    print("Triangle is valid")
else:
    print("Triangle is not valid")