class BankAccount:

    def __init__(self):
        self.accountNumber = 0
        self.name = "John Doe"
        self.balance = 0.0

    def Deposit(self, num):
        self.balance += num

    def Withdrawal(self, num):
        if self.balance > num or self.balance == num:
            self.balance -= num
        else:
            print("Insufficient Funds.")

    def bankFees(self):
        self.balance -= (self.balance*0.05)
    
    def display(self):
        print("Account Holder: ", self.name)
        print("Account Number: ", self.accountNumber)
        print("Balance: ", self.balance)

r = BankAccount()
r.Deposit(50)
r.Withdrawal(100) # should return Insufficient Funds
r.Withdrawal(50) # should drain account to zero
r.Deposit(50) # put account back at 50
r.bankFees()# balance = 47.5
r.display()

#heebee jeebies