import os
from PIL import Image


MAX_SIZE = (79, 56)
INTERNAL = 0
EXTERNAL = 1


class Props:
    def __init__(self):
        try:            
            path_project = os.path.dirname(__file__)
            self.path_internal = os.path.join(path_project, '../../ImagesSIS')
            self.path_external = os.path.join(path_project, '../../ImagesEXT')
            if(not os.path.isdir(self.path_internal)):
                os.makedirs(self.path_internal)
            if(not os.path.isdir(self.path_external)):
                os.makedirs(self.path_external)
        except (OSError, IOError) as e:
            print(e)

    def get_imgs_internal(self):
        paths_imgs = []
        try:
            for x in os.listdir(self.path_internal):
                if x.endswith(".jpg") or x.endswith(".png"):  # or x.endswith(".png")#Quitar el png en la version final
                    paths_imgs.append(self.path_internal + "/" + x)
            paths_imgs.reverse()
        except (OSError, IOError) as e:
            print(e)
        
        return sorted(paths_imgs, key=str.lower, reverse = True)

    def get_imgs_external(self):
        paths_imgs = []
        try:
            for x in os.listdir(self.path_external):
                if x.endswith(".png") or x.endswith(".jpg") or x.endswith(".jpeg"):
                    paths_imgs.append(self.path_external + "/" + x)
        except (OSError, IOError) as e:
            print(e)

        return sorted(paths_imgs, key=str.lower)

    @staticmethod
    def get_empty(int_or_ext):
        try:        
            path = os.path.dirname(__file__)
            filename = os.path.join(path, '../../media/Empty.png')
            temp_image = Image.open(filename)
            image = temp_image.copy()
            temp_image.close()
        
            image = image.resize(MAX_SIZE)
        
            return image.copy()
        except (OSError, IOError) as e:
            print(e)
