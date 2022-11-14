import datetime
import subprocess
import cv2
import pymongo.errors
from Code.props.props import Props
from Code.props.img import Img
from Code.views.gui import Gui
from Code.props.dataBaseR import DataBaseR
from Code.props.recognition import Recognition
from Code.props.result import Result
import re


INTERNAL = 0
EXTERNAL = 1
NUM_IMGS_GALLERY = 12

# Constant connection
MONGO_HOST = 'localhost'
MONGO_PORT = "27017"
MONGO_TIMEOUT = 1000


class ApplicationLogic:
    def __init__(self, props: Props, gui: Gui):
        self.props = props
        self.gui = gui
        try:
            subprocess.Popen(["/usr/bin/systemctl", "start", "mongod.service"])
        except FileNotFoundError as a:
            print(a)
        self.dataBaseR = DataBaseR(MONGO_HOST, MONGO_PORT, MONGO_TIMEOUT)
        # warnings in filters
        self.warnings = [True, True, True, True, True]

        # image data
        self.imgs_tk = []  # Display images
        self.select_img: Img = None  # Select image status

        # vars of control for gallery
        self.lists_imgs = None  # List of list // Each list is a page of gallery
        self.page = 0  # Page of gallery
        self.status_int_ext = INTERNAL  # Default option: intenal imgs

        # init gallery
        self.calculate_lists_imgs()  # Calculate lists_imgs
        # init recognition class
        self.r = Recognition()
    
    def after_init(self):
        # init gallery
        self.set_images_gui()
        self.status_next_back_btn()
        self.disabled_bottom_btns()

    # Gallery methods
    def select_image(self, img_num: int):
        if img_num == -1:
            self.select_img = None
            self.disabled_bottom_btns()
        elif len(self.imgs_tk) >= img_num:
            self.select_img = self.imgs_tk[img_num-1]
            self.enable_bottom_btns()
        else:
            self.select_img = None
            self.disabled_bottom_btns()
            print("Error")  # catch error / no deberia pasar

    def turn_page(self):
        self.page += 1
        self.calculate_lists_imgs()
        self.repaint()

    def return_page(self):
        self.page -= 1
        self.calculate_lists_imgs()
        self.repaint()

    def set_images_gui(self):
        self.list_tk()
        self.gui.frame_tab_gallery.set_images(self.imgs_tk)
    
    def calculate_lists_imgs(self):
        if self.status_int_ext == 0:
            self.lists_imgs = self.partition(self.props.get_imgs_internal(),
                                             NUM_IMGS_GALLERY)
        else:
            self.lists_imgs = self.partition(self.props.get_imgs_external(),
                                             NUM_IMGS_GALLERY)
    
    def list_tk(self):
        self.imgs_tk.clear()
        if self.page > (len(self.lists_imgs) - 1):  # Delete last image in page
            self.page = len(self.lists_imgs) - 1

        if len(self.lists_imgs) > 0:
            for img in self.lists_imgs[self.page]:
                self.imgs_tk.append(Img(img, self.status_int_ext))

    def status_next_back_btn(self):
        if self.page == 0:
            self.gui.frame_tab_gallery.disabled_btn_back()
        else:
            self.gui.frame_tab_gallery.enable_btn_back()

        if((self.page == (len(self.lists_imgs) - 1)) or 
           (len(self.lists_imgs) == 0)):
            self.gui.frame_tab_gallery.disabled_btn_next()
        else:
            self.gui.frame_tab_gallery.enable_btn_next()

    def set_ext_mode(self):
        self.status_int_ext = EXTERNAL

    def set_int_mode(self):
        self.status_int_ext = INTERNAL

    def update_gallery(self):
        self.lists_imgs = None  # List of list // Each list is a page of gallery
        self.page = 0  # Page of gallery
        self.calculate_lists_imgs()  # Calculate lists_imgs
        self.repaint()

    def repaint(self):
        self.set_images_gui()
        self.status_next_back_btn()
        self.disabled_bottom_btns()

    def get_empty_img(self):
        return self.props.get_empty(self.status_int_ext)

    def open_select_img(self):
        return self.select_img.open_image()

    def disabled_bottom_btns(self):
        self.gui.frame_tab_gallery.disabled_btn_open()
        self.gui.frame_tab_gallery.disabled_btn_delete()
        self.gui.frame_tab_gallery.disabled_btn_rename()
        self.gui.frame_tab_gallery.disabled_btn_recognize()

    def enable_bottom_btns(self):
        self.gui.frame_tab_gallery.enable_btn_open()
        self.gui.frame_tab_gallery.enable_btn_delete()
        self.gui.frame_tab_gallery.enable_btn_rename()
        self.gui.frame_tab_gallery.enable_btn_recognize()

    def delete_img_select(self):
        successfull = self.select_img.delete_image()
        return successfull

    def update_gallery_page(self, page):
        self.lists_imgs = None  # List of list // Each list is a page of gallery
        self.page = page  # Page of gallery
        self.calculate_lists_imgs()  # Calculate lists_imgs
        self.repaint()

    def get_name_select_img(self):
        return self.select_img.name

    def change_name_select_img(self, new_name):
        successful = self.select_img.rename_image(new_name)
        return successful

    @staticmethod
    def is_rename_valid(new_name):
        if re.match("^[A-Za-z0-9_-]+$", new_name):
            return True
        else:
            return False

    def recognition_plate(self):
        img = cv2.imread(self.select_img.path_and_name)
        results = self.r.yolo_predictions(img)
        r_db = Result(
                self.select_img.name,
                datetime.datetime(year=datetime.datetime.now().year, month=datetime.datetime.now().month,
                                  day=datetime.datetime.now().day, hour=0, minute=0, second=0),
                datetime.datetime(year=1970, month=1, day=1,
                                  hour=datetime.datetime.now().hour, minute=datetime.datetime.now().minute,
                                  second=datetime.datetime.now().second),
                results
            )
        if self.dataBaseR.push_result(r_db):
            return True, results
        else:
            return False, results

    def try_connect_mongodb(self):
        try:
            self.dataBaseR = DataBaseR(MONGO_HOST, MONGO_PORT, MONGO_TIMEOUT)
            if self.dataBaseR.on_connect():
                self.gui.frame_tab_results.get_results_gui()
            return self.dataBaseR.on_connect()
        except pymongo.errors.ServerSelectionTimeoutError:
            try:
                cb = subprocess.Popen(["/usr/bin/systemctl", "start", "mongod.service"], stdout=subprocess.PIPE,
                                      stderr=subprocess.STDOUT)
                if len(cb.stdout.readlines()) == 0:
                    self.gui.frame_tab_results.get_results_gui()
                    return True
                return False
            except FileNotFoundError as a:
                print(a)
                return False

    # Results methods
    def on_connect_mongodb(self):
        try:
            return self.dataBaseR.on_connect()
        except TypeError:
            return False
        except AttributeError:
            return False

    def disconnect_mongodb(self):
        try:
            self.dataBaseR.disconnect()
            cb = subprocess.Popen(["/usr/bin/systemctl", "stop", "mongod.service"], stdout=subprocess.PIPE,
                                  stderr=subprocess.STDOUT)
            if len(cb.stdout.readlines()) == 0:
                return True
            return False
        except FileNotFoundError as a:
            print(a)
            return False

    def drop_results(self):
        self.dataBaseR.drop()

    def get_size_mongodb(self):
        return self.dataBaseR.get_size()

    def create_backup(self, path):
        try:
            cb = subprocess.Popen(["/usr/bin/mongoexport", "--jsonFormat=canonical",
                                   '--uri="mongodb://localhost:27017"', "--collection=results", "--db=RPVDLSE",
                                   "--out="+path], stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
            res = cb.stdout.readlines()
            try:
                connect = res[0].decode('utf-8')
                correct = connect.find("connected to:")
                if correct != -1:
                    size_check = res[1].decode('utf-8')
                    correct = size_check.find("exported {0} records".format(self.get_size_mongodb()))
                    if correct != -1:
                        return True
                return False
            except TypeError:
                return False
            except IndexError:
                return False
        except FileNotFoundError as a:
            print(a)
            return False

    @staticmethod
    def update_restore_mongodb(path):
        try:
            cb = subprocess.Popen(["/usr/bin/mongoimport", '--uri="mongodb://localhost:27017"', "--collection=results",
                                   "--db=RPVDLSE", "--file="+path], stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
            res = cb.stdout.readlines()
            try:
                connect = res[0].decode('utf-8')
                correct = connect.find("connected to:")
                if correct != -1:
                    size_check = res[1].decode('utf-8')
                    correct = size_check.find("imported successfully")
                    if correct != -1:
                        return True
                return False
            except TypeError:
                return False
            except IndexError:
                return False
        except FileNotFoundError as a:
            print(a)
            return False

    def get_results(self, gui_date_begin=datetime.datetime, gui_date_end=datetime.datetime,
                    gui_time_begin=datetime.datetime, gui_time_end=datetime.datetime, gui_plate="", gui_name=""):
        response = self.dataBaseR.get_results(date_begin=gui_date_begin, date_end=gui_date_end,
                                              hour_begin=gui_time_begin, hour_end=gui_time_end,
                                              plate=gui_plate, name=gui_name)
        return response, self.warnings

    def is_dates_valid(self, date_begin, date_end):
        if date_end < date_begin:
            self.warnings[0] = False
            return False
        self.warnings[0] = True
        return True

    def is_hour_inversed(self, hour_begin, hour_end):
        if hour_end < hour_begin:
            self.warnings[1] = False
            return False
        self.warnings[1] = True
        return True

    def is_hour_valid(self, hour):
        try:
            if re.match("^[0-9:]+$", hour):
                separate = hour.find(":")
                if separate != -1:
                    str_hour = hour[0:int(separate)]
                    str_minute = hour[separate+1: len(hour)]
                    if int(str_hour) < 23 and int(str_minute) < 60:
                        time = datetime.datetime(year=1970, month=1, day=1, hour=int(str_hour), minute=int(str_minute))
                        self.warnings[2] = True
                        return True, time
            time = datetime.datetime(year=1970, month=1, day=1, hour=0, minute=0)
            if hour == "":
                self.warnings[2] = True
                return False, time
            self.warnings[2] = False
            return False, time
        except ValueError:
            time = datetime.datetime(year=1970, month=1, day=1, hour=0, minute=0)
            if hour == "":
                self.warnings[2] = True
                return False, time
            self.warnings[2] = False
            return False, time

    def is_name_plate_valid(self, name_plate: str):
        if re.match("^[A-Za-z0-9_ -]+$", name_plate):
            self.warnings[3] = True
            return True
        else:
            if name_plate == "":
                self.warnings[3] = True
                return False
            self.warnings[3] = False
            return False

    def is_name_valid(self, name: str):
        if re.match("^[A-Za-z0-9_ -]+$", name):
            self.warnings[4] = True
            return True
        else:
            if name == "":
                self.warnings[4] = True
                return False
            self.warnings[4] = False
            return False

    def ch_rute_camera(self, rute):
        self.gui.ch_rute(rute)

    # other methods
    @staticmethod
    def partition(lst, size):
        list_of_lists = []
        for i in range(0, len(lst), size):
            _list = lst[i: i+size]
            list_of_lists.append(_list)
        return list_of_lists
