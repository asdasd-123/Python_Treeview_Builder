from TreeBuild import TreeBuild
import tkinter as tk
import tkinter.ttk as ttk

search_headings = ("ID", "Name", "Item No. ", "Date")
search_widths = (40, 100, 150, 80)
search_data = (
    ('00001', 'Item001', '1121231302', '04 Jan 2005'),
    ('00002', 'Item002', '3798636533', '07 May 2005'),
    ('00003', 'Item003', '1704703785', '07 Sep 2005'),
    ('00004', 'Item004', '3234612220', '08 Jan 2006'),
    ('00005', 'Item005', '4873247479', '11 May 2006'),
    ('00006', 'Item006', '2710791076', '11 Sep 2006'),
    ('00007', 'Item007', '6143235832', '12 Jan 2007'),
    ('00008', 'Item008', '6752199391', '15 May 2007'),
    ('00009', 'Item009', '1615005792', '15 Sep 2007'),
    ('00010', 'Item010', '7097809495', '16 Jan 2008'),
    ('00011', 'Item011', '3402119654', '18 May 2008'),
    ('00012', 'Item012', '4540859794', '18 Sep 2008'),
    ('00013', 'Item013', '4311464661', '19 Jan 2009'),
    ('00014', 'Item014', '7738053214', '22 May 2009'),
    ('00015', 'Item015', '1024605797', '22 Sep 2009'),
    ('00016', 'Item016', '3205582001', '23 Jan 2010'),
    ('00017', 'Item017', '5233346823', '26 May 2010'),
    ('00018', 'Item018', '7510473130', '26 Sep 2010'),
    ('00019', 'Item019', '8207288923', '27 Jan 2011'),
    ('00020', 'Item020', '7812927148', '30 May 2011'),
    ('00021', 'Item021', '8846678009', '30 Sep 2011'),
    ('00022', 'Item022', '5390367260', '31 Jan 2012'),
    ('00023', 'Item023', '3398976849', '02 Jun 2012'),
    ('00024', 'Item024', '7561181812', '03 Oct 2012'),
    ('00025', 'Item025', '3705534712', '03 Feb 2013'),
    ('00026', 'Item026', '5082871436', '06 Jun 2013'),
    ('00027', 'Item027', '6565290991', '07 Oct 2013'),
    ('00028', 'Item028', '5713814353', '07 Feb 2014'),
    ('00029', 'Item029', '9684824930', '10 Jun 2014'),
    ('00030', 'Item030', '1316487806', '11 Oct 2014'),
    ('00031', 'Item031', '9318506871', '11 Feb 2015')
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