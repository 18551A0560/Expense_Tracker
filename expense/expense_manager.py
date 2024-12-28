#########Expense_Manager#############


import datetime

def validate_input(prompt, input_type):
    """Validates user input based on the specified type."""
    while True:
        user_input = input(prompt).strip()  # .strip() removes leading/trailing spaces
        if user_input:  # Ensure not empty
            if input_type == "date":
                try:
                    datetime.datetime.strptime(user_input, "%Y-%m-%d")
                    return user_input
                except ValueError:
                    print("Invalid date format. Please use YYYY-MM-DD.")
            elif input_type == "amount":
                try:
                    return float(user_input)
                except ValueError:
                    print("Invalid amount entered. Please enter numbers only.")
            else:  # Handle other types of input, e.g., category, description
                return user_input
        else:
           print("Input cannot be empty. Please provide value")


def add_expense(expenses):
    """Prompts user for expense details and adds it to the expenses list."""
    date = validate_input("Enter the date of the expense (YYYY-MM-DD): ", "date")
    category = validate_input("Enter the category of the expense (e.g., Food, Travel): ", "text")
    amount = validate_input("Enter the amount spent: ", "amount")
    description = validate_input("Enter a brief description of the expense: ", "text")
   
    expense = {
        "date": date,
        "category": category,
        "amount": amount,
        "description": description,
    }

    expenses.append(expense)
    print("Expense added successfully!\n")


def view_expenses(expenses):
    """Displays all stored expenses, validating each entry."""
    if not expenses:
        print("No expenses recorded yet.")
        return

    print("\n--- Expenses ---")
    for expense in expenses:
        if all(key in expense for key in ["date", "category", "amount", "description"]):
             print(
                f"Date: {expense['date']}, Category: {expense['category']}, "
                f"Amount: {expense['amount']:.2f}, Description: {expense['description']}"
            )
        else:
            print("Incomplete expense data found. Skipping.")

    print("--- End of Expenses ---")