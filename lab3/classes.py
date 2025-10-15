class Account:
    def __init__(self, owner, balance):
        self.owner = owner
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        print(f"Deposit of {amount} accepted. New balance: {self.balance}")

    def withdraw(self, amount):
        if amount > self.balance:
            print("Funds Unavailable!")
        else:
            self.balance -= amount
            print(f"Withdrawal of {amount} accepted. New balance: {self.balance}")
