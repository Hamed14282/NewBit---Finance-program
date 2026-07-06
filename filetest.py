import tkinter as tk
from tkinter import ttk

root = tk.Tk()
root.title("Merged Header Example")

# Create a frame for the merged header
header_frame = ttk.Frame(root)
header_frame.pack(fill="x")

# Create the Treeview
tree = ttk.Treeview(root, columns=("col1", "col2", "col3"), show="headings")
tree.pack(fill="both", expand=True)

# Configure columns
tree.heading("col1", text="A")
tree.heading("col2", text="B")
tree.heading("col3", text="C")
tree.column("col1", width=50)
tree.column("col2", width=50)
tree.column("col3", width=50)

# Create the merged header label
# 'col1' + 'col2' are merged under "Merged Header"
merged_label = ttk.Label(header_frame, text="Merged Header", font=("Arial", 10, "bold"))
merged_label.pack(side="left")

# Create a frame for the merged header
header_frame1 = ttk.Frame(root)
header_frame1.pack(fill="x")

# Create the Treeview
tree1 = ttk.Treeview(root, columns=("col1", "col2", "col3"), show="headings")
tree1.pack(fill="both", expand=True)

# Configure columns
tree1.heading("col1", text="A")
tree1.heading("col2", text="B")
tree1.heading("col3", text="C")
tree1.column("col1", width=50)
tree1.column("col2", width=50)
tree1.column("col3", width=50)

# Create the merged header label
# 'col1' + 'col2' are merged under "Merged Header"
merged_label1 = ttk.Label(header_frame1, text="Merged Header1", font=("Arial", 10, "bold"))
merged_label1.pack(side="left")

# Add a small spacer to align the second merged part if needed, 
# or simply place the label above the specific columns visually.
# For precise alignment, you might need to calculate pixel widths,
# but visually stacking a label above the widget is the standard Tkinter approach.

root.mainloop()   