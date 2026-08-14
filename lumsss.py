class BankAccount:
    total_accounts = 0

    def __init__(self, name, balance):
        self.name = name
        self.__balance = balance
        BankAccount.total_accounts += 1

    @property
    def balance(self):
        return self.__balance
    def deposit(self, amount):
        self.__balance += amount
        print("Deposit successful!")
    def withdraw(self, amount):
        if amount <= self.__balance:
            self.__balance -= amount
            print("Withdrawal successful!")
        else:
            print("Not enough balance!")

account = BankAccount("Ana", 5000)
print(f"Name: {account.name}")
print(f"Balance: {account.balance}")

account.deposit(1000)
account.withdraw(500)
print(f"New Balance: {account.balance}")
print(f"Total Accounts: {BankAccount.total_accounts}")