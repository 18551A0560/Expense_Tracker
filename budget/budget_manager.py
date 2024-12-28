########Budget_Manager#####################



def is_valid_amount(amount_str):
    """Validates if the amount string can be converted to a float."""
    try:
        float(amount_str)
        return True
    except ValueError:
        return False

def set_budget():
    """Allows user to set a monthly budget."""
    global monthly_budget
    while True:
        budget_str = input("Enter your monthly budget: ")
        if is_valid_amount(budget_str):
            monthly_budget = float(budget_str)
            print(f"Monthly budget set to: ${monthly_budget:.2f}")
            return monthly_budget
        else:
            print("Invalid budget entered. Please enter numbers only.")

def track_budget(expenses, monthly_budget):
    """Calculates total expenses and compares them to the budget."""
    if not expenses:
        print("No expenses recorded to compare with budget.")
        return

    total_expenses = sum(expense["amount"] for expense in expenses)
    if monthly_budget == 0:
        print("No monthly budget set. Please set it first.")
        return
    
    if total_expenses > monthly_budget:
        print(
            f"Warning: You have exceeded your budget by ${total_expenses - monthly_budget:.2f}!"
        )
    else:
        remaining_balance = monthly_budget - total_expenses
        print(f"You have ${remaining_balance:.2f} left for the month.")