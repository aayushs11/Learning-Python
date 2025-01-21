class BankAccount():
    def __init__(self,name,balance=0.00):
        self.name= name
        self.balance= balance
    
    def diposit(self,amount):
        if amount>0:
            self.balance +=amount
            print(f"Rs {amount:.2f} Deposit Sucessful to {self.name}'s account.")
        else:
            print('Deposit Unsucessfull. Please Try Again.')
        
    def withdraw(self,amount):
        if 0 < amount <= self.balance:
            self.balance -=amount
            print(f"Rs {amount:.2f} withdraw sucessful from {self.name}'s account")
        else:
            print('Amount withdraw unsuccessful! Please Try Again.')

    def get_balance(self):
        print(f"The balance of {self.name}'s is Rs {self.balance:.2f}")

account= BankAccount('Aayush')
account.diposit(1000.95)
account.withdraw(500.99)
account.get_balance()