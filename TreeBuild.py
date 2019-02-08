import tkinter as tk
import tkinter.ttk as ttk
import tkinter.font as tkfont

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

        self._convert_headings()

        # Saving the below example incase I need to access any kwargs
        # self.search = getattr(self, "search", None)
        if self.search == True:
            self._build_search_frame()

    def _convert_headings(self):
        """convert the headings list to a list of ID's needed"""
        new_headings = []       
        for item in self.headings:
            new_heading_list = [str(item), str(item) + '_frame']
            new_headings.append(new_heading_list)
        self.headings = list(new_headings)
        print("new headings:\n\n" + str(self.headings))
        
        # Now setting all new heading info as attributes of TreeBuild
        # for row in self.headings:
        #     for item in row:
        #         setattr(self, )

    def _build_search_frame(self):
        self.search_frame = ttk.Frame(self.parent, height="50", style="red.TFrame")
        self.search_frame.pack(side="top", anchor="n", expand=True, fill="x")
        for heading in self.headings:
            # Get width of heading in pixels
            w = tkfont.Font().measure(heading[0])
            setattr(self, heading[1], ttk.Frame(self.search_frame, padding="5", style="green.TFrame"))
            getattr(self, heading[1]).pack(side="left")
            setattr(self, heading[0], ttk.Entry(getattr(self, heading[1])))
            getattr(self, heading[0]).pack(side="left")
            

    def _build_tree_frame(self):
        print("tree frame")

