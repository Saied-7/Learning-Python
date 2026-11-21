
def input_number():
    # checking the number is positive or not 
    while True:
        n = int(input("Enter a number: "))
        if n > 0: 
            break
    return n

def print_meaw(n):
    # printing meaw n times 
    for _ in range(n):
        print("meaw")     


def main():
    # getting the input from user 
    n = input_number()
    # printing meaw n times
    print_meaw(n)

main()