print("BankAccount")
class BankAccount:
    def __init__(self,owner,balance,):
        self.owner = owner
        self.__balance = balance
    def deposit(self,amount):
        self.__balance += amount
        print(f"Added ${amount} to {self.owner}'s Account")
    def withdraw(self,amount):
        if self.__balance < amount:
            print("Insufficient Balance.")
        else:
            self.__balance -= amount
            print(f"WithDrawed ${amount} from {self.owner}'s Account")
    def show_balance(self):
        print(f"Balance in {self.owner}'s Account is: ${self.__balance}")
    def transfer(self,account,amount):
        if amount > self.__balance:
            print("Insufficient Balance Cannot Transfer The Money")
        else:
            account.__balance += amount
            self.__balance -= amount
            print(f"${amount} Transferred To {account.owner} from {self.owner}")
class SavingsAccount(BankAccount):
    def __init__(self,owner,balance,interest_rate):
        super().__init__(owner,balance)
        self.interest_rate = interest_rate
    def add_interest(self):
        self.__balance += (self.__balance* (self.interest_rate/100))
        print(f"Calculated Interest for {self.owner} is {self.__balance}")
    def monthly_update(self):
        self.add_interest()
        self.show_balance()
    def withdraw(self, amount):
        if self.__balance - amount < 1000:
            print("Minimum Balance Required!")
        else:
            return super().withdraw(amount)
                    

class CurrentAccount(BankAccount):
    def __init__(self, owner, balance):
        super().__init__(owner, balance)
    def withdraw(self,amount):
        if self.__balance - amount >= -5000:
            self.__balance -= amount
            print(f"${amount} Withdrawed From Current Account of{self.owner}. Remaining Balance is {self.__balance}")
        else:
            print("Limit Exceeded Than -5000!")        
account1 = CurrentAccount("Rahul",5000)
account2 = SavingsAccount("Vijay",2000,5)
account1.withdraw(1000)
account2.withdraw(1000)
