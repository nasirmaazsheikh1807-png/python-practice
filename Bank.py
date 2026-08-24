print("BankAccount")
class BankAccount:
    def __init__(self,owner,account_no,balance):
        self.account_no = account_no
        self.owner = owner
        self.__balance = balance
    def __str__(self):
        return f"Owner: {self.owner}, Account No: {self.account_no}"
    def get_balance(self):
        return self.__balance
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
            account._BankAccount__balance += amount
            self._BankAccount__balance -= amount
            print(f"${amount} Transferred To {account.owner} from {self.owner}")
class SavingsAccount(BankAccount):
    def __init__(self,owner,account_no,balance,interest_rate):
        super().__init__(owner,account_no,balance)
        self.interest_rate = interest_rate
    def add_interest(self):
        interest_rate = (self.get_balance()* (self.interest_rate/100))
        self._BankAccount__balance += interest_rate
        print(f"Calculated Interest for {self.owner} is {interest_rate}")
    def monthly_update(self):
        self.add_interest()
        self.show_balance()
    def withdraw(self, amount):
        if self.get_balance() - amount < 1000:
            print("Minimum Balance Required!")
        else:
            return super().withdraw(amount)
                    

class CurrentAccount(BankAccount):
    def __init__(self, owner,account_no, balance):
        super().__init__(owner,account_no, balance)
    def withdraw(self,amount):
        if self.__balance - amount >= -5000:
            self.__balance -= amount
            print(f"${amount} Withdrawed From Current Account of{self.owner}. Remaining Balance is {self.__balance}")
        else:
            print("Limit Exceeded Than -5000!")        
class Bank:
    def __init__(self):
        self.accounts = []
    def add_account(self,account):
        if self.find_account(account.owner):
            print("Account Already Exists")
        else:    
            self.accounts.append(account)
            print(f"Account Added: {account.owner}")
    def show_all_accounts(self):
        for account in self.accounts:
            account.show_balance()
    def find_account(self,owner):
        for account in self.accounts:
            if account.owner == owner:
                return account
    def find_account_by_no(self,account_no):
        for account in self.accounts:
            if account.account_no == account_no:
                return account
    def deposit(self,owner,amount):
        account = self.find_account(owner)
        if account:
            account.deposit(amount)
        else:
            print("Account Not Found")
    def withdraw(self,owner,amount):
            account = self.find_account(owner)
            if account:
                account.withdraw(amount)
            else:
                print("Account Not Found")
    
account1 = BankAccount("Rahul","AC001",10000)
account2 = SavingsAccount("Aman","AC002",10000,5)
bank = Bank()
bank.add_account(account2)
bank.add_account(account1)
account = bank.find_account_by_no("AC002")
account.show_balance()
print(account)

