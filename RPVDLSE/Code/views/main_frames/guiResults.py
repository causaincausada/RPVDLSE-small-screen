import datetime
from fileinput import fileno
import os
import subprocess
import tkinter as tk
from tkinter import DISABLED, NORMAL, ttk
from tkcalendar import DateEntry
from Code.views.others.language import Language
from Code.views.others.messages import Messages
from Code.props.tooltip import ToolTip


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
        self.frame_filters_date_hour.columnconfigure(1, weight=2)
        self.frame_filters_date_hour.columnconfigure(2, weight=1)
        self.frame_filters_date_hour.columnconfigure(3, weight=2)
        self.frame_filters_date_hour.columnconfigure(4, weight=1)
        self.frame_filters_date_hour.columnconfigure(5, weight=2)
        self.frame_filters_date_hour.columnconfigure(6, weight=1)
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

        label_filters_date.grid(column=1, row=0,  sticky="news", pady=5, padx=5)
        label_filters_hour.grid(column=3, row=0, sticky="news", pady=5, padx=5)
        label_filters_begin.grid(column=0, row=1, sticky="news", pady=5, padx=5)
        label_filters_end.grid(column=0, row=2, sticky="news", pady=5, padx=5)
        label_filters_plate.grid(column=5, row=1, sticky="news", pady=5, padx=25)

        self.date_entry_begin_text = tk.StringVar()
        self.date_entry_end_text = tk.StringVar()
        self.hour_entry_begin_text = tk.StringVar()
        self.hour_entry_end_text = tk.StringVar()
        self.entry_plate_text = tk.StringVar()
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
        self.date_entry_begin_text.trace(
            "w", lambda name, index, mode,
            sv=self.date_entry_begin_text: self.ch_date_entry_begin()
        )
        self.date_entry_end_text.trace(
            "w", lambda name, index, mode,
            sv=self.date_entry_end_text: self.ch_date_entry_end()
        )
        self.hour_entry_begin_text.trace(
            "w", lambda name, index, mode,
            sv=self.hour_entry_begin_text: self.ch_hour_entry_begin()
        )
        self.hour_entry_end_text.trace(
            "w", lambda name, index, mode,
            sv=self.hour_entry_end_text: self.ch_hour_entry_end()
        )
        self.entry_plate_text.trace(
            "w", lambda name, index, mode,
            sv=self.entry_plate_text: self.ch_entry_plate()
        )
        self.hour_entry_begin = ttk.Entry(self.frame_filters_date_hour,
                                          textvariable=self.hour_entry_begin_text)
        self.hour_entry_end = ttk.Entry(self.frame_filters_date_hour,
                                        textvariable=self.hour_entry_end_text)
        self.entry_plate = ttk.Entry(self.frame_filters_date_hour,
                                     textvariable=self.entry_plate_text)
        self.date_entry_begin.grid(column=1, row=1, columnspan=2, sticky="news", pady=5, padx=5)
        self.date_entry_end.grid(column=1, row=2, columnspan=2, sticky="news", pady=5, padx=5)
        self.hour_entry_begin.grid(column=3, row=1, columnspan=2, sticky="news", pady=5, padx=5)
        self.hour_entry_end.grid(column=3, row=2, columnspan=2, sticky="news", pady=5, padx=5)
        self.entry_plate.grid(column=5, row=2, columnspan=2, sticky="news", pady=5, padx=25)
        # Warnings in filters
        # icon
        path = os.path.dirname(__file__)
        filename = os.path.join(path, '../../../media/warning.png')
        self.warning_icon = tk.PhotoImage(file=filename)
        self.warning_icon_hour = ttk.Label(self.frame_filters_date_hour, image=self.warning_icon)
        self.warning_icon_date = ttk.Label(self.frame_filters_date_hour, image=self.warning_icon)
        self.warning_icon_plate = ttk.Label(self.frame_filters_date_hour, image=self.warning_icon)

        self.warning_icon_date.grid(column=2, row=0, sticky="nes", pady=5, padx=5)
        self.warning_icon_hour.grid(column=4, row=0, sticky="nes", pady=5, padx=5)
        self.warning_icon_plate.grid(column=6, row=1, sticky="nes", pady=5, padx=25)

        # Frame filters name
        # layout pack
        self.frame_filters_name = ttk.Frame(self.frame_filters)
        self.frame_filters_name.columnconfigure(0, weight=1)
        self.frame_filters_name.columnconfigure(1, weight=1)
        self.frame_filters_name.columnconfigure(2, weight=10)
        label_filters_name = ttk.Label(self.frame_filters_name, 
                                       text=self.language.name_image,
                                       font=("", size_font_labels))
        self.entry_name_text = tk.StringVar()
        self.entry_name_text.trace(
            "w", lambda name, index, mode,
            sv=self.entry_name_text: self.ch_entry_name()
        )
        self.entry_name = ttk.Entry(self.frame_filters_name, textvariable=self.entry_name_text)
        self.warning_icon_name = ttk.Label(self.frame_filters_name, image=self.warning_icon)

        label_filters_name.grid(column=0, row=0, sticky="news", pady=5, padx=5)
        self.warning_icon_name.grid(column=1, row=0, sticky="nes", pady=5, padx=5)
        self.entry_name.grid(column=2, row=0, sticky="news", pady=5, padx=25)
        
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
        self.table_results.column("1", width=120, anchor='c')
        self.table_results.column("2", width=35, anchor='c')
        self.table_results.column("3", width=35, anchor='c')
        self.table_results.column("4", width=210, anchor='c')
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

        self.warnings = [None, None, None, None]
        self.warnings[0] = ToolTip(self.warning_icon_date, self.language.warning_date, wraplength=300)
        self.warnings[1] = ToolTip(self.warning_icon_hour, self.language.warning_hour_inversed, wraplength=300)
        self.warnings[2] = ToolTip(self.warning_icon_plate, self.language.warning_invalid_plate_name, wraplength=300)
        self.warnings[3] = ToolTip(self.warning_icon_name, self.language.warning_invalid_name, wraplength=300)

    # Functions tracing StringVars
    def ch_date_entry_begin(self):
        try:
            if self.date_entry_begin_text.get() != "":
                self.gui_date_begin = datetime.datetime(year=self.date_entry_begin.get_date().year,
                                                        month=self.date_entry_begin.get_date().month,
                                                        day=self.date_entry_begin.get_date().day)
                self.ch_dates()
                self.get_results_gui()
            else:
                self.gui_date_begin = datetime.datetime(2000, 1, 1, 0, 0, 0)
                self.ch_dates()
                self.get_results_gui()
        except AttributeError:
            self.gui_date_begin = datetime.datetime(2000, 1, 1, 0, 0, 0)
            self.ch_dates()
            self.get_results_gui()

    def ch_date_entry_end(self):
        try:
            if self.date_entry_end_text.get() != "":
                self.gui_date_end = datetime.datetime(year=self.date_entry_end.get_date().year,
                                                      month=self.date_entry_end.get_date().month,
                                                      day=self.date_entry_end.get_date().day)
                self.ch_dates()
                self.get_results_gui()
            else:
                self.gui_date_end = datetime.datetime.now()
                self.ch_dates()
                self.get_results_gui()
        except AttributeError:
            self.gui_date_end = datetime.datetime.now()
            self.ch_dates()
            self.get_results_gui()

    def ch_dates(self):
        self.root.app_logic.is_dates_valid(self.gui_date_begin, self.gui_date_end)

    def ch_hour_entry_begin(self):
        try:
            val, self.gui_hour_begin = self.root.app_logic.is_hour_valid(self.hour_entry_begin_text.get())
            if val:
                self.ch_hours()
                self.get_results_gui()
            else:
                self.gui_hour_begin = datetime.datetime(year=1970, month=1, day=1, hour=0, minute=0, second=0)
                self.ch_hours()
                self.get_results_gui()
        except AttributeError:
            self.gui_hour_begin = datetime.datetime(year=1970, month=1, day=1, hour=0, minute=0, second=0)
            self.ch_hours()
            self.get_results_gui()

    def ch_hour_entry_end(self):
        try:
            val, self.gui_hour_end = self.root.app_logic.is_hour_valid(self.hour_entry_end_text.get())
            if val:
                self.ch_hours()
                self.get_results_gui()
            else:
                self.gui_hour_end = datetime.datetime(year=1970, month=1, day=1, hour=23, minute=59, second=59)
                self.ch_hours()
                self.get_results_gui()
        except AttributeError:
            self.gui_hour_end = datetime.datetime(year=1970, month=1, day=1, hour=23, minute=59, second=59)
            self.ch_hours()
            self.get_results_gui()

    def ch_hours(self):
        self.root.app_logic.is_hour_inversed(self.gui_hour_begin, self.gui_hour_end)

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
            val = self.root.app_logic.is_name_valid(self.entry_name_text.get())
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
                array_results, array_warnings = self.root.app_logic.get_results(gui_date_begin=self.gui_date_begin,
                                                                                gui_date_end=self.gui_date_end,
                                                                                gui_time_begin=self.gui_hour_begin,
                                                                                gui_time_end=self.gui_hour_end,
                                                                                gui_plate=self.gui_plate, gui_name=self.gui_name)
                self.update_warnings(array_warnings)
                self.table_results.delete(*self.table_results.get_children())

                for a in array_results:
                    date_in = a["date"]
                    hour_in = a["hour"]
                    date_text = ""+str(date_in.day)+"-"+str(date_in.month)+"-"+str(date_in.year)
                    if date_in.day < 10:
                        if date_in.month < 10:
                            date_text = "0"+str(date_in.day)+"-0"+str(date_in.month)+"-"+str(date_in.year)
                        else:
                            date_text = "0"+str(date_in.day)+"-"+str(date_in.month)+"-"+str(date_in.year)
                    elif date_in.month < 10:
                        date_text = ""+str(date_in.day)+"-0"+str(date_in.month)+"-"+str(date_in.year)
                    else:
                        date_text = ""+str(date_in.day)+"-"+str(date_in.month)+"-"+str(date_in.year)
                    if hour_in.hour < 10:
                        if hour_in.minute < 10:
                            hour_text = "0"+str(hour_in.hour)+":0"+str(hour_in.minute)
                        else:
                            hour_text = "0"+str(hour_in.hour)+":"+str(hour_in.minute)
                    elif hour_in.minute < 10:
                        hour_text = ""+str(hour_in.hour)+":0"+str(hour_in.minute)
                    else:
                        hour_text = ""+str(hour_in.hour)+":"+str(hour_in.minute)

                    self.table_results.insert("", 'end', text="L1", values=(a["name"],
                                              date_text, hour_text, a["result"]))
                self.update_warnings(array_warnings)
            else:
                if self.root.app_logic.try_connect_mongodb():
                    self.get_results_gui()
                else:
                    self.messages.lost_connection_db()
                    try:
                        subprocess.Popen(["/usr/bin/systemctl", "start", "mongod.service"])
                    except FileNotFoundError as a:
                        print(a)
        except TypeError as te:
            print(te)
            print("Error en get result gui")
        except AttributeError as ae:
            if ae.name == "on_connect_mongodb":
                pass
            else:
                print(ae.name)
                print("Error ae get result gui")

    def update_warnings(self, warnings):
        if warnings[0]:
            self.warnings[0].set_active(False)
            self.warning_icon_date.configure(state=DISABLED)
        else:
            self.warnings[0].set_active(True)
            self.warning_icon_date.configure(state=NORMAL)
        if warnings[1] and warnings[2]:
            self.warnings[1].set_active(False)
            self.warning_icon_hour.configure(state=DISABLED)
        elif not warnings[1]:
            self.warnings[1].set_text(self.language.warning_hour_inversed)
            self.warnings[1].set_active(True)
            self.warning_icon_hour.configure(state=NORMAL)
        elif not warnings[2]:
            self.warnings[1].set_text(self.language.warning_hour_invalid)
            self.warnings[1].set_active(True)
            self.warning_icon_hour.configure(state=NORMAL)
        else:
            self.warnings[1].set_text(self.language.warning_hour_invalid+"\n"+self.language.warning_hour_inversed)
            self.warnings[1].set_active(True)
            self.warning_icon_hour.configure(state=NORMAL)
        if warnings[3]:
            self.warnings[2].set_active(False)
            self.warning_icon_plate.configure(state=DISABLED)
        else:
            self.warnings[2].set_active(True)
            self.warning_icon_plate.configure(state=NORMAL)
        if warnings[4]:
            self.warnings[3].set_active(False)
            self.warning_icon_name.configure(state=DISABLED)
        else:
            self.warnings[3].set_active(True)
            self.warning_icon_name.configure(state=NORMAL)


