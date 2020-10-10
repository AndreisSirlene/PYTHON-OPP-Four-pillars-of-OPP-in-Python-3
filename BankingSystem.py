from abc import ABCMeta, abstractmethod
from random import randint


class Account(metaclass = ABCMeta):  
    @abstractmethod         
    def createAccount(self, name, initial_deposit):
        return 0

    @abstractmethod
    def authenticate(self, account_number):
        return 0

    @abstractmethod
    def withdraw(self, withdraw_amount):
        return 0

    @abstractmethod
    def initialDeposit(self, initial_deposit):
        return 0

    @abstractmethod
    def displayBalance(self, display_Balance):
        return 0
    


class savingsAccount(Account):
    def __init__(self):
        #[key][0] => name ; [key][1] => balance
        self.SavingsAccount = {}


    def createAccount(self, name, initialDeposit):
        self.accountNumber = randint(10000, 99999)
        self.SavingsAccount[self.accountNumber] = [name, initialDeposit]
        print('Account creation has been successful. Your account number is ', self.accountNumber)
        

    def authenticate(self, name, accountNumber):
        if accountNumber in self.SavingsAccount.keys():
            if self.SavingsAccount[accountNumber][0] == name:
                print('Authentication is Successful!')
                self.accountNumber = accountNumber
                return True
            else:
                print('Authentication Failed')
                return False
        else:
            print('Authentication Failed')
            return False 

  #Before withdraw is necessary check if the amount that has been withdraw is greater than the amount available,let the user know   he has insuficient balance       
    def withdraw(self, withdrawalAmount):  
        if withdrawalAmount > self.SavingsAccount[self.accountNumber][1]:
            print('Insuficient Balance')
        else:
            self.SavingsAccount[self.accountNumber][1] -= withdrawalAmount
            print('Withdrawal was successful.')
            self.displayBalance()


    def initialDeposit(self, depositAmount):
        self.SavingsAccount[self.accountNumber][1] += depositAmount
        print('Deposit was successful.')
        self.displayBalance()

    def displayBalance(self):
        print('Available Balance: ',self.SavingsAccount[self.accountNumber][1])
    

SavingsAccount = savingsAccount()
while True:
    print('Enter 1 to create a new account')
    print('Enter 2 to access an existing account')
    print('Enter 3 to logout')
    user_choice = int(input())
    if user_choice == 1:
        print('Enter your name: ')
        name = input()
        print('Enter the initial deposit: ')
        initialDeposit = int(input())
        SavingsAccount.createAccount(name, initialDeposit)
    elif user_choice == 2:
        print('Enter your name: ')
        name = input()
        print('Enter your account number: ')
        accountNumber = int(input())
        authenticationStatus = SavingsAccount.authenticate(name, accountNumber)
        if authenticationStatus is True:
            while True:
                print('Enter 1 to withdraw')
                print('Enter 2 to deposit')
                print('Enter 3 to display available balance')
                print('Enter 4 to go back to the previous menu')
                user_choice = int(input())
                if user_choice == 1:
                    print('Enter a withdraw amount')
                    withdrawalAmount = int(input())
                    SavingsAccount.withdraw(withdrawalAmount)
                elif user_choice == 2:
                    print('Enter an amount to be deposited')
                    depositAmount = int(input())
                    SavingsAccount.initialDeposit(depositAmount)
                elif user_choice == 3:
                    SavingsAccount.displayBalance()
                elif user_choice == 4:
                    break
    elif user_choice == 3:
        quit()
    



