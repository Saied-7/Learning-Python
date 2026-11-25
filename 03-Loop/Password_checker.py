# Password checker

user_password = input("Enter your password: ")
correct_password = "python123"


while correct_password != user_password:
    user_password = input("Enter your password: ")

print("Login successful")