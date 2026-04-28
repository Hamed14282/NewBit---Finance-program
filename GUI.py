from matplotlib.pylab import choice

import Finance
import customtkinter

customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("dark-blue")

window = customtkinter.CTk()
window.title("Finance app")

###############################################################################################################

frame1 = customtkinter.CTkFrame(master=window)
frame1.grid(row=0, column=0, pady=20, padx=60)

frame2 = None
frame3 = None

def create_frame2():
    global frame2
    frame2 = customtkinter.CTkFrame(master=window)
    frame2.grid(row=1, column=0, pady=20, padx=60)

def create_frame3():
    global frame3
    frame3 = customtkinter.CTkFrame(master=window)
    frame3.grid(row=2, column=0, pady=20, padx=60)

###############################################################################################################
#Frame 1

label = customtkinter.CTkLabel(master=frame1, text="Finance app", font=("Roboto", 24))
label.grid(row=0, column=1, pady=10, padx=10)

label2 = customtkinter.CTkLabel(master=frame1, text="Select an option:", font=("Roboto", 16))
label2.grid(row=1, column=0, pady=10, padx=10)

combobox = customtkinter.CTkComboBox(master=frame1, values=["Change values", "Projection calculations", "Interest", "Show expenses(table)", "Graph expenses (current month)", "Graph expenses (all months)"])
combobox.grid(row=1, column=1, pady=10, padx=10)

###############################################################################################################

def select():
    global frame2, frame3

    if frame2 is not None and frame2.winfo_exists():
        frame2.destroy()

    if frame3 is not None and frame3.winfo_exists():
        frame3.destroy()

    case = combobox.get()

    match case:

        case "Change values":
            create_frame2()

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
                        Finance.save_income()
                        
                    case "Savings":
                        Finance.savings = new_value
                        Finance.save_savings()
                        
                    case "Spendings":
                        Finance.spendings = new_value
                        Finance.save_spendings()

                label6 = customtkinter.CTkLabel(master=frame2, text="Values updated: Income: €" + str(Finance.income) + " / Savings: €" + str(Finance.savings) + " / Spendings: €" + str(Finance.spendings), font=("Roboto", 16))
                label6.grid(row=4, column=1, pady=10, padx=10)
            
            button3 = customtkinter.CTkButton(master=frame2, text="Change", command=change_value)
            button3.grid(row=3, column=2, pady=10, padx=10)

        case "Projection calculations":
            create_frame2()

            label3 = customtkinter.CTkLabel(master=frame2, text="Projection calculations: Total savings after projected months", font=("Roboto", 16))
            label3.grid(row=0, column=1, pady=10, padx=10)

            
            label4 = customtkinter.CTkLabel(master=frame2, text=f"Income: €{Finance.income:.2f} / Savings: €{Finance.savings:.2f} / Spendings: €{Finance.spendings:.2f}", font=("Roboto", 16))
            label4.grid(row=1, column=1, pady=10, padx=10)
            
            label5 = customtkinter.CTkLabel(master=frame2, text="Projected months:", font=("Roboto", 16))
            label5.grid(row=2, column=0, pady=10, padx=10)

            entry1 = customtkinter.CTkEntry(master=frame2, placeholder_text="Enter projected months")
            entry1.grid(row=2, column=1, pady=10, padx=10)

            def calculate_projection():
                months = int(entry1.get())
                result = Finance.projection(months)

                label6 = customtkinter.CTkLabel(master=frame2, text="Total savings of €" + str(result) + " after " + str(months) + " months", font=("Roboto", 16))
                label6.grid(row=3, column=1, pady=10, padx=10)

            button3 = customtkinter.CTkButton(master=frame2, text="Calculate", command=calculate_projection)
            button3.grid(row=2, column=2, pady=10, padx=10)


        case "Interest":
            create_frame2()

            label3 = customtkinter.CTkLabel(master=frame2, text="Select the type of interest calculation:", font=("Roboto", 16))
            label3.grid(row=0, column=0, pady=10, padx=10)

            def interest_selection(choice):
                if frame3 is not None and frame3.winfo_exists():
                    frame3.destroy()
                
                match choice:
                    case "Simple Interest":
                        create_frame3()

                        label4 = customtkinter.CTkLabel(master=frame3, text="Simple interest: Total savings after projected years with simple interest", font=("Roboto", 16))
                        label4.grid(row=1, column=1, pady=10, padx=10)

                        label5 = customtkinter.CTkLabel(master=frame3, text=f"Savings: €{Finance.savings:.2f}", font=("Roboto", 16))
                        label5.grid(row=2, column=1, pady=10, padx=10)

                        label6 = customtkinter.CTkLabel(master=frame3, text=f"Portion of savings affected by interest", font=("Roboto", 16))
                        label6.grid(row=3, column=0, pady=10, padx=10)

                        entry1 = customtkinter.CTkEntry(master=frame3, placeholder_text="Enter portion of savings affected by interest")
                        entry1.grid(row=3, column=1, pady=10, padx=10)

                        label7 = customtkinter.CTkLabel(master=frame3, text="Annual interest rate(percentage):", font=("Roboto", 16))
                        label7.grid(row=4, column=0, pady=10, padx=10)

                        entry2 = customtkinter.CTkEntry(master=frame3, placeholder_text="Enter annual interest rate")
                        entry2.grid(row=4, column=1, pady=10, padx=10)

                        label8 = customtkinter.CTkLabel(master=frame3, text="Projected months:", font=("Roboto", 16))
                        label8.grid(row=5, column=0, pady=10, padx=10)

                        entry3 = customtkinter.CTkEntry(master=frame3, placeholder_text="Enter projected months")
                        entry3.grid(row=5, column=1, pady=10, padx=10)


                        def calculate_simple_interest():
                            interest_money = float(entry1.get())
                            annual_rate = float(entry2.get())
                            years = int(entry3.get())/12
                            result = Finance.simple_interest(annual_rate, years, interest_money)

                            for widget in frame3.grid_slaves(row=6, column=1):
                                widget.destroy()  # Clear previous result if exists

                            if interest_money > Finance.savings or interest_money <= 0:
                                label9 = customtkinter.CTkLabel(master=frame3, text="Invalid portion of savings affected by interest. Please enter a value between 0 and " + str(Finance.savings), font=("Roboto", 16))
                                label9.grid(row=6, column=1, pady=10, padx=10)
                            else:
                                label9 = customtkinter.CTkLabel(master=frame3, text="Total savings of €" + str(result) + " after " + str(years) + " years with simple interest", font=("Roboto", 16))
                                label9.grid(row=6, column=1, pady=10, padx=10)

                        button4 = customtkinter.CTkButton(master=frame3, text="Calculate", command=calculate_simple_interest)
                        button4.grid(row=5, column=2, pady=10, padx=10)

                    case "Compound Interest":
                        create_frame3()

                        label4 = customtkinter.CTkLabel(master=frame3, text="Compound interest: Total savings after projected years with compound interest", font=("Roboto", 16))
                        label4.grid(row=1, column=1, pady=10, padx=10)

                        label5 = customtkinter.CTkLabel(master=frame3, text=f"Savings: €{Finance.savings:.2f}", font=("Roboto", 16))
                        label5.grid(row=2, column=1, pady=10, padx=10)
                        
                        label6 = customtkinter.CTkLabel(master=frame3, text=f"Portion of savings affected by interest", font=("Roboto", 16))
                        label6.grid(row=3, column=0, pady=10, padx=10)
                         
                        entry1 = customtkinter.CTkEntry(master=frame3, placeholder_text="Enter portion of savings affected by interest")
                        entry1.grid(row=3, column=1, pady=10, padx=10)

                        label7 = customtkinter.CTkLabel(master=frame3, text="Annual interest rate(percentage):", font=("Roboto", 16))
                        label7.grid(row=4, column=0, pady=10, padx=10)

                        entry2 = customtkinter.CTkEntry(master=frame3, placeholder_text="Enter annual interest rate")
                        entry2.grid(row=4, column=1, pady=10, padx=10)

                        label8 = customtkinter.CTkLabel(master=frame3, text="Projected months:", font=("Roboto", 16))
                        label8.grid(row=5, column=0, pady=10, padx=10)

                        entry3 = customtkinter.CTkEntry(master=frame3, placeholder_text="Enter projected months")
                        entry3.grid(row=5, column=1, pady=10, padx=10)

                        label9 = customtkinter.CTkLabel(master=frame3, text="Compounding periods per year:", font=("Roboto", 16))
                        label9.grid(row=6, column=0, pady=10, padx=10)

                        entry4 = customtkinter.CTkEntry(master=frame3, placeholder_text="Enter compounding periods per year")
                        entry4.grid(row=6, column=1, pady=10, padx=10)

                        def calculate_compound_interest():
                            interest_money = float(entry1.get())
                            annual_rate = float(entry2.get())
                            years = int(entry3.get())/12
                            periods = int(entry4.get())
                            result = Finance.compound_interest(annual_rate, years, interest_money, periods)

                            for widget in frame3.grid_slaves(row=7, column=1):
                                widget.destroy()  # Clear previous result if exists  
                            
                            if interest_money > Finance.savings or interest_money <= 0:
                                label10 = customtkinter.CTkLabel(master=frame3, text="Invalid portion of savings affected by interest. Please enter a value between 0 and " + str(Finance.savings), font=("Roboto", 16))
                                label10.grid(row=7, column=1, pady=10, padx=10)
                            else:
                                label10 = customtkinter.CTkLabel(master=frame3, text="Total savings of €" + str(result) + " after " + str(years) + " years with compound interest", font=("Roboto", 16))
                                label10.grid(row=7, column=1, pady=10, padx=10)
                        
                        button4 = customtkinter.CTkButton(master=frame3, text="Calculate", command=calculate_compound_interest)
                        button4.grid(row=6, column=2, pady=10, padx=10)

            combobox2 = customtkinter.CTkComboBox(master=frame2, values=["-", "Simple Interest", "Compound Interest"], command=interest_selection)
            combobox2.grid(row=0, column=1, pady=10, padx=10)


        case "Print all saved data":
            pass
        
        case "Add expense":
            pass
        case "Total expenses this month":
            pass
        
        case "Graph expenses (current month)":
            Finance.expenses_graph()

        case "Graph expenses (all months)":
            Finance.monthly_expenses_graph()
            
###############################################################################################################

button1 = customtkinter.CTkButton(master=frame1, text="Select", command=select)
button1.grid(row=1, column=3, pady=10, padx=10)

###############################################################################################################
#Frame 2

###############################################################################################################
#Frame 3

###############################################################################################################

window.mainloop()