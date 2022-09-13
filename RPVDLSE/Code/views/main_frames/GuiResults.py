import tkinter as tk 
from tkinter import ttk
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
        #comentario prueba