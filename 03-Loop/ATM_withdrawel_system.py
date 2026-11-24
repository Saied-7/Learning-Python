# ATM Withdrawal System

balance = 5000
user_withdraw = int(input("Enter a wirhdrawal amount: "))

while user_withdraw != 0:
    if balance < user_withdraw:
        print("Insufficient balance")
    elif balance >= user_withdraw:
        balance -= user_withdraw
        print(f"Withdraw: {user_withdraw} \nRemaining balance: {balance}")
    user_withdraw = int(input("Enter a wirhdrawal amount: "))

print(f"ATM session endedn \nBalance: {balance}")