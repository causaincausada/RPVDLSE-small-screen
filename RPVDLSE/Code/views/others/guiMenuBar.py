import tkinter as tk
import os
import datetime
from tkinter import Menu
from tkinter.filedialog import askopenfilename
from Code.views.others.language import Language
from Code.views.others.messages import Messages


class GuiMenuBar(Menu):
    def __init__(self, root):
        super().__init__(root)
        self.root = root
        self.language = Language()
        self.messages = Messages(root.num_language)
        self.language.language_change(root.num_language)
        results_menu = Menu(root, tearoff=0)
        restore_menu = Menu(root, tearoff=0)
        settings_menu = Menu(root, tearoff=0)
        language_menu = Menu(root, tearoff=0)
        size_font_menu_item = 15
        # add a menu item to the menu --back up--
        results_menu.add_command(
            label=self.language.backup,
            font=("", size_font_menu_item),
            command=self.act_ask_confirm_backup
        )
        # add menu items in menu restore
        restore_menu.add_command(
            label=self.language.restore_menu_file_label,
            font=("", size_font_menu_item),
            command=self.act_select_backup
        )
        restore_menu.add_command(
            label=self.language.restore,
            font=("", size_font_menu_item),
            command=self.messages.ask_confirm_restore
        )
        # add items in menu language
        self.variable_language = tk.IntVar()
        self.variable_language.set(value=root.num_language)
        language_menu.add_radiobutton(
            label=self.language.spanish,
            value=1,
            variable=self.variable_language,
            command=self.act_rb_change
        )
        language_menu.add_radiobutton(
            label=self.language.english,
            value=0,
            variable=self.variable_language,
            command=self.act_rb_change
        )
        
        # add menu radiobuttons Language in settings menu
        settings_menu.add_cascade(
            label=self.language.language,
            font=("", size_font_menu_item),
            menu=language_menu
        )
        # add a menu item to the menu --restore--
        results_menu.add_cascade(
            label=self.language.restore,
            font=("", size_font_menu_item),
            menu=restore_menu
        )

        # add the results menu to the menubar
        self.add_cascade(
            label=self.language.menubar_results_label,
            font=("", size_font_menu_item),
            menu=results_menu
        )
        self.add_cascade(
            label=self.language.settings,
            font=("", size_font_menu_item),
            menu=settings_menu
        )

    def act_rb_change(self):
        self.root.change_language(self.variable_language.get())

    def act_ask_confirm_backup(self):
        try:
            if not self.root.app_logic.on_connect_mongodb():
                self.root.app_logic.try_connect_mongodb()
            tam = self.root.app_logic.get_size_mongodb()
            if tam != -1:
                now = datetime.datetime.now()
                year = str(now.year)[2:]
                if len(str(now.month)) < 2:
                    month = "0{0}".format(now.month)
                else:
                    month = now.month
                if len(str(now.day)) < 2:
                    day = "0{0}".format(now.day)
                else:
                    day = now.day
                if len(str(now.hour)) < 2:
                    hour = "0{0}".format(now.hour)
                else:
                    hour = now.hour
                if len(str(now.minute)) < 2:
                    minute = "0{0}".format(now.minute)
                else:
                    minute = now.minute
                if len(str(now.second)) < 2:
                    second = "0{0}".format(now.second)
                else:
                    second = now.second
                name = 'ResManualResults{0}{1}{2}_{3}-{4}-{5}.json'.format(year, month, day, hour, minute, second)
                res = self.messages.ask_confirm_backup(tam, name=name)
                if res:
                    self.create_backup_event(auto=False, name=name)
            else:
                self.messages.message_error_backup()
        except AttributeError:
            self.messages.message_error_backup()

    def act_select_backup(self):
        filename = askopenfilename()
        print(filename)

    def create_backup_event(self, auto=True, name=""):
        path = os.path.dirname(__file__)
        if auto:
            now = datetime.datetime.now()
            year = str(now.year)[2:]
            if len(str(now.month)) < 2:
                month = "0{0}".format(now.month)
            else:
                month = now.month
            if len(str(now.day)) < 2:
                day = "0{0}".format(now.day)
            else:
                day = now.day
            if len(str(now.hour)) < 2:
                hour = "0{0}".format(now.hour)
            else:
                hour = now.hour
            if len(str(now.minute)) < 2:
                minute = "0{0}".format(now.minute)
            else:
                minute = now.minute
            if len(str(now.second)) < 2:
                second = "0{0}".format(now.second)
            else:
                second = now.second
            filename = os.path.join(path, '../../../persistence/ResAutoResults{0}{1}{2}_{3}-{4}-{5}.json'.format(
                                        year, month, day, hour, minute, second))
        else:
            filename = os.path.join(path, '../../../persistence/{0}'.format(name))
        if self.root.app_logic.create_backup(filename):
            self.messages.message_confirm_backup()
        else:
            self.messages.message_error_backup()
    def restore_backup_event(self):
        pass
