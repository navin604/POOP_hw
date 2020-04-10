import requests
import tkinter as tk
from tkinter import ttk
import tkinter.messagebox


class DeleteAccount(tk.Frame):


    def __init__(self, parent, close_callback):
        """ Constructor """

        tk.Frame.__init__(self, parent)
        self._close_cb = close_callback
        self.grid(rowspan=2, columnspan=2)

        ttk.Label(self, text="Account Number:").grid(row=1, column=1)
        self._acc_num = ttk.Entry(self)
        self._acc_num.grid(row=1, column=2)

        ttk.Button(self, text="Submit", command=self._submit_cb).grid(row=4, column=1)
        ttk.Button(self, text="Close", command=self._close_cb).grid(row=4, column=2)

    def _submit_cb(self):
        """ Submit removal """
        acc_num = self._acc_num.get()


        check = tkinter.messagebox.askquestion(title='Confirmation', message='Are you sure? press OK to confirm', icon='warning')
        if check == 'yes':
            response = requests.delete("http://localhost:5000/entitymanager/entities/" + str(acc_num))
            if response.status_code == 200:
                self._close_cb()
            if response.status_code == 400:
                tkinter.messagebox.showinfo(title='Value Error', message='Invalid Account Number')

        else:
            tk.messagebox.showinfo('Return', 'You will now return to the application screen')
            self._close_cb()