import datetime
import tkinter as tk
from tkinter import ttk
from tkcalendar import DateEntry
from Code.views.others.language import Language
from Code.views.others.messages import Messages


class GuiResults(ttk.Frame):
    def __init__(self, root):
        super().__init__(root.tab_control)
        size_font_labels = 15
        size_font_title = 20
        # Language pack
        self.root = root
        self.language = Language()
        self.messages = Messages(root.num_language)
        self.language.language_change(root.num_language)

        # gui_results
        self.gui_date_begin = datetime.datetime(2000, 1, 1, 0, 0, 0)
        self.gui_date_end = datetime.datetime.now()
        self.gui_hour_begin = datetime.datetime(year=1970, month=1, day=1, hour=0, minute=0)
        self.gui_hour_end = datetime.datetime(year=1970, month=1, day=1, hour=23, minute=59)
        self.gui_plate = ""
        self.gui_name = ""

        # frame config
        self.columnconfigure(0, weight=1)
        self.rowconfigure(0, weight=1)
        self.rowconfigure(1, weight=20)

        # Frame Filters
        # layout grid
        # configure grid
        self.frame_filters = ttk.Frame(self)
        self.frame_filters.columnconfigure(0, weight=2)
        self.frame_filters.columnconfigure(1, weight=1)
        self.frame_filters.rowconfigure(0, weight=1)
        self.frame_filters.rowconfigure(1, weight=1)
        self.frame_filters.rowconfigure(2, weight=1)
        self.frame_filters.rowconfigure(3, weight=1)

        # Frame filters date-hour
        # layout grid
        # configure grid
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
                                       font=("", size_font_labels))
        label_filters_hour = ttk.Label(self.frame_filters_date_hour,
                                       text=self.language.hour,
                                       font=("", size_font_labels))
        label_filters_begin = ttk.Label(self.frame_filters_date_hour,
                                        text=self.language.begin,
                                        font=("", size_font_labels))
        label_filters_end = ttk.Label(self.frame_filters_date_hour,
                                      text=self.language.end,
                                      font=("", size_font_labels))
        label_filters_plate = ttk.Label(self.frame_filters_date_hour, 
                                        text=self.language.plate,
                                        font=("", size_font_labels))

        label_filters_date.grid(column=1, row=0, sticky="news", pady=5, padx=5)
        label_filters_hour.grid(column=2, row=0, sticky="news", pady=5, padx=5)
        label_filters_begin.grid(column=0, row=1, sticky="news", pady=5, padx=5)
        label_filters_end.grid(column=0, row=2, sticky="news", pady=5, padx=5)
        label_filters_plate.grid(column=3, row=1, sticky="news", pady=5, padx=25)

        self.date_entry_begin_text = tk.StringVar()
        self.date_entry_begin_text.trace(
            "w", lambda name, index, mode,
            sv=self.date_entry_begin_text: self.ch_date_entry_begin()
        )
        self.date_entry_end_text = tk.StringVar()
        self.date_entry_end_text.trace(
            "w", lambda name, index, mode,
            sv=self.date_entry_end_text: self.ch_date_entry_end()
        )
        self.hour_entry_begin_text = tk.StringVar()
        self.hour_entry_begin_text.trace(
            "w", lambda name, index, mode,
            sv=self.hour_entry_begin_text: self.ch_hour_entry_begin()
        )
        self.hour_entry_end_text = tk.StringVar()
        self.hour_entry_end_text.trace(
            "w", lambda name, index, mode,
            sv=self.hour_entry_end_text: self.ch_hour_entry_end()
        )

        self.entry_plate_text = tk.StringVar()
        self.entry_plate_text.trace(
            "w", lambda name, index, mode,
            sv=self.entry_plate_text: self.ch_entry_plate()
        )

        self.date_entry_begin = DateEntry(self.frame_filters_date_hour,
                                          selectmode='day',
                                          date_pattern='dd/mm/y',
                                          state="readonly",
                                          textvariable=self.date_entry_begin_text)
        self.date_entry_end = DateEntry(self.frame_filters_date_hour,
                                        selectmode='day',
                                        date_pattern='dd/mm/y',
                                        state="readonly",
                                        textvariable=self.date_entry_end_text)
        self.date_entry_begin.set_date(datetime.datetime(2000, 1, 1, 0, 0, 0))
        self.date_entry_end.set_date(datetime.datetime.now())
        self.hour_entry_begin = ttk.Entry(self.frame_filters_date_hour,
                                          textvariable=self.hour_entry_begin_text)
        self.hour_entry_end = ttk.Entry(self.frame_filters_date_hour,
                                        textvariable=self.hour_entry_end_text)
        self.entry_plate = ttk.Entry(self.frame_filters_date_hour,
                                     textvariable=self.entry_plate_text)
        self.date_entry_begin.grid(column=1, row=1, sticky="news", pady=5, padx=5)
        self.date_entry_end.grid(column=1, row=2, sticky="news", pady=5, padx=5)
        self.hour_entry_begin.grid(column=2, row=1, sticky="news", pady=5, padx=5)
        self.hour_entry_end.grid(column=2, row=2, sticky="news", pady=5, padx=5)
        self.entry_plate.grid(column=3, row=2, sticky="news", pady=5, padx=25)
        # Frame filters name
        # layout pack
        self.frame_filters_name = ttk.Frame(self.frame_filters)
        self.frame_filters_name.columnconfigure(0, weight=1)
        self.frame_filters_name.columnconfigure(1, weight=10)
        label_filters_name = ttk.Label(self.frame_filters_name, 
                                       text=self.language.name_image,
                                       font=("", size_font_labels))
        self.entry_name_text = tk.StringVar()
        self.entry_name_text.trace(
            "w", lambda name, index, mode,
            sv=self.entry_name_text: self.ch_entry_name()
        )
        self.entry_name = ttk.Entry(self.frame_filters_name, textvariable=self.entry_name_text)

        label_filters_name.grid(column=0, row=0, sticky="news", pady=5, padx=5)
        self.entry_name.grid(column=1, row=0, sticky="news", pady=5, padx=25)
        
        # Frame results table
        self.frame_results = ttk.Frame(self)
        self.frame_results.columnconfigure(0, weight=1)
        self.frame_results.rowconfigure(0, weight=1)
        self.table_results = ttk.Treeview(self.frame_results, selectmode='browse')
        self.table_results.grid(column=0, row=0, sticky="news", pady=20, padx=20)

        scrollbar_table_results = ttk.Scrollbar(self.frame_results, orient="vertical", command=self.table_results.yview)
        scrollbar_table_results.grid(column=0, row=0, sticky="nes", pady=20, padx=20)

        self.table_results.configure(yscrollcommand=scrollbar_table_results.set)

        self.table_results["columns"] = ("1", "2", "3", "4")
        self.table_results['show'] = 'headings'
        self.table_results.column("1", width=100, anchor='c')
        self.table_results.column("2", width=100, anchor='c')
        self.table_results.column("3", width=100, anchor='c')
        self.table_results.column("4", width=100, anchor='c')
        self.table_results.heading("1", text=self.language.name)
        self.table_results.heading("2", text=self.language.date)
        self.table_results.heading("3", text=self.language.hour)
        self.table_results.heading("4", text=self.language.result)

        # add frames
        # layout grid
        self.frame_filters.grid(column=0, row=0, sticky="ew")
        self.frame_results.grid(column=0, row=1, sticky="news")

        self.label_top_filters = ttk.Label(self.frame_filters, 
                                           text=self.language.filters_title,
                                           font=("", size_font_title))
        self.label_top_filters.grid(column=0, row=0, columnspan=2, pady=2, padx=2)
        self.frame_filters_date_hour.grid(column=0, row=1, columnspan=2, sticky="news", pady=2, padx=2)
        self.frame_filters_name.grid(column=0, row=2, sticky="news", pady=2, padx=2)

    # Functions tracing StringVars
    def ch_date_entry_begin(self):
        try:
            if self.date_entry_begin_text.get() != "":
                self.gui_date_begin = datetime.datetime(year=self.date_entry_begin.get_date().year,
                                                        month=self.date_entry_begin.get_date().month,
                                                        day=self.date_entry_begin.get_date().day)
                self.get_results_gui()
            else:
                self.gui_date_begin = datetime.datetime(2000, 1, 1, 0, 0, 0)
                self.get_results_gui()
        except AttributeError:
            self.gui_date_begin = datetime.datetime(2000, 1, 1, 0, 0, 0)
            self.get_results_gui()

    def ch_date_entry_end(self):
        try:
            if self.date_entry_end_text.get() != "":
                self.gui_date_end = datetime.datetime(year=self.date_entry_end.get_date().year,
                                                      month=self.date_entry_end.get_date().month,
                                                      day=self.date_entry_end.get_date().day)
                self.get_results_gui()
            else:
                self.gui_date_end = datetime.datetime.now()
                self.get_results_gui()
        except AttributeError:
            self.gui_date_end = datetime.datetime.now()
            self.get_results_gui()

    def ch_hour_entry_begin(self):
        try:
            val, self.gui_hour_begin = self.root.app_logic.is_hour_valid(self.hour_entry_begin_text.get())
            if val:
                self.get_results_gui()
            else:
                self.gui_hour_begin = datetime.datetime(year=1970, month=1, day=1, hour=0, minute=0, second=0)
                self.get_results_gui()
        except AttributeError:
            self.gui_hour_begin = datetime.datetime(year=1970, month=1, day=1, hour=0, minute=0, second=0)
            self.get_results_gui()

    def ch_hour_entry_end(self):
        try:
            val, self.gui_hour_end = self.root.app_logic.is_hour_valid(self.hour_entry_end_text.get())
            if val:
                self.get_results_gui()
            else:
                self.gui_hour_end = datetime.datetime(year=1970, month=1, day=1, hour=23, minute=59, second=59)
                self.get_results_gui()
        except AttributeError:
            self.gui_hour_end = datetime.datetime(year=1970, month=1, day=1, hour=23, minute=59, second=59)
            self.get_results_gui()

    def ch_entry_plate(self):
        try:
            val = self.root.app_logic.is_name_plate_valid(self.entry_plate_text.get())
            if val:
                self.gui_plate = self.entry_plate_text.get()
                self.get_results_gui()
            else:
                self.gui_plate = ""
                self.get_results_gui()
        except AttributeError:
            self.gui_plate = ""
            self.get_results_gui()

    def ch_entry_name(self):
        try:
            val = self.root.app_logic.is_name_plate_valid(self.entry_name_text.get())
            if val:
                self.gui_name = self.entry_name_text.get()
                self.get_results_gui()
            else:
                self.gui_name = ""
                self.get_results_gui()
        except AttributeError:
            self.gui_name = ""
            self.get_results_gui()

    def get_results_gui(self):
        try:
            if self.root.app_logic.on_connect_mongodb():
                array_results = self.root.app_logic.get_results(gui_date_begin=self.gui_date_begin,
                                                                gui_date_end=self.gui_date_end,
                                                                gui_time_begin=self.gui_hour_begin,
                                                                gui_time_end=self.gui_hour_end,
                                                                gui_plate=self.gui_plate, gui_name=self.gui_name)
                self.table_results.delete(*self.table_results.get_children())

                for a in array_results:
                    date_in = a["date"]
                    hour_in = a["hour"]
                    date_text = ""+str(date_in.day)+"-"+str(date_in.month)+"-"+str(date_in.year)
                    self.table_results.insert("", 'end', text="L1", values=(a["name"],
                                              date_text, hour_in.time(), a["result"]))
            else:
                if self.root.app_logic.try_connect_mongodb():
                    self.get_results_gui()
                else:
                    self.messages.lost_connection_db()

        except TypeError as te:
            print(te)
            print("Error en get result gui")
        except AttributeError as ae:
            print(ae)
            print("Error ae get result gui")
