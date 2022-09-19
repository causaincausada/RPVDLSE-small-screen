import tkinter as tk 
import cv2
import os
import threading
import imutils
from tkinter import ttk
from PIL import Image, ImageTk


class GuiCamera(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title = "Camera"# add to pack language
        global cap
        cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)
        # frame to camera

        self.cam_video = tk.Label()
        self.cam_video.grid(column=0, row= 0, columnspan=3)

        # button snapshot
        path = os.path.dirname(__file__)
        filename = os.path.join(path, '../../../media/camera.png')
        img_cam = tk.PhotoImage(file=filename)
        self.button_snapshot = tk.Button(image=img_cam)
        self.button_snapshot.image = img_cam
        self.button_snapshot.grid(column=1, row= 1)
        

        # button to back
        path = os.path.dirname(__file__)
        filename = os.path.join(path, '../../../media/back.png')
        img_back = tk.PhotoImage(file=filename)
        self.button_back = tk.Button(image= img_back)
        self.button_back.image= img_back
        self.button_back.grid(column=2, row=1)

        # layout pack
        self.visualizar()
    def visualizar(self):
        global cap
        if cap is not None:
            ret, frame = cap.read()
            if ret == True:
                frame = imutils.resize(frame, width=640)
                #frame = imutils.resize(frame, width=640)
                frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
                im = Image.fromarray(frame)
                img = ImageTk.PhotoImage(image=im)
                self.cam_video.configure(image=img)
                self.cam_video.image = img
                self.cam_video.after(10, self.visualizar)
            else:
                self.cam.image = ""
                cap.release()
    def finalizar():
        global cap
        cap.release()
        
prueba = GuiCamera()
prueba.mainloop()

