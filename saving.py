from bank_account import BankAccount

class SavingAccount(BankAccount):
    """Class which represents a savings account"""

    def __init__(self, interest, max_withdraw, name, branch, acc_num):
        """Savings account constructor"""
        super().__init__(name, branch, acc_num)
        self._interest_rate = interest
        self._max_withdraw = max_withdraw


    def get_interest_rate(self):
        """Returns savings interest rate"""
        return self._interest_rate

    def get_max_withdraw(self):
        """Returns max withdrawal amount"""
        return self._max_withdraw



