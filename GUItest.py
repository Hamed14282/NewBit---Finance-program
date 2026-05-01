from matplotlib import style

import AddExpense
import Financetest
import customtkinter
from tkinter import ttk
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("dark-blue")

window = customtkinter.CTk()
window.title("Finance app")
window.minsize(500, 300)
window.grid_columnconfigure(0, weight=1)
window.grid_columnconfigure(1, weight=1)
window.grid_rowconfigure(0, weight=0)
window.grid_rowconfigure(1, weight=1)

style = ttk.Style()
style.theme_use('clam')
style.configure("TScrollbar", gripcount=0, background="lightgray", troughcolor="#232323", arrowcolor="white")

###############################################################################################################

frame1 = customtkinter.CTkFrame(master=window)
frame1.grid(row=0, column=0, pady=15, padx=15, rowspan=3, sticky="nsw")
frame1.grid_columnconfigure(0, weight=0)
frame1.grid_rowconfigure(0, weight=0)
frame1.grid_rowconfigure(1, weight=0)
frame1.grid_rowconfigure(2, weight=0)

frame2 = None
frame3 = None
frame4 = None
frame6 = None

def create_frame2():
    global frame2
    frame2 = customtkinter.CTkFrame(master=window)
    frame2.grid(row=0, column=1, pady=15, padx=15, sticky="nsew")
    frame2.grid_columnconfigure(0, weight=1)
    frame2.grid_columnconfigure(1, weight=1)

def create_frame2(x, y, m):
    global frame2
    frame2 = customtkinter.CTkFrame(master=m)
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

def create_frame3(x, y, m):
    global frame3
    frame3 = customtkinter.CTkFrame(master=m)
    frame3.grid(row=y, column=x, pady=15, padx=15, sticky="nsew")
    frame3.grid_columnconfigure(0, weight=1)
    frame3.grid_columnconfigure(1, weight=1)

def create_frame4(x, y, m):
    global frame4
    frame4 = customtkinter.CTkFrame(master=m)
    frame4.grid(row=y, column=x, pady=5, padx=5, sticky="new")
    frame4.grid_columnconfigure(0, weight=1)
    frame4.grid_rowconfigure(0, weight=0)
    frame4.grid_rowconfigure(1, weight=0)

def create_frame6(x, y, m):
    global frame6
    frame6 = customtkinter.CTkFrame(master=m, fg_color="transparent", bg_color="transparent")
    frame6.grid(row=y, column=x, pady=5, padx=5, sticky="new")
    frame6.grid_columnconfigure(0, weight=1)
    frame6.grid_rowconfigure(0, weight=0)

def string_to_num(s):
    try:
        if float(s).is_integer():
            return int(s)
        else:
            return float(s)
    except ValueError:
        return False

###############################################################################################################

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
    
    global frame4
    if frame4 is not None and frame4.winfo_exists():
        frame4.destroy()
    
    if frame1.grid_slaves(row=3, column=0):
        for widget in frame1.grid_slaves(row=3, column=0):
            widget.destroy()

    if frame1.grid_slaves(row=4, column=0):
        for widget in frame1.grid_slaves(row=4, column=0):
            widget.destroy()

    case = combobox.get()

    match case:

        case "Change values":
            create_frame3(1, 0, window)
            
            frame4 = customtkinter.CTkFrame(master=frame3, fg_color="transparent", bg_color="transparent")
            frame4.grid(row=0, column=0, columnspan=2, pady=0, padx=0)

            frame5 = customtkinter.CTkFrame(master=frame3, fg_color="transparent", bg_color="transparent")
            frame5.grid(row=1, column=0, columnspan=2, pady=0, padx=0)

            label3 = customtkinter.CTkLabel(master=frame4, text="Change values: Income, Savings, Spendings", font=("Roboto", 24))
            label3.grid(row=0, column=0, pady=10, padx=10)

            label4 = customtkinter.CTkLabel(master=frame4, text="Current values: Income: €" + str(Financetest.income) + " / Savings: €" + str(Financetest.savings) + " / Spendings: €" + str(Financetest.spendings), text_color="pink", font=("Roboto", 16))
            label4.grid(row=1, column=0, pady=10, padx=10)

            label5 = customtkinter.CTkLabel(master=frame5, text="Select value to change:", font=("Roboto", 17))
            label5.grid(row=0, column=0, pady=10, padx=10)

            combobox2 = customtkinter.CTkComboBox(master=frame5, values=["Income", "Savings", "Spendings"])
            combobox2.grid(row=1, column=0, pady=10, padx=10)

            entry1 = customtkinter.CTkEntry(master=frame5, placeholder_text="Enter new value")
            entry1.grid(row=1, column=1, pady=10, padx=10)

            def change_value():
                value = combobox2.get()
                new_value = entry1.get()

                global frame6
                match value:
                    case "Income":
                        if frame6 is not None and frame6.winfo_exists():
                            frame6.destroy()
                        
                        if new_value is not None and new_value != "":
                            if string_to_num(new_value) is False or string_to_num(new_value) <= 0:
                                if frame6 is None or not frame6.winfo_exists():
                                    create_frame6(0, 2, frame3)
                                error_label = customtkinter.CTkLabel(master=frame6, text="Invalid income input. Please enter a number greater than zero.", text_color="pink", font=("Roboto", 16))
                                error_label.grid(row=0, column=0, pady=10, padx=10)
                                return
                            else:
                                new_value = string_to_num(new_value)
                                Financetest.update_income(new_value)
                                Financetest.log.change_values("income", new_value)

                        elif new_value is None or new_value == "":
                            if frame6 is None or not frame6.winfo_exists():
                                create_frame6(0, 2, frame3)
                            error_label = customtkinter.CTkLabel(master=frame6, text="No income value entered.", text_color="pink", font=("Roboto", 16))
                            error_label.grid(row=0, column=0, pady=10, padx=10)
                            return
                        
                    case "Savings":
                        if frame6 is not None and frame6.winfo_exists():
                            frame6.destroy()
                        
                        if new_value is not None and new_value != "":
                            if string_to_num(new_value) is False or string_to_num(new_value) < 0:
                                if frame6 is None or not frame6.winfo_exists():
                                    create_frame6(0, 2, frame3)
                                error_label = customtkinter.CTkLabel(master=frame6, text="Invalid savings input. Please enter a number greater than or equal to zero.", text_color="pink", font=("Roboto", 16))
                                error_label.grid(row=0, column=0, pady=10, padx=10)
                                return
                            else:
                                new_value = string_to_num(new_value)
                                Financetest.update_savings(new_value, Financetest.current_date)
                                Financetest.log.change_values("savings", new_value)

                        elif new_value is None or new_value == "":
                            if frame6 is None or not frame6.winfo_exists():
                                create_frame6(0, 2, frame3)
                            error_label = customtkinter.CTkLabel(master=frame6, text="No savings value entered.", text_color="pink", font=("Roboto", 16))
                            error_label.grid(row=0, column=0, pady=10, padx=10)
                            return
                        
                    case "Spendings":
                        if frame6 is not None and frame6.winfo_exists():
                            frame6.destroy()

                        if new_value is not None and new_value != "":
                            if string_to_num(new_value) is False or string_to_num(new_value) < 0:
                                if frame6 is None or not frame6.winfo_exists():
                                    create_frame6(0, 2, frame3)
                                error_label = customtkinter.CTkLabel(master=frame6, text="Invalid spendings input. Please enter a number greater than or equal to zero.", text_color="pink", font=("Roboto", 16))
                                error_label.grid(row=0, column=0, pady=10, padx=10)
                                return
                            else:
                                new_value = string_to_num(new_value)
                                Financetest.update_spendings(new_value)
                                Financetest.log.change_values("spendings", new_value)

                        elif new_value is None or new_value == "":
                            if frame6 is None or not frame6.winfo_exists():
                                create_frame6(0, 2, frame3)
                            error_label = customtkinter.CTkLabel(master=frame6, text="No spendings value entered.", text_color="pink", font=("Roboto", 16))
                            error_label.grid(row=0, column=0, pady=10, padx=10)
                            return
                
                if frame6 is None or not frame6.winfo_exists():
                    frame6 = customtkinter.CTkFrame(master=frame3, fg_color="transparent", bg_color="transparent")
                    frame6.grid(row=2, column=0, columnspan=2, pady=10, padx=10)
                
                # Clear any existing frame at this position
                for widget in frame6.grid_slaves(row=0, column=0):
                    widget.destroy()

                label6 = customtkinter.CTkLabel(master=frame6, text="Values updated: Income: €" + f"{Financetest.income:.2f}" + " / Savings: €" + f"{Financetest.savings:.2f}" + " / Spendings: €" + f"{Financetest.spendings:.2f}", text_color="pink", font=("Roboto", 16))
                label6.grid(row=0, column=0, pady=10, padx=10)
            
            button3 = customtkinter.CTkButton(master=frame5, text="Change", command=change_value)
            button3.grid(row=1, column=2, pady=10, padx=10)

        ###############################################################################################################

        case "Projection calculations":
            create_frame3(1, 0, window)

            frame4 = customtkinter.CTkFrame(master=frame3, fg_color="transparent", bg_color="transparent")
            frame4.grid(row=0, column=0, columnspan=2, pady=0, padx=0)

            frame5 = customtkinter.CTkFrame(master=frame3, fg_color="transparent", bg_color="transparent")
            frame5.grid(row=1, column=0, columnspan=2, pady=0, padx=0)

            label3 = customtkinter.CTkLabel(master=frame4, text="Projection calculations: Total savings after projected months", font=("Roboto", 24))
            label3.grid(row=0, column=0, pady=10, padx=10)

            label4 = customtkinter.CTkLabel(master=frame4, text=f"Income: €{Financetest.income:.2f} / Savings: €{Financetest.savings:.2f} / Spendings: €{Financetest.spendings:.2f}", text_color="pink", font=("Roboto", 16))
            label4.grid(row=1, column=0, pady=10, padx=10)
            
            label5 = customtkinter.CTkLabel(master=frame5, text="Projected months:", font=("Roboto", 16))
            label5.grid(row=0, column=0, pady=10, padx=10)

            entry1 = customtkinter.CTkEntry(master=frame5, placeholder_text="Enter projected months")
            entry1.grid(row=0, column=1, pady=10, padx=10)

            def calculate_projection():
                months = entry1.get()

                global frame6
                if frame6 is None or not frame6.winfo_exists():
                    frame6 = customtkinter.CTkFrame(master=frame3, fg_color="transparent", bg_color="transparent")
                    frame6.grid(row=2, column=0, columnspan=2, pady=10, padx=10)
                
                # Clear any existing frame at this position
                for widget in frame6.grid_slaves(row=0, column=0):
                    widget.destroy()
                
                if months is not None and months != "":
                    if string_to_num(months) is False or string_to_num(months) <= 0:
                        label6 = customtkinter.CTkLabel(master=frame6, text="Invalid projected months input. Please enter a number greater than zero.", text_color="pink", font=("Roboto", 16))
                        label6.grid(row=0, column=0, pady=10, padx=10)
                        return
                    else:
                        months = int(string_to_num(months))
                        result = Financetest.projection(months)
                        label6 = customtkinter.CTkLabel(master=frame6, text="Total savings of €" + f"{result:.2f}" + " after " + str(months) + " months", text_color="pink", font=("Roboto", 16))
                        label6.grid(row=0, column=0, pady=10, padx=10)
                        
                elif months is None or months == "":
                    label6 = customtkinter.CTkLabel(master=frame6, text="No projected months entered.", text_color="pink", font=("Roboto", 16))
                    label6.grid(row=0, column=0, pady=10, padx=10)
                    return

                def save_projection(savings_result):
                    Financetest.savings = savings_result
                    Financetest.save_savings()
                    Financetest.log.projection_calculation(f"{savings_result:.2f}")

                button4 = customtkinter.CTkButton(master=frame6, text="Save value as current savings", command=lambda: save_projection(result))
                button4.grid(row=0, column=1, pady=10, padx=10)

            button3 = customtkinter.CTkButton(master=frame5, text="Calculate", command=calculate_projection)
            button3.grid(row=0, column=2, pady=10, padx=10)

        ###############################################################################################################

        case "Interest":

            label3 = customtkinter.CTkLabel(master=frame1, text="Type of interest calculation:", font=("Roboto", 16))
            label3.grid(row=3, column=0, pady=10, padx=10)

            def interest_selection(choice):
                if frame3 is not None and frame3.winfo_exists():
                    frame3.destroy()
                
                match choice:
                    case "Simple Interest":
                        create_frame3(1, 0, window)
                        
                        frame4 = customtkinter.CTkFrame(master=frame3, fg_color="transparent", bg_color="transparent")
                        frame4.grid(row=0, column=0, pady=0, padx=0)

                        frame5 = customtkinter.CTkFrame(master=frame3, fg_color="transparent", bg_color="transparent")
                        frame5.grid(row=1, column=0, pady=0, padx=0)


                        label4 = customtkinter.CTkLabel(master=frame4, text="Simple interest: Total savings after projected years with simple interest", font=("Roboto", 24))
                        label4.grid(row=0, column=0, pady=10, padx=10)

                        label5 = customtkinter.CTkLabel(master=frame4, text=f"Savings: €{Financetest.savings:.2f}", text_color="pink", font=("Roboto", 16))
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
                            interest_money = entry1.get()
                            annual_rate = entry2.get()
                            years = entry3.get() #/12

                            global frame6

                            # Clear any existing frame at this position
                            if frame6 is not None and frame6.winfo_exists():
                                frame6.destroy()
                            
                            if interest_money is not None and interest_money != "":
                                if string_to_num(interest_money) is False or string_to_num(interest_money) <= 0 or string_to_num(interest_money) > Financetest.savings:
                                    if frame6 is None or not frame6.winfo_exists():
                                        create_frame6(0, 2, frame3)
                                    error_label = customtkinter.CTkLabel(master=frame6, text="Invalid portion of savings affected by interest. Please enter a value between 0 and " + str(Financetest.savings), text_color="pink", font=("Roboto", 16))
                                    error_label.grid(row=0, column=0, pady=10, padx=10)
                                    return
                                else:
                                    interest_money = float(string_to_num(interest_money))
                            
                            elif interest_money is None or interest_money == "":
                                 if frame6 is None or not frame6.winfo_exists():
                                        create_frame6(0, 2, frame3)
                                 error_label = customtkinter.CTkLabel(master=frame6, text="No portion of savings affected by interest entered.", text_color="pink", font=("Roboto", 16))
                                 error_label.grid(row=0, column=0, pady=10, padx=10)
                                 return
                            
                            if annual_rate is not None and annual_rate != "":
                                if string_to_num(annual_rate) is False or string_to_num(annual_rate) <= 0:
                                    if frame6 is None or not frame6.winfo_exists():
                                        create_frame6(0, 2, frame3)
                                    error_label = customtkinter.CTkLabel(master=frame6, text="Invalid annual interest rate input. Please enter a number greater than zero.", text_color="pink", font=("Roboto", 16))
                                    error_label.grid(row=1, column=0, pady=10, padx=10)
                                    return
                                else:
                                    annual_rate = float(string_to_num(annual_rate))

                            elif annual_rate is None or annual_rate == "":
                                if frame6 is None or not frame6.winfo_exists():
                                        create_frame6(0, 2, frame3)
                                error_label = customtkinter.CTkLabel(master=frame6, text="No annual interest rate entered.", text_color="pink", font=("Roboto", 16))
                                error_label.grid(row=1, column=0, pady=10, padx=10)
                                return
                            
                            if years is not None and years != "":
                                if string_to_num(years) is False or string_to_num(years) <= 0:
                                    if frame6 is None or not frame6.winfo_exists():
                                        create_frame6(0, 2, frame3)
                                    error_label = customtkinter.CTkLabel(master=frame6, text="Invalid projected months input. Please enter a number greater than zero.", text_color="pink", font=("Roboto", 16))
                                    error_label.grid(row=2, column=0, pady=10, padx=10)
                                    return
                                else:
                                    years = float(string_to_num(years))/12

                            elif years is None or years == "":
                                if frame6 is None or not frame6.winfo_exists():
                                        create_frame6(0, 2, frame3)
                                error_label = customtkinter.CTkLabel(master=frame6, text="No projected months entered.", text_color="pink", font=("Roboto", 16))
                                error_label.grid(row=2, column=0, pady=10, padx=10)
                                return
                            
                            result = Financetest.simple_interest(annual_rate, years, interest_money)

                            create_frame6(0, 2, frame3)
                            result_label = customtkinter.CTkLabel(master=frame6, text="Total savings of €" + f"{result:.2f}" + " after " + f"{years:.2f}" + " years with simple interest", text_color="pink", font=("Roboto", 16))
                            result_label.grid(row=0, column=0, pady=10, padx=10)

                        button4 = customtkinter.CTkButton(master=frame5, text="Calculate", command=calculate_simple_interest)
                        button4.grid(row=2, column=2, pady=10, padx=10)

                    case "Compound Interest":
                        create_frame3(1, 0, window)
                        
                        frame4 = customtkinter.CTkFrame(master=frame3, fg_color="transparent", bg_color="transparent")
                        frame4.grid(row=0, column=0, pady=0, padx=0)

                        frame5 = customtkinter.CTkFrame(master=frame3, fg_color="transparent", bg_color="transparent")
                        frame5.grid(row=1, column=0, pady=0, padx=0)


                        label4 = customtkinter.CTkLabel(master=frame4, text="Compound interest: Total savings after projected years with compound interest", font=("Roboto", 24))
                        label4.grid(row=0, column=1, pady=10, padx=10)

                        label5 = customtkinter.CTkLabel(master=frame4, text=f"Savings: €{Financetest.savings:.2f}", text_color="pink", font=("Roboto", 16))
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
                            interest_money = entry1.get()
                            annual_rate = entry2.get()
                            years = entry3.get() #/12
                            periods = entry4.get()

                            global frame6
                            if frame6 is not None and frame6.winfo_exists():
                                frame6.destroy()

                            if interest_money is not None and interest_money != "":
                                if string_to_num(interest_money) is False or string_to_num(interest_money) <= 0 or string_to_num(interest_money) > Financetest.savings:
                                    if frame6 is None or not frame6.winfo_exists():
                                        create_frame6(0, 2, frame3)
                                    error_label = customtkinter.CTkLabel(master=frame6, text="Invalid portion of savings affected by interest. Please enter a value between 0 and " + str(Financetest.savings), text_color="pink", font=("Roboto", 16))
                                    error_label.grid(row=0, column=0, pady=10, padx=10)
                                    return
                                else:
                                    interest_money = float(string_to_num(interest_money))
                            
                            elif interest_money is None or interest_money == "":
                                 if frame6 is None or not frame6.winfo_exists():
                                        create_frame6(0, 2, frame3)
                                 error_label = customtkinter.CTkLabel(master=frame6, text="No portion of savings affected by interest entered.", text_color="pink", font=("Roboto", 16))
                                 error_label.grid(row=0, column=0, pady=10, padx=10)
                                 return
                            
                            if annual_rate is not None and annual_rate != "":
                                if string_to_num(annual_rate) is False or string_to_num(annual_rate) <= 0:
                                    if frame6 is None or not frame6.winfo_exists():
                                        create_frame6(0, 2, frame3)
                                    error_label = customtkinter.CTkLabel(master=frame6, text="Invalid annual interest rate input. Please enter a number greater than zero.", text_color="pink", font=("Roboto", 16))
                                    error_label.grid(row=1, column=0, pady=10, padx=10)
                                    return
                                else:
                                    annual_rate = float(string_to_num(annual_rate))
                            
                            elif annual_rate is None or annual_rate == "":
                                if frame6 is None or not frame6.winfo_exists():
                                        create_frame6(0, 2, frame3)
                                error_label = customtkinter.CTkLabel(master=frame6, text="No annual interest rate entered.", text_color="pink", font=("Roboto", 16))
                                error_label.grid(row=1, column=0, pady=10, padx=10)
                                return
                            
                            if years is not None and years != "":
                                if string_to_num(years) is False or string_to_num(years) <= 0:
                                    if frame6 is None or not frame6.winfo_exists():
                                        create_frame6(0, 2, frame3)
                                    error_label = customtkinter.CTkLabel(master=frame6, text="Invalid projected months input. Please enter a number greater than zero.", text_color="pink", font=("Roboto", 16))
                                    error_label.grid(row=2, column=0, pady=10, padx=10)
                                    return
                                else:
                                    years = float(string_to_num(years))/12

                            elif years is None or years == "":
                                if frame6 is None or not frame6.winfo_exists():
                                        create_frame6(0, 2, frame3)
                                error_label = customtkinter.CTkLabel(master=frame6, text="No projected months entered.", text_color="pink", font=("Roboto", 16))
                                error_label.grid(row=2, column=0, pady=10, padx=10)
                                return

                            if periods is not None and periods != "":
                                if string_to_num(periods) is False or string_to_num(periods) <= 0:
                                    if frame6 is None or not frame6.winfo_exists():
                                        create_frame6(0, 2, frame3)
                                    error_label = customtkinter.CTkLabel(master=frame6, text="Invalid compounding periods input. Please enter a number greater than zero.", text_color="pink", font=("Roboto", 16))
                                    error_label.grid(row=3, column=0, pady=10, padx=10)
                                    return
                                else:
                                    periods = int(string_to_num(periods))

                            elif periods is None or periods == "":
                                if frame6 is None or not frame6.winfo_exists():
                                        create_frame6(0, 2, frame3)
                                error_label = customtkinter.CTkLabel(master=frame6, text="No compounding periods entered.", text_color="pink", font=("Roboto", 16))
                                error_label.grid(row=3, column=0, pady=10, padx=10)
                                return
                                
                            result = Financetest.compound_interest(annual_rate, years, interest_money, periods)

                            create_frame6(0, 2, frame3)
                            result_label = customtkinter.CTkLabel(master=frame6, text="Total savings of €" + f"{result:.2f}" + " after " + f"{years:.2f}" + " years with compound interest", text_color="pink", font=("Roboto", 16))
                            result_label.grid(row=0, column=0, pady=10, padx=10)
                        
                        button4 = customtkinter.CTkButton(master=frame5, text="Calculate", command=calculate_compound_interest)
                        button4.grid(row=3, column=2, pady=10, padx=10)

            combobox2 = customtkinter.CTkComboBox(master=frame1, values=["-Select-", "Simple Interest", "Compound Interest"], command=interest_selection)
            combobox2.grid(row=4, column=0, pady=10, padx=10)

        ###############################################################################################################

        case "Show expenses(table)":
            create_frame2(1, 1, window)
            frame2.grid_rowconfigure(0, weight=1)
            frame2.grid_columnconfigure(0, weight=1)   
            
            frame3 = customtkinter.CTkFrame(master=window, fg_color="transparent", bg_color="transparent")
            frame3.grid(row=0, column=1, pady=5, padx=5, sticky="new")
            frame3.grid_columnconfigure(0, weight=0)
            frame3.grid_columnconfigure(1, weight=0)
            frame3.grid_columnconfigure(2, weight=0)
            frame3.grid_columnconfigure(3, weight=0)
            frame3.grid_rowconfigure(0, weight=0)

            def add_expense(category, amount, date):
                global frame4

                if frame4 is not None and frame4.winfo_exists():
                    frame4.destroy()

                if amount is not None and amount != "":
                    if string_to_num(amount) is False or string_to_num(amount) <= 0:
                        if frame4 is None or not frame4.winfo_exists():
                            create_frame4(1, 2, window)
                        error_label = customtkinter.CTkLabel(master=frame4, text="Invalid expense input. Please enter a number greater than zero, and seperate decimals with a period.", text_color="pink", font=("Roboto", 16))
                        error_label.grid(row=0, column=0, pady=10, padx=10)
                        return
                    else:
                        amount = string_to_num(amount)

                elif amount is None or amount == "":
                    if frame4 is None or not frame4.winfo_exists():
                        create_frame4(1, 2, window)
                    error_label = customtkinter.CTkLabel(master=frame4, text="No expense amount entered.", text_color="pink", font=("Roboto", 16))
                    error_label.grid(row=0, column=0, pady=10, padx=10)
                    return

                if date is not None and date != "":
                    if not Financetest.validate_date(date):
                        if frame4 is None or not frame4.winfo_exists():
                            create_frame4(1, 2, window)
                        error_label = customtkinter.CTkLabel(master=frame4, text="Invalid date format. Please enter date as DD.MM.YYYY.", text_color="pink", font=("Roboto", 16))
                        error_label.grid(row=1, column=0, pady=10, padx=10)
                        return
                elif date is None or date == "":
                    if frame4 is None or not frame4.winfo_exists():
                        create_frame4(1, 2, window)
                    error_label = customtkinter.CTkLabel(master=frame4, text="No date entered. Using current date: " + Financetest.current_date, text_color="pink", font=("Roboto", 16))
                    error_label.grid(row=1, column=0, pady=10, padx=10)
                    
                if category is not None and category != "":
                    category = category.lower()
                elif category is None or category == "":
                    if frame4 is None or not frame4.winfo_exists():
                        create_frame4(1, 2, window)
                    error_label = customtkinter.CTkLabel(master=frame4, text="No category entered. Using default category: misc.", text_color="pink", font=("Roboto", 16))
                    error_label.grid(row=2, column=0, pady=10, padx=10)
                    category = "misc."

                date = Financetest.current_date if not date else date
                Financetest.add_expense(amount, date, category)
                Financetest.log.add_expense(category, amount, date)

                last_savings = float(Financetest.find_last_savings_value(date))
                if date == Financetest.current_date:
                    Financetest.update_savings(last_savings - float(amount), date)
                else:
                    Financetest.add_saving(last_savings - float(amount), date)
                    
                Financetest.log.update_savings(last_savings - float(amount), last_savings)

                item_id = Financetest.all_expense_lines[-1][1]

                table.insert(parent="", index=0, iid=item_id, values=(category, amount, date), tags=('fg', "oddrow" if len(table.get_children()) % 2 == 0 else "evenrow"))

            button3 = customtkinter.CTkButton(master=frame3, text="Add expense", command=lambda: open_add_expense_window())
            button3.grid(row=0, column=3, pady=10, padx=10, sticky="e")


            table = ttk.Treeview(frame2, 
                                columns=("Category", "Amount", "Day"), 
                                show="headings", 
                                height=len(Financetest.all_expense_lines) if len(Financetest.all_expense_lines) < 15 else 15,
                                style="Treeview",
                                selectmode='browse')
            
            vsb = ttk.Scrollbar(frame2, 
                                orient="vertical", 
                                style="TScrollbar",
                                command=table.yview)
            
            table.configure(yscrollcommand=vsb.set)
            
            table.heading("Category", text="Category")
            table.heading("Amount", text="Amount")
            table.heading("Day", text="Day(date)")
            table.tag_configure("oddrow", background="#333333")
            table.tag_configure("evenrow", background="#232323")
            table.tag_configure('fg', foreground='white')
            
            for i, x in enumerate(Financetest.all_expense_lines):
                tag = "oddrow" if i % 2 == 0 else "evenrow"
                item_id = x[1]
                table.insert(parent="", index=0, iid=item_id, values=(x[3], x[0], x[2]), tags=('fg', tag))
            
            table.grid(row=0, column=0, sticky="nsew")
            vsb.grid(row=0, column=1, sticky="ns")
            
            def open_add_expense_window():
                # Open AddExpense window and pass GUItest's take_expense_data as the save callback
                AddExpense.main(on_save=take_expense_data)
            
            def take_expense_data():
                add_expense(AddExpense.get_category(), AddExpense.get_amount(), AddExpense.get_date())
                AddExpense.window.destroy()
            
            def delete_expense(event=None):
                x = table.selection()
                if not x:
                    return
                
                item_id = x[0]
                Financetest.delete_expense(item_id)
                table.delete(item_id)
            
            table.bind('d', delete_expense)

        ###############################################################################################################

        case "Graph expenses":
            create_frame2(1, 0, window)
            
            label3 = customtkinter.CTkLabel(master=frame1, text="Select month:", font=("Roboto", 16))
            label3.grid(row=3, column=0, pady=10, padx=10)

            def month_selection(choice):
                if choice == "All months":
                    fig = Financetest.monthly_expenses_graph()
                elif choice == "Current month":
                    fig = Financetest.expenses_graph(float(Financetest.current_month))
                else:
                    fig = Financetest.expenses_graph(float(choice))
                canvas = FigureCanvasTkAgg(fig, master=frame2)
                canvas.draw()
                canvas.get_tk_widget().grid(row=0, column=0, sticky="nsew")

            month_selection(Financetest.current_month)  # Show current month graph by default

            combobox2 = customtkinter.CTkComboBox(master=frame1, values=["Current month", *Financetest.get_all_months(), "All months"], command=month_selection)
            combobox2.grid(row=4, column=0, pady=10, padx=10)

###############################################################################################################

combobox = customtkinter.CTkComboBox(master=frame1, values=["-Select-", "Change values", "Projection calculations", "Interest", "Show expenses(table)", "Graph expenses"], command=select)
combobox.grid(row=2, column=0, pady=10, padx=10)

###############################################################################################################

window.mainloop()
window.protocol("WM_DELETE_WINDOW", Financetest.log.login("logged out"))