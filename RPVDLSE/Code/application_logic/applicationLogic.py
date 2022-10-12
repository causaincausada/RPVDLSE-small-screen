import datetime
from Code.props.props import Props
from Code.props.img import Img
from Code.views.gui import Gui
from Code.props.dataBaseR import DataBaseR
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
        self.dataBaseR = DataBaseR(MONGO_HOST, MONGO_PORT, MONGO_TIMEOUT)

        # image data
        self.imgs_tk = []  # Display images
        self.select_img: Img = None  # Select image status

        # vars of control for gallery
        self.lists_imgs = None  # List of list // Each list is a page of gallery
        self.page = 0  # Page of gallery
        self.status_int_ext = INTERNAL  # Default option: intenal imgs

        # init gallery
        self.calculate_lists_imgs()  # Calculate lists_imgs
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

    def get_empty_img(self):
        return self.props.get_empty(self.status_int_ext)

    def open_select_img(self):
        successfull = self.select_img.open_image()
        return successfull

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
        successfull = self.select_img.rename_image(new_name)
        return successfull

    @staticmethod
    def is_raname_valid(new_name):
        if re.match("^[A-Za-z0-9_-]+$", new_name):
            return True
        else:
            return False

    def try_connect_mongodb(self):
        try:
            self.dataBaseR = DataBaseR(MONGO_HOST, MONGO_PORT, MONGO_TIMEOUT)
            return self.dataBaseR.on_connect()
        except ConnectionError:
            return false

    # Results methods
    def on_connect_mongodb(self):
        try:
            return self.dataBaseR.on_connect()
        except TypeError:
            return False

    def get_results(self, gui_date_begin=datetime.datetime, gui_date_end=datetime.datetime,
                    gui_time_begin=datetime.datetime, gui_time_end=datetime.datetime, gui_plate="", gui_name=""):

        response = self.dataBaseR.get_results(date_begin=gui_date_begin, date_end=gui_date_end, hour_begin=gui_time_begin,
                                   hour_end=gui_time_end, plate=gui_plate, name=gui_name)
        return response

    @staticmethod
    def is_hour_valid(hour):
        try:
            if re.match("^[0-9:]+$", hour):
                separate = hour.find(":")
                if separate != -1:
                    str_hour = hour[0:int(separate)]
                    str_minute = hour[separate+1: len(hour)]
                    if int(str_hour) < 23 and int(str_minute) < 60:
                        time = datetime.datetime(year=1970, month=1, day=1, hour=int(str_hour), minute=int(str_minute))
                        return True, time
            time = datetime.datetime(year=1970, month=1, day=1, hour=0, minute=0)
            return False, time
        except ValueError as ve:
            # print(ve)
            time = datetime.datetime(year=1970, month=1, day=1, hour=0, minute=0)
            return False, time

    @staticmethod
    def is_name_plate_valid(name_plate: str):
        if re.match("^[A-Za-z0-9_-]+$", name_plate):
            return True
        else:
            return False

    # other methods
    @staticmethod
    def partition(lst, size):
        list_of_lists = []
        for i in range(0, len(lst), size):
            _list = lst[i: i+size]
            list_of_lists.append(_list)
        return list_of_lists
