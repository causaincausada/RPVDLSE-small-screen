import tkinter as tk 
from tkinter import ttk
from tkcalendar import DateEntry 
from Code.views.others.Language import Language
from Code.views.others.Messages import Messages

DEFAULT_SIZE_RADIO_BUTTON = 15

class GuiResults(ttk.Frame):
    def __init__(self, root):
        super().__init__(root.tab_control)
        
        #Language pack
        self.root = root
        self.language = Language()
        self.messages = Messages(root.numlanguage)
        self.language.languageChange(root.numlanguage)

        #Style
        style = ttk.Style()
        style.configure('Big.TRadiobutton', 
                        font=(None, DEFAULT_SIZE_RADIO_BUTTON))
        #Layout Management: pack
        
        #Frame Filters 
        #layout pack
        frame_filters = ttk.Frame(self)


        #Frame filters date-hour
        #layout grid
        #configure grid
        frame_filters_date_hour = ttk.Frame(self)
        frame_filters_date_hour.columnconfigure(0, wight=1)
        frame_filters_date_hour.columnconfigure(1, wight=1)
        frame_filters_date_hour.columnconfigure(2, wight=1)
        frame_filters_date_hour.rowconfigure(0, wight=1)
        frame_filters_date_hour.rowconfigure(1, wight=1)
        frame_filters_date_hour.rowconfigure(2, wight=1)

        label_filters_date = ttk.Label(frame_filters_date_hour,
                                       text=self.language.date)
        label_filters_hour = ttk.Label(frame_filters_date_hour,
                                       text=self.language.hour)
        label_filters_begin = ttk.Label(frame_filters_date_hour,
                                       text=self.language.begin)
        label_filters_end = ttk.Label(frame_filters_date_hour,
                                       text=self.language.end)

        label_filters_date.grid(column=1, row=0)
        label_filters_hour.grid(column=2, row=0)
        label_filters_begin.grid(column=0, row=1)
        label_filters_end.grid(column=0, row=2)

        dateentry_filters_begin_date = DateEntry(frame_filters_date_hour, selectmode='day')
        dateentry_filters_end_date = DateEntry(frame_filters_date_hour, selectmode='day')
        self.entry_filters_begin_hour_text = tk.StringVar()
        self.entry_filters_end_hour_text = tk.StringVar()
        entry_filters_begin_hour = ttk.Entry(frame_filters_date_hour, textvariable=self.entry_filters_begin_hour_text)
        entry_filters_end_hour = ttk.Entry(frame_filters_date_hour, textvariable=self.entry_filters_end_hour_text)
        dateentry_filters_begin_date.grid(column=1, row=1)
        dateentry_filters_end_date.grid(column=1, row=2)
        entry_filters_begin_hour.grid(column=2, row=1)
        entry_filters_end_hour.grid(column=2, row=2)
        #Frame filters Plate
        #layout pack


        #Frame filters name
        #layout pack

        


        #Frame results table

        