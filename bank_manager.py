from bank_account import BankAccount
from saving import SavingAccount
from chequing import ChequingAccount
import json
from database import db


def create_account(acc):
    """This method creates accounts using the BankAccount class and saves them into the database"""
    acc1 = BankAccount(interest_rate=acc[0], max_withdraw=acc[1], type = acc[2], person_name=acc[3], home_branch=acc[4],
                           account_number=acc[5], balance=acc[6], min_bal=acc[7], stock=acc[8])
    acc1.save()

def delete_account(account):
    """This method deletes all accounts from the database"""
    del_people = db.cursor()
    del_people.execute(f'DELETE from bankaccount where account_number="{account}"')

def get_account_info(account_number):
    """Gets account info for one account"""
    account_exec = db.cursor()
    account = account_exec.execute(f'SELECT * from bankaccount where account_number="{account_number}"')
    for i in account:
        return i


def update_home_branch(new_home_branch, account_num):
    """Updates home branch for selected acc"""
    account_exec = db.cursor()
    account_exec.execute(f'UPDATE bankaccount SET home_branch = "{new_home_branch}" WHERE account_number="{account_num}"')


def get_all_accounts():
    """Gets all accounts"""
    arr = []
    account_exec = db.cursor()
    accounts = account_exec.execute('SELECT * from bankaccount')
    for i in accounts:
        arr.append(i)
    return arr

def get_acc_by_type(type):
    """Gets acc by type"""
    account_exec = db.cursor()
    account = account_exec.execute(f'SELECT * from bankaccount where type="{type}"')
    for i in account:
        return i


def stats():

    "Returns Stats"
    count = 0
    account_exec = db.cursor()
    accounts = account_exec.execute('SELECT * from bankaccount')
    for i in accounts:
        count +=1
    total = f'Bank Name: TD Canada Trust. Number of accounts: {count}'
    return total




if __name__ == "__main__":
    stats()

