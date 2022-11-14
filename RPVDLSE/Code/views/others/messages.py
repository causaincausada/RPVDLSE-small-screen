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

    def ask_confirm_backup(self, num, name):
        text = str(self.language.ask_confirm_backup_text1) + \
               str(num)+str(self.language.ask_confirm_backup_text2) + str(name)
        return tkinter.messagebox.askokcancel(self.language.ask_confirm_backup_title, text)

    # messages Restore
    def ask_confirm_restore(self):
        return tkinter.messagebox.askokcancel(self.language.ask_confirm_restore_title,
                                              self.language.ask_confirm_restore_text)

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

    # messages recognition
    def message_recognition_complete(self, result):
        tkinter.messagebox.showinfo(self.language.message_recognition_complete_title,
                                    self.language.message_recognition_complete_text.format(str(result)))

    def message_error_db(self, result):
        tkinter.messagebox.showerror(self.language.error_database_title,
                                     self.language.error_database_text.format(str(result)))

    # messages results
    def lost_connection_db(self):
        tkinter.messagebox.showerror(self.language.mes_error_connect_db_title, self.language.mes_error_connect_db_text)

    def ask_confirm_close_main(self):
        return tkinter.messagebox.askokcancel(self.language.ask_confirm_close_main_title,
                                              self.language.ask_confirm_close_main_text)

    def new_host_ip(self):
        return tkinter.simpledialog.askstring(self.language.message_ip_camera_title,
                                              self.language.message_ip_camera_text)
