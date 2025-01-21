class account():
    def __init__(self,name,number,balance=0.00):
        self.name= name
        self.number= number
        self.balance= balance
    
    def deposit(self,amount):
        if amount>0:
            self.balance += amount
            print(f"Rs {amount:.2f} has been deposited sucessfully in {self.name}'s account.")
        else:
            print('Deposit Fail! Please Try Again')
    
    def withdraw(self,amount):
        if 0 < amount <= self.balance:
            self.balance -= amount
            print(f"Rs {amount:.2f} has been withdrawn sucessfully from {self.name}'s account.")
        else:
            print('Withdraw Failed! Insufficient Balance')

    def get_balance(self):
        print(f"Dear {self.name} your balance is Rs {self.balance:.2f} in your account")

aayush= account('Aayush',9810000000)
aayush.deposit(5000.85)
aayush.withdraw(999.99)
aayush.get_balance()

print()

a1= account('RAJA',9876543210)
a1.deposit(10000)
a1.withdraw(5000.99)
a1.get_balance()