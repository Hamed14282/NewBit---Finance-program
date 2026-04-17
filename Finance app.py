""" 
TODO
UI
Track real date and time to know when the month is over
Create file for every month to store expense list (January_expenses)
Display expenses in a list in ui

"""

totalData = 3 #Number of constant variables in file

#Constant variables
"""
1 - income
2 - savings
3 - spendings
"""

########################################################################################################

import os

from datetime import datetime
now = datetime.now()

current_month = now.strftime("%m-%Y")
current_day = now.strftime("%d-%m-%Y")

########################################################################################################

#Non constant variables
months = 0
years = 0
annual_rate = 0
periods = 0


#read at retrieve main data
file = open("data.txt", "r")
lines = file.readlines()
file.close()

#read at retrieve expense data
expense_file = open(f"{current_month}_expenses", "r")
expense_lines = expense_file.readlines()
expense_file.close()

########################################################################################################

def accumulation():
    months = float(input("Projected months: "))
    print(f"Total savings of {savings + (income * months) - (spendings * months)} after {months} months")

def simple_interest():
    annual_rate = float(input("Annual interest rate(percentage): "))
    years = float(input("Projected months: "))/12
    print(f"After {years} years of simple interest at a rate of {annual_rate}%, the total savings amount to {savings + (savings * annual_rate/100 * years)}€ (interest withuot income)")

def compound_interest():
    annual_rate = float(input("Annual interest rate(percentage): "))
    years = float(input("Projected months: "))/12
    periods = int(input("Compounding periods per year: "))
    print(f"After {years} years of compound interest at a rate of {annual_rate}%, the total savings amount to {savings * (1 + (annual_rate/100)/periods) ** (periods * years)}€ (interest withuot income)")

def print_data():
    print(f"Income: {lines[0]}")
    print(f"Savings: {lines[1]}")
    print(f"Spendings: {lines[2]}")

def check_expense_file():
    if not os.path.exists(f"{current_month}_expenses"):
        file = open(f"{current_month}_expenses", "x")
        file.close()
    
def total_monthly_expenses():
    parts = []
    total = 0

    for x in expense_lines:
        parts = x.split(", ")
        total += float(parts[0])

    print(f"Total expenses this month {total}\n")

def save_data():
    with open("data.txt", "w") as file:
        lines[0] = str(income) + "\n"
        lines[1] = str(savings) + "\n"
        lines[2] = str(spendings) + "\n"
        file.writelines(lines)
    
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
    check_expense_file()

    expense = input("Input an expense(euros): ")
    now = datetime.now()
    current_time = now.strftime("%H:%M:%S")
    expense_lines.append(f"{expense}, {current_time}, {current_day}\n")

    expense_file = open(f"{current_month}_expenses", "w")
    expense_file.writelines(expense_lines)
    expense_file.close()

########################################################################################################

while len(lines) < totalData:
    lines.append("\n")

if lines[0].strip() == "":
    income = float(input("Initial income missing, enter initial income: "))
else:
    income = float(lines[0].strip())

if lines[1].strip() == "":
    savings = float(input("Initial savings missing, enter initial savings: "))
else:
    savings = float(lines[1].strip())

if lines[2].strip() == "":
    spendings = float(input("Initial spendings missing, enter initial spendings: "))
else:
    spendings = float(lines[2].strip())

save_data()
########################################################################################################

print_data()
print("0.End program")
print("1.Projection calculations")
print("2.Interest")
print("3.Print all saved data")
print("4.Change income value")
print("5.Change savings value")
print("6.Change spendings value")
print("7.Add expense")
print("8.Total expenses this month")
print("9.-")

option = -1
while option != 0:
    option = int(input("Select an option: "))
    match (option):
        case 0:
            break
        case 1:
            accumulation()
            
        case 2:
            print("1.Simple interest\n2.Compound interest")
            option = int(input("Select the interest type: "))
            match (option):
                case 1:
                    simple_interest()
                case 2:
                    compound_interest()
        case 3:
            print_data()
        case 4:
            change_income()
        case 5:
            change_savings()
        case 6:
            change_spendings()
        case 7:
            add_expense()
        case 8: 
            total_monthly_expenses()

########################################################################################################

save_data()

########################################################################################################

print("End of program")