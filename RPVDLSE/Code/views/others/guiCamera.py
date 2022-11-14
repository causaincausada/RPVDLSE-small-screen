import tkinter as tk 
import cv2
import os
import imutils
import time
from datetime import datetime
from tkinter import DISABLED, NORMAL
from PIL import Image, ImageTk
from Code.views.others.messages import Messages
from Code.views.others.language import Language


class GuiCamera(tk.Toplevel):
    def __init__(self, root, rute, master=None):
        super().__init__(master=master)
        self.img_back = None
        self.button_snapshot = None
        self.cam_video = None
        self.button_back = None
        self.cap = None
        self.img_cam = None
        self.root = root
        self.protocol("WM_DELETE_WINDOW", self.click_button_back)
        self.resizable(False, False)
        self.messages = Messages(root.root.num_language)
        self.language = Language()
        self.rute = rute

    def initialize(self):
        # self.cap = cv2.VideoCapture(0)
        self.cap = cv2.VideoCapture()
        self.cap.open(self.rute)
        if not self.cap.isOpened():
            self.messages.message_error_camera()
            self.click_button_back()
        else:
            # frame to camera
            self.title = ""  # Language.title_camera
            self.cam_video = tk.Label(self)
            self.cam_video.grid(column=0, row=0, columnspan=3)

            # button snapshot
            path = os.path.dirname(__file__)
            filename = os.path.join(path, '../../../media/camera.png')
            self.img_cam = tk.PhotoImage(file=filename)
            self.button_snapshot = tk.Button(self, image=self.img_cam, command=self.click_button_snapshot)
            self.button_snapshot.image = self.img_cam
            self.button_snapshot.grid(column=0, row=1, columnspan=3, padx=15, pady=5)

            # button to back
            path = os.path.dirname(__file__)
            filename = os.path.join(path, '../../../media/return1.png')
            self.img_back = tk.PhotoImage(file=filename)
            self.button_back = tk.Button(self, image=self.img_back, command=self.click_button_back)
            self.button_back.image = self.img_back
            self.button_back.grid(column=2, row=1, sticky="e", padx=5, pady=5)

            # layout pack

            self.visualize()

    def visualize(self):
        if self.cap is not None:
            ret, self.frame = self.cap.read()
            if ret:
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

    def finalize(self):
        self.cap.release()

    def click_button_back(self):
        self.root.btn_camera.config(state=NORMAL)
        self.finalize()
        self.destroy()

    def click_button_snapshot(self):
        self.button_snapshot.config(state=DISABLED)
        frame_save = self.frame
        frame_save = imutils.resize(frame_save, width=640)
        frame_save = cv2.cvtColor(frame_save, cv2.COLOR_BGR2RGB)
        now = datetime.now()
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
        photo_name = "IMGSIS{0}{1}{2}_{3}-{4}-{5}.jpg".format(year, month, day, hour, minute, second)
        cv2.imwrite('ImagesSIS/{}'.format(photo_name), frame_save)
        time.sleep(.5)
        self.button_snapshot.config(state=NORMAL)
        self.root.root.app_logic.update_gallery()
