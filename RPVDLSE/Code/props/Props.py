import os


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
        return paths_imgs

    def get_imgs_external(self):
        paths_imgs = []
        for x in os.listdir(self.path_external):
            if x.endswith(".png") or x.endswith(".jpg") or x.endswith(".jpeg"):
                paths_imgs.append(self.path_external + "/" + x)
        return paths_imgs

