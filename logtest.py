from datetime import datetime
import Usertest

now = datetime.now()
current_month = now.strftime("%m.%Y")
current_day = now.strftime("%d")
current_date = now.strftime("%d.%m.%Y")

def get_user():
    return Usertest.get_user()

def get_current_time():
    now = datetime.now()
    current_time = now.strftime("%H:%M:%S")
    return current_time

def login(type):
    user = get_user()
    match type:
        case "logged in":
            with open(f"data/{user}/{float(current_month)}/{float(current_month)}_logs.txt", "a") as log_file:
                log_file.write(f"{current_date} - {get_current_time()} || Logged in as {user}\n") #Logged in as ___ USER

        case "logged out":
            with open(f"data/{user}/{float(current_month)}/{float(current_month)}_logs.txt", "a") as log_file:
                log_file.write(f"{current_date} - {get_current_time()} || Logged out as {user}\n") #Logged out as ___ USER

def change_values(type, amount): #types: Income, Savings, Spendings
    user = get_user()
    with open(f"data/{user}/{float(current_month)}/{float(current_month)}_logs.txt", "a") as log_file:
        log_file.write(f"{current_date} - {get_current_time()} |Change Values| {type} changed to {amount} euros\n")

def projection_calculation(savings):
    user = get_user()
    with open(f"data/{user}/{float(current_month)}/{float(current_month)}_logs.txt", "a") as log_file:
        log_file.write(f"{current_date} - {get_current_time()} |Projection Calc.| Changed savings amount to {savings} euros from projection calculation\n")
        
def add_expense(category, amount, date):
    user = get_user()
    with open(f"data/{user}/{float(current_month)}/{float(current_month)}_logs.txt", "a") as log_file:
        log_file.write(f"{current_date} - {get_current_time()} |Add Expense| Added expense: {category}, {amount} euros, {date}\n")

def add_income(savings, income, date):
    user = get_user()
    with open(f"data/{user}/{float(current_month)}/{float(current_month)}_logs.txt", "a") as log_file:
        log_file.write(f"{current_date} - {get_current_time()} |Auto| Increased savings amount from {(float(savings) - float(income)):.2f} to {savings} euros by adding income of {income} euros for {date}\n")

def add_savings(savings, date):
    user = get_user()
    with open(f"data/{user}/{float(current_month)}/{float(current_month)}_logs.txt", "a") as log_file:
        log_file.write(f"{current_date} - {get_current_time()} |Auto| Added savings of {savings} euros for {date}\n")

def update_savings(amount, previous_amount):
    user = get_user()
    with open(f"data/{user}/{float(current_month)}/{float(current_month)}_logs.txt", "a") as log_file:
        log_file.write(f"{current_date} - {get_current_time()} |Auto| Updated savings from {previous_amount:.2f} to {amount:.2f} euros due to change in expense\n")

def delete_expense(category, amount, date):
    user = get_user()
    with open(f"data/{user}/{float(current_month)}/{float(current_month)}_logs.txt", "a") as log_file:
        log_file.write(f"{current_date} - {get_current_time()} |Table| Deleted expense: {category}, {amount} euros, {date}\n")

def create_file(type, month): #types: expenses, savings
    user = get_user()
    with open(f"data/{user}/{float(current_month)}/{float(current_month)}_logs.txt", "a") as log_file:
        log_file.write(f"{current_date} - {get_current_time()} |Auto| Created {type} file for {month}\n")



#############################################################################################
#LOG ERRORS

def invalid_input(type, input, data):
    user = get_user()
    match type:
        case "expense":
            with open(f"data/{user}/{float(current_month)}/{float(current_month)}_logs.txt", "a") as log_file:
                log_file.write(f"{current_date} - {get_current_time()} |Add Expense| Invalid expense input: {input} (Please enter a number greater than zero, and seperate decimals with a period.)\n")

        case "date format":
            with open(f"data/{user}/{float(current_month)}/{float(current_month)}_logs.txt", "a") as log_file:
                log_file.write(f"{current_date} - {get_current_time()} |Add Expense| Invalid date format: {input} (Please enter date as DD.MM.YYYY.)\n")

        case "months":
            with open(f"data/{user}/{float(current_month)}/{float(current_month)}_logs.txt", "a") as log_file:
                log_file.write(f"{current_date} - {get_current_time()} |Projection Calc.| Invalid projected months input: {input} (Please enter a number greater than zero.)\n")

        case "savings":
            with open(f"data/{user}/{float(current_month)}/{float(current_month)}_logs.txt", "a") as log_file:
                log_file.write(f"{current_date} - {get_current_time()} |Simple Interest| Invalid portion of savings affected by interest: {input} (Please enter a value between 0 and {data})\n")

        case "interest rate":
            with open(f"data/{user}/{float(current_month)}/{float(current_month)}_logs.txt", "a") as log_file:
                log_file.write(f"{current_date} - {get_current_time()} |Simple Interest| Invalid annual interest rate input: {input} (Please enter a number greater than zero.)\n")

        case "months1":
            with open(f"data/{user}/{float(current_month)}/{float(current_month)}_logs.txt", "a") as log_file:
                log_file.write(f"{current_date} - {get_current_time()} |Simple Interest| Invalid projected months input: {input} (Please enter a number greater than zero.)\n")

        case "savings1":
            with open(f"data/{user}/{float(current_month)}/{float(current_month)}_logs.txt", "a") as log_file:
                log_file.write(f"{current_date} - {get_current_time()} |Compound Interest| Invalid portion of savings affected by interest: {input} (Please enter a value between 0 and {data})\n")

        case "interest rate1":
            with open(f"data/{user}/{float(current_month)}/{float(current_month)}_logs.txt", "a") as log_file:
                log_file.write(f"{current_date} - {get_current_time()} |Compound Interest| Invalid annual interest rate input: {input} (Please enter a number greater than zero.)\n")

        case "months2":
            with open(f"data/{user}/{float(current_month)}/{float(current_month)}_logs.txt", "a") as log_file:
                log_file.write(f"{current_date} - {get_current_time()} |Compound Interest| Invalid projected months input: {input} (Please enter a number greater than zero.)\n")

        case "periods":
            with open(f"data/{user}/{float(current_month)}/{float(current_month)}_logs.txt", "a") as log_file:
                log_file.write(f"{current_date} - {get_current_time()} |Compound Interest| Invalid compounding periods input: {input} (Please enter a number greater than zero.)\n")

        case "income":
            with open(f"data/{user}/{float(current_month)}/{float(current_month)}_logs.txt", "a") as log_file:
                log_file.write(f"{current_date} - {get_current_time()} |Change Values| Invalid income input: {input} (Please enter a number greater than zero.)\n")

        case "savings2":
            with open(f"data/{user}/{float(current_month)}/{float(current_month)}_logs.txt", "a") as log_file:
                log_file.write(f"{current_date} - {get_current_time()} |Change Values| Invalid savings input: {input} (Please enter a number greater than or equal to zero.)\n")

        case "spendings":
            with open(f"data/{user}/{float(current_month)}/{float(current_month)}_logs.txt", "a") as log_file:
                log_file.write(f"{current_date} - {get_current_time()} |Change Values| Invalid spendings input: {input} (Please enter a number greater than or equal to zero.)\n")

def no_input(type):
    user = get_user()
    match type:
        case "expense":
            with open(f"data/{user}/{float(current_month)}/{float(current_month)}_logs.txt", "a") as log_file:
                log_file.write(f"{current_date} - {get_current_time()} |Add Expense| No expense amount entered.\n")

        case "date":
            with open(f"data/{user}/{float(current_month)}/{float(current_month)}_logs.txt", "a") as log_file:
                log_file.write(f"{current_date} - {get_current_time()} |Add Expense| No date entered. Using current date: {current_date}\n")

        case "category":
            with open(f"data/{user}/{float(current_month)}/{float(current_month)}_logs.txt", "a") as log_file:
                log_file.write(f"{current_date} - {get_current_time()} |Add Expense| No category entered. Using default category: misc.\n")

        case "months":
            with open(f"data/{user}/{float(current_month)}/{float(current_month)}_logs.txt", "a") as log_file:
                log_file.write(f"{current_date} - {get_current_time()} |Projection Calc.| No projected months entered.\n")

        case "savings":
            with open(f"data/{user}/{float(current_month)}/{float(current_month)}_logs.txt", "a") as log_file:
                log_file.write(f"{current_date} - {get_current_time()} |Simple Interest| No portion of savings affected by interest entered.\n")

        case "interest rate":
            with open(f"data/{user}/{float(current_month)}/{float(current_month)}_logs.txt", "a") as log_file:
                log_file.write(f"{current_date} - {get_current_time()} |Simple Interest| No annual interest rate entered.\n")

        case "months1":
            with open(f"data/{user}/{float(current_month)}/{float(current_month)}_logs.txt", "a") as log_file:
                log_file.write(f"{current_date} - {get_current_time()} |Simple Interest| No projected months entered.\n")

        case "savings1":
            with open(f"data/{user}/{float(current_month)}/{float(current_month)}_logs.txt", "a") as log_file:
                log_file.write(f"{current_date} - {get_current_time()} |Compound Interest| No portion of savings affected by interest entered.\n")

        case "interest rate1":
            with open(f"data/{user}/{float(current_month)}/{float(current_month)}_logs.txt", "a") as log_file:
                log_file.write(f"{current_date} - {get_current_time()} |Compound Interest| No annual interest rate entered.\n")

        case "months2":
            with open(f"data/{user}/{float(current_month)}/{float(current_month)}_logs.txt", "a") as log_file:
                log_file.write(f"{current_date} - {get_current_time()} |Compound Interest| No projected months entered.\n")

        case "periods":
            with open(f"data/{user}/{float(current_month)}/{float(current_month)}_logs.txt", "a") as log_file:
                log_file.write(f"{current_date} - {get_current_time()} |Compound Interest| No compounding periods entered.\n")

        case "income":
            with open(f"data/{user}/{float(current_month)}/{float(current_month)}_logs.txt", "a") as log_file:
                log_file.write(f"{current_date} - {get_current_time()} |Change Values| No income value entered.\n")

        case "savings2":
            with open(f"data/{user}/{float(current_month)}/{float(current_month)}_logs.txt", "a") as log_file:
                log_file.write(f"{current_date} - {get_current_time()} |Change Values| No savings value entered.\n")

        case "spendings":
            with open(f"data/{user}/{float(current_month)}/{float(current_month)}_logs.txt", "a") as log_file:
                log_file.write(f"{current_date} - {get_current_time()} |Change Values| No spendings value entered.\n")

def dummy():
    user = get_user()
    with open(f"data/{user}/{float(current_month)}/{float(current_month)}_logs.txt", "a") as log_file:
        log_file.write(f"{current_date} - {get_current_time()} |Table| Dummy pressed delete without selecting anything in the table\n")
