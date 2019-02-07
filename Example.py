from TreeBuild import TreeBuild
import tkinter as tk
import tkinter.ttk as ttk

root = tk.Tk()

main_frame = ttk.Frame(root, width="500", height="500")
main_frame.pack(expand=True, fill="both")

Tree1 = TreeBuild(main_frame)

root.mainloop()