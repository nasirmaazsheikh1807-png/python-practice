class BankAccount:

#     @staticmethod
#     def bank_name():
#         print("ABC Bank")
# BankAccount.bank_name()
    bank_name = "ABC Bank"
    @classmethod
    def show_bank(cls):
        print(cls.bank_name)
BankAccount.show_bank()
