from Finance import result
from Finance import months

import customtkinter

#from Finance import save_data

customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("dark-blue")

window = customtkinter.CTk()
window.title("Finance app")
#window.geometry("800x450")

###############################################################################################################

frame1 = customtkinter.CTkFrame(master=window)
frame1.pack(pady=20, padx=60, fill="both", expand=True)

frame2 = customtkinter.CTkFrame(master=window)
frame2.pack(pady=20, padx=60, fill="both", expand=True)

frame3 = customtkinter.CTkFrame(master=window)
frame3.pack(pady=20, padx=60, fill="both", expand=True)

###############################################################################################################
#Frame 1

label = customtkinter.CTkLabel(master=frame1, text="Finance app", font=("Roboto", 24))
label.grid(row=0, column=1, pady=10, padx=10)

label2 = customtkinter.CTkLabel(master=frame1, text="Select an option:", font=("Roboto", 16))
label2.grid(row=1, column=0, pady=10, padx=10)

combobox = customtkinter.CTkComboBox(master=frame1, values=["Projection calculations", "Interest", "Print all saved data", "Change income value", "Change savings value", "Change spendings value", "Add expense", "Total expenses this month", "Graph expenses (current month)", "Graph expenses (all months)"])
combobox.grid(row=1, column=1, pady=10, padx=10)

###############################################################################################################

def select():
    case = combobox.get()
    match case:
        case "Projection calculations":
            label3 = customtkinter.CTkLabel(master=frame2, text="Projected months:", font=("Roboto", 16))
            label3.grid(row=0, column=0, pady=10, padx=10)

            button3 = customtkinter.CTkButton(master=frame2, text="Calculate", command=select)
            button3.grid(row=0, column=2, pady=10, padx=10)

            label4 = customtkinter.CTkLabel(master=frame2, text="Total savings of " + str(result) + " after " + str(months) + " months", font=("Roboto", 16))
            label4.grid(row=1, column=0, pady=10, padx=10)


        case "Interest":
            pass
        case "Print all saved data":
            pass
        case "Change income value":
            pass
        case "Change savings value":
            pass
        case "Change spendings value":
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