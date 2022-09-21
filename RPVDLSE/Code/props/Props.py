import os
from PIL import Image


MAX_SIZE_INT = (160, 160)
MAX_SIZE_EXT = (215, 150)
INTERNAL = 0
EXTERNAL = 1


class Props():
    def __init__(self):
        path_project = os.path.dirname(__file__)
        self.path_internal = os.path.join(path_project, '../../ImagesSIS')
        self.path_external = os.path.join(path_project, '../../ImagesEXT')

    def get_imgs_internal(self):
        paths_imgs = []
        for x in os.listdir(self.path_internal):
            if x.endswith(".jpg") or x.endswith(".png"): #or x.endswith(".png")#Quitar el png en la version final
                paths_imgs.append(self.path_internal + "/" + x)

        paths_imgs.reverse()
        return paths_imgs

    def get_imgs_external(self):
        paths_imgs = []
        for x in os.listdir(self.path_external):
            if x.endswith(".png") or x.endswith(".jpg") or x.endswith(".jpeg"):
                paths_imgs.append(self.path_external + "/" + x)
        return paths_imgs

    def get_empty(self, int_or_ext):
        path = os.path.dirname(__file__)
        filename = os.path.join(path, '../../media/Empty.png')
        temp_image = Image.open(filename)
        image = temp_image.copy()
        temp_image.close()
        
        if(int_or_ext == INTERNAL):
            image.thumbnail(MAX_SIZE_INT)
        else:
            image = image.resize(MAX_SIZE_EXT)
        
        return image.copy()
