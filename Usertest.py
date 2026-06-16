import csv
import os

import customtkinter

user = ""
users = []
users_list = []
temp_choice = ""

def check_users_file():
    if not os.path.exists("data/users.csv"):
        file = open("data/users.csv", "x")
        file.close()

def get_all_users():
    global users, users_list
    with open("data/users.csv", "r") as file:
            reader = csv.reader(file)
            for row in reader:
                users.append(row)
                users_list.append(row[0])

def save_new_user(new_user):
    global users
    users.append(new_user)

    with open(f"data/users.csv", "w", newline="") as file:
        writer = csv.writer(file)
        writer.writerows(users)

def save_selection(select):
    global user
    user = select

def save(select): #Throw error if value is "-Select-"
    global temp_choice
    temp_choice = select

def choose():
    global users, user
    
    check_users_file()
    get_all_users()
    print(users)

    window = customtkinter.CTk()
    window.title("Choose user")

    frame1 = customtkinter.CTkFrame(master=window)
    frame1.grid(row=0, column=0, pady=5, padx=10)
    
    label1 = customtkinter.CTkLabel(master=frame1, text="Select User", font=("Roboto", 24))
    label1.grid(row=0, column=1, pady=10, padx=10)

    label2 = customtkinter.CTkLabel(master=frame1, text="Choose profile:", font=("Roboto", 17))
    label2.grid(row=1, column=0, pady=10, padx=10)

    def select(choice):
        match choice:
            case "Select Existing":
                combobox = customtkinter.CTkComboBox(master=frame1, values=["-Select-", *users_list], command=save)
                combobox.grid(row=2, column=1, pady=10, padx=10)

                def on_login(value):

                    save_selection(value)
                    print(user)
                    
                    # Closes every process
                    window.quit()
                    # Closes window
                    window.destroy()

                button1 = customtkinter.CTkButton(master=frame1, text="Login", command=lambda:on_login(temp_choice))
                button1.grid(row=2, column=3, pady=10, padx=10)

            case "Add New":
                entry1 = customtkinter.CTkEntry(master=frame1, placeholder_text="Enter new user")
                entry1.grid(row=2, column=1, pady=10, padx=10)

                def on_login(value):
                    save_new_user([value, "password"])
                    save_selection(value)
                    print(user)


                    # Closes every process
                    window.quit()
                    # Closes window
                    window.destroy()

                button1 = customtkinter.CTkButton(master=frame1, text="Login", command=lambda:on_login(entry1.get()))
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
