import tkinter as tk
from tkinter import ttk


def create_merged_header_treeview(name):
    # Create a frame for the merged header
    header_frame = ttk.Frame(root)
    header_frame.pack(fill="x")

    # Create the merged header label
    # 'col1' + 'col2' are merged under "Merged Header"
    merged_label = ttk.Label(header_frame, text=name, font=("Arial", 10, "bold"))
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
tree = ttk.Treeview(root, columns=("col1", "col2", "col3"), show="headings", height=5)
tree.pack(fill="both", expand=True)

# Configure columns
tree.heading("col1", text="A")
tree.heading("col2", text="B")
tree.heading("col3", text="C")
tree.column("col1", width=50)
tree.column("col2", width=50)
tree.column("col3", width=50)

# Add a small spacer to align the second merged part if needed, 
# or simply place the label above the specific columns visually.
# For precise alignment, you might need to calculate pixel widths,
# but visually stacking a label above the widget is the standard Tkinter approach.

root.mainloop()   