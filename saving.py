from bank_account import BankAccount
from peewee import *

class SavingAccount(BankAccount):
    """Class which represents a savings account"""
    ACC_TYPE = 'savings'
    interest_rate = CharField()
    max_withdraw = CharField()


    def get_interest_rate(self):
        """Returns savings interest rate"""
        return self._interest_rate

    def get_max_withdraw(self):
        """Returns max withdrawal amount"""
        return self._max_withdraw


    def to_dict(self):
        acc_dict = {'name': self._person_name, 'acc_num': self._account_number, 'branch': self._home_branch,
                    'interest_rate': self._interest_rate, 'max_withdraw': self._max_withdraw,'type':self.ACC_TYPE}
        return acc_dict





