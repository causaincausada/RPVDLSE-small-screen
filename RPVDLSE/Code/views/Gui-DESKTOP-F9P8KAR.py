from tkinter import ttk
from ttkthemes import ThemedTk
from ctypes import windll
from Code.views.main_frame.GuiGallery import GuiGallery
from Code.views.others.GuiMenuBar import GuiMenuBar

DEFAULT_THEME = 'adapta'
DEFAULT_WINDOW_TITLE = 'RPVDLSE'
GEOMETRY = '700x600+0+0'
MINSIZE_WINDOW_X = 700
MINSIZE_WINDOW_Y = 600
TEXT_TAB_GALLERY = 'Galería' #!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!! Texto Ingles/Español


class Gui(ThemedTk):
    def __init__(self):
        super().__init__()
        #Set window parameters
        self.set_theme(DEFAULT_THEME)
        self.geometry(GEOMETRY)
        self.minsize(MINSIZE_WINDOW_X, MINSIZE_WINDOW_Y)
        self.title(DEFAULT_WINDOW_TITLE)
        self.state('zoomed')
        
        #Menu bar
        menubar= GuiMenuBar(self, 0)
        self.config(menu=menubar)
        #Tabs GUI: i.e. Gallery and Results
        tab_control = ttk.Notebook(self)
        frame_tab_gallery = GuiGallery(tab_control) #Frame gallery
        #Poner aqui #Frame Results
        tab_control.add(frame_tab_gallery, text = TEXT_TAB_GALLERY)
        #tab_control.add(frame_tab_gallery, text ='Tab 1')
        tab_control.pack(expand = 1, fill ="both") #!!!!!!!!!!!!!!!!!!!!!! Ver si pack, grid o place
        
        try:
            #Configuration to Windows OS
            windll.shcore.SetProcessDpiAwareness(1)
        finally:
            pass;


