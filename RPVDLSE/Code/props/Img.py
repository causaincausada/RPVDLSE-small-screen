import os
import cv2
from PIL import Image, ImageTk


MAX_SIZE_INT = (160, 160)
MAX_SIZE_EXT = (215, 150)
INTERNAL = 0
EXTERNAL = 1


class Img():
    def __init__(self, image_path, int_or_ext):
        super().__init__()
        try:
            self.path_and_name = image_path
            self.path = os.path.dirname(image_path)
            self.name = os.path.basename(image_path)
            self.extension = os.path.splitext(image_path)[1]
            self.size_bytes = os.stat(image_path).st_size
            temp_image = Image.open(image_path)
            image = temp_image.copy()
            temp_image.close()
        
            if(int_or_ext == INTERNAL):
                image.thumbnail(MAX_SIZE_INT)
            else:
                image = image.resize(MAX_SIZE_EXT)
        
            self.python_image = ImageTk.PhotoImage(image)
            self.height = image.height
            self.width = image.width

        except (OSError, IOError) as e:
            print(e)

    def open_image(self):
        try:
            t_img = cv2.imread(self.path_and_name)
            cv2.imshow(self.name, t_img)
        except cv2.error as e:
            print(e)
            return False

    def delete_image(self):
        try:
            os.remove(self.path_and_name)
            return True
        except (OSError, IOError) as e:
            print(e)
            return False

    def rename_image(self, new_name):
        new_file = os.path.join(self.path, new_name + self.extension)
        os.rename(self.path_and_name, new_file) #Catch exception 
        #Check this error in Windows and linux [WinError 32] El proceso no tiene acceso al archivo porque est� siendo utilizado por otro proceso
