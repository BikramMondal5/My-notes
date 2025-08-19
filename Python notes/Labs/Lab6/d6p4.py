class BankAccount:
    def __init__(self, balance=0):
        self.__balance = balance   # private variable

    def deposit(self, amount):
        self.__balance += amount

    def get_balance(self):
        return self.__balance

    def withdraw_balance(self, amount):
        if amount <= self.__balance:
            self.__balance -= amount
        else:
            print("❌ Error: Insufficient balance")

# Usage
acc = BankAccount(1000)
acc.deposit(500)
print(acc.get_balance())  # 1500
acc.withdraw_balance(2000)  # Error
