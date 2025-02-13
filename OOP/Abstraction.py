# Abstraction => Hiding the implementation details and showing only the functionality to the user.


class Account:
    def __init__(self,bal,acc_no):
        self.balance=bal
        self.acc_no=acc_no


    def debit(self,amount):
            amount=int(amount)
            if amount>self.balance:
                print('Insufficient balance')
                return 0
            else:
                self.balance-=amount
                print('MRP', amount ,'debited successfully')


    def credit(self,amount):
            amount=int(amount)
            if amount<=0:
                print('Invalid amount')
                return 0
            else:
                self.balance+=amount
                print('MRP', amount ,'credited successfully')


user1=Account(1000,5812)
print("your account balance is :",user1.balance)

account_number= input("Enter your accoutn number:")
account_number=int(account_number)
if account_number==user1.acc_no:
    print('Account number matched')
    amount=input('Enter the amount you want to debit : ')
    user1.debit(amount)
    print("your account balance is :",user1.balance)
    amount=input('Enter the amount you want to credit : ')
    user1.credit(amount)
    print("your account balance is :",user1.balance)


else:
    print('Account number not matched')
    print('Please enter the correct account number')
    print('Thank you')