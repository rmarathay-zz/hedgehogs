# bankAccount.py
import pytest

class InsufficientAmount(Exception):
    pass
class BankAccount(object):
    
    def __init__(self, initial_amount = 0):
        self.balance = initial_amount
    
    def deposit(self, amount):
        self.balance += amount
    
    def withdraw(self, amount):
        if self.balance < amount:
            raise InsufficientAmount('Insufficient Balance in account to withdraw {}'.format(amount))
        self.balance -= amount
    