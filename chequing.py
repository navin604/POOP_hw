from bank_account import BankAccount

class ChequingAccount(BankAccount):
    """Class which represents a chequing account"""
    ACC_TYPE = 'chequing'
    def __init__(self, max_spend, min_spend, name, branch, acc_num):
        """Chequing account constructor"""
        super().__init__(name, branch, acc_num)
        self._maximum_spend = max_spend
        self._minimum_spend = min_spend



    def get_max_spend(self):
        """Returns the max spend for account"""
        return self._maximum_spend


    def get_min_spend(self):
        """Returns min spend for acc"""
        return self._minimum_spend

    def to_dict(self):

        acc_dict = {'name': self._person_name, 'acc_num': self._account_number, 'branch':self._home_branch, 'min_spend':self._minimum_spend, 'max_spend': self._maximum_spend, 'type':self.ACC_TYPE}
        return acc_dict

