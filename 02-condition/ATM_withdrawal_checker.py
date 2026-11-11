#ATM Withdrawal Checker

balance = float(input("Enter your account balance "))
withdramo = int(input("Enter your withdrawal amount "))

if withdramo <= balance and (withdramo % 500) == 0 and withdramo > 0:
    remaining = balance - withdramo
    print(f"Withdrawal successful!\nRemaining balance: Tk {remaining:.2f}")
else:
    print("Withdrawal not allowed!")