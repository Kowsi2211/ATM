import tkinter as tk
from tkinter import messagebox

class ATMApp:
    def __init__(self, root):
        self.bal = 0.0
        self.transaction_history = []
        self.pin_code = '1234' 
        self.root = root
        self.root.title("ATM Application")
        self.root.geometry('1200x1200') 
        self.root.config(bg='black')

       
        self.pin_frame = tk.Frame(root,bg='black')
        self.pin_frame.pack(pady=20)

        self.pin_label = tk.Label(self.pin_frame, text="Enter PIN:", bg='black', fg='yellow', font=('Arial', 20))
        self.pin_label.grid(row=0, column=0, padx=10,pady=10)

        self.pin_entry = tk.Entry(self.pin_frame, show="*", font=('Arial', 20))
        self.pin_entry.grid(row=0, column=1, padx=10,pady=10)

        self.pin_button = tk.Button(self.pin_frame, text="Submit", bg='black', fg='gray', font=('Arial', 20), command=self.check_pin, bd=5, padx=10, pady=10)
        self.pin_button.grid(row=1, columnspan=2, pady=20)


    def check_pin(self):
        entered_pin = self.pin_entry.get()
        if len(entered_pin) == 4 and entered_pin.isdigit():
            if entered_pin == self.pin_code:
                self.pin_frame.pack_forget() 
                self.show_options()
            else:
                messagebox.showerror("Error", "Incorrect PIN")
        else:
            messagebox.showerror("Error", "Invalid PIN format")

    def show_options(self):
       
        self.option_frame = tk.Frame(self.root, bg='black')
        self.option_frame.pack(pady=20)

        self.balance_button = tk.Button(self.option_frame, text="Check Balance", bg='black', fg='yellow', font=('Arial', 20), width=20, bd=5, padx=10, pady=10, command=self.check_balance)
        self.balance_button.grid(row=0, column=0, pady=10,padx=10)

        self.deposit_button = tk.Button(self.option_frame, text="Deposit", bg='black', fg='yellow', font=('Arial', 20), width=20, bd=5, padx=10, pady=10, command=self.deposit)
        self.deposit_button.grid(row=0, column=1, pady=10,padx=10)

        self.withdraw_button = tk.Button(self.option_frame, text="Withdraw", bg='black', fg='yellow', font=('Arial', 20), width=20, bd=5, padx=10, pady=10, command=self.withdraw)
        self.withdraw_button.grid(row=1, column=0, pady=10,padx=10)

        self.history_button = tk.Button(self.option_frame, text="Transaction History", bg='black', fg='yellow', font=('Arial', 20), width=20, bd=5, padx=10, pady=10, command=self.view_history)
        self.history_button.grid(row=1, column=1, pady=10,padx=10)

        self.change_pin_button = tk.Button(self.option_frame, text="Change PIN", bg='black', fg='yellow', font=('Arial', 20), width=20, bd=5, padx=10, pady=10, command=self.change_pin)
        self.change_pin_button.grid(row=2, column=0, pady=10,padx=10)

        self.exit_button = tk.Button(self.option_frame, text="Exit", bg='black', fg='yellow', font=('Arial', 20), width=20, bd=5, padx=10, pady=10, command=self.exit_app)
        self.exit_button.grid(row=2, column=1, pady=10,padx=10)

    def check_balance(self):
        messagebox.showinfo("Balance", f"Current balance: ${self.bal}")
        
    def deposit(self):
        self.prompt_amount("Deposit", self.deposit_action)

    def deposit_action(self, amount):
        self.bal += amount
        self.transaction_history.append(f"Deposit: ${amount}")
        messagebox.showinfo("Deposit", f"Deposited ${amount}. Current balance: ${self.bal}")

    def withdraw(self):
        self.prompt_amount("Withdrawal", self.withdraw_action)

    def withdraw_action(self, amount):
        if self.bal >= amount:
            self.bal -= amount
            self.transaction_history.append(f"Withdrawal: ${amount}")
            messagebox.showinfo("Withdrawal", f"Withdrew ${amount}. Current balance: ${self.bal}")
        else:
            messagebox.showerror("Error", "Insufficient funds")

    def prompt_amount(self, transaction_type, action):
    
        self.amount_window = tk.Toplevel(self.root)
        self.amount_window.title(transaction_type)

        label = tk.Label(self.amount_window, text=f"Enter amount for {transaction_type.lower()}:", font=('Arial', 20))
        label.pack(pady=10)

        self.amount_entry = tk.Entry(self.amount_window, font=('Arial', 20))
        self.amount_entry.pack(pady=10)

        submit_button = tk.Button(self.amount_window, text="Submit", bg='black', fg='yellow', font=('Arial', 20), command=lambda: self.submit_amount(action), bd=5, padx=10, pady=10)
        submit_button.pack(pady=10)

    def submit_amount(self, action):
        try:
            amount = float(self.amount_entry.get())
            if amount <= 0:
                messagebox.showerror("Error", "Amount must be greater than zero")
            else:
                action(amount)
                self.amount_window.destroy()
        except ValueError:
            messagebox.showerror("Error", "Invalid amount")

    def view_history(self):
        if self.transaction_history:
            history = "\n".join(self.transaction_history)
            messagebox.showinfo("Transaction History", history)
        else:
            messagebox.showinfo("Transaction History", "No transactions found.")

    def change_pin(self):
        self.change_pin_window = tk.Toplevel(self.root)
        self.change_pin_window.title("Change PIN")

        self.old_pin_label = tk.Label(self.change_pin_window, text="Enter current PIN:", font=('Arial', 20))
        self.old_pin_label.pack(pady=10)

        self.old_pin_entry = tk.Entry(self.change_pin_window, show="*", font=('Arial', 20))
        self.old_pin_entry.pack(pady=10)

        self.new_pin_label = tk.Label(self.change_pin_window, text="Enter new PIN (4 digits):", font=('Arial', 20))
        self.new_pin_label.pack(pady=10)

        self.new_pin_entry = tk.Entry(self.change_pin_window, show="*", font=('Arial', 20))
        self.new_pin_entry.pack(pady=10)

        submit_button = tk.Button(self.change_pin_window, text="Submit", bg='black', fg='yellow', font=('Arial', 20), command=self.submit_new_pin, bd=5, padx=10, pady=10)
        submit_button.pack(pady=20)

    def submit_new_pin(self):
        old_pin = self.old_pin_entry.get()
        new_pin = self.new_pin_entry.get()

        if old_pin == self.pin_code:
            if len(new_pin) == 4 and new_pin.isdigit():
                self.pin_code = new_pin
                messagebox.showinfo("Success", "PIN successfully changed.")
                self.change_pin_window.destroy()
            else:
                messagebox.showerror("Error", "New PIN must be 4 digits")
        else:
            messagebox.showerror("Error", "Incorrect current PIN")

    def exit_app(self):
        self.root.quit()


if __name__ == "__main__":
    root = tk.Tk()
    app = ATMApp(root)
    root.mainloop()
