########Main############
import os
from expense.expense_manager import add_expense, view_expenses
from budget.budget_manager import set_budget, track_budget
from file_io.file_manager import save_expenses, load_expenses, EXPENSES_FILE
from menu.menu_manager import display_menu

expenses = []
monthly_budget = 0
if __name__ == "__main__":
    expenses = load_expenses() # Passing the empty list to fill up
    display_menu(expenses)