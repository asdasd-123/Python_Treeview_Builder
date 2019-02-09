from TreeBuild import TreeBuild
import tkinter as tk
import tkinter.ttk as ttk

search_headings = ("ID", "Name", "Chip No. ", "Vaccinated")
search_widths = (40, 100, 150, 80)
search_data = (
    ("01", "Cookie", "7493732", "42005"),
    ("02", "Gibbie", "7342152", "42038"),
    ("03", "Tinkerbelle", "1681023", "42071"),
    ("04", "Wispa", "6369268", "42104"),
    ("05", "Pebbles", "4362464", "42137"),
    ("06", "Tatsiana", "5674374", "42170"),
    ("07", "Cookiea", "9076052", "42203"),
    ("08", "Gibbiea", "6237524", "42236"),
    ("09", "Tinkerbellea", "6159266", "42269"),
    ("10", "Wispaa", "1521653", "42302"),
    ("11", "Pebblesa", "8150588", "42335"),
    ("12", "Tatsianaa", "1505322", "42368"),
    ("13", "Cookieaa", "4445858", "42401"),
    ("14", "Gibbieaa", "6390976", "42434"),
    ("15", "Tinkerbelleaa", "1968907", "42467"),
    ("16", "Wispaaa", "1501928", "42500"),
    ("17", "Pebblesaa", "3430556", "42533"),
    ("18", "Tatsianaaa", "6453150", "42566"),
    ("19", "Cookieaaa", "3750061", "42599"),
    ("20", "Gibbieaaa", "1742287", "42632"),
    ("21", "Tinkerbelleaaa", "7138771", "42665"),
    ("22", "Wispaaaa", "4020316", "42698"),
    ("23", "Pebblesaaa", "6514509", "42731"),
    ("24", "Tatsianaaaa", "1438670", "42764"),
    ("25", "Cookieaaaa", "1151414", "42797"),
    ("26", "Gibbieaaaa", "8535522", "42830"),
    ("27", "Tinkerbelleaaaa", "4106620", "42863"),
    ("28", "Wispaaaaa", "4390267", "42896"),
    ("29", "Pebblesaaaa", "2554880", "42929"),
    ("30", "Tatsianaaaaa", "7180502", "42962"),
    ("31", "Cookieaaaaa", "9735914", "42995")
    )



root = tk.Tk()

blue_frame = ttk.Style()
blue_frame.configure("blue.TFrame", background="blue")

main_frame = ttk.Frame(root, width="500", height="500", style="blue.TFrame")
main_frame.pack_propagate(0)
main_frame.pack(expand=True, fill="both")

tree_1 = TreeBuild(
    main_frame, 
    search=True, 
    data=search_data,
    widths=search_widths,
    headings=search_headings)


root.mainloop()