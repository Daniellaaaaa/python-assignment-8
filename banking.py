class BankAccount:
    def __init__(self, name, balance):
        self.name=name
        self.balance=balance
        self.history={}

    def deposit(self, amount):
        self.balance=self.balance+amount
        self.history["deposit"]=amount
        return f"{amount} was deposited in {self.name} account, New balance: {self.balance}"
    
    def withdraw(self, amount):
        if self.balance>= amount:
            self.balance=self.balance-amount
            self.history["withdraw"]=amount
            return f"200 withdrawn successfully, Remaining balance: {self.balance}"
        else:
            return "Insufficient balance"   

    def get_balance(self):
        return f"{self.name} balance is {self.balance}"
    
    def get_tx_history(self):
        if len(self.history)>0:
            return f"Transaction history: {self.history}"
        else:
            return "No transaction made yet"
        
    def transfer(self, amount, acc2):
        if self.balance >= amount:
            self.balance-=amount
            acc2.deposit(200)
            self.history["transfer"]=amount
            return f"Transfer of {amount} was successful"
        else:
            return f"Insufficient balance"



acc = BankAccount("Alice", 1000)
acc2 = BankAccount("John", 100)
print(acc.deposit(500))
print(acc.withdraw(200))
print(acc.get_balance()) 
#print(acc.get_tx_history())

print(acc.transfer(200, acc2))
#print(acc2.deposit(200))
print(acc2.get_balance())

#print(acc.get_balance()) 
print(acc.get_tx_history())