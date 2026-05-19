import customtkinter

# Module-level references so other modules can access the window, frame and getters
window = None
frame1 = None

def main(on_save=None):
    """Create and show the Add Expense window.

    Args:
        on_save (callable|None): Optional callback called when the Save button
            is pressed. If provided it will be used as the button command.
    """
    global window, frame1, entry_cat, entry_amt, entry_date

    window = customtkinter.CTk()
    window.title("Add Expense")

    frame1 = customtkinter.CTkFrame(master=window)
    frame1.grid(row=0, column=0, pady=10, padx=10)

    entry_cat = customtkinter.CTkEntry(master=frame1, placeholder_text="Enter Category")
    entry_cat.grid(row=0, column=0, pady=10, padx=10)

    entry_amt = customtkinter.CTkEntry(master=frame1, placeholder_text="Enter Amount")
    entry_amt.grid(row=0, column=1, pady=10, padx=10)

    entry_date = customtkinter.CTkEntry(master=frame1, placeholder_text="Enter Date (DD.MM.YYYY)")
    entry_date.grid(row=0, column=2, pady=10, padx=10)

    # Create Save button inside this window. If caller provided a callback,
    # use it; otherwise provide a default that simply closes the window.
    if on_save is not None:
        save_cmd = on_save
    else:
        save_cmd = lambda: window.destroy()

    button1 = customtkinter.CTkButton(master=frame1, text="Save", command=save_cmd)
    button1.grid(row=0, column=3, pady=10, padx=10)

    window.mainloop()


def get_category():
    return entry_cat.get()


def get_amount():
    return entry_amt.get()


def get_date():
    return entry_date.get()