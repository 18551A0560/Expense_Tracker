#######Menu_Manager############


from expense.expense_manager import add_expense, view_expenses
from budget.budget_manager import set_budget, track_budget
from file_io.file_manager import save_expenses

def display_menu(expenses):
    """Displays the interactive menu and handles user input."""
    monthly_budget = 0
    while True:
        print("\n--- Expense Tracker Menu ---")
        print("1. Add expense")
        print("2. View expenses")
        print("3. Track budget")
        print("4. Save expenses")
        print("5. Exit")

        choice = input("Enter your choice (1-5): ")

        if choice == "1":
            add_expense(expenses)
        elif choice == "2":
            view_expenses(expenses)
        elif choice == "3":
            if monthly_budget == 0:
                monthly_budget = set_budget()
            track_budget(expenses, monthly_budget)
        elif choice == "4":
            save_expenses(expenses)
        elif choice == "5":
            save_expenses(expenses)
            print("Exiting the program.")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 5.")