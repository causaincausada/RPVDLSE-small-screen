import tkinter.messagebox
import tkinter.simpledialog
from Code.views.others.language import Language


class Messages:
    def __init__(self, num_language):
        super().__init__()
        self.language = Language()
        self.language.language_change(num_language)
    
    # messages back up
    def message_confirm_backup(self):
        tkinter.messagebox.showinfo(self.language.message_confirm_backup_title,
                                    self.language.message_confirm_backup_text)

    def message_error_backup(self):
        tkinter.messagebox.showerror(self.language.message_error_backup_title,
                                     self.language.message_error_backup_text)

    def ask_confirm_backup(self, num):
        text = str(self.language.ask_confirm_backup_text1)+str(num)+str(self.language.ask_confirm_backup_text2)
        tkinter.messagebox.askokcancel(self.language.ask_confirm_backup_title, text)

    # messages Restore
    def ask_confirm_restore(self):
        tkinter.messagebox.askokcancel(self.language.ask_confirm_restore_title, self.language.ask_confirm_restore_text)

    def message_confirm_restore(self):
        tkinter.messagebox.showinfo(self.language.Message_confirm_restore_title,
                                    self.language.Message_confirm_restore_text)

    def message_error_restore(self):
        tkinter.messagebox.showerror(self.language.Message_error_restore_title,
                                     self.language.Message_error_restore_text)

    # messages gallery
    def ask_confirm_delete(self, name):
        return tkinter.messagebox.askyesno(self.language.message_confirm_delete_img_title,
                                           self.language.message_confirm_delete_img.format(name))

    def rename(self):
        return tkinter.simpledialog.askstring(self.language.message_rename_title, self.language.message_rename)

    def delete_image_ok(self):
        tkinter.messagebox.showinfo(self.language.message_ok_delete_title, self.language.message_ok_delete)

    def image_error_location(self):
        tkinter.messagebox.showerror(self.language.message_error_img_location_title,
                                     self.language.message_error_img_location)

    def rename_image_ok(self):
        tkinter.messagebox.showinfo(self.language.message_rename_title, self.language.rename_ok)

    def no_valid_name(self):
        tkinter.messagebox.showerror(self.language.message_rename_title, self.language.no_valid_name)

    def message_error_camera(self):
        tkinter.messagebox.showerror(self.language.message_error_camera_title, self.language.message_error_camera_text)

    # messages results
    def lost_connection_db(self):
        tkinter.messagebox.showerror(self.language.mes_error_connect_db_title, self.language.mes_error_connect_db_text)
