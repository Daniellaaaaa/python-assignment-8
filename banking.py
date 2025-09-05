class BankAccount:
    def __init__(self, name, balance):
        self.name=name
        self.balance=balance

    def deposit(self, amount):
        self.balance=self.balance+amount
        return f"500 was deposited, New balance: {self.balance}"
    def withdraw(self, amount):
        if self.balance>= amount:
            self.balance=self.balance-amount
            return f"200 withdrawn successfully, Remaining balance: {self.balance}"
        else:
            return "Insufficient balance"   

    def get_balance(self):
        return self.balance

acc = BankAccount("Alice", 1000) 
print(acc.deposit(500))
print(acc.withdraw(200))
print(acc.get_balance()) 