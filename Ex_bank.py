print("Example Bank for understanding the abstractmethod")
from abc import ABC , abstractmethod

class BankAccount(ABC):
    @abstractmethod
    def withdraw(self,amount):
        pass
class SavingsAccount(BankAccount):
    def withdraw(self, amount):
        print(f"Withdrawing {amount} from savings Account ")
account = SavingsAccount()
account.withdraw(1000)