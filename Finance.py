#pyinstaller GUItest.py --onefile --noconsole

""" 
TODO
UI
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

from datetime import datetime
now = datetime.now()

current_month = now.strftime("%m-%Y")
current_day = now.strftime("%d")

########################################################################################################

#Non constant variables
months = 0
years = 0
annual_rate = 0
periods = 0
global expense_lines
expense_lines = []
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
    plt.close('all')
    plt.title(f"{current_month} expenses")
    plt.xlabel("Days")
    plt.ylabel("Expenses(Euros)")

    exp = {}    
    num = 0
    
    for x in expense_lines:
        if exp.get(x[2]):
            num = float(exp.get(x[2])) + float(x[0])
            exp.update({x[2]: num})
        else:
            exp.update({x[2]: float(x[0])})
    
    days = list(exp.keys())
    expenses = list(exp.values())
    plt.plot(days, expenses)
    plt.show()

def monthly_expenses_graph():
    plt.close('all')
    plt.title("Monthly expenses")
    plt.xlabel("Month")
    plt.ylabel("Expenses (Euros)")

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

    plt.plot(months, values)
    plt.show()

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

def add_expense():
    expense = input("Input an expense(euros): ")
    now = datetime.now()
    current_time = now.strftime("%H:%M:%S")

    global expense_lines
    expense_lines.append([expense, current_time, current_day])

    with open(f"data/{current_month}_expenses.csv", "w", newline="") as expense_file:
        writer = csv.writer(expense_file)
        writer.writerows(expense_lines)

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

########################################################################################################

check_data_file()
check_expense_file()

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

# print_data()
# print("0.End program")
# #print("1.Projection calculations")
# print("2.Interest")


# # print("4.Change income value")
# # print("5.Change savings value")
# # print("6.Change spendings value")


#### table of expenses with all the data (amount, time, day) and a total of all the data for current month (also include the option to select other months in the future)
# print("7.Add expense")
# print("8.Total expenses this month")
# print("3.Print all saved data")


# print("9.Graph expenses (current month)")
# print("10.Graph expenses (all months)")
# print("11.-")

# option = -1
# while option != 0:
#     option = int(input("Select an option: "))
#     match (option):
#         case 0:
#             break
#         case 1:
#             projection()
            
#         case 2:
#             print("1.Simple interest\n2.Compound interest")
#             option = int(input("Select the interest type: "))
#             match (option):
#                 case 1:
#                     simple_interest()
#                 case 2:
#                     compound_interest()
#         case 3:
#             print_data()
#         case 4:
#             change_income()
#         case 5:
#             change_savings()
#         case 6:
#             change_spendings()
#         case 7:
#             add_expense()
#         case 8: 
#             total_monthly_expenses()
#         case 9: 
#             expenses_graph()
#         case 10: 
#             monthly_expenses_graph()

########################################################################################################

# print("End of program")