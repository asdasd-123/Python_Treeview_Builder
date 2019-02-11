## TreeBuild:
This library will build a TTK Treeview widget inside a supplied frame.

Features:
- Option to enable search boxes.
- Easily toggle between column widths being supplied or calculated automatically based on heading title width

# How to use it: (Check example.py for full working example)
- Create a frame you want it to be housed in.
```python
main_frame = ttk.Frame(root, width="500", height="500", style="blue.TFrame")
main_frame.pack_propagate(0)
main_frame.pack(expand=True, fill="both")
```
It will look like this:

![](https://user-images.githubusercontent.com/35167513/52554698-8a22bc80-2ddf-11e9-919a-4c6cae18ba3c.png)

- Call TreeBuild and send it the required info: 
```python
tree_1 = TreeBuild(
    main_frame,                # Parent frame
    search=True,               # Enable search boxes or not (True/False)
    data=search_data,          # Data list of lists for Tree
    widths=search_widths,      # List of heading widths (optional)
    headings=search_headings)  # List of tree headings
```
And thats it, you have a Treeview with full functioning search boxes, with headings that sort the data when clicked.

It should then look something like this:

![](https://user-images.githubusercontent.com/35167513/52554944-4c726380-2de0-11e9-9300-85c6ab9eaf1f.png)

# How to communicate with it
- To bind events to the Treeview:
```python
tree_1.tree.bind(
    "<Double-1>",
    lambda c: test_func(tree_1.tree.item(tree_1.tree.focus())))
```
This will call the function 'test_func' and send it the current selected row information.

- To read data from the search box:
```python
temp_var = getattr(tree_1, search_headings[1]).get()
```

# To-Do list
- Add optional parameter to enable multiple selection in Treeview