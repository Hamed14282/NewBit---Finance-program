#pyinstaller GUItest.py --onefile --noconsole

""" 
TODO
Allow the user to select profiles (different users with different data files)
- Data folder with different user folders (user1, user2, etc.) and inside them the data files (data.txt, month_expenses.csv)
- Password protection for profiles?

Ability to change themes
Make expense table editable
Delete empty expense month files

CATEGORIES
-Allow the data in the table to be categorized by user defined categories (food, transport, etc.)
-Create a graph of expenses by category (pie chart)

ERROR CHECKING
-input expense (check all values)

UPDATING
-Table update after adding expense (Oragnize the data in the table per month?)
-Log user login and logout times (for multiple profiles) (writes entries to log.txt file)
-Mainwindow problem: multiple root windows created resulting in constant running of the program in the background after closing the main window (fix by using Toplevel instead of Tk for the main window and only creating one root window for the entire program)

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
import log
import pandas as pd
from matplotlib import style 
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
global temp_expense_lines
temp_expense_lines = []
global savings_lines
savings_lines = []
global all_savings_lines
all_savings_lines = []
days = []
expenses = []

global savings
savings = 0
global income
income = 0
global spendings
spendings = 0

########################################################################################################

def get_current_time():
    now = datetime.now()
    current_time = now.strftime("%H:%M:%S")
    return current_time

def projection(months):
    result = savings + (income * months) - (spendings * months)
    return result

def simple_interest(annual_rate, years, interest_money):
    result = savings + (interest_money * annual_rate/100 * years)
    return result

def compound_interest(annual_rate, years, interest_money, periods):
    result = (savings - interest_money) + (interest_money * (1 + (annual_rate/100)/periods) ** (periods * years))
    return result

def check_expense_file(month):
    if not os.path.exists(f"data/{float(month)}_expenses.csv"):
        file = open(f"data/{float(month)}_expenses.csv", "x")
        file.close()

def check_savings_file(month):
    global savings
    if not os.path.exists(f"data/{float(month)}_savings.csv"):
        file = open(f"data/{float(month)}_savings.csv", "x")
        file.close()
        if month == current_month:
            write_savings_lines(month, [[1, savings, current_date]])

def check_data_file():
    global income, savings, spendings
    if not os.path.exists("data"):
        os.makedirs("data")

    if not os.path.exists("data/data.txt"):
        file = open("data/data.txt", "x")
        file.close()
    else:
        with open("data/data.txt", "r") as f:
            lines = f.readlines()
            income = float(lines[0].strip())
            savings = float(lines[1].strip())
            spendings = float(lines[2].strip())


def check_empty_files():
    files = glob.glob("data/*_expenses.csv") + glob.glob("data/*_savings.csv")

    for file_name in files:
        with open(file_name, "r") as f:
            reader = csv.reader(f)
            is_empty = not any(reader)
        if is_empty:
            os.remove(file_name)
    
def total_monthly_expenses():
    total = 0

    for x in expense_lines:
        total += float(x[0])
        
    print(f"Total expenses this month {total}\n")

def expenses_graph(month):
    exp = {}
    sav = {}
    temp = [] # to store different values of the same day and check which is the leatest
    leatest = []
    num1 = 0
    num2 = 0
    num3 = 0


    expense_lines = get_expense_lines(float(month))
    savings_lines = get_savings_lines(float(month))

    for x in expense_lines:
        if exp.get(int(x[2][:2])):
            num1 = float(exp.get(int(x[2][:2]))) + float(x[0])
            exp.update({int(x[2][:2]): num1})
        else:
            exp.update({int(x[2][:2]): float(x[0])})
    
    for x in savings_lines:
        if sav.get(int(x[2][:2])):
            num2 = sav.get(int(x[2][:2]))

            for y in savings_lines:
                if int(y[2][:2]) == int(x[2][:2]):
                    temp.append(y) # not currently in use / maybe future?
                    if int(y[0]) > num3:
                        num3 = int(y[0])
                        leatest = y
            
            num2 = float(leatest[1])

            sav.update({int(x[2][:2]): num2})
        else:
            sav.update({int(x[2][:2]): float(x[1])})

    days = list(dict(sorted(exp.items())).keys())
    expenses = list(exp.values())

    days_sav = list(dict(sorted(sav.items())).keys())
    savings = list(dict(sorted(sav.items())).values())

    fig = Figure(figsize=(5, 4), dpi=100)
        
    ax = fig.add_subplot(111)

    ax.plot(days, expenses, marker='o', label='Expenses')
    ax.plot(days_sav, savings, marker='s', label='Savings')

    ax.set_title(f"{float(month)} expenses")
    ax.set_xlabel("Days")
    ax.set_ylabel("Euros")
    ax.legend(loc='upper left')
    ax.grid(True)

    return fig

def monthly_expenses_graph():
    exp = {}
    temp = [] # to store different values of the same month and check which is the leatest
    savings_values = [] # to store the last savings value of each month

    files = glob.glob("data/*_expenses.csv")

    for file_name in files:
        month = os.path.basename(file_name).replace("_expenses.csv", "")

        total = 0
        with open(file_name, "r") as f:
            reader = csv.reader(f)
            for row in reader:
                total += float(row[0])

        exp[month] = total

    files = glob.glob("data/*_savings.csv")

    for file_name in files:
        temp = []
        with open(file_name, "r") as f:
            reader = csv.reader(f)
            for row in reader:
                if int(row[0]) == 1:
                    temp = row
                
                if int(row[0]) > int(temp[0]):
                    temp = row
            savings_values.append(float(temp[1]))

    months = sorted(exp.keys())
    expense_values = [exp[m] for m in months]

    fig = Figure(figsize=(6, 4), dpi=100)
    ax = fig.add_subplot(111)
    ax.plot(months, expense_values, marker='o', label='Expenses')
    ax.plot(months, savings_values, marker='s', label='Savings')

    ax.set_title("Monthly expenses")
    ax.set_xlabel("Month")
    ax.set_ylabel("Euros")
    ax.legend(loc='upper left')
    ax.grid(True)

    return fig

def get_all_expense_lines():
    global all_expense_lines
    all_expense_lines = []
    files = glob.glob("data/*_expenses.csv")

    for file_name in files:
        with open(file_name, "r") as f:
            reader = csv.reader(f)
            for row in reader:
                all_expense_lines.append(row)

def get_all_savings_lines():
    global all_savings_lines
    all_savings_lines = []
    files = glob.glob("data/*_savings.csv")

    for file_name in files:
        with open(file_name, "r") as f:
            reader = csv.reader(f)
            for row in reader:
                all_savings_lines.append(row)

# -----------------------------------------------------
def categories_distribution(month=None):
    plt.style.use('seaborn-v0_8-darkgrid')

    if month is None:
        months = get_all_months()
        all_dfs = []
        for m in months:
            filename = f"data/{m}_expenses.csv"
            df = pd.read_csv(filename, header=None)
            df.columns = ["A", "B", "C", "D"]
            all_dfs.append(df)
        df = pd.concat(all_dfs)
    else:
        filename = f"data/{month}_expenses.csv"
        df = pd.read_csv(filename, header=None)
        df.columns = ["A", "B", "C", "D"]

    df_pie = df.groupby('D', as_index=False)['A'].sum()
    df_pie = df_pie.set_index('D')

    fig, ax = plt.subplots()
    df_pie["A"].plot(
        kind="pie",
        ax=ax,
        labels=None,
        autopct=lambda pct: f"{pct:.1f}%" if pct > 5 else ""
    )

    total = df_pie["A"].sum()
    legend_labels = [f"{cat} ({val/total*100:.1f}%)" for cat, val in zip(df_pie.index, df_pie["A"])]


    ax.set_title("Categories")
    ax.legend(legend_labels, loc="upper left", bbox_to_anchor=(-0.3, 1))
    ax.set_ylabel("")
    return fig

# -----------------------------------------------------

def get_expense_lines(month):
    lines = []

    with open(f"data/{float(month)}_expenses.csv", "r") as expense_file:
        reader = csv.reader(expense_file)
        for row in reader:
            lines.append(row)
    return lines

def get_savings_lines(month):
    check_savings_file(month)
    lines = []
    with open(f"data/{float(month)}_savings.csv", "r") as savings_file:
        reader = csv.reader(savings_file)
        for row in reader:
            lines.append(row)
    return lines

def write_expense_lines(month, lines):
    with open(f"data/{float(month)}_expenses.csv", "w", newline="") as expense_file:
        writer = csv.writer(expense_file)
        writer.writerows(lines)

def write_savings_lines(month, lines):
    with open(f"data/{float(month)}_savings.csv", "w", newline="") as savings_file:
        writer = csv.writer(savings_file)
        writer.writerows(lines)

def get_all_months():
    months = set()

    files = glob.glob("data/*_expenses.csv")

    for file_name in files:
        month = os.path.basename(file_name).replace("_expenses.csv", "")
        months.add(month)

    return sorted(months)

########################################################################################################

def add_expense(expense, date, category):
    now = datetime.now()
    current_time = now.strftime("%H:%M:%S")

    expense = str(expense)
    date = str(date)
    category = str(category)

    if date[3:10] != current_month:
        global temp_expense_lines
        check_expense_file(date[3:10])
        temp_expense_lines = []
        temp_expense_lines = get_expense_lines(date[3:10])
        temp_expense_lines.append([expense, f"{current_date}-{current_time}", date, category])
        write_expense_lines(date[3:10], temp_expense_lines)

    else:
        global expense_lines
        expense_lines = []
        expense_lines = get_expense_lines(current_month)
        expense_lines.append([expense, f"{current_date}-{current_time}", date, category])
        write_expense_lines(current_month, expense_lines)
    
    all_expense_lines.append([expense, f"{current_date}-{current_time}", date, category])

def add_saving(saving):
    global savings_lines
    savings_lines = []
    savings_lines = get_savings_lines(current_month)
    num = 1

    if savings_lines:
        num = int(savings_lines[-1][0]) + 1

    savings_lines.append([num, saving, current_date])
    write_savings_lines(current_month, savings_lines)

def delete_expense(id):
    id = str(id)
    line = []

    for x in all_expense_lines:
        if x[1] == id:
            line = x
            break
    
    temp_expense_lines = get_expense_lines(line[2][3:10])
    temp_expense_lines.remove(line)
    write_expense_lines(line[2][3:10], temp_expense_lines)
    all_expense_lines.remove(line)

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
    add_saving(savings)

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
log.add("logged in")
check_empty_files()
check_data_file()
check_expense_file(current_month)
check_savings_file(current_month)
get_all_expense_lines()

#read at retrieve main data
with open("data/data.txt", "r") as file:
    lines = file.readlines()

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