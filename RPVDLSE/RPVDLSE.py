from Code.views.Gui import Gui
#from Code.props.Img import Img #quitar


class RPVDLSE():
    def __init__(self):
        # create Props

        # create GUI 
        gui = Gui()

        # create ApplicationLogic
        # e.g. appLogic = ApplicationLogic(props, gui)

        # set the controller to view
        # eg. gui.set_controller(appLogic)
        
        #initialize window
        gui.mainloop()

if __name__ == '__main__':
    ###tests
    #i = Img("C:/Users/carlo/Downloads/hola2.jpg")
    #i.open_image()

    #list_img = [i]


    #print(i.size_bytes)
    #print(i.path)
    #print(i.name)
    #print(i.extension)
    #print(i.height)
    #print(i.width)

    ##i.rename_image("hola2")
    
    #i.delete_image()
    
    app = RPVDLSE()