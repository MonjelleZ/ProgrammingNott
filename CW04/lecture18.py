#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Nov 10 16:22:00 2021

@author: pszit
"""

class Account:
    limit = -1000 # class variable
    
    class_name = "Account"
    
    def __init__(self,owner,amount=0):
        self.owner = owner
        self.amount = amount
       
    def __str__(self):
        return f"{self.class_name}({self.owner},{self.amount}) "
    
    def withdraw(self,howmuch):
        new_balance = self.amount - howmuch
        if new_balance < Account.limit:
            print("No way, you don't have money.... ")
        else:
            self.amount = new_balance
    
    def deposit(self,howmuch): 
        self.amount = self.amount+howmuch
        
    def statement(self):
        return f"Owner: {self.owner}, Amount: {self.amount}"


class SavingsAccount(Account):
    
    interest_rate = 0.05
    
    class_name = "SavingsAccount"

    def add_interest(self):
        self.deposit(self.amount*SavingsAccount.interest_rate)
        # self.amount += self.amount*SavingsAccount.interest_rate

    def withdraw(self,howmuch):
        if self.amount -howmuch < 0:
            print("Sorry, Savings account cannot be overdrawn...")
        else:
            #super(SavingsAccount,self).withdraw(howmuch)
            Account.withdraw(self,howmuch)
            
    
mine = Account('Isaac')

thor = Account("Thorsten")

another_account = Account("another name",20)

my_savings = SavingsAccount("Isaac",20)

lst = [mine, thor,another_account]

for elem in lst:
    print(elem.statement())

