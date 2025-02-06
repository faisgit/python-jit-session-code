class Account:
    def __init__(self, account_number, balance):
        self.account_number = account_number
        self.balance = balance
    
    def get_balance(self):
        return self.balance
    
    def deposit(self, amount):
        self.balance = self.balance + amount
        print(f"Deposited {amount}. New Balance: {self.balance}")
    def withdraw(self, amount):
        if amount <=self.balance:
            self.balance = self.balance - amount
            print(f"Withdraw {amount} New Balance : {self.balance}")
        else:
            print("Insufficient Balance")

# account = Account('12345678', 2000)
# print(account.get_balance())
piyush = Account('200000000000000000000',500000)
print(piyush.get_balance())
piyush.deposit(10000)