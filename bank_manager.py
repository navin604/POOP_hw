from bank_account import BankAccount
from saving import SavingAccount
from chequing import ChequingAccount
import json

class Bank:

    def __init__(self, bank_name):
        self.bank_name = bank_name
        self.accounts = []
        self._filepath = './json/savestate.json'
        self._read_from_file()

    """add an account to the account array"""
    def add_account(self, account):
        self.accounts.append(account)
        self._write_to_file()

    """removes an account from the account array"""
    def close_account(self, account):
        for i in self.accounts:
            if i._account_number == account:
                self.accounts.remove(i)
        self._write_to_file()

    """return account information"""
    def get_account_info(self, account_number):
        for i in self.accounts:
            if i._account_number == account_number:
                return i

    """changes the home branch of an account"""
    def update_home_branch(self, new_home_branch, account_num):
        for i in self.accounts:
            if i._account_number == account_num:
                i._home_branch = new_home_branch
        self._write_to_file()

    def get_all_accounts(self):
        """Gets account number of all accounts and returns it in a list"""
        acc_list = []
        for i in self.accounts:
            acc_list.append(i._account_number)
        return acc_list

    def get_acc_by_type(self, type):
        acc_arr = []
        for i in self.accounts:
            if i.ACC_TYPE == type:
                acc_arr.append(i._account_number)
        return acc_arr


    def _read_from_file(self):
        with open(self._filepath) as f:
            data = json.load(f)
        for i in data:
            if i['type'] == 'chequing':
                i['acc_num'] = ChequingAccount(max_spend=i['max_spend'], min_spend=i['min_spend'], name=i['name'], branch=i['branch'], acc_num=i['acc_num'])
                self.accounts.append(i['acc_num'])
            if i['type'] == 'savings':
                i['acc_num'] = SavingAccount(interest=i['interest_rate'], max_withdraw=i['max_withdraw'], name=i['name'], branch=i['branch'], acc_num=i['acc_num'])
                self.accounts.append(i['acc_num'])

    def _write_to_file(self):
        data_list =[]
        for i in self.accounts:
            data = i.to_dict()
            data_list.append(data)
        with open(self._filepath, "w") as write_file:
            json.dump(data_list, write_file)



    def stats(self):
        name = self.bank_name
        num_of_acc = len(self.accounts)
        total = f'Bank Name: {name}. Number of accounts: {num_of_acc}'
        return total




if __name__ == "__main__":
    bank = Bank('TD')
    x = bank.get_all_accounts()
    print(x)

