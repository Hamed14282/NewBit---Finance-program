import csv
import os
from cryptography.fernet import Fernet

import customtkinter

user = ""
users = []
users_list = []
temp_choice = ""
key = ""

def check_key():
    global key

    if not os.path.exists("data/users.key"):
        with open("data/users.key", "wb") as key_file:
            key_file.write(Fernet.generate_key())
    with open("data/users.key", "rb") as key_file:
        key = key_file.read()

def get_user():
    global user
    user1 = user
    return user1

def check_users_file():
    if not os.path.exists("data/users.csv"):
        file = open("data/users.csv", "x")
        file.close()

def check_user_folder():
    global user
    if not os.path.exists(f"data/{user}"):
        os.makedirs(f"data/{user}")

def get_all_users():
    global users, users_list, key


    #DECRYPT######################################################################
    cypher = Fernet(key)

    with open("data/users.csv", "rb") as encrypted_file:
        encrypted = encrypted_file.read()

    if not encrypted == b"":
        decrypted = cypher.decrypt(encrypted)

        with open("data/users.csv", "wb") as decrypted_file:
            decrypted_file.write(decrypted)

    #######################################################################

        with open("data/users.csv", "r") as file:
                reader = csv.reader(file)
                for row in reader:
                    users.append(row)
                    users_list.append(row[0])

    #REWRITE ENCRYPTED######################################################################
        with open("data/users.csv", "wb") as encrypted_file:
            encrypted_file.write(encrypted)

    #######################################################################
    
def save_new_user(new_user):
    global users, key
    users.append(new_user)

    #DECRYPT######################################################################
    cypher = Fernet(key)

    with open("data/users.csv", "rb") as encrypted_file:
        encrypted = encrypted_file.read()

    if not encrypted == b"":
        decrypted = cypher.decrypt(encrypted)

        with open("data/users.csv", "wb") as decrypted_file:
            decrypted_file.write(decrypted)

    #######################################################################

    with open(f"data/users.csv", "w", newline="") as file:
        writer = csv.writer(file)
        writer.writerows(users)

    #ENCRYPT######################################################################

    with open("data/users.csv", "rb") as decrypted_file:
        decrypted = decrypted_file.read()

    encrypted = cypher.encrypt(decrypted)

    with open("data/users.csv", "wb") as encrypted_file:
        encrypted_file.write(encrypted)

    #######################################################################

def save_selection(select):
    global user
    user = select

def save(select): #Throw error if value is "-Select-"
    global temp_choice
    temp_choice = select

def ask_password(current_user):
    global users
    password = ""

    for user in users:
        if user[0] == current_user:
            password = user[1]
    
    window = customtkinter.CTk()
    window.title("Log in")

    frame1 = customtkinter.CTkFrame(master=window)
    frame1.grid(row=0, column=0, pady=5, padx=10)
    
    label1 = customtkinter.CTkLabel(master=frame1, text="Enter password", font=("Arial", 14))
    label1.grid(row=0, column=0, pady=5, padx=5)

    entry1 = customtkinter.CTkEntry(master=frame1, placeholder_text="")
    entry1.grid(row=0, column=1, pady=5, padx=5)

    def pass_check(entry):
        global temp_choice

        if entry == password:
            save_selection(temp_choice)
            check_user_folder()

            # Closes every process
            window.quit()
            # Closes window
            window.destroy()
        
        else:
            window1 = customtkinter.CTk()
            window1.title("Error")
            
            frame1 = customtkinter.CTkFrame(master=window1)
            frame1.grid(row=0, column=0, pady=5, padx=10)
            
            label1 = customtkinter.CTkLabel(master=frame1, text="Wrong password entered", font=("Arial", 20))
            label1.grid(row=0, column=0, pady=5, padx=5)

            def close():
                # Closes every process
                window.quit()
                # Closes window
                window.destroy()

            window.protocol("WM_DELETE_WINDOW", close)
            window1.mainloop()

    button1 = customtkinter.CTkButton(master=frame1, text="Login", command=lambda:pass_check(entry1.get()))
    button1.grid(row=0, column=2, pady=10, padx=10)
    
    def on_close():
        # Closes every process
        window.quit()
        # Closes window
        window.destroy()

    window.protocol("WM_DELETE_WINDOW", on_close)
    window.mainloop()

def choose():
    global users, user
    
    check_key()
    check_users_file()
    get_all_users()

    window = customtkinter.CTk()
    window.title("Login page")

    frame1 = customtkinter.CTkFrame(master=window)
    frame1.grid(row=0, column=0, pady=5, padx=10)
    
    label1 = customtkinter.CTkLabel(master=frame1, text="Select User", font=("Roboto", 24))
    label1.grid(row=0, column=1, columnspan=2, pady=10, padx=10)

    label2 = customtkinter.CTkLabel(master=frame1, text="Choose profile:", font=("Roboto", 17))
    label2.grid(row=1, column=0, pady=2, padx=10)

    def select(choice):
        match choice:
            case "Select Existing":
                combobox = customtkinter.CTkComboBox(master=frame1, values=["-Select-", *users_list], command=save)
                combobox.grid(row=2, column=1, pady=10, padx=10)

                def on_login():
                    ask_password(temp_choice)
                    
                    # Closes every process
                    window.quit()
                    # Closes window
                    window.destroy()

                button1 = customtkinter.CTkButton(master=frame1, text="Login", command=on_login)
                button1.grid(row=2, column=3, pady=10, padx=10)

            case "Add New":
                entry1 = customtkinter.CTkEntry(master=frame1, placeholder_text="Enter new user")
                entry1.grid(row=2, column=1, pady=10, padx=10)

                entry2 = customtkinter.CTkEntry(master=frame1, placeholder_text="Enter password")
                entry2.grid(row=2, column=2, pady=10, padx=10)

                def on_login():
                    new_user_value = entry1.get()
                    password = entry2.get()

                    save_new_user([new_user_value, password])
                    save_selection(new_user_value)
                    check_user_folder()

                    # Closes every process
                    window.quit()
                    # Closes window
                    window.destroy()

                button1 = customtkinter.CTkButton(master=frame1, text="Login", command=on_login)
                button1.grid(row=2, column=3, pady=10, padx=10)

    if not users:
        select("Add New")
        combobox = customtkinter.CTkComboBox(master=frame1, values=[ "Add New", "Select Existing"], command=select)
        combobox.grid(row=2, column=0, pady=10, padx=10)

    else:
        select("Select Existing") # Show list of existing users by default
        combobox = customtkinter.CTkComboBox(master=frame1, values=["Select Existing", "Add New"], command=select)
        combobox.grid(row=2, column=0, pady=10, padx=10)

    def on_close():
        # Closes every process
        window.quit()
        # Closes window
        window.destroy()
    
    window.protocol("WM_DELETE_WINDOW", on_close)
    window.mainloop()
    return user