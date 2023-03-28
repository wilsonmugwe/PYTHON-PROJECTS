class BankAccount:
    def deposit(self):
        print("Depositing")
    def withdraw(self):
        print("Withdrawing")

    def checkBalance(self):
        print("Checking")

    def transfer(self):
        print("Transferring")

class InterestAccount(BankAccount):
    def interest(self):
        print("checked")

    def deposit(self):
        print("deposited")

class ChargingAccount(InterestAccount):
    def fee(self):
        print("cost")

    def withdraw(self):
        print("withdraw")

a = BankAccount()
a.checkBalance()

b = InterestAccount()
b.interest()

c = ChargingAccount()
c.withdraw()