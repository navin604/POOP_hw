from bank_account import BankAccount
from saving import SavingAccount
from chequing import ChequingAccount

class Bank:

    def __init__(self, bank_name):
        self.bank_name = bank_name
        self.accounts = []

    """add an account to the account array"""
    def add_account(self, account):
        self.accounts.append(account)

    """removes an account from the account array"""
    def close_account(self, account):
        for i in self.accounts:
            if i[1] == account:
                self.accounts.remove(i)

    """return account information"""
    def get_account_info(self, account_number):
        for i in self.accounts:
            if i[1] == account_number:
                return i

    """changes the home branch of an account"""
    def update_home_branch(self, new_home_branch, account_num):
        for i in self.accounts:
            if i[1] == account_num:
                i[5] = new_home_branch

if __name__ == "__main__":
    pass