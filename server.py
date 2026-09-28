import json
import pandas as pd
from fastmcp import FastMCP

mcp = FastMCP(name='Expense Server')

#df = pd.read_excel('expenses.xlsx')

data = [
    ["2026-07-01 00:00:00", 1850, "Food", "Groceries", "Monthly grocery shopping"],
    ["2026-07-03 00:00:00", 420, "Food", "Dining Out", "Family dinner"],
    ["2026-07-06 00:00:00", 180, "Food", "Coffee", "Coffee and snacks"],
    ["2026-07-10 00:00:00", 1250, "Food", "Groceries", "Vegetables and household groceries"],
    ["2026-07-14 00:00:00", 560, "Food", "Delivery", "Food delivery"],
    ["2026-07-19 00:00:00", 780, "Food", "Dining Out", "Weekend lunch"],
    ["2026-07-25 00:00:00", 320, "Food", "Coffee", "Coffee with colleagues"],
    ["2026-07-29 00:00:00", 1450, "Food", "Groceries", "Supermarket purchase"],

    ["2026-07-02 00:00:00", 2400, "Transport", "Fuel", "Car fuel"],
    ["2026-07-05 00:00:00", 220, "Transport", "Metro", "Metro recharge"],
    ["2026-07-09 00:00:00", 650, "Transport", "Cab", "Office commute"],
    ["2026-07-13 00:00:00", 2100, "Transport", "Fuel", "Car fuel"],
    ["2026-07-18 00:00:00", 400, "Transport", "Parking", "Mall parking"],
    ["2026-07-23 00:00:00", 720, "Transport", "Cab", "Airport cab"],
    ["2026-07-27 00:00:00", 300, "Transport", "Metro", "Metro recharge"],

    ["2026-07-04 00:00:00", 3200, "Shopping", "Clothing", "Shirts and trousers"],
    ["2026-07-08 00:00:00", 950, "Shopping", "Personal Care", "Grooming products"],
    ["2026-07-15 00:00:00", 1400, "Shopping", "Electronics", "Computer accessories"],
    ["2026-07-20 00:00:00", 2600, "Shopping", "Household", "Home supplies"],
    ["2026-07-24 00:00:00", 850, "Shopping", "Footwear", "Casual shoes"],
    ["2026-07-30 00:00:00", 1100, "Shopping", "Accessories", "Backpack and accessories"],

    ["2026-07-05 00:00:00", 1850, "Bills", "Electricity", "Electricity bill"],
    ["2026-07-09 00:00:00", 999, "Bills", "Internet", "Broadband bill"],
    ["2026-07-12 00:00:00", 699, "Bills", "Mobile", "Mobile recharge"],
    ["2026-07-17 00:00:00", 1200, "Bills", "Gas", "Cooking gas"],
    ["2026-07-22 00:00:00", 850, "Bills", "DTH", "DTH recharge"],
    ["2026-07-28 00:00:00", 1500, "Bills", "Maintenance", "Apartment maintenance"],

    ["2026-07-07 00:00:00", 500, "Entertainment", "Movies", "Movie tickets"],
    ["2026-07-11 00:00:00", 750, "Entertainment", "Streaming", "OTT subscription"],
    ["2026-07-16 00:00:00", 450, "Entertainment", "Games", "Gaming purchase"],
    ["2026-07-21 00:00:00", 1100, "Entertainment", "Dining Out", "Dinner with friends"],
    ["2026-07-26 00:00:00", 600, "Entertainment", "Events", "Event tickets"],
    ["2026-07-31 00:00:00", 850, "Entertainment", "Movies", "Weekend movie"],

    ["2026-08-02 00:00:00", 2100, "Food", "Groceries", "Monthly grocery shopping"],
    ["2026-08-05 00:00:00", 650, "Food", "Dining Out", "Family dinner"],
    ["2026-08-08 00:00:00", 220, "Food", "Coffee", "Coffee and snacks"],
    ["2026-08-12 00:00:00", 1350, "Food", "Groceries", "Supermarket purchase"],
    ["2026-08-17 00:00:00", 580, "Food", "Delivery", "Food delivery"],
    ["2026-08-22 00:00:00", 920, "Food", "Dining Out", "Weekend lunch"],
    ["2026-08-27 00:00:00", 300, "Food", "Coffee", "Coffee with colleagues"],
    ["2026-08-30 00:00:00", 1600, "Food", "Groceries", "Monthly grocery top-up"],

    ["2026-08-03 00:00:00", 2600, "Transport", "Fuel", "Car fuel"],
    ["2026-08-07 00:00:00", 250, "Transport", "Metro", "Metro recharge"],
    ["2026-08-11 00:00:00", 780, "Transport", "Cab", "Office commute"],
    ["2026-08-16 00:00:00", 2300, "Transport", "Fuel", "Car fuel"],
    ["2026-08-20 00:00:00", 500, "Transport", "Parking", "Mall parking"],
    ["2026-08-24 00:00:00", 850, "Transport", "Cab", "Airport cab"],
    ["2026-08-29 00:00:00", 350, "Transport", "Metro", "Metro recharge"],

    ["2026-08-04 00:00:00", 2800, "Shopping", "Clothing", "New clothes"],
    ["2026-08-09 00:00:00", 1200, "Shopping", "Electronics", "Headphones"],
    ["2026-08-14 00:00:00", 750, "Shopping", "Personal Care", "Grooming products"],
    ["2026-08-19 00:00:00", 3100, "Shopping", "Household", "Furniture and home supplies"],
    ["2026-08-23 00:00:00", 1250, "Shopping", "Footwear", "Sports shoes"],
    ["2026-08-28 00:00:00", 900, "Shopping", "Accessories", "Wallet and accessories"],

    ["2026-08-06 00:00:00", 2100, "Bills", "Electricity", "Electricity bill"],
    ["2026-08-10 00:00:00", 999, "Bills", "Internet", "Broadband bill"],
    ["2026-08-13 00:00:00", 699, "Bills", "Mobile", "Mobile recharge"],
    ["2026-08-18 00:00:00", 1250, "Bills", "Gas", "Cooking gas"],
    ["2026-08-21 00:00:00", 850, "Bills", "DTH", "DTH recharge"],
    ["2026-08-26 00:00:00", 1500, "Bills", "Maintenance", "Apartment maintenance"],

    ["2026-08-03 00:00:00", 600, "Entertainment", "Movies", "Movie tickets"],
    ["2026-08-08 00:00:00", 750, "Entertainment", "Streaming", "OTT subscription"],
    ["2026-08-15 00:00:00", 550, "Entertainment", "Games", "Gaming purchase"],
    ["2026-08-20 00:00:00", 1300, "Entertainment", "Dining Out", "Dinner with friends"],
    ["2026-08-25 00:00:00", 800, "Entertainment", "Events", "Event tickets"],
    ["2026-08-31 00:00:00", 950, "Entertainment", "Movies", "Weekend movie"],

    ["2026-09-01 00:00:00", 2200, "Food", "Groceries", "Monthly grocery shopping"],
    ["2026-09-04 00:00:00", 480, "Food", "Dining Out", "Family dinner"],
    ["2026-09-07 00:00:00", 200, "Food", "Coffee", "Coffee and snacks"],
    ["2026-09-11 00:00:00", 1450, "Food", "Groceries", "Supermarket purchase"],
    ["2026-09-16 00:00:00", 620, "Food", "Delivery", "Food delivery"],
    ["2026-09-21 00:00:00", 850, "Food", "Dining Out", "Weekend lunch"],
    ["2026-09-25 00:00:00", 280, "Food", "Coffee", "Coffee with colleagues"],
    ["2026-09-27 00:00:00", 1700, "Food", "Groceries", "Supermarket purchase"],
]

df = pd.DataFrame(data, columns=["date", "amount", "category", "subcategory", "note"])

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

    #df.to_excel('expenses.xlsx', index=False)

    return df.tail(1).to_json(orient="records")
    

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
    mcp.run(transport="streamable-http")
