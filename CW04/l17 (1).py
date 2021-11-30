#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Nov  9 13:49:41 2021

@author: pszit

Object-Oriented Programming
"""


class Account:
    limit = -1000 # class variable
    
    def __init__(self,owner):
        self.owner = owner
        self.amount = 0
    
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

mine = Account('Isaac')

thor = Account("Thorsten")

