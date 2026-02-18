from atm_utils import withdraw

try:
    balance = int(input("Enter balance: "))
    amount = int(input("Enter withdrawal amount: "))

    updated_balance = withdraw(balance, amount)
    print("Withdrawal successful!")
    print("Updated Balance:", updated_balance)

except TypeError as e:
    print("Type Error:", e)

except ValueError as e:
    print("Value Error:", e)

except Exception as e:
    print("Unexpected Error:", e)
