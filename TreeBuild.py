# =============================================
#   _______            ____        _ _     _
#  |__   __|          |  _ \      (_) |   | |
#     | |_ __ ___  ___| |_) |_   _ _| | __| |
#     | | '__/ _ \/ _ \  _ <| | | | | |/ _` |
#     | | | |  __/  __/ |_) | |_| | | | (_| |
#     |_|_|  \___|\___|____/ \__,_|_|_|\__,_|
#
# =============================================
# This library will build a TTK Treeview widget inside a supplied frame.
#
# An example of how to create one:
# tree_1 = TreeBuild(
#     main_frame,                # Parent frame
#     search=True,               # Enable search boxes or not (True/False)
#     data=search_data,          # Data list of lists for Tree
#     widths=search_widths,      # List of heading widths (optional)
#     headings=search_headings)  # List of tree headings
#
# An example of how to then bind a function to the treeview
# tree_1.tree.bind(
#     "<Double-1>",
#     lambda c: test_func(tree_1.tree.item(tree_1.tree.focus())))
#
# An example of how to read the contents of one of the search boxes.
# temp_var = getattr(tree_1, search_headings[1]).get()

import tkinter.ttk as ttk
import tkinter.font as tkfont


class TreeBuild:
    """Will place a treeview with provided data set,
    complete with search boxes if needed.
    * - Optional
    parent  - parent frame
    data    - list of lists containing row data
    heading - list of heading names
    search* - Default=False. True to add search boxes
    widths* - List of fixed column widths, otherwise auto selected
    """
    def __init__(self, parent, data, headings, search=False, widths=[]):
        """Will place a treeview with provided data set,
        complete with search boxes if needed.
        * - Optional
        parent  - parent frame
        data    - list of lists containing row data
        heading - list of heading names
        search* - Default=False. True to add search boxes
        widths* - List of fixed column widths, otherwise auto selected
        """

        self.parent = parent
        self.original_data = list(data)
        self.data = list(data)
        self.original_headings = list(headings)
        self.headings = list(headings)
        self.search = search
        self.widths = list(widths)
        if len(widths) > 0:
            self.widths_supplied = True
        else:
            self.widths_supplied = False

        # Setup any styles used.
        self._setup_styles()
        self._convert_headings()

        # Saving the below example incase I need to access any kwargs
        # self.search = getattr(self, "search", None)

        if self.search:
            self._build_search_frame()

        self._build_tree()
        self._populate_tree()

    def _setup_styles(self):
        self.blue_frame = ttk.Style()
        self.blue_frame.configure("blue.TFrame", background="blue")
        self.green_frame = ttk.Style()
        self.green_frame.configure("green.TFrame", background="green")
        self.red_frame = ttk.Style()
        self.red_frame.configure("red.TFrame", background="red")
        self.yellow_frame = ttk.Style()
        self.yellow_frame.configure("yellow.TFrame", background="yellow")
        self.pink_frame = ttk.Style()
        self.pink_frame.configure("pink.TFrame", background="pink")
        self.brown_frame = ttk.Style()
        self.brown_frame.configure("brown.TFrame", background="brown")
        self.grey_frame = ttk.Style()
        self.grey_frame.configure("grey.TFrame", background="grey")
        self.purple_frame = ttk.Style()
        self.purple_frame.configure("purple.TFrame", background="purple")
        self.white_frame = ttk.Style()
        self.white_frame.configure("white.TFrame", background="white")

    def _convert_headings(self):
        """convert the headings list to a list of ID's
        needed for building up the search list"""
        new_headings = []
        for counter, item in enumerate(self.headings):
            new_heading_list = [str(item),
                                str(item) + '_frame',
                                str(item) + '_text_data']
            if self.widths_supplied:
                new_heading_list.append(self.widths[counter])
            new_headings.append(new_heading_list)
        self.headings = list(new_headings)

        # Now setting all new heading info as attributes of TreeBuild
        # for row in self.headings:
        #     for item in row:
        #         setattr(self, )

    def _build_search_frame(self):
        self.search_frame = ttk.Frame(self.parent, height="50")
        self.search_frame.pack(side="top", anchor="n", fill="x")
        for heading in self.headings:
            # Get width of heading in pixels
            if self.widths_supplied:
                w = heading[3]
            else:
                w = tkfont.Font().measure(heading[0]) + 20

            # Build the frame and then the entry box inside.
            setattr(self, heading[1], ttk.Frame(self.search_frame,
                                                padding="3",
                                                width=w,
                                                height="30"))
            getattr(self, heading[1]).pack_propagate(0)
            getattr(self, heading[1]).pack(side="left")
            setattr(self, heading[0], ttk.Entry(getattr(self, heading[1]),
                                                exportselection=0,
                                                textvariable=heading[2]))
            getattr(self, heading[0]).name = heading[0]
            getattr(self, heading[0]).bind(
                "<KeyRelease>",
                lambda event: self._search_tree(
                    self.tree,
                    self.original_data,
                    self.original_headings,
                    event.widget.name,
                    event.widget.get()))
            getattr(self, heading[0]).pack(side="left",
                                           fill="x",
                                           expand="True")

    def _build_tree(self):

        # Creating the tree frame
        self.tree_frame = ttk.Frame(self.parent)
        self.tree_frame.pack(side="bottom",
                             anchor="n",
                             expand=True,
                             fill="both")

        # Build tree
        self.tree = ttk.Treeview(columns=self.original_headings,
                                 show="headings",
                                 selectmode="browse")
        vsb = ttk.Scrollbar(orient="vertical", command=self.tree.yview)
        self.tree.configure(yscrollcommand=vsb.set)
        self.tree.grid(column=0, row=0, sticky="nsew", in_=self.tree_frame)
        vsb.grid(column=1, row=0, sticky="ns", in_=self.tree_frame)

        self.tree_frame.grid_columnconfigure(0, weight=1)
        self.tree_frame.grid_rowconfigure(0, weight=1)

        # Setting up column widths
        for col in self.headings:
            # Get width of column in pixels
            if self.widths_supplied:
                w = col[3]
            else:
                w = tkfont.Font().measure(col[0]) + 20

            self.tree.heading(
                col[0],
                text=col[0],
                anchor="w",
                command=lambda c=col[0]: self._sort_tree(self.tree, c, 0))
            self.tree.column(col[0], width=w, anchor="w", stretch="No")

    def _populate_tree(self):
        for item in self.data:
            self.tree.insert('', 'end', values=item)

    def _sort_tree(self, tree, col, descending):
        """Sort the tree column when clicked on"""
        # Grab values to sort
        data = [(tree.set(child, col), child)
                for child in tree.get_children('')]

        # Re-order ther data
        data.sort(reverse=descending)

        # Update the tree with new order.
        for index, item in enumerate(data):
            tree.move(item[1], '', index)

        # Switch the heading so that it will sort in the opposite order
        tree.heading(
            col,
            command=lambda col=col: self._sort_tree(tree,
                                                    col,
                                                    int(not descending)))

    def _search_tree(self, tree, ds, dh, col_st, st):
        """Will search through any tree or column for a specific string.
        The following must be supplied:
        tree     - tree to adjust
        ds       - data set to search
        dh       - data headings to find which col number
        col_st   - column string to check against headings
        st       - text in search box"""
        # If search str empty, use full data set.
        # Slightly more efficient as it avoids the search
        if st == '':
            tree.delete(*tree.get_children())   # Delete all items in tree
            for row in ds:
                tree.insert('', 'end', values=row)
            return

        col = dh.index(col_st)
        new_data = []   # List to store new filtered list
        for row in ds:  # Build new filtered list
            if (row[col].upper()).__contains__(st.upper()):
                new_data.append(row)
        tree.delete(*tree.get_children())   # Delete all items in tree
        self.data = new_data
        for row in new_data:                # Build up tree with new data
            tree.insert('', 'end', values=row)

    def refresh_data(self, new_data):
        """Will refresh the data in the tree with a new set provided.
        Will not affect columns/headings"""
        self.tree.delete(*self.tree.get_children())
        for row in new_data:
            self.tree.insert('', 'end', values=row)
