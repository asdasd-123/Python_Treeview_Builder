import tkinter as tk
import tkinter.ttk as ttk

class TreeBuild:
    def __init__(self, parent, search=False, **kwargs):
        """parent - """
        for key, value in kwargs.items():
            setattr(self, key, value)
            print("self." + key + " = " + str(value))
        
        self.parent = parent
        self.search = search
        # Saving the below example incase I need to access any kwargs
        # self.search = getattr(self, "search", None)
        if self.search == True:
            self._build_search_frame()
    
    def _build_tree_frame(self):
        print("tree frame")
    
    def _build_search_frame(self):
        print("search frame")