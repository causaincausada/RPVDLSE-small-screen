import os
from PIL import Image, ImageTk


MAX_SIZE = (160, 160)


class Img():
    def __init__(self, image_path):
        super().__init__()
        
        self.path_and_name = image_path
        self.path = os.path.dirname(image_path)
        self.name = os.path.basename(image_path)
        self.extension = os.path.splitext(image_path)[1]
        self.size_bytes = os.stat(image_path).st_size
        temp_image = Image.open(image_path)
        self.image = temp_image.copy()
        temp_image.close()
        self.image.thumbnail(MAX_SIZE) 
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
