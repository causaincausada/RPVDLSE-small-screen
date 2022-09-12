import tkinter as tk
from tkinter import Menu
from Code.views.others.Language import Language

class GuiMenuBar(Menu):
    def __init__(self, root):
        super().__init__(root)

        language = Language()
        language.languageChange(0)
        results_menu = Menu(root, tearoff=0)
        restore_menu = Menu(root, tearoff=0)
        settings_menu = Menu(root, tearoff=0)
        language_menu = Menu(root, tearoff=0)

        # add a menu item to the menu --back up--
        results_menu.add_command(
            label= language.backup,
            font = ("", size_font_menu_item),
            command= activador_ask_ConfirmBackup
        )
        # add menu items in menu restore
        restore_menu.add_command(
            label= language.restoreMenuFile_label,
            font = ("", size_font_menu_item),
            command=messages.ask_ConfirmRestore
        )
        restore_menu.add_command(
            label= language.restoreMenuInitiate_label,
            font = ("", size_font_menu_item),
            command= messages.ask_ConfirmRestore
        )
        # add items in menu language
        variable_Language = tk.IntVar()
        language_menu.add_radiobutton(
            label = "Español",
            value = 1,
            variable = variable_Language,
            command = activador_RadiobuttonChange
        )
        language_menu.add_radiobutton(
            label = "ingles",
            value = 0,
            variable = variable_Language,
            command = activador_RadiobuttonChange
        )
        # add menu radiobuttons Language in settings menu
        settings_menu.add_cascade(
            label= "lenguage",
            font = ("", size_font_menu_item),
            menu = language_menu
        )
        # add a menu item to the menu --restore--
        results_menu.add_cascade(
            label=language.restoreMenu_label,
            font = ("", size_font_menu_item),
            menu= restore_menu
        )

        # add the results menu to the menubar
        self.add_cascade(
            label=language.menubarResults_label,
            font = ("", size_font_menu_item),
            menu=results_menu
        )
        self.add_cascade(
            label = "Settings",
            font = ("", size_font_menu_item),
            menu = settings_menu
        )

    def activador_ask_ConfirmBackup():
        messages.ask_ConfirmBackup(5)

    def activador_RadiobuttonChange():
        language.languageChange(variable_Language.get())

