import tkinter as tk 
import cv2
import os
import threading
import imutils
import time
from datetime import datetime
from tkinter import DISABLED, NORMAL, ttk
from PIL import Image, ImageTk
from Code.views.others.messages import Messages

class GuiCamera(tk.Toplevel):
    def __init__(self, root, master=None):
        super().__init__(master=master)
        self.root = root
        self.protocol("WM_DELETE_WINDOW", self.click_button_back)
        self.resizable(False, False)
        self.messages = Messages(root.root.numlanguage)
    def initialize(self):
        global cap
        cap = cv2.VideoCapture(0)
        if not cap.isOpened():
            self.messages.message_error_camera()
            self.click_button_back()
        else:
            #frame to camera
            self.title = "Camera"# add to pack language
            self.cam_video = tk.Label(self)
            self.cam_video.grid(column=0, row= 0, columnspan=3)

            # button snapshot
            path = os.path.dirname(__file__)
            filename = os.path.join(path, '../../../media/camera.png')
            self.img_cam = tk.PhotoImage(file=filename)
            self.button_snapshot = tk.Button(self, image=self.img_cam, command=self.click_button_snapshot)
            self.button_snapshot.image = self.img_cam
            self.button_snapshot.grid(column=0, row= 1, columnspan=3, padx = 15, pady = 5)


            # button to back
            path = os.path.dirname(__file__)
            filename = os.path.join(path, '../../../media/return1.png')
            self.img_back = tk.PhotoImage(file=filename)
            self.button_back = tk.Button(self, image= self.img_back, command=self.click_button_back)
            self.button_back.image= self.img_back
            self.button_back.grid(column=2, row=1, sticky= "e", padx = 5, pady = 5)

            # layout pack

            self.visualize()


    def visualize(self):
        global cap
        if cap is not None:
            ret, self.frame = cap.read()
            if ret == True:
                self.frame = imutils.resize(self.frame, width=640)
                self.frame = cv2.cvtColor(self.frame, cv2.COLOR_BGR2RGB)
                im = Image.fromarray(self.frame)
                img = ImageTk.PhotoImage(image=im)
                self.cam_video.configure(image=img)
                self.cam_video.image = img
                self.cam_video.after(100, self.visualize)
            else:
                self.messages.message_error_camera()
                self.click_button_back()
    def finalizar(self):
        global cap
        cap.release()
    def click_button_back(self):
        self.root.btn_camera.config(state=NORMAL)
        self.finalizar()
        self.destroy()
    def click_button_snapshot(self):
        self.button_snapshot.config(state=DISABLED)
        frame_guardar = self.frame
        frame_guardar = imutils.resize(frame_guardar, width=640)
        frame_guardar = cv2.cvtColor(frame_guardar, cv2.COLOR_BGR2RGB)
        now = datetime.now()
        year = str(now.year)[2:]
        if(len(str(now.month))<2):
            month = "0{0}".format(now.month)
        else:
            month = now.month
        if(len(str(now.day))<2):
            day = "0{0}".format(now.day)
        else:
            day = now.day
        if(len(str(now.hour))<2):
            hour = "0{0}".format(now.hour)
        else:
            hour = now.hour
        if(len(str(now.minute))<2):
            minute = "0{0}".format(now.minute)
        else:
            minute = now.minute
        if(len(str(now.second))<2):
            second = "0{0}".format(now.second)
        else:
            second = now.second
        photo_name= "IMGSIS{0}{1}{2}_{3}-{4}-{5}.jpg".format(year, month, day, hour, minute, second)
        cv2.imwrite('ImagesSIS/{}'.format(photo_name), frame_guardar)
        time.sleep(.5)
        self.button_snapshot.config(state=NORMAL)

        

#gui = GuiCamera()
#gui.initialize()
#gui.mainloop()
