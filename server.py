import json
import pandas as pd
from fastmcp import FastMCP

mcp = FastMCP(name='Expense Server')

df = pd.read_excel('expenses.xlsx')

df["date"] = pd.to_datetime(df["date"])


@mcp.tool
def add_expense(date, amount, category, subcategory="", note=""):
    '''Add a new expense entry to dataframe'''
    
    new_expense = {
    'date': date,
    'amount': amount,
    'category': category,
    'subcategory': subcategory,
    'note': note
    }

    df.loc[len(df)] = new_expense

    df.to_excel('expenses.xlsx', index=False)

    return {"Expense Inserted Successfully"}
    

@mcp.tool
def list_expenses(start_date, end_date):
    '''List expense entries within an inclusive date range'''

    start_date = pd.to_datetime(start_date)
    end_date = pd.to_datetime(end_date)
    range_expenses = df[(df['date']>= start_date) & (df['date']<= end_date)]

    return range_expenses.to_json(orient="records")



@mcp.tool()
def summarize(start_date, end_date, category):
    '''Summarize expenses by category within an inclusive date range.'''

    start_date = pd.to_datetime(start_date)
    end_date = pd.to_datetime(end_date)

    category_expenses =  df[df['category'].str.strip().str.lower()==category.lower()]
    range_expenses = category_expenses[(category_expenses['date']>= start_date) & (category_expenses['date']<= end_date)]

    return range_expenses['amount'].sum()


allowed_categories = {
    "Food": {
        "Groceries": [
            "Monthly grocery shopping",
            "Supermarket purchase",
        ],
        "Dining Out": [
            "Family dinner",
            "Weekend lunch",
        ],
        "Coffee": [
            "Coffee and snacks",
            "Coffee with colleagues",
        ],
        "Delivery": [
            "Food delivery",
        ],
    },

    "Transport": {
        "Fuel": [
            "Car fuel",
        ],
        "Metro": [
            "Metro recharge",
            "Office commute",
        ],
        "Cab": [
            "Airport cab",
        ],
        "Parking": [
            "Mall parking",
        ],
    },

    "Shopping": {
        "Clothing": [
            "New clothes",
        ],
        "Personal Care": [
            "Grooming products",
        ],
        "Electronics": [
            "Computer accessories",
        ],
        "Household": [
            "Home supplies",
        ],
        "Footwear": [
            "Casual shoes",
        ],
        "Accessories": [
            "Backpack and accessories",
        ],
    },

    "Bills": {
        "Electricity": [
            "Electricity bill",
        ],
        "Internet": [
            "Broadband bill",
        ],
        "Mobile": [
            "Mobile recharge",
        ],
        "Gas": [
            "Cooking gas",
        ],
        "DTH": [
            "DTH recharge",
        ],
        "Maintenance": [
            "Apartment maintenance",
        ],
    },

    "Entertainment": {
        "Movies": [
            "Movie tickets",
            "Weekend movie",
        ],
        "Streaming": [
            "OTT subscription",
        ],
        "Games": [
            "Gaming purchase",
        ],
        "Dining Out": [
            "Dinner with friends",
        ],
        "Events": [
            "Event tickets",
        ],
    },
}

@mcp.resource("expense-classification://allowed")
def allowed_expense_classification() -> str:
    """
    Allowed category, subcategory and note combinations
    for expense classification.
    """

    return json.dumps(allowed_categories, indent=2, ensure_ascii=False)


if __name__ == "__main__":
    mcp.run()
