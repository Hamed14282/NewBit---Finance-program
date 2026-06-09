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

def add(type, amount):
    match type:
        case "projection_calculation":
            with open("log.txt", "a") as log_file:
                log_file.write(f"Changed savings amount to {amount} euros from projection calculation on {current_date} at {get_current_time()}\n")