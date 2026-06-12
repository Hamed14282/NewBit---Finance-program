from datetime import datetime

now = datetime.now()
current_month = now.strftime("%m.%Y")
current_day = now.strftime("%d")
current_date = now.strftime("%d.%m.%Y")

def get_current_time():
    now = datetime.now()
    current_time = now.strftime("%H:%M:%S")
    return current_time

def login(type):
    match type:
        case "logged in":
            with open(f"logs/{float(current_month)}_logs.txt", "a") as log_file:
                log_file.write(f"{current_date} - {get_current_time()} || Logged in\n")

        case "logged out":
            with open(f"logs/{float(current_month)}_logs.txt", "a") as log_file:
                log_file.write(f"{current_date} - {get_current_time()} || Logged out\n")

def change_values(type, amount): #types: Income, Savings, Spendings
    with open(f"logs/{float(current_month)}_logs.txt", "a") as log_file:
        log_file.write(f"{current_date} - {get_current_time()} || {type} changed to {amount} euros\n")

def projection_calculation(savings):
    with open(f"logs/{float(current_month)}_logs.txt", "a") as log_file:
        log_file.write(f"{current_date} - {get_current_time()} || Changed savings amount to {savings} euros from projection calculation\n")
        
def add_expense(category, amount, date):
    with open(f"logs/{float(current_month)}_logs.txt", "a") as log_file:
        log_file.write(f"{current_date} - {get_current_time()} || Added expense: {category}, {amount} euros, {date}\n")

def add_income(savings, income, date):
    with open(f"logs/{float(current_month)}_logs.txt", "a") as log_file:
        log_file.write(f"{current_date} - {get_current_time()} || Increased savings amount from {(float(savings) - float(income)):.2f} to {savings} euros by adding income of {income} euros for {date}\n")

def add_savings(savings, date):
    with open(f"logs/{float(current_month)}_logs.txt", "a") as log_file:
        log_file.write(f"{current_date} - {get_current_time()} || Added savings of {savings} euros for {date}\n")

def update_savings(amount, previous_amount):
    with open(f"logs/{float(current_month)}_logs.txt", "a") as log_file:
        log_file.write(f"{current_date} - {get_current_time()} || Updated savings from {previous_amount:.2f} to {amount:.2f} euros due to change in expense\n")

def delete_expense(category, amount, date):
    with open(f"logs/{float(current_month)}_logs.txt", "a") as log_file:
        log_file.write(f"{current_date} - {get_current_time()} || Deleted expense: {category}, {amount} euros, {date}\n")

def create_file(type, month): #types: expenses, savings
    with open(f"logs/{float(current_month)}_logs.txt", "a") as log_file:
        log_file.write(f"{current_date} - {get_current_time()} || Created {type} file for {month}\n")



#############################################################################################
#LOG ERRORS

def invalid_date_format(input):
    pass

#for projection calc, change_value(), simple and compound interest, add expense,
def invalid_input(type, input): #types: income, savings, spendings, months, expense, date, 
    match type:
        case "1":
            pass
        case "2":
            pass

#for add expense,
def no_input(type, input): #types: categories, expense, date, (EVERYWHERE)
    match type:
        case "1":
            pass
        case "2":
            pass
