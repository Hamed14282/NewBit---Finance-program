import tkinter as tk
from tkinter import ttk
import customtkinter


def create_merged_header_treeview(name):
    # Create a frame for the merged header
    header_frame = customtkinter.CTkFrame(root)
    header_frame.pack(fill="x")

    # Create the merged header label
    # 'col1' + 'col2' are merged under "Merged Header"
    merged_label = customtkinter.CTkLabel(header_frame, text=name, font=("Arial", 10, "bold"))
    merged_label.pack(side="left")

root = tk.Tk()
root.title("Merged Header Example")

create_merged_header_treeview("Games")

# Create the Treeview
tree = ttk.Treeview(root, columns=("col1", "col2", "col3"), show="headings", height=5)
tree.pack(fill="both", expand=True)

# Configure columns
tree.heading("col1", text="A")
tree.heading("col2", text="B")
tree.heading("col3", text="C")
tree.column("col1", width=50)
tree.column("col2", width=50)
tree.column("col3", width=50)

create_merged_header_treeview("misc.")

# Create the Treeview
tree1 = ttk.Treeview(root, columns=("col1", "col2", "col3"), show="headings", height=5)
tree1.pack(fill="both", expand=True)

# Configure columns
tree1.heading("col1", text="A")
tree1.heading("col2", text="B")
tree1.heading("col3", text="C")
tree1.column("col1", width=50)
tree1.column("col3", width=50)
tree1.column("col2", width=50)

t = 3
def del1():
    global t
    tree.delete(t)
    t -=1

button3 = customtkinter.CTkButton(master=root, text="Del 1", command=del1)
button3.pack()

v = 3
def del2():
    global v
    tree1.delete(v)
    v -=1

button32 = customtkinter.CTkButton(master=root, text="Del 2", command=del2)
button32.pack()

tree.insert(parent="", index=0, iid=1, values=("A1", "B1", "C1"))
tree.insert(parent="", index=0, iid=2, values=("A2", "B2", "C2"))
tree.insert(parent="", index=0, iid=3, values=("A3", "B3", "C3"))
tree1.insert(parent="", index=0, iid=1, values=("xA1", "B1", "C1"))
tree1.insert(parent="", index=0, iid=2, values=("xA2", "B2", "C2"))
tree1.insert(parent="", index=0, iid=3, values=("xA3", "B3", "C3"))
# Add a small spacer to align the second merged part if needed, 
# or simply place the label above the specific columns visually.
# For precise alignment, you might need to calculate pixel widths,
# but visually stacking a label above the widget is the standard Tkinter approach.

root.mainloop()   

#maybe put everything in a function, then return the root
# so in GUItest it would be Games_part = create_table(name, col1, col2)