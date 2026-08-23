class BankAccount:

#     @staticmethod
#     def bank_name():
#         print("ABC Bank")
# BankAccount.bank_name()
#     bank_name = "ABC Bank"
#     @classmethod
#     def show_bank(this):
#         print(this.bank_name)
# BankAccount.show_bank()

# Property Decorator.
    def __init__(self,owner,balance):
        self.owner = owner
        self.balance = balance
    # @property
    # def balance(self):
    #     return self.__balance
    # @balance.setter
    # def balance(self, value):
    #     if value < 0:
    #         print("Balance cannot be negative.")
    #     else:
    #         self.__balance = value
    def __str__(self):
        return f"{self.owner}'s Account - Balance ${self.balance}"

account = BankAccount("Rahul",5000)
print(account)

    


        
