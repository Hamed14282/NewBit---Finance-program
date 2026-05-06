import Financetest
import customtkinter
from tkinter import ttk
from CTkTreeview.treeview import CTkTreeview
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg


customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("dark-blue")

window = customtkinter.CTk()
window.title("Finance app")
window.minsize(500, 300)
window.grid_columnconfigure(0, weight=1)
window.grid_columnconfigure(1, weight=1)
window.grid_rowconfigure(0, weight=1)
window.grid_rowconfigure(1, weight=1)

###############################################################################################################

frame1 = customtkinter.CTkFrame(master=window)
frame1.grid(row=0, column=0, pady=15, padx=15, sticky="nsw")
frame1.grid_columnconfigure(0, weight=0)
frame1.grid_rowconfigure(0, weight=0)
frame1.grid_rowconfigure(1, weight=0)
frame1.grid_rowconfigure(2, weight=0)


frame2 = None
frame3 = None
frame6 = None

def create_frame2():
    global frame2
    frame2 = customtkinter.CTkFrame(master=window)
    frame2.grid(row=0, column=1, pady=15, padx=15, sticky="nsew")
    frame2.grid_columnconfigure(0, weight=1)
    frame2.grid_columnconfigure(1, weight=1)

def create_frame2(x, y):
    global frame2
    frame2 = customtkinter.CTkFrame(master=window)
    frame2.grid(row=y, column=x, pady=15, padx=15, sticky="nsew")
    if x == 0 and y == 1:
        frame2.grid(row=y, column=x, pady=15, padx=15, sticky="nsew")
        frame2.grid_columnconfigure(0, weight=0)
        frame2.grid_rowconfigure(0, weight=0)
    frame2.grid_columnconfigure(0, weight=1)
    frame2.grid_columnconfigure(1, weight=1)

def create_frame3():
    global frame3
    frame3 = customtkinter.CTkFrame(master=window)
    frame3.grid(row=1, column=1, pady=15, padx=15, sticky="nsew")
    frame3.grid_columnconfigure(0, weight=1)
    frame3.grid_columnconfigure(1, weight=1)

def create_frame3(x, y):
    global frame3
    frame3 = customtkinter.CTkFrame(master=window)
    frame3.grid(row=y, column=x, pady=15, padx=15, sticky="nsew")
    frame3.grid_columnconfigure(0, weight=1)
    frame3.grid_columnconfigure(1, weight=1)

###############################################################################################################
#Frame 1

label = customtkinter.CTkLabel(master=frame1, text="Finance app", font=("Roboto", 30))
label.grid(row=0, column=0, pady=10, padx=10)

label2 = customtkinter.CTkLabel(master=frame1, text="Select an option:", font=("Roboto", 16))
label2.grid(row=1, column=0, pady=10, padx=10)

###############################################################################################################

def select(case):
    global frame2, frame3

    if frame2 is not None and frame2.winfo_exists():
        frame2.destroy()

    if frame3 is not None and frame3.winfo_exists():
        frame3.destroy()

    case = combobox.get()

    match case:

        case "Change values":
            create_frame2(1, 0)

            label3 = customtkinter.CTkLabel(master=frame2, text="Change values: Income, Savings, Spendings", font=("Roboto", 24))
            label3.grid(row=0, column=1, pady=10, padx=10)

            label4 = customtkinter.CTkLabel(master=frame2, text="Current values: Income: €" + str(Financetest.income) + " / Savings: €" + str(Financetest.savings) + " / Spendings: €" + str(Financetest.spendings), font=("Roboto", 16))
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
                        Financetest.income = new_value
                        Financetest.save_income()
                        
                    case "Savings":
                        Financetest.savings = new_value
                        Financetest.save_savings()
                        
                    case "Spendings":
                        Financetest.spendings = new_value
                        Financetest.save_spendings()

                label6 = customtkinter.CTkLabel(master=frame2, text="Values updated: Income: €" + f"{Financetest.income:.2f}" + " / Savings: €" + f"{Financetest.savings:.2f}" + " / Spendings: €" + f"{Financetest.spendings:.2f}", font=("Roboto", 16))
                label6.grid(row=4, column=1, pady=10, padx=10)
            
            button3 = customtkinter.CTkButton(master=frame2, text="Change", command=change_value)
            button3.grid(row=3, column=2, pady=10, padx=10)

        case "Projection calculations":
            create_frame3(1, 0)

            frame4 = customtkinter.CTkFrame(master=frame3, fg_color="transparent", bg_color="transparent")
            frame4.grid(row=0, column=0, columnspan=2, pady=0, padx=0)

            frame5 = customtkinter.CTkFrame(master=frame3, fg_color="transparent", bg_color="transparent")
            frame5.grid(row=1, column=0, columnspan=2, pady=0, padx=0)

            label3 = customtkinter.CTkLabel(master=frame4, text="Projection calculations: Total savings after projected months", font=("Roboto", 24))
            label3.grid(row=0, column=0, pady=10, padx=10)

            label4 = customtkinter.CTkLabel(master=frame4, text=f"Income: €{Financetest.income:.2f} / Savings: €{Financetest.savings:.2f} / Spendings: €{Financetest.spendings:.2f}", font=("Roboto", 16))
            label4.grid(row=1, column=0, pady=10, padx=10)
            
            label5 = customtkinter.CTkLabel(master=frame5, text="Projected months:", font=("Roboto", 16))
            label5.grid(row=0, column=0, pady=10, padx=10)

            entry1 = customtkinter.CTkEntry(master=frame5, placeholder_text="Enter projected months")
            entry1.grid(row=0, column=1, pady=10, padx=10)

            def calculate_projection():
                months = int(entry1.get())
                result = Financetest.projection(months)

                global frame6
                if frame6 is None or not frame6.winfo_exists():
                    frame6 = customtkinter.CTkFrame(master=frame3, fg_color="transparent", bg_color="transparent")
                    frame6.grid(row=2, column=0, columnspan=2, pady=10, padx=10)
                
                # Clear any existing frame at this position
                for widget in frame6.grid_slaves(row=0, column=0):
                    widget.destroy()

                label6 = customtkinter.CTkLabel(master=frame6, text="Total savings of €" + f"{result:.2f}" + " after " + str(months) + " months", font=("Roboto", 16))
                label6.grid(row=0, column=0, pady=10, padx=10)

                def save_projection():
                    Financetest.savings = result
                    Financetest.save_savings()

                button4 = customtkinter.CTkButton(master=frame6, text="Save value", command=save_projection)
                button4.grid(row=0, column=1, pady=10, padx=10)

            button3 = customtkinter.CTkButton(master=frame5, text="Calculate", command=calculate_projection)
            button3.grid(row=0, column=2, pady=10, padx=10)


        case "Interest":

            label3 = customtkinter.CTkLabel(master=frame1, text="Type of interest calculation:", font=("Roboto", 16))
            label3.grid(row=3, column=0, pady=10, padx=10)

            def interest_selection(choice):
                if frame3 is not None and frame3.winfo_exists():
                    frame3.destroy()
                
                match choice:
                    case "Simple Interest":
                        create_frame3(1, 0)
                        
                        frame4 = customtkinter.CTkFrame(master=frame3, fg_color="transparent", bg_color="transparent")
                        frame4.grid(row=0, column=0, pady=0, padx=0)

                        frame5 = customtkinter.CTkFrame(master=frame3, fg_color="transparent", bg_color="transparent")
                        frame5.grid(row=1, column=0, pady=0, padx=0)


                        label4 = customtkinter.CTkLabel(master=frame4, text="Simple interest: Total savings after projected years with simple interest", font=("Roboto", 24))
                        label4.grid(row=0, column=0, pady=10, padx=10)

                        label5 = customtkinter.CTkLabel(master=frame4, text=f"Savings: €{Financetest.savings:.2f}", font=("Roboto", 16))
                        label5.grid(row=1, column=0, pady=10, padx=10)

                        label6 = customtkinter.CTkLabel(master=frame5, text="Portion of savings affected by interest:", font=("Roboto", 16))
                        label6.grid(row=0, column=0, pady=10, padx=10)

                        entry1 = customtkinter.CTkEntry(master=frame5, placeholder_text="Enter portion of savings affected by interest")
                        entry1.grid(row=0, column=1, pady=10, padx=10)

                        label7 = customtkinter.CTkLabel(master=frame5, text="Annual interest rate(percentage):", font=("Roboto", 16))
                        label7.grid(row=1, column=0, pady=10, padx=10)

                        entry2 = customtkinter.CTkEntry(master=frame5, placeholder_text="Enter annual interest rate")
                        entry2.grid(row=1, column=1, pady=10, padx=10)

                        label8 = customtkinter.CTkLabel(master=frame5, text="Projected months:", font=("Roboto", 16))
                        label8.grid(row=2, column=0, pady=10, padx=10)

                        entry3 = customtkinter.CTkEntry(master=frame5, placeholder_text="Enter projected months")
                        entry3.grid(row=2, column=1, pady=10, padx=10)


                        def calculate_simple_interest():
                            interest_money = float(entry1.get())
                            annual_rate = float(entry2.get())
                            years = int(entry3.get())/12
                            result = Financetest.simple_interest(annual_rate, years, interest_money)

                            global frame6
                            if frame6 is None or not frame6.winfo_exists():
                                frame6 = customtkinter.CTkFrame(master=frame3, fg_color="transparent", bg_color="transparent")
                                frame6.grid(row=2, column=0, columnspan=2, pady=10, padx=10)
                            
                            # Clear any existing frame at this position
                            for widget in frame6.grid_slaves(row=0, column=0):
                                widget.destroy()
                            
                            if interest_money > Financetest.savings or interest_money <= 0:
                                label10 = customtkinter.CTkLabel(master=frame6, text="Invalid portion of savings affected by interest. Please enter a value between 0 and " + str(Financetest.savings), font=("Roboto", 16))
                                label10.grid(row=0, column=0, pady=10, padx=10)
                            else:
                                label9 = customtkinter.CTkLabel(master=frame6, text="Total savings of €" + f"{result:.2f}" + " after " + str(years) + " years with simple interest", font=("Roboto", 16))
                                label9.grid(row=0, column=0, pady=10, padx=10)

                        button4 = customtkinter.CTkButton(master=frame5, text="Calculate", command=calculate_simple_interest)
                        button4.grid(row=2, column=2, pady=10, padx=10)

                    case "Compound Interest":
                        create_frame3(1, 0)
                        
                        frame4 = customtkinter.CTkFrame(master=frame3, fg_color="transparent", bg_color="transparent")
                        frame4.grid(row=0, column=0, pady=0, padx=0)

                        frame5 = customtkinter.CTkFrame(master=frame3, fg_color="transparent", bg_color="transparent")
                        frame5.grid(row=1, column=0, pady=0, padx=0)


                        label4 = customtkinter.CTkLabel(master=frame4, text="Compound interest: Total savings after projected years with compound interest", font=("Roboto", 24))
                        label4.grid(row=0, column=1, pady=10, padx=10)

                        label5 = customtkinter.CTkLabel(master=frame4, text=f"Savings: €{Financetest.savings:.2f}", font=("Roboto", 16))
                        label5.grid(row=1, column=1, pady=10, padx=10)
                        
                        label6 = customtkinter.CTkLabel(master=frame5, text="Portion of savings affected by interest:", font=("Roboto", 16))
                        label6.grid(row=0, column=0, pady=10, padx=10)
                         
                        entry1 = customtkinter.CTkEntry(master=frame5, placeholder_text="Enter portion of savings affected by interest")
                        entry1.grid(row=0, column=1, pady=10, padx=10)

                        label7 = customtkinter.CTkLabel(master=frame5, text="Annual interest rate(percentage):", font=("Roboto", 16))
                        label7.grid(row=1, column=0, pady=10, padx=10)

                        entry2 = customtkinter.CTkEntry(master=frame5, placeholder_text="Enter annual interest rate")
                        entry2.grid(row=1, column=1, pady=10, padx=10)

                        label8 = customtkinter.CTkLabel(master=frame5, text="Projected months:", font=("Roboto", 16))
                        label8.grid(row=2, column=0, pady=10, padx=10)

                        entry3 = customtkinter.CTkEntry(master=frame5, placeholder_text="Enter projected months")
                        entry3.grid(row=2, column=1, pady=10, padx=10)

                        label9 = customtkinter.CTkLabel(master=frame5, text="Compounding periods per year:", font=("Roboto", 16))
                        label9.grid(row=3, column=0, pady=10, padx=10)

                        entry4 = customtkinter.CTkEntry(master=frame5, placeholder_text="Enter compounding periods per year")
                        entry4.grid(row=3, column=1, pady=10, padx=10)

                        def calculate_compound_interest():
                            interest_money = float(entry1.get())
                            annual_rate = float(entry2.get())
                            years = int(entry3.get())/12
                            periods = int(entry4.get())
                            result = Financetest.compound_interest(annual_rate, years, interest_money, periods)

                            global frame6
                            if frame6 is None or not frame6.winfo_exists():
                                frame6 = customtkinter.CTkFrame(master=frame3, fg_color="transparent", bg_color="transparent")
                                frame6.grid(row=2, column=0, columnspan=2, pady=10, padx=10)

                            for widget in frame6.grid_slaves(row=0, column=0):
                                widget.destroy()  # Clear previous result if exists  
                            
                            if interest_money > Financetest.savings or interest_money <= 0:
                                label10 = customtkinter.CTkLabel(master=frame6, text="Invalid portion of savings affected by interest. Please enter a value between 0 and " + str(Financetest.savings), font=("Roboto", 16))
                                label10.grid(row=0, column=0, pady=10, padx=10)
                            else:
                                label10 = customtkinter.CTkLabel(master=frame6, text="Total savings of €" + f"{result:.2f}" + " after " + str(years) + " years with compound interest", font=("Roboto", 16))
                                label10.grid(row=0, column=0, pady=10, padx=10)
                        
                        button4 = customtkinter.CTkButton(master=frame5, text="Calculate", command=calculate_compound_interest)
                        button4.grid(row=3, column=2, pady=10, padx=10)

            combobox2 = customtkinter.CTkComboBox(master=frame1, values=["-Select-", "Simple Interest", "Compound Interest"], command=interest_selection)
            combobox2.grid(row=4, column=0, pady=10, padx=10)


        case "Show expenses(table)":
            create_frame2(1, 0)

            table = ttk.Treeview(frame2, 
                                columns=("Amount", "Time", "Day"), 
                                show="headings", 
                                height=len(Financetest.expense_lines) if len(Financetest.expense_lines) < 15 else 15,
                                style="Treeview")
            
            table.heading("Amount", text="Amount")
            table.heading("Time", text="Time")
            table.heading("Day", text="Day")
            table.grid(row=0, column=0, sticky="nsew")

            for x in Financetest.expense_lines:
                table.insert(parent="", index="end", values=(x[0], x[1], x[2]))
            
            # Configure column widths for better appearance
            table.column("Amount", width=80)
            table.column("Time", width=100)
            table.column("Day", width=60)

        case "Graph expenses (current month)":
            create_frame2(1, 0)
            fig = Financetest.expenses_graph()
            canvas = FigureCanvasTkAgg(fig, master=frame2)
            canvas.draw()
            canvas.get_tk_widget().grid(row=0, column=0, sticky="nsew")

        case "Graph expenses (all months)":
            create_frame2(1, 0)
            fig = Financetest.monthly_expenses_graph()
            canvas = FigureCanvasTkAgg(fig, master=frame2)
            canvas.draw()
            canvas.get_tk_widget().grid(row=0, column=0, sticky="nsew")


###############################################################################################################

combobox = customtkinter.CTkComboBox(master=frame1, values=["-Select-", "Change values", "Projection calculations", "Interest", "Show expenses(table)", "Graph expenses (current month)", "Graph expenses (all months)"], command=select)
combobox.grid(row=2, column=0, pady=10, padx=10)

###############################################################################################################

window.mainloop()