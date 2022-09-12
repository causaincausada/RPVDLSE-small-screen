import tkinter.messagebox
from Code.views.others.Language import Language


class Messages():
    def __init__(self, numlanguage):
        super().__init__()
        self.language = Language()
        self.language.languageChange(numlanguage )
    # messages back up
    def message_confirm_backup(self):
        tkinter.messagebox.showinfo(self.lenguage.message_confirm_backup_title, self.language.message_confirm_backup_text)
    def message_error_backup(self):
        tkinter.messagebox.showerror(self.language.message_error_backup_title, self.language.message_error_backup_text)
    def ask_confirm_backup(self, num):
        text = self.language.ask_confirm_backup_text1,num, self.language.ask_confirm_backup_text2
        tkinter.messagebox.askokcancel(self.language.ask_confirm_backup_title, text)
    # messages Restore
    def ask_confirm_restore(self):
        tkinter.messagebox.askokcancel(self.language.ask_confirm_restore_title, self.language.ask_confirm_restore_text)
    def message_confirm_restore(self):
        tkinter.messagebox.showinfo(self.language.Message_confirm_restore_title, self.language.Message_confirm_restore_text)
    def message_Error_restore(self):
        tkinter.messagebox.showerror(self.language.Message_error_restore_title, self.language.Message_error_restore_text)
    # 