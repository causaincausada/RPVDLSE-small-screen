import tkinter as tk
from tkinter import ttk, Menu
from Code.views.others.Language import Language
from Code.views.others.Messages import Messages


class GuiMenuBar(Menu):
    def __init__(self, root):
        super().__init__(root)
        self.root = root
        self.language = Language()
        self.messages = Messages(root.numlanguage)
        self.language.languageChange(root.numlanguage)
        results_menu = Menu(root, tearoff=0)
        restore_menu = Menu(root, tearoff=0)
        settings_menu = Menu(root, tearoff=0)
        language_menu = Menu(root, tearoff=0)
        size_font_menu_item = 15
        # add a menu item to the menu --back up--
        results_menu.add_command(
            label= self.language.backup,
            font = ("", size_font_menu_item),
            command= self.activador_ask_confirm_backup
        )
        # add menu items in menu restore
        restore_menu.add_command(
            label= self.language.restore_menu_file_label,
            font = ("", size_font_menu_item),
            command=self.messages.ask_confirm_restore
        )
        restore_menu.add_command(
            label= self.language.restore,
            font = ("", size_font_menu_item),
            command= self.messages.ask_confirm_restore
        )
        # add items in menu language
        self.variable_language = tk.IntVar()
        self.variable_language.set(value=root.numlanguage)
        language_menu.add_radiobutton(
            label = self.language.spanish,
            value = 1,
            variable = self.variable_language,
            command = self.activador_RadiobuttonChange
        )
        language_menu.add_radiobutton(
            label = self.language.english,
            value = 0,
            variable = self.variable_language,
            command = self.activador_RadiobuttonChange
        )
        
        # add menu radiobuttons Language in settings menu
        settings_menu.add_cascade(
            label= self.language.language,
            font = ("", size_font_menu_item),
            menu = language_menu
        )
        # add a menu item to the menu --restore--
        results_menu.add_cascade(
            label=self.language.restore,
            font = ("", size_font_menu_item),
            menu= restore_menu
        )

        # add the results menu to the menubar
        self.add_cascade(
            label=self.language.menubar_results_label,
            font = ("", size_font_menu_item),
            menu=results_menu
        )
        self.add_cascade(
            label = self.language.settings,
            font = ("", size_font_menu_item),
            menu = settings_menu
        )
    def activador_ask_confirm_backup(self):
        self.messages.ask_confirm_backup(5)

    def activador_RadiobuttonChange(self):
        self.root.change_language(self.variable_language.get())
