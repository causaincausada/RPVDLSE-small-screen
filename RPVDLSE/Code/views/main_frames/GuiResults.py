import tkinter as tk 
from tkinter import ttk
from tkcalendar import DateEntry 
from Code.views.others.Language import Language
from Code.views.others.Messages import Messages


class GuiResults(ttk.Frame):
    def __init__(self, root):
        super().__init__(root.tab_control)
        
        #Language pack
        self.root = root
        self.language = Language()
        self.messages = Messages(root.numlanguage)
        self.language.languageChange(root.numlanguage)

        #Layout Management: pack
        
        #Frame Filters 
        #layout grid
        #configure grid
        self.frame_filters = ttk.Frame(self)
        self.frame_filters.columnconfigure(0, weight=5)
        self.frame_filters.columnconfigure(1, weight=5)
        self.frame_filters.rowconfigure(0, weight=5)
        self.frame_filters.rowconfigure(1, weight=5)
        self.frame_filters.rowconfigure(2, weight=5)
        self.frame_filters.rowconfigure(3, weight=5)

        #Frame filters date-hour
        #layout grid
        #configure grid
        self.frame_filters_date_hour = ttk.Frame(self.frame_filters)
        self.frame_filters_date_hour.columnconfigure(0, weight=5)
        self.frame_filters_date_hour.columnconfigure(1, weight=5)
        self.frame_filters_date_hour.columnconfigure(2, weight=5)
        self.frame_filters_date_hour.rowconfigure(0, weight=5)
        self.frame_filters_date_hour.rowconfigure(1, weight=5)
        self.frame_filters_date_hour.rowconfigure(2, weight=5)

        label_filters_date = ttk.Label(self.frame_filters_date_hour,
                                       text=self.language.date)
        label_filters_hour = ttk.Label(self.frame_filters_date_hour,
                                       text=self.language.hour)
        label_filters_begin = ttk.Label(self.frame_filters_date_hour,
                                       text=self.language.begin)
        label_filters_end = ttk.Label(self.frame_filters_date_hour,
                                       text=self.language.end)

        label_filters_date.grid(column=1, row=0)
        label_filters_hour.grid(column=2, row=0)
        label_filters_begin.grid(column=0, row=1)
        label_filters_end.grid(column=0, row=2)

        dateentry_filters_begin_date = DateEntry(self.frame_filters_date_hour, selectmode='day')
        dateentry_filters_end_date = DateEntry(self.frame_filters_date_hour, selectmode='day')
        self.entry_filters_begin_hour_text = tk.StringVar()
        self.entry_filters_end_hour_text = tk.StringVar()
        entry_filters_begin_hour = ttk.Entry(self.frame_filters_date_hour, textvariable=self.entry_filters_begin_hour_text)
        entry_filters_end_hour = ttk.Entry(self.frame_filters_date_hour, textvariable=self.entry_filters_end_hour_text)
        dateentry_filters_begin_date.grid(column=1, row=1)
        dateentry_filters_end_date.grid(column=1, row=2)
        entry_filters_begin_hour.grid(column=2, row=1)
        entry_filters_end_hour.grid(column=2, row=2)
        #Frame filters Plate
        #layout pack
        self.frame_filters_plate = ttk.Frame(self.frame_filters)
        label_filters_plate = ttk.Label(self.frame_filters_plate, text=self.language.plate_result)
        self.entry_filters_plate_text = tk.StringVar()
        entry_filters_plate = ttk.Entry(self.frame_filters_plate, textvariable=self.entry_filters_plate_text)
        
        label_filters_plate.pack(side=tk.TOP)
        entry_filters_plate.pack(side=tk.TOP)

        #Frame filters name
        #layout pack
        self.frame_filters_name = ttk.Frame(self.frame_filters)
        label_filters_name = ttk.Label(self.frame_filters_name, text=self.language.name_image)
        self.entry_filters_name_text = tk.StringVar()
        entry_filters_name = ttk.Entry(self.frame_filters_name, textvariable=self.entry_filters_name_text)

        label_filters_name.pack(side=tk.LEFT)
        entry_filters_name.pack(side=tk.LEFT)
        


        #Frame results table

        #add frames
        #layout grid
        self.frame_filters.pack(side=tk.TOP)
        self.label_top_filters = ttk.Label(self.frame_filters, text=self.language.filters_title)
        self.label_top_filters.grid(column=0, row=1, columnspan=2, pady=2, padx=2)
        self.frame_filters_date_hour.grid(column=0, row=2, sticky= "news", pady=2, padx=2)
        self.frame_filters_plate.grid(column=1, row=2, sticky= "news", pady=2, padx=2)
        self.frame_filters_name.grid(column=0, row=3, columnspan=2, sticky= "news", pady=2, padx=2)


        #layout pack
        #self.frame_filters.pack(side=tk.TOP, fill=tk.BOTH)
        #self.label_top_filters = ttk.Label(self.frame_filters, text=self.language.filters_title)
        #self.label_top_filters.pack(side=tk.TOP)
        #self.frame_filters_date_hour.pack(side=tk.LEFT)
        #self.frame_filters_plate.pack(side=tk.LEFT)
        #self.frame_filters_name.pack(side=tk.TOP)
        
        