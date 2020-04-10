import requests
import tkinter as tk
from tkinter import ttk
import tkinter.messagebox
import random


class CreateAccountPopup(tk.Frame):
    """ Popup Frame to create an account """

    def __init__(self, parent, close_callback):
        """ Constructor """

        tk.Frame.__init__(self, parent)
        self._close_cb = close_callback
        self.grid(rowspan=2, columnspan=2)

        ttk.Label(self, text="Account Holder:").grid(row=1, column=1)
        self._name = ttk.Entry(self)
        self._name.grid(row=1, column=2)
        ttk.Label(self, text="Maximum Withdrawal:").grid(row=2, column=1)
        self._max_withdraw = ttk.Entry(self)
        self._max_withdraw.grid(row=2, column=2)
        ttk.Label(self, text="Account Type:").grid(row=3, column=1)
        self._type = ttk.Entry(self)
        self._type.grid(row=3, column=2)
        ttk.Label(self, text="Interest Rate:").grid(row=4, column=1)
        self._interest_rate = ttk.Entry(self)
        self._interest_rate .grid(row=4, column=2)
        ttk.Label(self, text="Branch:").grid(row=5, column=1)
        self._branch = ttk.Entry(self)
        self._branch.grid(row=5, column=2)

        ttk.Label(self, text="Min Balance:").grid(row=6, column=1)
        self._min_bal = ttk.Entry(self)
        self._min_bal.grid(row=6, column=2)
        ttk.Label(self, text="Stock:").grid(row=7, column=1)
        self._stock = ttk.Entry(self)
        self._stock.grid(row=7, column=2)
        ttk.Button(self, text="Submit", command=self._submit_cb).grid(row=8, column=1)
        ttk.Button(self, text="Close", command=self._close_cb).grid(row=8, column=2)

    def _submit_cb(self):
        """ Submits request to create account """
        name = self._name.get()
        if not name:
            tkinter.messagebox.showerror(title='Value Error', message='Name must contain letters')
            return None
        rate = self._interest_rate.get()
        if float(rate) < 0:
            tkinter.messagebox.showerror(title='Value Error', message='Interest Rate must be greater than 0')
            return None
        rate = str(rate)
        max_withdraw = self._max_withdraw.get()
        if float(max_withdraw) < 0:
            tkinter.messagebox.showerror(title='Value Error', message='Max Withdrawal must be greater than 0')
            return None
        if max_withdraw.isalpha():
            tkinter.messagebox.showerror(title='Value Error', message='Max withdraw must be int')
            return None

        type = self._type.get()
        if type != "chequing" and type != "saving":
            tkinter.messagebox.showerror(title='Value Error', message='Type must be "chequing" or "savings"')
            return None
        data = {}
        data['interest_rate'] = str(self._interest_rate.get())
        data['max_withdraw'] = self._max_withdraw.get()
        data['type'] = self._type.get()
        data['person_name'] = self._name.get()
        data['home_branch'] = self._branch.get()
        data['account_number'] = str(random.randint(10000, 99999))
        data['balance'] = 0
        data['min_bal'] = int(self._min_bal.get())
        data['stock'] = self._stock.get()
        response = requests.post("http://127.0.0.1:5000/entitymanager/create", json=data)
        if response.status_code == 200:
            self._close_cb()

