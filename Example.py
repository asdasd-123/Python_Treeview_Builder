from TreeBuild import TreeBuild
import tkinter as tk
import tkinter.ttk as ttk

# Tuples containing data to build the tree in
search_headings = ("ID", "Name", "Item No. ", "Date")
search_widths = (40, 100, 150, 80)
search_data = (
    ('00001', 'Item001', '1121231302', '04 Jan 2005'),
    ('00002', 'Item002', '3798636533', '07 May 2005'),
    ('00003', 'Item003', '1704703785', '07 Sep 2005'),
    ('00004', 'Item004', '3234612220', '08 Jan 2006'),
    )

# Build a simple GUI for testing
root = tk.Tk()

# Creating a quick test style to colour the background blue
blue_frame = ttk.Style()
blue_frame.configure("blue.TFrame", background="blue")

# Creating a simple frame to house the treeview
main_frame = ttk.Frame(root, width="500", height="500", style="blue.TFrame")
main_frame.pack_propagate(0)
main_frame.pack(expand=True, fill="both")

# This function builds the treeview in a single command
tree_1 = TreeBuild(
    main_frame,                         # Parent frame
    search=True,                        # Enable search boxes or not
    data=search_data,                   # Data list if lists for Tree
    widths=search_widths,               # List of heading widths (optional)
    headings=search_headings)           # List of tree headings     


# How to bind a function to the treeview event.
def test_func(test):
    print("teststring = " + str(test['values'][0]))
tree_1.tree.bind("<Double-1>", lambda c: test_func(tree_1.tree.item(tree_1.tree.focus())))

# test_button = ttk.Button(root, text="test button", command=print_id_contents)
# test_button.pack(side="bottom")

root.mainloop()


# How to access search box contents.
# temp_var = getattr(tree_1, search_headings[1]).get()