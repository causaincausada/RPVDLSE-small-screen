from Code.views.gui import Gui
from Code.props.props import Props
from Code.application_logic.applicationLogic import ApplicationLogic


class RPVDLSE:
    def __init__(self):
        # create Props (Model)
        props = Props()
        # create GUI (View)
        gui = Gui()
        # create ApplicationLogic (Controller)
        app_logic = ApplicationLogic(props, gui)

        # set the controller to view
        gui.set_controller(app_logic)

        # set results
        gui.frame_tab_results.get_results_gui()

        # initialize window
        gui.mainloop()


if __name__=='__main__':
    app = RPVDLSE()
