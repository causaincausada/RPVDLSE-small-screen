import tkinter as tk
from tkinter import DISABLED, NORMAL, ttk
from Code.views.others.messages import Messages
from Code.views.others.language import Language


class InputRute(tk.Toplevel):
    def __init__(self, root, master=None):
        super().__init__(master=master)
        self.button_cancel = None
        self.frame_protocol = None
        self.root = root
        self.columnconfigure(0, weight=1)
        self.columnconfigure(1, weight=1)
        self.rowconfigure(0, weight=1)
        self.rowconfigure(1, weight=1)
        self.rowconfigure(2, weight=1)
        self.rowconfigure(3, weight=1)
        self.rowconfigure(4, weight=1)
        self.rowconfigure(5, weight=1)
        self.rowconfigure(6, weight=1)
        self.rowconfigure(7, weight=1)
        self.button_sumit = None
        self.text_ext = None
        self.text_port = None
        self.text_ip = None
        self.text_pass = None
        self.variable_ext = None
        self.text_user = None
        self.variable_protection = None
        self.variable_port = None
        self.variable_ip = None
        self.enable_protect = None
        self.variable_user = None
        self.variable_pass = None
        self.label_ext = None
        self.label_port = None
        self.label_ip = None
        self.label_pass = None
        self.label_user = None
        self.label_protocol = None
        self.language = Language()
        self.messages = Messages(root.root.num_language)
        self.language.language_change(root.root.num_language)

    def initialize(self):
        size_font_labels = 12
        self.label_protocol = ttk.Label(self,
                                        text=self.language.protocol,
                                        font=("", size_font_labels))
        self.label_user = ttk.Label(self,
                                    text=self.language.user,
                                    font=("", size_font_labels))
        self.label_pass = ttk.Label(self,
                                    text=self.language.password,
                                    font=("", size_font_labels))
        self.label_ip = ttk.Label(self,
                                  text=self.language.ip,
                                  font=("", size_font_labels))
        self.label_port = ttk.Label(self,
                                    text=self.language.port,
                                    font=("", size_font_labels))
        self.label_ext = ttk.Label(self,
                                   text=self.language.ext,
                                   font=("", size_font_labels))
        self.protocol = ttk.Combobox(
            self,
            state="readonly",
            values=["rtsp", "http", "https"]
        )
        self.protocol.set("rtsp")
        self.variable_user = tk.StringVar()
        self.variable_pass = tk.StringVar()
        self.variable_ip = tk.StringVar()
        self.variable_port = tk.StringVar()
        self.variable_ext = tk.StringVar()
        self.variable_protection = tk.IntVar()
        self.text_user = ttk.Entry(self,
                                   textvariable=self.variable_user)
        self.text_pass = ttk.Entry(self,
                                   textvariable=self.variable_pass)
        self.text_ip = ttk.Entry(self,
                                 textvariable=self.variable_ip)
        self.text_port = ttk.Entry(self,
                                   textvariable=self.variable_port)
        self.text_ext = ttk.Entry(self,
                                  textvariable=self.variable_ext)
        self.enable_protect = ttk.Checkbutton(self, text=self.language.protection,
                                              variable=self.variable_protection,
                                              command=self.ch_protect)
        self.button_sumit = ttk.Button(self, text=self.language.confirm, command=self.click_button_confirm)
        self.button_cancel = ttk.Button(self, text=self.language.cancel, command=self.click_button_cancel)
        self.label_protocol.grid(column=0, row=0, sticky="news", pady=5, padx=5)
        self.enable_protect.grid(column=0, row=1, sticky="news", pady=5, padx=5)
        self.label_user.grid(column=0, row=2, sticky="news", pady=5, padx=5)
        self.label_pass.grid(column=0, row=3, sticky="news", pady=5, padx=5)
        self.label_ip.grid(column=0, row=4, sticky="news", pady=5, padx=5)
        self.label_port.grid(column=0, row=5, sticky="news", pady=5, padx=5)
        self.label_ext.grid(column=0, row=6, sticky="news", pady=5, padx=5)
        self.protocol.grid(column=1, columnspan=2, row=0, sticky="news", pady=5, padx=5)
        self.text_user.grid(column=1, row=2, sticky="news", pady=5, padx=5)
        self.text_pass.grid(column=1, row=3, sticky="news", pady=5, padx=5)
        self.text_ip.grid(column=1, row=4, sticky="news", pady=5, padx=5)
        self.text_port.grid(column=1, row=5, sticky="news", pady=5, padx=5)
        self.text_ext.grid(column=1, row=6, sticky="news", pady=5, padx=5)
        self.button_sumit.grid(column=1, row=7, sticky="news", pady=5, padx=5)
        self.button_cancel.grid(column=0, row=7, sticky="news", pady=5, padx=5)
        self.text_user.configure(state=DISABLED)
        self.text_pass.configure(state=DISABLED)
        self.label_user.configure(state=DISABLED)
        self.label_pass.configure(state=DISABLED)
        self.set_camera_ip()
        self.mainloop()

    def set_camera_ip(self):
        camera_ip = self.root.root.app_logic.get_rute_camera()
        try:
            settings = camera_ip[0]
            self.variable_protection.set(settings["protection"])
            self.protocol.set(settings["protocol"])
            self.variable_user.set(settings["user"])
            self.variable_pass.set(settings["pass"])
            self.variable_ip.set(settings["ip"])
            self.variable_port.set(settings["port"])
            self.variable_ext.set(settings["ext"])
            self.ch_protect()
        except IndexError:
            print("Error index")

    def ch_protect(self):
        if not self.variable_protection.get():
            self.text_user.configure(state=DISABLED)
            self.text_pass.configure(state=DISABLED)
            self.label_user.configure(state=DISABLED)
            self.label_pass.configure(state=DISABLED)
        else:
            self.text_user.configure(state=NORMAL)
            self.text_pass.configure(state=NORMAL)
            self.label_user.configure(state=NORMAL)
            self.label_pass.configure(state=NORMAL)

    def click_button_confirm(self):
        if not self.variable_protection:
            if not (self.variable_ip.get() == "") and \
                    not (self.variable_port.get() == "") and \
                    not (self.variable_ext.get() == ""):
                self.root.root.app_logic.ch_rute_camera(self.variable_protection.get(),
                                                        self.protocol.get(),
                                                        self.variable_user.get(), self.variable_pass.get(),
                                                        self.variable_ip.get(), self.variable_port.get(),
                                                        self.variable_ext.get())
                self.destroy()
            else:
                self.messages.error_rute()
                self.destroy()
        else:
            if not (self.variable_ip.get() == "") and \
                    not (self.variable_user.get() == "") and \
                    not (self.variable_pass.get() == "") and \
                    not (self.variable_port.get() == "") and \
                    not (self.variable_ext.get() == ""):
                self.root.root.app_logic.ch_rute_camera(self.variable_protection.get(),
                                                        self.protocol.get(),
                                                        self.variable_user.get(), self.variable_pass.get(),
                                                        self.variable_ip.get(), self.variable_port.get(),
                                                        self.variable_ext.get())
                self.destroy()
            else:
                self.messages.error_rute()
                self.destroy()

    def click_button_cancel(self):
        self.destroy()
