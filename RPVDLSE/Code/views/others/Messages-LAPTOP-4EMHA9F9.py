import tkinter.messagebox
import Language

language = Language()
# messages back up
def message_ConfirmBackup():
    tkinter.messagebox.showinfo(Language.message_ConfirmBackup_title, Language.message_ConfirmBackup_text)
def message_ErrorBackup():
    tkinter.messagebox.showerror(Language.message_ErrorBackup_title, Language.message_ErrorBackup_text)
def ask_ConfirmBackup(num):
    text = Language.ask_ConfirmBackup_text1,num,Language.ask_ConfirmBackup_text2
    tkinter.messagebox.askokcancel(Language.ask_ConfirmBackup_title, text)
# messages Restore
def ask_ConfirmRestore():
    tkinter.messagebox.askokcancel(Language.ask_ConfirmRestore_title, Language.ask_ConfirmRestore_text)
def message_ConfirmRestore():
    tkinter.messagebox.showinfo(Language.Message_ConfirmRestore_title, Language.Message_ConfirmRestore_text)
def message_ErrorRestore():
    tkinter.messagebox.showerror(Language.Message_ErrorRestore_title, Language.Message_ErrorRestore_text)
# 