# income_expense.py

# Global variables to track income, expenses, and budget
total_income = 0.0
total_expenses = 0.0
user_budget = 0.0

# List to store income and expense entries
income_list = []
expense_list = []

def update_income(income):
    """
    Adds a new income value to the income list and updates the total income.
    Args:
        income (float): The income amount to add.
    """
    global total_income
    income_list.append(income)
    total_income += income

def add_expense(expense):
    """
    Adds a new expense value to the expense list and updates the total expenses.
    Args:
        expense (float): The expense amount to add.
    """
    global total_expenses
    expense_list.append(expense)
    total_expenses += expense

def update_expense_display(income_label, expense_label, remaining_label):
    """
    Updates the provided Tkinter labels to display current income, expenses, and remaining budget.
    Args:
        income_label (tk.Label): Label to show total income.
        expense_label (tk.Label): Label to show total expenses.
        remaining_label (tk.Label): Label to show remaining budget.
    """
    remaining = user_budget - total_expenses
    income_label.config(text=f"Total Income: ${total_income:.2f}")
    expense_label.config(text=f"Total Expenses: ${total_expenses:.2f}")
    remaining_label.config(text=f"Remaining Budget: ${remaining:.2f}")

def set_budget(budget):
    """
    Sets the user-defined budget.
    Args:
        budget (float): The budget amount to set.
    """
    global user_budget
    user_budget = budget


