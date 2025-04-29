"""
Author: Jalen Hall
Date written: 04/16/25
Assignment: Final Project
Short Desc: Half-built GUI for a Personal Budget Tracker. Includes two windows, navigation, images, input validation, and basic setup.
"""

import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk  # For displaying images

class BudgetTrackerApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Personal Budget Tracker - Main Menu")

        # Main menu widgets
        self.main_label = tk.Label(root, text="Welcome to Personal Budget Tracker", font=("Arial", 16))
        self.main_label.pack(pady=10)

        # Load and display image 1
        self.img1 = ImageTk.PhotoImage(Image.open("budget.png").resize((150, 150)))
        self.img1_label = tk.Label(root, image=self.img1)
        self.img1_label.pack(pady=5)
        self.img1_label.config(text="Image: Budget Icon", compound="top")  # Alt text

        # Navigation buttons
        self.income_button = tk.Button(root, text="Enter Income", command=self.open_income_window)
        self.income_button.pack(pady=5)

        self.expense_button = tk.Button(root, text="Enter Expenses", command=self.open_expense_window)
        self.expense_button.pack(pady=5)

        self.exit_button = tk.Button(root, text="Exit", command=root.quit)
        self.exit_button.pack(pady=5)

    def open_income_window(self):
        income_window = tk.Toplevel(self.root)
        income_window.title("Income Entry")

        label = tk.Label(income_window, text="Enter your income:", font=("Arial", 14))
        label.pack(pady=10)

        # Entry box for income
        self.income_entry = tk.Entry(income_window)
        self.income_entry.pack(pady=5)

        submit_btn = tk.Button(income_window, text="Submit Income", command=self.submit_income)
        submit_btn.pack(pady=5)

        # Load and display second image
        self.img2 = ImageTk.PhotoImage(Image.open("money.png").resize((150, 150)))
        self.img2_label = tk.Label(income_window, image=self.img2)
        self.img2_label.pack(pady=5)
        self.img2_label.config(text="Image: Money Icon", compound="top")  # Alt text

    def open_expense_window(self):
        expense_window = tk.Toplevel(self.root)
        expense_window.title("Expense Entry")

        label = tk.Label(expense_window, text="Enter your expense:", font=("Arial", 14))
        label.pack(pady=10)

        self.expense_entry = tk.Entry(expense_window)
        self.expense_entry.pack(pady=5)

        submit_btn = tk.Button(expense_window, text="Submit Expense", command=self.submit_expense)
        submit_btn.pack(pady=5)

    def submit_income(self):
        income = self.income_entry.get()
        if not income:
            messagebox.showerror("Input Error", "Please enter an income amount.")
            return
        try:
            income_value = float(income)
            if income_value < 0:
                raise ValueError
            messagebox.showinfo("Income Added", f"Income of ${income_value:.2f} added successfully!")
        except ValueError:
            messagebox.showerror("Input Error", "Income must be a positive number.")

    def submit_expense(self):
        expense = self.expense_entry.get()
        if not expense:
            messagebox.showerror("Input Error", "Please enter an expense amount.")
            return
        try:
            expense_value = float(expense)
            if expense_value < 0:
                raise ValueError
            messagebox.showinfo("Expense Added", f"Expense of ${expense_value:.2f} added successfully!")
        except ValueError:
            messagebox.showerror("Input Error", "Expense must be a positive number.")

if __name__ == "__main__":
    root = tk.Tk()
    app = BudgetTrackerApp(root)
    root.mainloop()
