#pyinstaller --onefile --name Sepo --noconsole GUItest.py

""" 
TODO
Allow the user to select profiles (different users with different data files)
-Encrypt user passwords so nobody can see them in the csv file

Ability to change themes
Ability to change/choose profiles from the main page
Ability to delete profile
Ability to change name of profile
Make expense table editable
Make the format of logs better on the eyes

CATEGORIES
-Allow the data in the table to be categorized by user defined categories (food, transport, etc.)
-Create a graph of expenses by category (pie chart)

UPDATING
-Table update after adding expense (Oragnize the data in the table per month?)

CHECKING
-Check if data.txt is empty not throw an error
-Check if the users list in users.csv matches with the available folders: delete users if not
-Add synchronisation between data.txt and last savings value in *_savings.csv
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
import sys

import customtkinter
from matplotlib import pyplot as plt
import numpy as np
from datetime import datetime
from matplotlib.figure import Figure
import logtest

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

def check_file(month, type):
    global savings, income

    check_month_folder(month)

    format = ".csv"
    if type == "logs":
        format = ".txt"

    
    if not os.path.exists(f"data/{user}/{float(month)}/{float(month)}_{type}{format}"):
        file = open(f"data/{user}/{float(month)}/{float(month)}_{type}{format}", "x")
        file.close()
        logtest.create_file(type, float(month))
        if type == "savings":
            if month == current_month:
                savings += income
                write_lines(month, [[1, savings, f"01.{current_month}"]], "savings")
                logtest.add_income(f"{savings:.2f}", income, f"01.{month}")
                logtest.add_savings(f"{savings:.2f}", f"01.{month}")
            else:
                write_lines(month, [[1, income, f"01.{month}"]], "savings")
                logtest.add_savings(income, f"01.{month}")

def check_data_file():
    global income, savings, spendings
    
    if not os.path.exists(f"data/{user}/data.txt"):
        file = open(f"data/{user}/data.txt", "x")
        file.close()

def get_main_data():
    with open(f"data/{user}/data.txt", "r") as f:
            lines = f.readlines()
            if lines == None or lines == "":
                income = float(lines[0].strip())
                savings = float(lines[1].strip())
                spendings = float(lines[2].strip())
                
def check_empty_files():
    files = glob.glob(f"data/{user}/*/*_expenses.csv") + glob.glob(f"data/{user}/*/*_savings.csv") + glob.glob(f"data/{user}/*/*_logs.txt")

    for file_name in files:
        with open(file_name, "r") as f:
            reader = csv.reader(f)
            is_empty = not any(reader)
        if is_empty:
            os.remove(file_name)

def check_month_folder(month):
    if not os.path.exists(f"data/{user}/{float(month)}"):
        os.makedirs(f"data/{user}/{float(month)}")

def check_data_folder():
    if not os.path.exists("data"):
        os.makedirs("data")

#Finds the last savings value of the date inputted and returns it. If there is no savings value for that date, it returns the last savings value before that date.
def find_last_savings_value(date):
    last = "00.00.0000"
    dic = {}
    dic2 = []
    month = date[3:10]
    #check file with month, then make first savings entry on 01.XX.XXXX automatically with current income
    lines = get_lines(month, "", "savings")

    for x in lines:
        if dic.get(x[2]):
            if int(x[0]) > int(dic.get(x[2])[0]):
                dic.update({x[2]: x})
        else:
            dic.update({x[2]: x})

    if dic.get(date):
        last = float(dic.get(date)[1])
    else:
        #I want to find the last date entry exactly one before "date" and return its savings value. only works if the dates have the same format and same length (05.06.2024||13.06.2024)
        for y in dic:
            if y < date:
                dic2.append(dic.get(y))

        last = dic2[-1][1]
    return str(last)

# ##################################################################################################
# Maybe useful in the future?
#     else:
#         #I want to find the last date entry exactly one before "date" and return its savings value. only works if the dates have the same format and same length (05.06.2024||13.06.2024)
#         for y in dic:
#             dic2.append(dic.get(y))
#         if dic2[-1][2][3:10] < month: # if different month
#             last = dic2[-1][1]
#         else: # if same month
#             dic2 = []
#             for y in dic:
#                 if y < date:
#                     dic2.append(dic.get(y))
#             last = dic2[-1][1]
# ##################################################################################################

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

    expense_lines = get_lines(float(month), "", "expenses")
    savings_lines = get_lines(float(month), "", "savings")

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
    expenses = list(dict(sorted(exp.items())).values())

    days_sav = list(dict(sorted(sav.items())).keys())
    savings = list(dict(sorted(sav.items())).values())

    fig = Figure(figsize=(5, 4), dpi=100)
    ax = fig.add_subplot(111)

    ax.plot(days, expenses, marker='o', label='Expenses')
    ax.plot(days_sav, savings, marker='s', label='Savings')

    # Changes the x and y axis steps to show only multiples of 1 for x and multiples of 25 for y
    # ax.yaxis.set_major_locator(plt.MultipleLocator(25))

    #Sets x axis minimum to 1
    ax.set_xlim(left=1)

    ax.set_title(f"{float(month)} expenses")
    ax.set_xlabel("Days")
    ax.set_ylabel("Euros")
    ax.legend(loc='upper left')
    ax.grid(True)

    return fig

def monthly_expenses_graph():
    exp = {} # stores total expense value + month
    sav = {} # stores last savings value + month
    temp = [] # to store different values of the same month and check which is the leatest
    savings_values = [] # to store the last savings value of each month

    files = glob.glob(f"data/{user}/*/*_expenses.csv")

    for file_name in files:
        month = os.path.basename(file_name).replace("_expenses.csv", "")

        total = 0
        with open(file_name, "r") as f:
            reader = csv.reader(f)
            for row in reader:
                total += float(row[0])

        exp[month] = total

    files = glob.glob(f"data/{user}/*/*_savings.csv")

    for file_name in files:
        month = os.path.basename(file_name).replace("_savings.csv", "")

        temp = []
        with open(file_name, "r") as f:
            reader = csv.reader(f)
            for row in reader:
                if int(row[0]) == 1:
                    temp = row
                
                if int(row[0]) > int(temp[0]):
                    temp = row

        sav[month] = float(temp[1])

    months = sorted(exp.keys(), key=lambda x: datetime.strptime(x, "%m.%Y")) ###
    expense_values = [exp[m] for m in months]
    savings_values = [sav[m] for m in months]

    fig = Figure(figsize=(6, 4), dpi=100)
    ax = fig.add_subplot(111)

    ax.plot(months, expense_values, marker='o', label='Expenses')
    ax.plot(months, savings_values, marker='s', label='Savings')

    # Changes the y axis steps to show only multiples of 25
    # ax.yaxis.set_major_locator(plt.MultipleLocator(25))

    ax.set_title("Monthly expenses")
    ax.set_xlabel("Month")
    ax.set_ylabel("Euros")
    ax.legend(loc='upper left')
    ax.grid(True)

    return fig

def get_all_lines(type):
    all_lines = []

    files = glob.glob(f"data/{user}/*/*_{type}.csv")

    for file_name in files:
        with open(file_name, "r") as f:
            reader = csv.reader(f)
            for row in reader:
                all_lines.append(row)
    return all_lines

def get_lines(month, category, type):
    lines = []
    if type == "savings":
        check_file(month, "savings")

    if category == "":       
            with open(f"data/{user}/{float(month)}/{float(month)}_{type}.csv", "r") as file:
                reader = csv.reader(file)
                for row in reader:
                    lines.append(row)
    else:
        with open(f"data/{user}/{float(month)}/{float(month)}_{category}_{type}.csv", "r") as file:
                reader = csv.reader(file)
                for row in reader:
                    lines.append(row)
    return lines

def write_lines(month, lines, type):
    with open(f"data/{user}/{float(month)}/{float(month)}_{type}.csv", "w", newline="") as file:
        writer = csv.writer(file)
        writer.writerows(lines)

def get_all_months():
    months = set()

    files = glob.glob(f"data/{user}/*/*_expenses.csv")

    for file_name in files:
        month = os.path.basename(file_name).replace("_expenses.csv", "")
        months.add(month)

    return sorted(months, key=lambda x: datetime.strptime(x, "%m.%Y"))

def get_logs(month):
    logs = []

    if month == "all":
        files = glob.glob(f"data/{user}/*/*_logs.txt")
        for file in files:
            with open(file, "r", encoding="utf-8") as file:
                for row in file:
                    logs.append(row.strip())

        if logs == "" or logs == None:
            logs.append("No logs")
        return logs
    
    else:
        with open(f"data/{user}/{month}/{month}_logs.txt", "r", encoding="utf-8") as file:
            for row in file:
                logs.append(row.strip())

        if logs == "" or logs == None:
            logs.append("No logs")
        return logs


def get_logs_months():
    months = set()

    files = glob.glob(f"data/{user}/*/*_logs.txt")

    for file_name in files:
        month = os.path.basename(file_name).replace("_logs.txt", "")
        months.add(month)

    return sorted(months, key=lambda x: datetime.strptime(x, "%m.%Y"))


########################################################################################################

def add_expense(expense, date, category):
    now = datetime.now()
    current_time = now.strftime("%H:%M:%S")

    expense = str(expense)
    date = str(date)
    category = str(category)

    if date[3:10] != current_month:
        global temp_expense_lines
        check_file(date[3:10], "expenses")
        temp_expense_lines = []
        temp_expense_lines = get_lines(date[3:10], "", "expenses")
        temp_expense_lines.append([expense, f"{current_date}-{current_time}", date, category])
        write_lines(date[3:10], temp_expense_lines, "expenses")

    else:
        global expense_lines
        expense_lines = []
        expense_lines = get_lines(current_month, "", "expenses")
        expense_lines.append([expense, f"{current_date}-{current_time}", date, category])
        write_lines(current_month, expense_lines, "expenses")
    
    all_expense_lines.append([expense, f"{current_date}-{current_time}", date, category])

def add_saving(saving, date):
    global savings_lines
    savings_lines = []
    savings_lines = get_lines(float(date[3:10]), "", "savings")
    num = 1

    if savings_lines:
        num = int(savings_lines[-1][0]) + 1

    savings_lines.append([num, saving, date])
    write_lines(date[3:10], savings_lines, "savings")

def delete_expense(id):
    id = str(id)
    line = []

    for x in all_expense_lines:
        if x[1] == id:
            line = x
            break
    
    logtest.delete_expense(line[3], line[0], line[2])    

    last_savings = float(find_last_savings_value(line[2]))

    if line[2] == current_date:
        update_savings(last_savings + float(line[0]), line[2])
    else:
        add_saving(last_savings + float(line[0]), line[2])
        
    logtest.update_savings(last_savings + float(line[0]), last_savings)
    
    temp_expense_lines = get_lines(line[2][3:10], "", "expenses")
    temp_expense_lines.remove(line)
    write_lines(line[2][3:10], temp_expense_lines, "expenses")
    all_expense_lines.remove(line)

def save_data():
    with open(f"data/{user}/data.txt", "w") as file:
        lines[0] = str(income) + "\n"
        lines[1] = str(savings) + "\n"
        lines[2] = str(spendings) + "\n"
        file.writelines(lines)

def save_income():
    with open(f"data/{user}/data.txt", "w") as file:
        lines[0] = str(income) + "\n"
        file.writelines(lines)
    
def save_savings(date):
    with open(f"data/{user}/data.txt", "w") as file:
        lines[1] = str(savings) + "\n"
        file.writelines(lines)
    add_saving(savings, date)

def save_spendings():
    with open(f"data/{user}/data.txt", "w") as file:
        lines[2] = str(spendings) + "\n"
        file.writelines(lines)

def update_savings(amount, date):
    global savings
    savings = amount
    save_savings(date)

def update_spendings(amount):
    global spendings
    spendings = amount
    save_spendings()

def update_income(amount):
    global income
    income = amount
    save_income()

def validate_date(date_str):
    try:
        datetime.strptime(date_str, "%d.%m.%Y")
        return True
    except ValueError:
        return False

########################################################################################################

logtest.Usertest.choose()
user = logtest.Usertest.get_user()

# Closes the program if no user is selected
if user == "" or user == None:
    sys.exit()

check_file(current_month, "logs")
logtest.login("logged in")

check_data_folder()
check_empty_files()
check_data_file()

########################################################################################################

#read at retrieve main data
with open(f"data/{user}/data.txt", "r") as file:
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
    save_savings(current_date)

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
    def on_close():
        # Closes every process
        window.quit()
        # Closes window
        window.destroy()

    window.protocol("WM_DELETE_WINDOW", on_close)
    window.mainloop()

########################################################################################################

get_main_data()
check_file(current_month, "expenses")
check_file(current_month, "savings")
all_expense_lines = get_all_lines("expenses")
all_savings_lines = get_all_lines("savings")

########################################################################################################
