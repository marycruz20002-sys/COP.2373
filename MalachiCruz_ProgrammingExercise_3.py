import functools
import operator

def get_expenses():
    """
    Asks the user for a list of expenses (type and amount) 
    and returns a list of dictionaries.
    """
    expenses = []
    print("Enter your monthly expenses.")
    print("Type 'done' when you are finished.")

    while True:
        expense_type = input("Enter expense type (or 'done'): ")
        if expense_type.lower() == 'done':
            break
        
        while True:
            try:
                amount = float(input(f"Enter amount for {expense_type}: $"))
                if amount <= 0:
                    print("Amount must be a positive number.")
                    continue
                expenses.append({'type': expense_type, 'amount': amount})
                break
            except ValueError:
                print("Invalid input. Please enter a valid number.")
    return expenses

def analyze_expenses(expenses):
    """
    Analyzes the expenses using the reduce method to find total, highest, and lowest.
    """
    if not expenses:
        print("No expenses entered.")
        return

    # Extract amounts into a list for easier reduction
    amounts = [expense['amount'] for expense in expenses]

    # Calculate total using reduce and operator.add
    total_expense = functools.reduce(operator.add, amounts)

    # Find the highest expense using reduce and a lambda function
    # The lambda function compares two numbers and returns the larger one
    highest_amount = functools.reduce(lambda x, y: x if x > y else y, amounts)
    # Find the type of the highest expense
    highest_expense_type = next(item['type'] for item in expenses if item['amount'] == highest_amount)

    # Find the lowest expense using reduce and a lambda function
    # The lambda function compares two numbers and returns the smaller one
    lowest_amount = functools.reduce(lambda x, y: x if x < y else y, amounts)
    # Find the type of the lowest expense
    lowest_expense_type = next(item['type'] for item in expenses if item['amount'] == lowest_amount)


    # Display the results
    print("-" * 30)
    print(f"Total expense: ${total_expense:.2f}")
    print(f"Highest expense: {highest_expense_type} (${highest_amount:.2f})")
    print(f"Lowest expense: {lowest_expense_type} (${lowest_amount:.2f})")
    print("-" * 30)


if __name__ == "__main__":
    user_expenses = get_expenses()
    analyze_expenses(user_expenses)
