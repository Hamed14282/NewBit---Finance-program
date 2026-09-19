import csv
import os
import random
from cryptography.fernet import Fernet

import customtkinter

user = ""
users = []
users_list = []
user_id = ""
user_ids_list = []
temp_choice = ""
key = ""
decrypted = []

def check_key():
    global key

    if not os.path.exists("data/users.key"):
        with open("data/users.key", "wb") as key_file:
            key_file.write(Fernet.generate_key())
    with open("data/users.key", "rb") as key_file:
        key = key_file.read()

def get_user():
    global user
    return user

def get_user_id():
    global user_id
    check_user_id()
    return user_id

def check_users_file():
    if not os.path.exists("data/users.csv"):
        file = open("data/users.csv", "x")
        file.close()

def check_user_folder():
    global user_id
    if not os.path.exists(f"data/{user_id}"):
        os.makedirs(f"data/{user_id}")

def decrypt_file(path):
    global key, decrypted
    
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

def check_user_id():
    global user_id, users

    for user1 in users:
        if user1[0] == user:
            user_id = user1[2]

def check_user_id(user):
    global users

    for user1 in users:
        if user1[0] == user:
            user_id = user1[2]

    return user_id

def delete_user(user_id):
    global users, users_list, user_ids_list, temp_choice

    #Removes User from users.csv ######################################################################

    x = 0

    for user1 in users:
        if user1[2] == user_id:
            del users[x]

        x += 1

    #DECRYPT###########################################

    decrypt_file("data/users.csv")

    #######################################################################

    with open(f"data/users.csv", "w", newline="") as file:
        writer = csv.writer(file)
        writer.writerows(users)

    #ENCRYPT######################################################################

    encrypt_file("data/users.csv")

    #Removes User from users list ######################################################################

    for user1 in users_list:
        if user1 == temp_choice:
            users_list.remove(user1)

    #Removes User ID from list ######################################################################

    for id in user_ids_list:
        if id == user_id:
            user_ids_list.remove(id)

    #Removes User data folder ######################################################################

    if os.path.exists(f"data/{user_id}"):
        for root, dirs, files in os.walk(f"data/{user_id}", topdown=False):
            for name in files:
                os.remove(os.path.join(root, name))
            for name in dirs:
                os.rmdir(os.path.join(root, name))
                
        os.rmdir(f"data/{user_id}")

def get_all_users():
    global users, users_list, user_ids_list, key, decrypted
    users = []
    users_list = []
    user_ids_list = []


    #DECRYPT########################################### not necessary?

    decrypted = decrypt_file("data/users.csv")

    ###################################################
    if not decrypted == b"":
        with open("data/users.csv", "r") as file:
                reader = csv.reader(file)
                for row in reader:
                    users.append(row)
                    users_list.append(row[0])
                    user_ids_list.append(row[2])

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

def check_password(user, old_pass):
    global users
    pass1 = ""
    
    for user1 in users:
        if user1[0] == user:
            pass1 = user1[1]
    
    if not old_pass == pass1:
        popup_window("Error", "Wrong password entered")
        return False
    
    else:
        return True

def change_password(user, new_pass):
    global users
    x = 0

    for user1 in users:
        if user1[0] == user:
            users[x] = [user, new_pass]

        x += 1

    #DECRYPT###########################################

    decrypt_file("data/users.csv")

    #######################################################################

    with open(f"data/users.csv", "w", newline="") as file:
        writer = csv.writer(file)
        writer.writerows(users)

    #ENCRYPT######################################################################

    encrypt_file("data/users.csv")

    #######################################################################
    
    popup_window("Info", "Password changed successfully")

    #Add log for changing password

def change_username(old_username, new_username):
    global users
    x = 0

    for user1 in users:
        if user1[0] == old_username:
            user1[0] = new_username
            users[x] = user1

        x += 1

    #DECRYPT###########################################

    decrypt_file("data/users.csv")

    #######################################################################

    with open(f"data/users.csv", "w", newline="") as file:
        writer = csv.writer(file)
        writer.writerows(users)

    #ENCRYPT######################################################################

    encrypt_file("data/users.csv")

    #######################################################################
    
    popup_window("Info", "Username changed successfully")

    get_all_users()

    #Add log for changing username

def gen_id(r):

    id = ""

    set = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0, "a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z", "A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
    
    for i in range(r):
        random_num = random.randint(0, len(set)-1)
        id += str(set[random_num])

    return id

def check_id(id):
    global user_ids_list

    for name in user_ids_list:
        if name == id:
            return True

        return False

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

                entry1 = customtkinter.CTkEntry(master=frame1, placeholder_text="Enter password")
                entry1.grid(row=2, column=2, pady=10, padx=10)
                
                def on_login():
                    
                    if check_password(temp_choice, entry1.get()):
                        save_selection(temp_choice)
                        check_user_folder()

                        # Closes every process
                        window.quit()
                        # Closes window
                        window.destroy()

                button1 = customtkinter.CTkButton(master=frame1, text="Login", command=on_login)
                button1.grid(row=2, column=3, pady=10, padx=10)

            case "Create New":
                entry1 = customtkinter.CTkEntry(master=frame1, placeholder_text="Enter new user")
                entry1.grid(row=2, column=1, pady=10, padx=10)

                entry2 = customtkinter.CTkEntry(master=frame1, placeholder_text="Create password")
                entry2.grid(row=2, column=2, pady=10, padx=10)

                def on_login():
                    id = gen_id(15)

                    while check_id(id) == True:
                        id = gen_id(15)


                    new_user_value = entry1.get()
                    password = entry2.get()

                    save_new_user([new_user_value, password, id])
                    save_selection(new_user_value)
                    check_user_folder()

                    # Closes every process
                    window.quit()
                    # Closes window
                    window.destroy()

                button1 = customtkinter.CTkButton(master=frame1, text="Login", command=on_login)
                button1.grid(row=2, column=3, pady=10, padx=10)
            
            case "Change Profile Name":
                global temp_choice

                combobox = customtkinter.CTkComboBox(master=frame1, values=["-Select User-", *users_list], command=save)
                combobox.grid(row=2, column=1, pady=10, padx=10)

                entry1 = customtkinter.CTkEntry(master=frame1, placeholder_text="Enter new profile name")
                entry1.grid(row=2, column=2, pady=10, padx=10)

                def change():
                    old_username = temp_choice
                    new_username = entry1.get()

                    change_username(old_username, new_username)

                button1 = customtkinter.CTkButton(master=frame1, text="Apply", command=change)
                button1.grid(row=2, column=3, pady=10, padx=10)


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

                    if check_password(temp_choice, old_password):
                        change_password(temp_choice, new_password)

                button1 = customtkinter.CTkButton(master=frame1, text="Apply", command=change)
                button1.grid(row=2, column=3, pady=10, padx=10)


            case "Delete User":
                combobox = customtkinter.CTkComboBox(master=frame1, values=["-Select User-", *users_list], command=save)
                combobox.grid(row=2, column=1, pady=10, padx=10)

                entry1 = customtkinter.CTkEntry(master=frame1, placeholder_text="Enter password")
                entry1.grid(row=2, column=2, pady=10, padx=10)

                entry2 = customtkinter.CTkEntry(master=frame1, placeholder_text="Enter password again")
                entry2.grid(row=3, column=2, pady=10, padx=10)

                def delete():
                    pass1 = entry1.get()
                    pass2 = entry2.get()

                    if pass1 == pass2 and check_password(temp_choice, pass1):

                            delete_user(check_user_id(temp_choice))

                            popup_window("Info", "User deleted successfully")

                    elif pass1 == pass2 and not check_password(temp_choice, pass1):
                        popup_window("Error", "Invalid password")

                    else:
                        popup_window("Error", "Passwords do not match")

                button1 = customtkinter.CTkButton(master=frame1, text="Delete User", command=delete)
                button1.grid(row=2, column=3, pady=10, padx=10)

    if not users:
        select("Add New")
        combobox = customtkinter.CTkComboBox(master=frame1, values=[ "Create New", "Select Existing", "Change Profile Name", "Change Password", "Delete User"], command=select)
        combobox.grid(row=2, column=0, pady=10, padx=10)

    else:
        select("Select Existing") # Show list of existing users by default
        combobox = customtkinter.CTkComboBox(master=frame1, values=["Select Existing", "Create New", "Change Profile Name", "Change Password", "Delete User"], command=select)
        combobox.grid(row=2, column=0, pady=10, padx=10)

    def on_close():
        # Closes every process
        window.quit()
        # Closes window
        window.destroy()
    
    window.protocol("WM_DELETE_WINDOW", on_close)
    window.mainloop()
    return user