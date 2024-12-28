##########File_Manager#########

import csv
import os

EXPENSES_FILE = "expenses.csv"
def save_expenses(expenses):
    """Saves all expenses to a CSV file."""
    if not expenses:
        print("No expenses to save.")
        return

    with open(EXPENSES_FILE, "w", newline="") as file:
        writer = csv.DictWriter(file, fieldnames=expenses[0].keys())
        writer.writeheader()
        writer.writerows(expenses)
    print(f"Expenses saved to '{EXPENSES_FILE}' successfully.")


def load_expenses():
    """Loads expenses from a CSV file."""
    expenses = []
    if not os.path.exists(EXPENSES_FILE):
        print("No previous expense file found. Starting with an empty list.")
        return expenses

    try:
        with open(EXPENSES_FILE, "r") as file:
            reader = csv.DictReader(file)
            for row in reader:
                # Convert amount to float
                try:
                    row["amount"] = float(row["amount"])
                    expenses.append(row)
                except ValueError:
                    print(f"Skipping row due to invalid amount: {row}")
    except Exception as e:
        print(f"Error loading expenses: {e}")
    print("Expenses loaded successfully.")
    return expenses