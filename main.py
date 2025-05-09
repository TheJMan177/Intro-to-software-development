import tkinter as tk
from income_expense import update_income, add_expense, update_expense_display, set_budget
from report import open_report_window

# Global variables to track total income, expenses, and budget
total_income = 0.0
total_expenses = 0.0
user_budget = 0.0

# Global variables for labels
total_income_label = None
total_expenses_label = None
remaining_balance_label = None

# Function to initialize the main window
def create_main_window():
    """
    Creates the main window for the budget tracker.
    This window will have buttons to navigate to income, expense, and budget sections.
    """
    root = tk.Tk()
    root.title("Personal Budget Tracker")

    # Define window size
    root.geometry("400x400")

    # Add buttons to navigate to different sections
    income_button = tk.Button(root, text="Income Entry", command=open_income_window)
    income_button.pack(pady=10)

    expense_button = tk.Button(root, text="Expense Entry", command=open_expense_window)
    expense_button.pack(pady=10)

    budget_button = tk.Button(root, text="Budget Overview", command=open_budget_window)
    budget_button.pack(pady=10)

    report_button = tk.Button(root, text="View Report", command=lambda: open_report_window(total_income, total_expenses, total_income - total_expenses, user_budget))
    report_button.pack(pady=10)

    # Initialize labels for total income, expenses, and remaining balance in the main window
    global total_income_label, total_expenses_label, remaining_balance_label
    total_income_label = tk.Label(root, text="Total Income: $0.00")
    total_income_label.pack(pady=10)

    total_expenses_label = tk.Label(root, text="Total Expenses: $0.00")
    total_expenses_label.pack(pady=10)

    remaining_balance_label = tk.Label(root, text="Remaining Budget: $0.00")
    remaining_balance_label.pack(pady=10)

    # Start the Tkinter main loop
    root.mainloop()

# Function to open the income entry window
def open_income_window():
    """
    Opens the income entry window where the user can input income details.
    """
    window = tk.Toplevel()
    window.title("Income Entry")

    income_label = tk.Label(window, text="Enter Income Amount")
    income_label.pack(pady=10)

    income_entry = tk.Entry(window)
    income_entry.pack(pady=10)

    save_button = tk.Button(window, text="Save Income", command=lambda: save_income(income_entry.get(), window))
    save_button.pack(pady=10)

# Function to save income
def save_income(income, window):
    """
    Saves the income value entered by the user and updates the budget label.
    """
    global total_income
    try:
        income = float(income)
        if income < 0:
            raise ValueError("Income cannot be negative.")
        total_income += income
        update_income(income)  # Update income function
        window.destroy()
        update_budget_window()  # Update budget window after saving income
    except ValueError:
        error_label = tk.Label(window, text="Please enter a valid positive number")
        error_label.pack(pady=5)

# Function to open the expense entry window
def open_expense_window():
    """
    Opens the expense entry window where the user can input expense details.
    """
    window = tk.Toplevel()
    window.title("Expense Entry")

    expense_label = tk.Label(window, text="Enter Expense Amount")
    expense_label.pack(pady=10)

    expense_entry = tk.Entry(window)
    expense_entry.pack(pady=10)

    save_button = tk.Button(window, text="Save Expense", command=lambda: save_expense(expense_entry.get(), window))
    save_button.pack(pady=10)

# Function to save expense
def save_expense(expense, window):
    """
    Saves the expense value entered by the user and updates the expense display.
    """
    global total_expenses
    try:
        expense = float(expense)
        if expense < 0:
            raise ValueError("Expense cannot be negative.")
        total_expenses += expense
        add_expense(expense)  # Update expense function
        window.destroy()
        update_budget_window()  # Update budget window after saving expense
    except ValueError:
        error_label = tk.Label(window, text="Please enter a valid positive number")
        error_label.pack(pady=5)

# Function to set the user-defined budget
def set_user_budget(budget, window):
    """
    Sets the user-defined budget and checks if the user is within the budget.
    """
    global user_budget
    try:
        budget = float(budget)
        if budget < 0:
            raise ValueError("Budget cannot be negative.")
        user_budget = budget
        set_budget(budget)  # Update the user-defined budget function
        window.destroy()
        update_budget_window()  # Update budget window after setting the budget
    except ValueError:
        error_label = tk.Label(window, text="Please enter a valid positive number for the budget")
        error_label.pack(pady=5)

# Function to update the budget window labels with the latest data
def update_budget_window():
    """
    Updates the budget window with the latest values for income, expenses, and remaining balance.
    """
    global total_income, total_expenses, user_budget

    # Check if the labels are not None before updating
    if total_income_label and total_expenses_label and remaining_balance_label:
        remaining_budget = user_budget - total_expenses
        total_income_label.config(text=f"Total Income: ${total_income:.2f}")
        total_expenses_label.config(text=f"Total Expenses: ${total_expenses:.2f}")
        remaining_balance_label.config(text=f"Remaining Budget: ${remaining_budget:.2f}")
    else:
        print("Error: Budget window labels are not initialized properly.")

# Function to open the budget overview window
def open_budget_window():
    """
    Opens the budget overview window where the user can view total income, expenses, and the remaining budget.
    """
    window = tk.Toplevel()
    window.title("Budget Overview")

    # Create input field for setting the budget
    budget_label = tk.Label(window, text="Set Your Budget:")
    budget_label.pack(pady=10)

    budget_entry = tk.Entry(window)
    budget_entry.pack(pady=10)

    # Button to set the budget
    set_budget_button = tk.Button(window, text="Set Budget", command=lambda: set_user_budget(budget_entry.get(), window))
    set_budget_button.pack(pady=10)

    window.mainloop()

# Run the application
if __name__ == "__main__":
    create_main_window()



