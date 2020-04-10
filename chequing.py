from peewee import *
from bank_account import BankAccount

class ChequingAccount(BankAccount):
    """Class which represents a chequing account"""
    ACC_TYPE = 'chequing'

    maximum_spend = CharField()
    minimum_spend = CharField()



    def get_max_spend(self):
        """Returns the max spend for account"""
        return self._maximum_spend


    def get_min_spend(self):
        """Returns min spend for acc"""
        return self._minimum_spend

    def to_dict(self):

        acc_dict = {'name': self._person_name, 'acc_num': self._account_number, 'branch':self._home_branch, 'min_spend':self._minimum_spend, 'max_spend': self._maximum_spend, 'type':self.ACC_TYPE}
        return acc_dict

