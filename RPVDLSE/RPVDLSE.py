from Code.views.Gui import Gui
from Code.props.Props import Props
from Code.application_logic.ApplicationLogic import ApplicationLogic


class RPVDLSE():
    def __init__(self):
        # create Props (Model)
        props = Props()
        # create GUI (View)
        gui = Gui()
        # create ApplicationLogic (Controller)
        appLogic = ApplicationLogic(props, gui)

        # set the controller to view
        gui.set_controller(appLogic)
        
        #initialize window
        gui.mainloop()

if __name__ == '__main__':

    app = RPVDLSE()