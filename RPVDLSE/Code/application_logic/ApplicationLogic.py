from Code.props.Props import Props
from Code.props.Img import Img

class ApplicationLogic():
    def __init__(self, props:Props, gui):
        self.props = props
        self.gui = gui

        #image data
        self.imgs = [] #Display images
        self.select_img:Img = None #select image
    
    #Gallery methods
    def select_image(self, img_num: int):
        if(img_num == -1):
            self.select_img = None
        elif(len(self.imgs) >= img_num):
            self.select_img = self.imgs[img_num-1]
        else:
            self.select_img = None

    #Results methods





