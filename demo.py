import json
import datetime

# File to store the finance data
FINANCE_FILE = "personal_finance.json"

# Load finance data from the file if it exists, else create an empty structure
def load_data():
    try:
        with open(FINANCE_FILE, "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return {"income": [], "expenses": []}

# Save finance data to the file
def save_data(data):
    with open(FINANCE_FILE, "w") as file:
        json.dump(data, file, indent=4)

# Add an income entry
def add_income(amount, description):
    data = load_data()
    entry = {
        "amount": amount,
        "description": description,
        "date": str(datetime.date.today())
    }
    data["income"].append(entry)
    save_data(data)
    print("Income added successfully.")

# Add an expense entry
def add_expense(amount, description):
    data = load_data()
    entry = {
        "amount": amount,
        "description": description,
        "date": str(datetime.date.today())
    }
    data["expenses"].append(entry)
    save_data(data)
    print("Expense added successfully.")

# Get a summary of income, expenses, and balance
def get_summary():
    data = load_data()
    total_income = sum(item["amount"] for item in data["income"])
    total_expenses = sum(item["amount"] for item in data["expenses"])
    balance = total_income - total_expenses

    print("\n--- Financial Summary ---")
    print(f"Total Income: ${total_income}")
    print(f"Total Expenses: ${total_expenses}")
    print(f"Balance: ${balance}")
    print("-------------------------")

# Main loop
while True:
    print("\nPersonal Finance Tracker")
    print("1. Add Income")
    print("2. Add Expense")
    print("3. Show Summary")
    print("4. Exit")
    choice = input("Choose an option (1-4): ")

    if choice == "1":
        amount = float(input("Enter income amount: "))
        description = input("Enter income description: ")
        add_income(amount, description)
    elif choice == "2":
        amount = float(input("Enter expense amount: "))
        description = input("Enter expense description: ")
        add_expense(amount, description)
    elif choice == "3":
        get_summary()
    elif choice == "4":
        print("Exiting the program.")
        break
    else:
        print("Invalid option. Please choose a valid option.")