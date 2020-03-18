from bank_account import BankAccount

class SavingAccount(BankAccount):
    """Class which represents a savings account"""
    ACC_TYPE = 'savings'

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


    def to_dict(self):
        acc_dict = {'name': self._person_name, 'acc_num': self._account_number, 'branch': self._home_branch,
                    'interest_rate': self._interest_rate, 'max_withdraw': self._max_withdraw,'type':self.ACC_TYPE}
        return acc_dict





