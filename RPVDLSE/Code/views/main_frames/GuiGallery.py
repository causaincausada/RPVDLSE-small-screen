import os
import tkinter as tk 
from PIL import Image, ImageTk
from tkinter import Toplevel, ttk
from Code.views.others.Language import Language
from Code.views.others.Messages import Messages

DEFAULT_SIZE_RADIO_BUTTON = 15

class GuiGallery(ttk.Frame):
    def __init__(self, root):
        super().__init__(root.tab_control)
        selected_radio_button = tk.StringVar()
        #Language pack
        self.root = root
        self.language = Language()
        self.messages = Messages(root.numlanguage)
        self.language.languageChange(root.numlanguage)

        #Style
        style = ttk.Style()
        style.configure('Big.TRadiobutton', 
                        font=(None, DEFAULT_SIZE_RADIO_BUTTON))

        #Layout Management: Grid
        #Configure the grid
        self.columnconfigure(0, weight=1)

        self.rowconfigure(0, weight = 1)
        self.rowconfigure(1, weight = 9)
        self.rowconfigure(2, weight = 1)


        #Frame Up
        #Layout Management: Place
        frame_up = ttk.Frame(self)
        frame_up.grid(column=0, row=0, sticky='NEWS')

        #Buttons Frame Up: Control of Gallery
        path = os.path.dirname(__file__)
        filename = os.path.join(path, '../../../media/back.png')
        #icons
        self.back_icon = tk.PhotoImage(file=filename)
        filename = os.path.join(path, '../../../media/next.png')
        self.next_icon = tk.PhotoImage(file=filename)
        filename = os.path.join(path, '../../../media/update.png')
        self.update_icon = tk.PhotoImage(file=filename)
        filename = os.path.join(path, '../../../media/camera.png')
        self.camera_icon = tk.PhotoImage(file=filename)

        btn_back = ttk.Button(frame_up, image=self.back_icon)
        btn_next = ttk.Button(frame_up, image=self.next_icon)
        btn_update = ttk.Button(frame_up, image=self.update_icon)
        btn_camera = ttk.Button(frame_up, image=self.camera_icon)

        #Frame RadioButton in Frame Up
        #Layout Management: Place
        frame_radio_button_ie = ttk.Frame(frame_up)
        frame_radio_button_ie.place(relx=0.75, 
                                    rely=0.0, 
                                    relheight=1, 
                                    relwidth=0.20)
        
        rb_internas = ttk.Radiobutton(frame_radio_button_ie, 
                                      text=self.language.internals, #!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!! Texto Ingles/Español
                                      value='inter', #!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!! Texto Ingles/Español
                                      variable=selected_radio_button,
                                      style = "Big.TRadiobutton")
        rb_externas = ttk.Radiobutton(frame_radio_button_ie, 
                                      text=self.language.externals, #!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!! Texto Ingles/Español
                                      value='exter', #!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!! Texto Ingles/Español
                                      variable=selected_radio_button,
                                      style = "Big.TRadiobutton")
        selected_radio_button.set("inter") #Default option #!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!! Texto Ingles/Español

        #Lacation elements (Buttons and Radiobutton in Frame Up y Frame)
        btn_back.place(relx=0.05, rely=0.0, relheight=1, relwidth=0.10)
        btn_next.place(relx=0.15, rely=0.0, relheight=1, relwidth=0.10)
        btn_update.place(relx=0.25, rely=0.0, relheight=1, relwidth=0.10)
        btn_camera.place(relx=0.65, rely=0.0, relheight=1, relwidth=0.10)
        rb_internas.place(relx=0.15, rely=0.00, relheight=0.5, relwidth=0.85)
        rb_externas.place(relx=0.15, rely=0.5, relheight=0.5, relwidth=0.85)

        
        #Frame Center
        #Layout Management: Place
        frame_center = ttk.Frame(self)
        frame_center.grid(column=0, row=1, sticky='NEWS')
        #Frame Middle
        #Layout Management: Grid
        frame_middle = ttk.Frame(frame_center)
        frame_middle.place(relx=0.05, rely=0.01, relheight=0.98, relwidth=0.9)
        frame_middle.config(relief="groove") #Frame outline
        frame_middle.config(padding=10)

        #Configure the grid
        frame_middle.columnconfigure(0, weight=1)
        frame_middle.columnconfigure(1, weight=1)
        frame_middle.columnconfigure(2, weight=1)
        frame_middle.columnconfigure(3, weight=1)

        frame_middle.rowconfigure(0, weight = 4)
        frame_middle.rowconfigure(1, weight = 1)
        frame_middle.rowconfigure(2, weight = 4)
        frame_middle.rowconfigure(3, weight = 1)
        frame_middle.rowconfigure(4, weight = 4)
        frame_middle.rowconfigure(5, weight = 1)

        bbprueba = ttk.Button(frame_middle, text="Ejemplo1")
        bbprueba.grid(column = 0, row = 0, sticky='NEWS')
        l1 = ttk.Label(frame_middle, text = "Imagen 1")
        l1.grid(column = 0, row = 1)

        bbprueba2 = ttk.Button(frame_middle, text="Ejemplo2")
        bbprueba2.grid(column = 1, row = 0, sticky='NEWS')
        l2 = ttk.Label(frame_middle, text = "Imagen 2")
        l2.grid(column = 1, row = 1)

        bbprueba3 = ttk.Button(frame_middle, text="Ejemplo3")
        bbprueba3.grid(column = 2, row = 0, sticky='NEWS')
        l3 = ttk.Label(frame_middle, text = "Imagen 3")
        l3.grid(column = 2, row = 1)

        bbprueba4 = ttk.Button(frame_middle, text="Ejemplo4")
        bbprueba4.grid(column = 3, row = 0, sticky='NEWS')
        l4 = ttk.Label(frame_middle, text = "Imagen 4")
        l4.grid(column = 3, row = 1)

        bbprueba5 = ttk.Button(frame_middle, text="Ejemplo5")
        bbprueba5.grid(column = 0, row = 2, sticky='NEWS')
        l5 = ttk.Label(frame_middle, text = "Imagen 5")
        l5.grid(column = 0, row = 3)

        bbprueba6 = ttk.Button(frame_middle, text="Ejemplo6")
        bbprueba6.grid(column = 1, row = 2, sticky='NEWS')
        l6 = ttk.Label(frame_middle, text = "Imagen 6")
        l6.grid(column = 1, row = 3)

        bbprueba7 = ttk.Button(frame_middle, text="Ejemplo7")
        bbprueba7.grid(column = 2, row = 2, sticky='NEWS')
        l7 = ttk.Label(frame_middle, text = "Imagen 7")
        l7.grid(column = 2, row = 3)

        bbprueba8 = ttk.Button(frame_middle, text="Ejemplo8")
        bbprueba8.grid(column = 3, row = 2, sticky='NEWS')
        l8 = ttk.Label(frame_middle, text = "Imagen 8")
        l8.grid(column = 3, row = 3)

        bbprueba9 = ttk.Button(frame_middle, text="Ejemplo9")
        bbprueba9.grid(column = 0, row = 4, sticky='NEWS')
        l9 = ttk.Label(frame_middle, text = "Imagen 9")
        l9.grid(column = 0, row = 5)

        bbprueba10 = ttk.Button(frame_middle, text="Ejemplo10")
        bbprueba10.grid(column = 1, row = 4, sticky='NEWS')
        l10 = ttk.Label(frame_middle, text = "Imagen 10")
        l10.grid(column = 1, row = 5)

        bbprueba11 = ttk.Button(frame_middle, text="Ejemplo11")
        bbprueba11.grid(column = 2, row = 4, sticky='NEWS')
        l11 = ttk.Label(frame_middle, text = "Imagen 11")
        l11.grid(column = 2, row = 5)

        bbprueba12 = ttk.Button(frame_middle, text="Ejemplo12")
        bbprueba12.grid(column = 3, row = 4, sticky='NEWS')
        l12 = ttk.Label(frame_middle, text = "Imagen 12")
        l12.grid(column = 3, row = 5)
        
        
        #Frame Down
        #Layout Management: Place
        frame_down = ttk.Frame(self)
        #Location (Frame Down in Gallery Frame)
        frame_down.grid(column=0, row=2, sticky='NEWS')

        #Buttons Frame Down: Gallery Images Options
        btn_open = ttk.Button(frame_down, text=self.language.open)#!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!! Texto Ingles/Español
        btn_delete = ttk.Button(frame_down, text=self.language.delet)#!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!! Texto Ingles/Español
        btn_rename = ttk.Button(frame_down, text=self.language.rename)#!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!! Texto Ingles/Español
        btn_recognize = ttk.Button(frame_down, text=self.language.recognize)#!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!! Texto Ingles/Español

        #Lacation elements (Buttons in Frame Down)
        btn_open.place(relx=0.05, rely=0.0, relheight=1, relwidth=0.1875)
        btn_delete.place(relx=0.2875, rely=0.0, relheight=1, relwidth=0.1875)
        btn_rename.place(relx=0.525, rely=0.0, relheight=1, relwidth=0.1875)
        btn_recognize.place(relx=0.7625, rely=0.0, relheight=1, relwidth=0.1875)
