from bank_account import BankAccount

class ChequingAccount(BankAccount):
    """Class which represents a chequing account"""
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

