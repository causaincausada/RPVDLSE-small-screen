from tkinter import ttk
from ttkthemes import ThemedTk
from Code.views.main_frames.guiGallery import GuiGallery
from Code.views.main_frames.guiResults import GuiResults
from Code.views.others.guiMenuBar import GuiMenuBar
from Code.views.others.language import Language
from Code.views.others.messages import Messages
from Code.application_logic.applicationLogic import ApplicationLogic


DEFAULT_THEME = 'plastik'
DEFAULT_WINDOW_TITLE = 'RPVDLSE'
GEOMETRY = '1050x750+0+0'
MINSIZE_WINDOW_X = 1050
MINSIZE_WINDOW_Y = 750


class Gui(ThemedTk):
    def __init__(self):
        super().__init__()
        #Language pack
        self.numlanguage = 0
        self.language = Language()
        self.messages = Messages(self.numlanguage)
        self.language.languageChange(self.numlanguage)

        #Set window parameters
        self.set_theme(DEFAULT_THEME)
        self.geometry(GEOMETRY)
        self.minsize(MINSIZE_WINDOW_X, MINSIZE_WINDOW_Y)
        self.title(DEFAULT_WINDOW_TITLE)
        self.resizable(False, False)
        #self.state('zoomed') #quitar?

        #Menu bar
        self.menubar= GuiMenuBar(self)
        self.config(menu=self.menubar)
        #Tabs GUI: i.e. Gallery and Results
        self.tab_control = ttk.Notebook(self)
        self.frame_tab_gallery = GuiGallery(self) #Frame gallery
        self.frame_tab_results = GuiResults(self) #Frame results
        #Poner aqui #Frame Results
        self.tab_control.add(self.frame_tab_gallery, text = self.language.gallery)
        self.tab_control.add(self.frame_tab_results, text = self.language.results)
        self.tab_control.pack(expand = 1, fill ="both") #!!!!!!!!!!!!!!!!!!!!!! Ver si pack, grid o place
        

    
    #fuction to change language
    def change_language(self, numlanguage):
        self.numlanguage = numlanguage
        self.messages = Messages(self.numlanguage)
        self.language.languageChange(self.numlanguage)
        self.menubar = GuiMenuBar(self)
        self.config(menu=self.menubar)
        self.tab_control.destroy()
        self.tab_control = ttk.Notebook(self)
        self.frame_tab_gallery= GuiGallery(self)
        self.frame_tab_results = GuiResults(self)
        self.tab_control.add(self.frame_tab_gallery, text=self.language.gallery)
        self.tab_control.add(self.frame_tab_results, text = self.language.results)
        self.tab_control.pack(expand = 1, fill ="both")
        self.appLogic.update_gallery()

    def set_controller(self, appLogic: ApplicationLogic):
        self.appLogic = appLogic
        
