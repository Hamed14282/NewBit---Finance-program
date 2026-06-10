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
            with open("log.txt", "a") as log_file:
                log_file.write(f"Logged in on {current_date} at {get_current_time()}\n")

        case "logged out":
            with open("log.txt", "a") as log_file:
                log_file.write(f"Logged out on {current_date} at {get_current_time()}\n")

def change_values(type, amount):
    match type:
        case "income":
            with open("log.txt", "a") as log_file:
                log_file.write(f"Income changed to {amount} euros on {current_date} at {get_current_time()}\n")

        case "savings":
            with open("log.txt", "a") as log_file:
                log_file.write(f"Savings changed to {amount} euros on {current_date} at {get_current_time()}\n")

        case "spendings":
            with open("log.txt", "a") as log_file:
                log_file.write(f"Spendings changed to {amount} euros on {current_date} at {get_current_time()}\n")

def projection_calculation(amount):
    with open("log.txt", "a") as log_file:
        log_file.write(f"Changed savings amount to {amount} euros from projection calculation on {current_date} at {get_current_time()}\n")
        
def add_expense(category, amount, date):
    with open("log.txt", "a") as log_file:
        log_file.write(f"Added expense: {category}, {amount} euros, {date} || on {current_date} at {get_current_time()}\n")

def update_savings(amount, previous_amount):
    with open("log.txt", "a") as log_file:
        log_file.write(f"Updated savings from {previous_amount} to {amount} euros due to change in expense on {current_date} at {get_current_time()}\n")

def delete_expense(category, amount, date):
    with open("log.txt", "a") as log_file:
        log_file.write(f"Deleted expense: {category}, {amount} euros, {date} || on {current_date} at {get_current_time()}\n")