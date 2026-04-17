import tkinter as tk

window = tk.Tk()

 
window.title("GUI test")
window.geometry("800x600")

label = tk.Label(window, text="GUI app", font=('Arial', 19))
label.pack()

frame = tk.Frame(window)
frame.pack()



window.mainloop() 