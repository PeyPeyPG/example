#new CLASS Bank being made
class Bank:
    #CONSTRUCTOR for class being made
    def __init__(self, user, starting_amount):
        self.user_name = user
        self.balance = starting_amount

    #FUNCTION to add money to the account referenced
    def addMoney(self, amount_to_add):
        self.balance += amount_to_add
        print("added " + str(amount_to_add) + " to " + self.user_name + "'s account")

    #FUNCTION to add withdraw from the account referenced
    def withdrawMoney(self, amount_to_take):
        self.balance -= amount_to_take
        print("withdrew " + str(amount_to_take) + " from " + self.user_name + "'s account")

    #FUNCTION to check balance
    def checkBalance(self):
        print("your balance is " + str(self.balance))

#Tommy decided to open a new bank account and the bank saved it to a VARIABLE named Tommys_Bank_Account
#The new Bank account is made using the CONSTRUCTOR (__init__(user, starting_amount))
Tommys_Bank_Account = Bank("Tommy", 2000)

#Tommy's bank used a FUNCTION (withdrawMoney(amount_to_take) to add $300 to his acount
#this FUNCTION is called on the VARIABLE (Tommys_Bank_Account) of Tommy's Acount
Tommys_Bank_Account.addMoney(300)

#Tommy needs to pay for gas and uses a FUNCTION (withdrawMoney(amount_to_take)) to withdraw $500 from his account
#this FUNCTION is called on the VARIABLE (Tommys_Bank_Account) of Tommy's Acount
Tommys_Bank_Account.withdrawMoney(500)

#Tommy's mom said he needs to keep his balance above $1500, but Tommy spend a lot of money on gas and does not know what his balance is
#Tommy uses the FUNCTION (checkBalance()) to see how much money he has
#this FUNCTION is called on the VARIABLE (Tommys_Bank_Account) of Tommy's Acount
Tommys_Bank_Account.checkBalance()


