import Finance

import customtkinter

#from Finance import save_data

customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("dark-blue")

window = customtkinter.CTk()
window.title("Finance app")
#window.geometry("800x450")

###############################################################################################################

frame1 = customtkinter.CTkFrame(master=window)
frame1.grid(row=0, column=0, pady=20, padx=60)

frame2 = customtkinter.CTkFrame(master=window)
frame2.grid(row=1, column=0, pady=20, padx=60)

frame3 = customtkinter.CTkFrame(master=window)
frame3.grid(row=2, column=0, pady=20, padx=60)

###############################################################################################################
#Frame 1

label = customtkinter.CTkLabel(master=frame1, text="Finance app", font=("Roboto", 24))
label.grid(row=0, column=1, pady=10, padx=10)

label2 = customtkinter.CTkLabel(master=frame1, text="Select an option:", font=("Roboto", 16))
label2.grid(row=1, column=0, pady=10, padx=10)

combobox = customtkinter.CTkComboBox(master=frame1, values=["Change values", "Projection calculations", "Interest", "Print all saved data", "Add expense", "Total expenses this month", "Graph expenses (current month)", "Graph expenses (all months)"])
combobox.grid(row=1, column=1, pady=10, padx=10)

###############################################################################################################

def select():
    # Clear all widgets in frame2 before adding new ones
    for widget in frame2.winfo_children():
        widget.destroy()
    
    case = combobox.get()
    match case:
        # case "Change income value":
        #     pass
        # case "Change savings value":
        #     pass
        # case "Change spendings value":
        #     pass
        case "Change values":
            label3 = customtkinter.CTkLabel(master=frame2, text="Change values: Income, Savings, Spendings", font=("Roboto", 16))
            label3.grid(row=0, column=1, pady=10, padx=10)

            label4 = customtkinter.CTkLabel(master=frame2, text="Current values: Income: €" + str(Finance.income) + " / Savings: €" + str(Finance.savings) + " / Spendings: €" + str(Finance.spendings), font=("Roboto", 16))
            label4.grid(row=1, column=1, pady=10, padx=10)

            label5 = customtkinter.CTkLabel(master=frame2, text="Select value to change:", font=("Roboto", 16))
            label5.grid(row=2, column=0, pady=10, padx=10)

            combobox2 = customtkinter.CTkComboBox(master=frame2, values=["Income", "Savings", "Spendings"])
            combobox2.grid(row=3, column=0, pady=10, padx=10)

            entry1 = customtkinter.CTkEntry(master=frame2, placeholder_text="Enter new value")
            entry1.grid(row=3, column=1, pady=10, padx=10)

            def change_value():
                value = combobox2.get()
                new_value = float(entry1.get())
                match value:
                    case "Income":
                        Finance.income = new_value
                    case "Savings":
                        Finance.savings = new_value
                    case "Spendings":
                        Finance.spendings = new_value

                label6 = customtkinter.CTkLabel(master=frame2, text="Values updated: Income: €" + str(Finance.income) + " / Savings: €" + str(Finance.savings) + " / Spendings: €" + str(Finance.spendings), font=("Roboto", 16))
                label6.grid(row=4, column=1, pady=10, padx=10)
            
            button3 = customtkinter.CTkButton(master=frame2, text="Change", command=change_value)
            button3.grid(row=3, column=2, pady=10, padx=10)

        case "Projection calculations":
            label3 = customtkinter.CTkLabel(master=frame2, text="Projection calculations: Total savings after projected months", font=("Roboto", 16))
            label3.grid(row=0, column=1, pady=10, padx=10)

            label4 = customtkinter.CTkLabel(master=frame2, text="Projected months:", font=("Roboto", 16))
            label4.grid(row=1, column=0, pady=10, padx=10)

            entry1 = customtkinter.CTkEntry(master=frame2, placeholder_text="Enter projected months")
            entry1.grid(row=1, column=1, pady=10, padx=10)

            def calculate_projection():
                months = int(entry1.get())
                result = Finance.projection(months)

                label5 = customtkinter.CTkLabel(master=frame2, text=f"Income: €{Finance.income:.2f} / Savings: €{Finance.savings:.2f} / Spendings: €{Finance.spendings:.2f}", font=("Roboto", 16))
                label5.grid(row=2, column=1, pady=10, padx=10)

                label6 = customtkinter.CTkLabel(master=frame2, text="Total savings of €" + str(result) + " after " + str(months) + " months", font=("Roboto", 16))
                label6.grid(row=3, column=1, pady=10, padx=10)

            button3 = customtkinter.CTkButton(master=frame2, text="Calculate", command=calculate_projection)
            button3.grid(row=1, column=2, pady=10, padx=10)


        case "Interest":
            pass
        case "Print all saved data":
            pass
        
        case "Add expense":
            pass
        case "Total expenses this month":
            pass
        case "Graph expenses (current month)":
            pass
        case "Graph expenses (all months)":
            pass
            
###############################################################################################################

button1 = customtkinter.CTkButton(master=frame1, text="Select", command=select)
button1.grid(row=1, column=3, pady=10, padx=10)

###############################################################################################################
#Frame 2

###############################################################################################################
#Frame 3

button2 = customtkinter.CTkButton(master=frame3, text="Save", command=select)
button2.grid(row=0, column=3, pady=10, padx=10)




###############################################################################################################

window.mainloop()