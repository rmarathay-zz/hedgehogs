# testing bankAcount.py
import pytest
from bankAccount import BankAccount, InsufficientAmount

"""
test fixtures are used to provide a fixed baseline upon which 
tests can reliably and repeatedly execute.
"""

"""
empty_bankAccount returns a new instance of BankAccount with 
balance 0.
"""
@pytest.fixture
def empty_bankAccount():
    return BankAccount()

"""
bankAccount returns a new instance of BankAccount with a
balance of 100.
"""
@pytest.fixture
def bankAccount():
    return BankAccount(100)

def test_default_initial_amount(empty_bankAccount):
    assert empty_bankAccount.balance == 0

def test_setting_initial_amount(bankAccount):
    assert bankAccount.balance == 100

def test_deposit(bankAccount):
    bankAccount.deposit(100)
    assert bankAccount.balance == 100

def test_withdraw(bankAccount):
    previous_balance = bankAccount.balance
    after_balance = previous_balance - 10
    bankAccount.withdraw(10)
    assert bankAccount.balance == after_balance

def test_withdraw_raises_exception(empty_bankAccount):
    with pytest.raises(InsufficientAmount):
        empty_bankAccount.withdraw(300)
    