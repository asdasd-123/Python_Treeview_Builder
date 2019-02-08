import tkinter as tk
import tkinter.ttk as ttk

class TreeBuild:
    def __init__(self, parent, data, headings, search=False, widths=[], **kwargs):
        """Will place a treeview with provided data set, complete with search boxes if needed.
        * - Optional
        parent  - parent frame
        data    - list of lists containing row data
        heading - list of heading names
        search* - Default=False. True to add search boxes
        widths* - List of fixed column widths, otherwise auto selected
        """
        # Setting attributes as the kwargs (planning to use this later.)
        for key, value in kwargs.items():
            setattr(self, key, value)
            print("self." + key + " = " + str(value))
        
        self.parent = parent
        self.data = list(data)
        self.headings = list(headings)
        self.search = search
        self.widths = list(widths)

        # Saving the below example incase I need to access any kwargs
        # self.search = getattr(self, "search", None)
        if self.search == True:
            self._build_search_frame()

    def _build_tree_frame(self):
        print("tree frame")
    
    def _build_search_frame(self):
        print("search frame")