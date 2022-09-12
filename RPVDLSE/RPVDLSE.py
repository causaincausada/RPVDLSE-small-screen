from Code.views.Gui import Gui


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
    app = RPVDLSE()
