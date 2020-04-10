import tkinter as tk
import tkinter.font
from tkinter import ttk
import requests
from add_account_popup import CreateAccountPopup
from delete_account import DeleteAccount
from update_account import UpdateAccount


class MainAppController(tk.Frame):
    """ Main Application for GUI """

    def __init__(self, parent):
        """ Initialize Main Application """
        tk.Frame.__init__(self, parent)


        left_frame = tk.Frame(master=self)
        left_frame.grid(row=1, column=1)


        right_frame = tk.Frame(master=self)
        right_frame.grid(row=1, column=2)


        tk.Label(left_frame, text="Accounts:").grid(row=1, column=1, columnspan=3)
        self._account_list = tk.Listbox(left_frame, width=20)
        self._account_list.grid(row=2, column=1, columnspan=3)

        self._account_list.bind("<<ListboxSelect>>", self._update_acc_info_box)
        ttk.Button(left_frame, text="Create Account", command=self._create_account).grid(row=3, column=1)
        ttk.Button(left_frame, text="Terminate Account", command=self._delete_account).grid(row=3, column=2)
        ttk.Button(left_frame, text="Update Home Branch", command=self._update).grid(row=4, column=1)
        ttk.Button(left_frame, text="Statistics", command=self._stats).grid(row=4, column=2)


        self._info_text = tk.Text(master=right_frame, height=10, width=40, font=("TkTextFont", 10))
        self._info_text.grid(row=1, column=1)
        self._info_text.tag_configure("bold", font=("TkTextFont", 10, "bold"))

        self._update_account_list()


    def _update(self):
        self._popup_win = tk.Toplevel()
        self._popup = UpdateAccount(self._popup_win, self._close_acc_cb)

    def _create_account(self):
        """ Create Popup """
        self._popup_win = tk.Toplevel()
        self._popup = CreateAccountPopup(self._popup_win, self._close_acc_cb)

    def _delete_account(self):
        """Removes account"""
        self._popup_win = tk.Toplevel()
        self._popup = DeleteAccount(self._popup_win, self._close_acc_cb)

    def _close_acc_cb(self):
        """ Close Create Acc Popup """
        self._popup_win.destroy()
        self._update_account_list()

    def _stats(self):
        r = requests.get("http://localhost:5000/entitymanager/entities/stats")

        root = tk.Tk()
        text = tk.Text(root, height=10, width=28)
        text.pack()
        text.insert(tk.END, r.json())




    def _update_account_list(self):
        """ Updates account listbox """
        results = requests.get("http://localhost:5000/entitymanager/entities/all")
        self._account_list.delete(0, tk.END)

        for i in results.json():
            self._account_list.insert(tk.END, i[2])
        if i[7] == "chequing":
            self._account_list.itemconfig(tk.END, {'fg': 'grey'})
        else:
            self._account_list.itemconfig(tk.END, {'fg': 'black'})

    def _update_acc_info_box(self, evt):
        """ Updates the info text box on the right"""

        # This is a list, so we take just the first item (could be multi select...)
        selected_values = self._account_list.curselection()

        selected_index = selected_values[0]
        acc_num = self._account_list.get(selected_index)

        # Make a GET request
        result = requests.get("http://localhost:5000/entitymanager/entities/" + acc_num)

        # Clear the text box
        self._info_text.delete(1.0, tk.END)

        # Check the request status code
        if result.status_code != 200:
            self._info_text.insert(tk.END, "Error running the request!")

        # For every item (key, value) in the JSON response, display them:
        for k, v in result.json().items():
            self._info_text.insert(tk.END, f"{k.capitalize()}\t\t", "bold")
            self._info_text.insert(tk.END, f"{v}\n")


if __name__ == "__main__":
    root = tk.Tk()
    root.geometry("500x300")
    MainAppController(root).pack()
    root.mainloop()



