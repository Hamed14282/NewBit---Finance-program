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

def decrypt_file(path):
    global key
    cypher = Fernet(key)

    with open(path, "rb") as encrypted_file:
        encrypted = encrypted_file.read()

    if not encrypted == b"":
        decrypted = cypher.decrypt(encrypted)

        with open(path, "wb") as decrypted_file:
            decrypted_file.write(decrypted)
    else:
        decrypted = b""

    return decrypted

def encrypt_file(path):
    global key
    cypher = Fernet(key)

    with open("data/users.csv", "rb") as decrypted_file:
        decrypted = decrypted_file.read()

    encrypted = cypher.encrypt(decrypted)

    with open("data/users.csv", "wb") as encrypted_file:
        encrypted_file.write(encrypted)

def get_all_users():
    global users, users_list, key


    #DECRYPT###########################################

    decrypted = decrypt_file("data/users.csv")

    ###################################################
    if not decrypted == b"":
        with open("data/users.csv", "r") as file:
                reader = csv.reader(file)
                for row in reader:
                    users.append(row)
                    users_list.append(row[0])

    #REWRITE ENCRYPTED#################################

    encrypt_file("data/users.csv")

    ###################################################
    
def save_new_user(new_user):
    global users, key
    users.append(new_user)

    #DECRYPT###########################################

    decrypt_file("data/users.csv")

    #######################################################################

    with open(f"data/users.csv", "w", newline="") as file:
        writer = csv.writer(file)
        writer.writerows(users)

    #ENCRYPT######################################################################

    encrypt_file("data/users.csv")

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
            popup_window("Error", "Wrong password entered")

    button1 = customtkinter.CTkButton(master=frame1, text="Login", command=lambda:pass_check(entry1.get()))
    button1.grid(row=0, column=2, pady=10, padx=10)
    
    def on_close():
        # Closes every process
        window.quit()
        # Closes window
        window.destroy()

    window.protocol("WM_DELETE_WINDOW", on_close)
    window.mainloop()

def popup_window(type, message):
    window1 = customtkinter.CTk()
    window1.title(type)
    
    frame1 = customtkinter.CTkFrame(master=window1)
    frame1.grid(row=0, column=0, pady=5, padx=10)
    
    label1 = customtkinter.CTkLabel(master=frame1, text=message, font=("Arial", 20))
    label1.grid(row=0, column=0, pady=5, padx=5)

    def close():
        # Closes every process
        window1.quit()
        # Closes window
        window1.destroy()

    window1.protocol("WM_DELETE_WINDOW", close)
    window1.mainloop()

def check_password(user, old_pass, new_pass):
    global users
    pass1 = ""
    
    for user1 in users:
        if user1[0] == user:
            pass1 = user1[1]
    
    if not old_pass == pass1:
        popup_window("Error", "Wrong password entered")

    else:
        change_password(user, new_pass)

def change_password(user, new_pass):
    global users
    x = 0
    for user1 in users:
        if user1[0] == user:
            users[x] = [user, new_pass]

            popup_window("Info", "Password changed successfully")
            break
        
        x += 1

def choose():
    global users, user, temp_choice
    
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

        if frame1.grid_slaves(row=2, column=1):
            for widget in frame1.grid_slaves(row=2, column=1):
                widget.destroy()

        if frame1.grid_slaves(row=2, column=2):
            for widget in frame1.grid_slaves(row=2, column=2):
                widget.destroy()

        if frame1.grid_slaves(row=2, column=3):
            for widget in frame1.grid_slaves(row=2, column=3):
                widget.destroy()

        if frame1.grid_slaves(row=3, column=2):
            for widget in frame1.grid_slaves(row=3, column=2):
                widget.destroy()

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
            
            case "Delete User":
                pass

            case "Change Password":

                combobox = customtkinter.CTkComboBox(master=frame1, values=["-Select User-", *users_list], command=save)
                combobox.grid(row=2, column=1, pady=10, padx=10)

                entry1 = customtkinter.CTkEntry(master=frame1, placeholder_text="Enter old password")
                entry1.grid(row=2, column=2, pady=10, padx=10)

                entry2 = customtkinter.CTkEntry(master=frame1, placeholder_text="Enter new password")
                entry2.grid(row=3, column=2, pady=10, padx=10)

                def change():
                    old_password = entry1.get()
                    new_password = entry2.get()

                    check_password(temp_choice, old_password, new_password)

                button1 = customtkinter.CTkButton(master=frame1, text="Apply", command=change)
                button1.grid(row=2, column=3, pady=10, padx=10)

    if not users:
        select("Add New")
        combobox = customtkinter.CTkComboBox(master=frame1, values=[ "Add New", "Select Existing", "Change Password", "Delete User"], command=select)
        combobox.grid(row=2, column=0, pady=10, padx=10)

    else:
        select("Select Existing") # Show list of existing users by default
        combobox = customtkinter.CTkComboBox(master=frame1, values=["Select Existing", "Add New", "Change Password", "Delete User"], command=select)
        combobox.grid(row=2, column=0, pady=10, padx=10)

    def on_close():
        # Closes every process
        window.quit()
        # Closes window
        window.destroy()
    
    window.protocol("WM_DELETE_WINDOW", on_close)
    window.mainloop()
    return user