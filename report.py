import tkinter as tk

# Function to open the report window
def open_report_window(total_income, total_expenses, remaining_budget, user_budget):
    """
    Opens the report window and displays the current income, expenses, and budget details.
    """
    window = tk.Toplevel()
    window.title("Budget Report")

    # Labels to display total income, expenses, remaining budget, and user budget
    income_label = tk.Label(window, text=f"Total Income: ${total_income:.2f}")
    income_label.pack(pady=10)

    expenses_label = tk.Label(window, text=f"Total Expenses: ${total_expenses:.2f}")
    expenses_label.pack(pady=10)

    remaining_label = tk.Label(window, text=f"Remaining Budget: ${remaining_budget:.2f}")
    remaining_label.pack(pady=10)

    user_budget_label = tk.Label(window, text=f"User Budget: ${user_budget:.2f}")
    user_budget_label.pack(pady=10)

    window.mainloop()


