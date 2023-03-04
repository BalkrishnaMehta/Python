class bank_account:
    def __init__(self,account_number,owner_name,account_balance):
        self.acc_number = account_number
        self.name = owner_name
        self.acc_balance = account_balance
    def deposit(self,amount):
        self.acc_balance += amount
        print("successfully credited: ",amount)
        print("Balance after Deposit: ",self.acc_balance,"\n\n")

    def withdraw(self,amount):
        if(amount <= self.acc_balance):
            print("successfully debited: ",amount)
            self.acc_balance -= amount
            print("Balance after Withdrwal: ",self.acc_balance,"\n\n")
        else:
            print("Sorry Insufficient Balance. ","\n\n")

    def display(self):
        print("Owner Name: ",self.name)
        print("Account Number: ",self.acc_number)
        print("Account Balance: ",self.acc_balance,"\n\n")

acc_no=int(input("Enter you Account Number: "))
owner_name=input("Enter account holder's Name: ")
acc_balance=int(input("Enter Intitial account Balance: "))
obj=bank_account(acc_no,owner_name,acc_balance)
opt="hello"
while(opt!="exit"):
    opt=input("What you have to do deposit, withdraw or account_status or exit: ")
    if(opt=="deposit"):
        amount=int(input("Enter Amount You want to deposit and give it to cashier 😊: "))
        obj.deposit(amount)
    if(opt=="withdraw"):
        amt=int(input("Enter Amount You want to Withdraw and Collect your Money 😊: "))
        obj.withdraw(amt)
    if(opt=="account_status"):
        obj.display()

