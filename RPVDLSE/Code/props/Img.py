import os
from PIL import Image, ImageTk


MAX_SIZE_INT = (160, 160)
MAX_SIZE_EXT = (215, 150)
INTERNAL = 0
EXTERNAL = 1


class Img():
    def __init__(self, image_path, int_or_ext):
        super().__init__()
        
        self.path_and_name = image_path
        self.path = os.path.dirname(image_path)
        self.name = os.path.basename(image_path)
        self.extension = os.path.splitext(image_path)[1]
        self.size_bytes = os.stat(image_path).st_size
        temp_image = Image.open(image_path)
        self.image = temp_image.copy()
        temp_image.close()
        
        if(int_or_ext == INTERNAL):
            self.image.thumbnail(MAX_SIZE_INT)
        else:
            self.image = self.image.resize(MAX_SIZE_EXT)
        
        self.python_image = ImageTk.PhotoImage(self.image)
        self.height = self.image.height
        self.width = self.image.width

    def open_image(self):
        self.image.show()

    def delete_image(self):
        os.remove(self.path_and_name) #Catch exception

    def rename_image(self, new_name):
        new_file = os.path.join(self.path, new_name + self.extension)
        os.rename(self.path_and_name, new_file) #Catch exception 
        #Check this error in Windows and linux [WinError 32] El proceso no tiene acceso al archivo porque est� siendo utilizado por otro proceso
