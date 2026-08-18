print("BankAccount")
class BankAccount:
    def __init__(self,owner,balance,):
        self.owner = owner
        self.balance = balance
    def deposit(self,amount):
        self.balance += amount
        print(f"Added ${amount} to {self.owner}'s Account")
    def withdraw(self,amount):
        if self.balance < amount:
            print("Insufficient Balance.")
        else:
            self.balance -= amount
            print(f"WithDrawed ${amount} from {self.owner}'s Account")
    def show_balance(self):
        print(f"Balance in {self.owner}'s Account is: ${self.balance}")
    def transfer(self,account,amount):
        if amount > self.balance:
            print("Insufficient Balance Cannot Transfer The Money")
        else:
            account.balance += amount
            self.balance -= amount
            print(f"${amount} Transferred To {account.owner} from {self.owner}")
class SavingsAccount(BankAccount):
    def __init__(self,owner,balance,interest_rate):
        self.owner = owner
        self.balance = balance
        self.interest_rate = interest_rate
    def add_interest(self):
        self.balance += (self.balance* (self.interest_rate/100))
        print(f"Calculated Interest for {self.owner} is {self.balance}")
    def monthly_update(self):
        self.add_interest()
        self.show_balance()
        


account1 = SavingsAccount("Rahul",10000,5)
account2 = BankAccount("Aman",3000)
account1.monthly_update()