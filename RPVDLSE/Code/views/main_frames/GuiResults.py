from array import array
from msilib import Table
import tkinter as tk
from tkinter import ttk
from tracemalloc import Statistic
from tkcalendar import DateEntry 
from Code.views.others.Language import Language
from Code.views.others.Messages import Messages
from Code.views.others.Result import Result

class GuiResults(ttk.Frame):
    def __init__(self, root):
        super().__init__(root.tab_control)
        size_font_labels = 15
        size_font_title = 20

        #Language pack
        self.root = root
        self.language = Language()
        self.messages = Messages(root.numlanguage)
        self.language.languageChange(root.numlanguage)
        self.columnconfigure(0, weight=1)
        self.rowconfigure(0, weight=1)
        self.rowconfigure(1, weight=20)

        #Frame Filters 
        #layout grid
        #configure grid
        self.frame_filters = ttk.Frame(self)
        self.frame_filters.columnconfigure(0, weight=2)
        self.frame_filters.columnconfigure(1, weight=1)
        self.frame_filters.rowconfigure(0, weight=1)
        self.frame_filters.rowconfigure(1, weight=1)
        self.frame_filters.rowconfigure(2, weight=1)
        self.frame_filters.rowconfigure(3, weight=1)

        #Frame filters date-hour
        #layout grid
        #configure grid
        self.frame_filters_date_hour = ttk.Frame(self.frame_filters)
        self.frame_filters_date_hour.columnconfigure(0, weight=1)
        self.frame_filters_date_hour.columnconfigure(1, weight=3)
        self.frame_filters_date_hour.columnconfigure(2, weight=3)
        self.frame_filters_date_hour.columnconfigure(3, weight=3)
        self.frame_filters_date_hour.rowconfigure(0, weight=1)
        self.frame_filters_date_hour.rowconfigure(1, weight=1)
        self.frame_filters_date_hour.rowconfigure(2, weight=1)

        label_filters_date = ttk.Label(self.frame_filters_date_hour,
                                       text=self.language.date,
                                       font = ("", size_font_labels))
        label_filters_hour = ttk.Label(self.frame_filters_date_hour,
                                       text=self.language.hour,
                                       font = ("", size_font_labels))
        label_filters_begin = ttk.Label(self.frame_filters_date_hour,
                                       text=self.language.begin,
                                       font = ("", size_font_labels))
        label_filters_end = ttk.Label(self.frame_filters_date_hour,
                                       text=self.language.end,
                                       font = ("", size_font_labels))
        label_filters_plate = ttk.Label(self.frame_filters_date_hour, 
                                        text=self.language.plate,
                                        font = ("", size_font_labels))

        label_filters_date.grid(column=1, row=0, sticky="news", pady=5, padx=5)
        label_filters_hour.grid(column=2, row=0, sticky="news", pady=5, padx=5)
        label_filters_begin.grid(column=0, row=1, sticky="news", pady=5, padx=5)
        label_filters_end.grid(column=0, row=2, sticky="news", pady=5, padx=5)
        label_filters_plate.grid(column=3, row=1, sticky="news", pady=5, padx=25)

        dateentry_filters_begin_date = DateEntry(self.frame_filters_date_hour, selectmode='day')
        dateentry_filters_end_date = DateEntry(self.frame_filters_date_hour, selectmode='day')
        self.entry_filters_begin_hour_text = tk.StringVar()
        self.entry_filters_end_hour_text = tk.StringVar()
        self.entry_filters_plate_text = tk.StringVar()
        entry_filters_begin_hour = ttk.Entry(self.frame_filters_date_hour, textvariable=self.entry_filters_begin_hour_text)
        entry_filters_end_hour = ttk.Entry(self.frame_filters_date_hour, textvariable=self.entry_filters_end_hour_text)
        entry_filters_plate = ttk.Entry(self.frame_filters_date_hour, textvariable=self.entry_filters_plate_text)
        dateentry_filters_begin_date.grid(column=1, row=1, sticky="news", pady=5, padx=5)
        dateentry_filters_end_date.grid(column=1, row=2, sticky="news", pady=5, padx=5)
        entry_filters_begin_hour.grid(column=2, row=1, sticky="news", pady=5, padx=5)
        entry_filters_end_hour.grid(column=2, row=2, sticky="news", pady=5, padx=5)
        entry_filters_plate.grid(column=3, row=2, sticky="news", pady=5, padx=25)
        #Frame filters name
        #layout pack
        self.frame_filters_name = ttk.Frame(self.frame_filters)
        self.frame_filters_name.columnconfigure(0, weight=1)
        self.frame_filters_name.columnconfigure(1, weight=10)
        label_filters_name = ttk.Label(self.frame_filters_name, 
                                       text=self.language.name_image,
                                       font = ("", size_font_labels))
        self.entry_filters_name_text = tk.StringVar()
        entry_filters_name = ttk.Entry(self.frame_filters_name, textvariable=self.entry_filters_name_text)

        label_filters_name.grid(column=0, row=0, sticky="news", pady=5, padx=5)
        entry_filters_name.grid(column=1, row=0, sticky="news", pady=5, padx=25)
        
        #Frame results table
        self.frame_results = ttk.Frame(self)
        self.frame_results.columnconfigure(0, weight=1)
        self.frame_results.columnconfigure(1, weight=10)
        table_results = ttk.Treeview(self.frame_results, selectmode='browse')
        table_results.grid(column=0, row=0, sticky="news")

        scrollbar_table_results = ttk.Scrollbar(self.frame_results, orient="vertical", command=table_results)
        scrollbar_table_results.grid(column=1, row=0, sticky="news")

        table_results.configure(yscrollcommand=scrollbar_table_results.set)

        res = Result()
        array_results = res.crear_results()

        table_results["columns"] = ("1", "2", "3", "4")
        table_results['show'] = 'headings'
        table_results.column("1", width=100, anchor='c')
        table_results.column("2", width=100, anchor='c')
        table_results.column("3", width=100, anchor='c')
        table_results.column("4", width=100, anchor='c')
        table_results.heading("1", text = self.language.name)
        table_results.heading("2", text = self.language.date)
        table_results.heading("3", text = self.language.hour)
        table_results.heading("4", text = self.language.result)
        for a in array_results:
            table_results.insert("", 'end', text= "L1", values=(a.name, a.date, a.hour, a.result))



        #add frames
        #layout grid
        self.frame_filters.grid(column=0, row=0, sticky="ew")
        self.frame_results.grid(column=0, row=1, sticky="news")

        self.label_top_filters = ttk.Label(self.frame_filters, 
                                           text=self.language.filters_title,
                                           font = ("", size_font_title))
        self.label_top_filters.grid(column=0, row=0, columnspan=2, pady=2, padx=2)
        self.frame_filters_date_hour.grid(column=0, row=1, columnspan=2, sticky= "news", pady=2, padx=2)
        self.frame_filters_name.grid(column=0, row=2, sticky= "news", pady=2, padx=2)


        #layout pack
        #self.frame_filters.pack(side=tk.TOP, fill=tk.BOTH)
        #self.label_top_filters = ttk.Label(self.frame_filters, text=self.language.filters_title)
        #self.label_top_filters.pack(side=tk.TOP)
        #self.frame_filters_date_hour.pack(side=tk.LEFT)
        #self.frame_filters_plate.pack(side=tk.LEFT)
        #self.frame_filters_name.pack(side=tk.TOP)
        
        