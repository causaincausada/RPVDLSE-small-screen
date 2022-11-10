from tkinter import ttk
from ttkthemes import ThemedTk
from Code.views.main_frames.guiGallery import GuiGallery
from Code.views.main_frames.guiResults import GuiResults
from Code.views.others.guiMenuBar import GuiMenuBar
from Code.views.others.language import Language
from Code.views.others.messages import Messages


DEFAULT_THEME = 'plastik'
DEFAULT_WINDOW_TITLE = 'RPVDLSE'
GEOMETRY = '1050x750+0+0'
MINSIZE_WINDOW_X = 1050
MINSIZE_WINDOW_Y = 750


class Gui(ThemedTk):
    def __init__(self):
        super().__init__()
        # Language pack
        self.app_logic = None
        self.num_language = 0
        self.language = Language()
        self.messages = Messages(self.num_language)
        self.language.language_change(self.num_language)

        # Set window parameters
        self.set_theme(DEFAULT_THEME)
        self.geometry(GEOMETRY)
        self.minsize(MINSIZE_WINDOW_X, MINSIZE_WINDOW_Y)
        self.title(DEFAULT_WINDOW_TITLE)
        self.resizable(False, False)
        self.protocol("WM_DELETE_WINDOW", self.on_close)
        # self.state('zoomed') #quitar?

        # Menu bar
        self.menubar = GuiMenuBar(self)
        self.config(menu=self.menubar)
        # Tabs GUI: i.e. Gallery and Results
        self.tab_control = ttk.Notebook(self)
        self.tab_control.bind("<ButtonRelease-1>", self.change_tab)
        self.frame_tab_gallery = GuiGallery(self)  # Frame gallery
        self.frame_tab_results = GuiResults(self)  # Frame results
        self.tab_control.add(self.frame_tab_gallery, text=self.language.gallery)
        self.tab_control.add(self.frame_tab_results, text=self.language.results)
        self.tab_control.pack(expand=1, fill="both")

    # function to change language
    def change_language(self, num_language):
        self.num_language = num_language
        self.messages = Messages(self.num_language)
        self.language.language_change(self.num_language)
        self.menubar = GuiMenuBar(self)
        self.config(menu=self.menubar)
        self.tab_control.destroy()
        self.tab_control = ttk.Notebook(self)
        self.tab_control.bind("<ButtonRelease-1>", self.change_tab)
        self.frame_tab_gallery = GuiGallery(self)
        self.frame_tab_results = GuiResults(self)
        self.tab_control.add(self.frame_tab_gallery, text=self.language.gallery)
        self.tab_control.add(self.frame_tab_results, text=self.language.results)
        self.tab_control.pack(expand=1, fill ="both")
        self.app_logic.update_gallery()

    def set_controller(self, app_logic):
        self.app_logic = app_logic
        self.app_logic.after_init()

    def change_tab(self, event=None):
        if self.tab_control.tab(self.tab_control.select(), "text") == self.language.results:
            self.frame_tab_results.get_results_gui()

    def on_close(self):
        if self.messages.ask_confirm_close_main():
            self.app_logic.disconnect_mongodb()
            self.after(10, self.destroy())
