import os
import threading

import cv2
from PIL import Image, ImageTk


MAX_SIZE = (79, 56)
INTERNAL = 0
EXTERNAL = 1


class Img:
    def __init__(self, image_path, int_or_ext):
        super().__init__()
        self.t_img = None
        try:
            self.path_and_name = image_path
            self.path = os.path.dirname(image_path)
            self.name = os.path.basename(image_path)
            self.extension = os.path.splitext(image_path)[1]
            self.size_bytes = os.stat(image_path).st_size
            temp_image = Image.open(image_path)
            image = temp_image.copy()
            temp_image.close()
        
            image = image.resize(MAX_SIZE)
        
            self.python_image = ImageTk.PhotoImage(image)
            self.height = image.height
            self.width = image.width

        except (OSError, IOError) as e:
            print(e)

    def open_image(self):
        try:
            self.t_img = cv2.imread(self.path_and_name)
            thread = threading.Thread(target=self.thread_showimage)
            thread.start()
            return True
        except cv2.error as e:
            print(e)
            return False

    def thread_showimage(self):
        cv2.imshow(self.name, self.t_img)
        while 1:
            cv2.waitKey()
            if cv2.getWindowProperty(self.name, cv2.WND_PROP_AUTOSIZE) < 1:
                break
        cv2.destroyAllWindows()

    def delete_image(self):
        try:
            os.remove(self.path_and_name)
            return True
        except (OSError, IOError) as e:
            print(e)
            return False

    def rename_image(self, new_name):
        try:
            new_file = os.path.join(self.path, new_name + self.extension)
            os.rename(self.path_and_name, new_file)
            return True
        except (OSError, IOError) as e:
            print(e)
            return False
