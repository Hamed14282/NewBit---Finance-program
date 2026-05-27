#pyinstaller GUItest.py --onefile --noconsole

""" 
TODO
Allow the user to select profiles (different users with different data files)
- Data folder with different user folders (user1, user2, etc.) and inside them the data files (data.txt, month_expenses.csv)

Ability to change themes
Make expense table editable
Take all of the data from all files (all_expense_lines) and reorganize it into files of different months (in case the user adds a different month expense to the current month file)

CATEGORIES
-Allow the data in the table to be categorized by user defined categories (food, transport, etc.)
-Create a graph of expenses by category (pie chart)

ERROR CHECKING
-input expense (check all values)

UPDATING
-Table update after adding expense

"""

#Number of constant variables in file
totalData = 3 

#Constant variables
"""
1 - income
2 - savings
3 - spendings
"""

########################################################################################################

import os
import csv
import glob

import customtkinter
from matplotlib import pyplot as plt
import numpy as np
from datetime import datetime
from matplotlib.figure import Figure
now = datetime.now()

current_month = now.strftime("%m.%Y")
current_day = now.strftime("%d")
current_date = now.strftime("%d.%m.%Y")

########################################################################################################

#Non constant variables
months = 0
years = 0
annual_rate = 0
periods = 0
global expense_lines
expense_lines = []
global all_expense_lines
all_expense_lines = []
days = []
expenses = []

########################################################################################################

def projection(months):
    result = savings + (income * months) - (spendings * months)
    return result

def simple_interest(annual_rate, years, interest_money):
    result = savings + (interest_money * annual_rate/100 * years)
    return result

def compound_interest(annual_rate, years, interest_money, periods):
    result = (savings - interest_money) + (interest_money * (1 + (annual_rate/100)/periods) ** (periods * years))
    return result

def check_expense_file():
    if not os.path.exists(f"data/{current_month}_expenses.csv"):
        file = open(f"data/{current_month}_expenses.csv", "x")
        file.close()

def check_data_file():
    if not os.path.exists("data"):
        os.makedirs("data")

    if not os.path.exists("data/data.txt"):
        file = open("data/data.txt", "x")
        file.close()
    
def total_monthly_expenses():
    total = 0

    for x in expense_lines:
        total += float(x[0])
        
    print(f"Total expenses this month {total}\n")

def expenses_graph():
    exp_by_day = {} 
    exp_by_category = {}   
    
    for x in expense_lines:
        amount = float(x[0])
        category = x[1]
        day = x[2]

        exp_by_day[day] = exp_by_day.get(day, 0) + amount
        exp_by_category[category] = exp_by_category.get(category, 0) + amount
    
    days = list(exp_by_day.keys())
    expenses = list(exp_by_day.values())

    fig = Figure(figsize=(5, 4), dpi=100)
        
    ax = fig.add_subplot(111)
    ax.plot(days, expenses, marker='o')
    
    ax.set_title(f"{current_month} expenses")
    ax.set_xlabel("Days")
    ax.set_ylabel("Expenses (Euros)")
    ax.grid(True)

    return fig

def monthly_expenses_graph():
    exp = {}

    files = glob.glob("data/*_expenses.csv")

    for file_name in files:
        month = os.path.basename(file_name).replace("_expenses.csv", "")

        total = 0
        with open(file_name, "r") as f:
            reader = csv.reader(f)
            for row in reader:
                total += float(row[0])

        exp[month] = total

    months = sorted(exp.keys())
    values = [exp[m] for m in months]

    fig = Figure(figsize=(6, 4), dpi=100)
    ax = fig.add_subplot(111)
    ax.plot(months, values, marker='o')

    ax.set_title("Monthly expenses")
    ax.set_xlabel("Month")
    ax.set_ylabel("Expenses (Euros)")
    ax.grid(True)

    return fig

def get_all_expense_lines():
    files = glob.glob("data/*_expenses.csv")

    for file_name in files:
        with open(file_name, "r") as f:
            reader = csv.reader(f)
            for row in reader:
                all_expense_lines.append(row)


########################################################################################################

def change_income():
    global income
    income = float(input("Income(euro, monthly): "))
    lines[0] = str(income) + "\n"

def change_savings():
    global savings
    savings = float(input("savings(euro, monthly): "))
    lines[1] = str(savings) + "\n"

def change_spendings():
    global spendings
    spendings = float(input("Spendings(euro, monthly): "))
    lines[2] = str(spendings) + "\n"

def add_expense(expense, date, category):
    now = datetime.now()
    current_time = now.strftime("%H:%M:%S")

    global expense_lines
    expense_lines.append([expense, current_time, date[:2], date, category])
    all_expense_lines.append([expense, current_time, date[:2], date, category])

    with open(f"data/{current_month}_expenses.csv", "w", newline="") as expense_file:
        writer = csv.writer(expense_file)
        writer.writerows(expense_lines)

def get_current_time():
    now = datetime.now()
    current_time = now.strftime("%H:%M:%S")
    return current_time

def save_data():
    with open("data/data.txt", "w") as file:
        lines[0] = str(income) + "\n"
        lines[1] = str(savings) + "\n"
        lines[2] = str(spendings) + "\n"
        file.writelines(lines)

def save_income():
    with open("data/data.txt", "w") as file:
        lines[0] = str(income) + "\n"
        file.writelines(lines)
    
def save_savings():
    with open("data/data.txt", "w") as file:
        lines[1] = str(savings) + "\n"
        file.writelines(lines)

def save_spendings():
    with open("data/data.txt", "w") as file:
        lines[2] = str(spendings) + "\n"
        file.writelines(lines)

def validate_date(date_str):
    try:
        datetime.strptime(date_str, "%d.%m.%Y")
        return True
    except ValueError:
        return False

########################################################################################################

check_data_file()
check_expense_file()
get_all_expense_lines()

#read at retrieve main data
with open("data/data.txt", "r") as file:
    lines = file.readlines()

#read at retrieve expense data
with open(f"data/{current_month}_expenses.csv", "r") as expense_file:
    reader = csv.reader(expense_file)
    for row in reader:
        expense_lines.append(row)

########################################################################################################

while len(lines) < totalData:
    lines.append("\n")

window = customtkinter.CTk()
window.title("Missing data")

frame1 = customtkinter.CTkFrame(master=window)
frame1.grid(row=0, column=0, pady=20, padx=60)

row = 0  # keep track of rows

def save1():
    global income
    income = float(entry1.get())
    save_income()

def save2():
    global savings
    savings = float(entry2.get())
    save_savings()

def save3():
    global spendings
    spendings = float(entry3.get())
    save_spendings()

def save_all():
    if 'entry1' in globals():
        save1()
    if 'entry2' in globals():
        save2()
    if 'entry3' in globals():
        save3()
    window.destroy()


# ---- income ----
if lines[0].strip() == "":
    label1 = customtkinter.CTkLabel(master=frame1, text="Initial income:", font=("Roboto", 24))
    label1.grid(row=row, column=0, pady=10, padx=10)

    entry1 = customtkinter.CTkEntry(master=frame1, placeholder_text="Enter initial income")
    entry1.grid(row=row, column=1, pady=10, padx=10)

    row += 1
else:
    income = float(lines[0].strip())

# ---- savings ----
if lines[1].strip() == "":
    label2 = customtkinter.CTkLabel(master=frame1, text="Initial savings:", font=("Roboto", 24))
    label2.grid(row=row, column=0, pady=10, padx=10)

    entry2 = customtkinter.CTkEntry(master=frame1, placeholder_text="Enter initial savings")
    entry2.grid(row=row, column=1, pady=10, padx=10)

    row += 1
else:
    savings = float(lines[1].strip())

# ---- spendings ----
if lines[2].strip() == "":
    label3 = customtkinter.CTkLabel(master=frame1, text="Initial spendings:", font=("Roboto", 24))
    label3.grid(row=row, column=0, pady=10, padx=10)

    entry3 = customtkinter.CTkEntry(master=frame1, placeholder_text="Enter initial spendings")
    entry3.grid(row=row, column=1, pady=10, padx=10)

    row += 1
else:
    spendings = float(lines[2].strip())

button = customtkinter.CTkButton(master=frame1, text="Save", command=save_all)
button.grid(row=row, column=0, columnspan=2, pady=10, padx=10)

if row > 0:  #at least one field missing
    
    window.mainloop()

########################################################################################################