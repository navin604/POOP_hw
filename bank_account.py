class BankAccount:
    """Base Bank Account class"""
    def __init__(self,name,branch, acc_num):
        """Constructs account object"""
        self.validate_values(name,branch,acc_num)
        self._person_name = name
        self._account_number = acc_num
        self._balance = 0
        self._min_bal = 0
        self._stock = False
        self._home_branch = branch

    @staticmethod
    def validate_values(name, branch, acc_num):
        """Validate input values"""
        if name == '':
            raise ValueError
        elif type(name) != str:
            raise ValueError

        if branch == '':
            raise ValueError
        elif type(branch) != str:
            raise ValueError

        if acc_num == '':
            raise ValueError
        elif type(acc_num) != str:
            raise ValueError


    def update_balance(self):
        """Allows user to alter bank balance"""
        option = input('Enter y/Y for deposit or n/N to withdraw: ')
        if ((option == 'y') or (option == 'Y')):
            deposit = int(input('Enter the deposit amount:'))
        if ((option == 'n') or (option == 'N')):
            deposit = int(input('Enter the withdrawal amount:'))
        self._balance += deposit

    def account_info(self):
        """Prints bank statement"""
        if self._stock is False:
            stock = 'None'
        if self._stock is True:
            stock = "Yes"
        print(f"Account Holder: {self._person_name}\n"
              f"Account Number: {self._account_number}\n"
              f"Balance: {self._balance}\n"
              f"Minimum Balance {self._min_bal}\n"
              f"Home Branch: {self._home_branch}")


    def get_account_array(self):
        """gets an array of the account values"""
        account_array = [self._person_name, self._account_number, self._balance, self._min_bal, self._stock,
                         self._home_branch]
        return account_array