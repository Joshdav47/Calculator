from PyQt6.QtWidgets import *
from ui_calculator import *

class calc_logic(QMainWindow, Ui_UI_Calculator):
    def __init__(self) -> None:
        """
        Method to initialize the Calculator controls
        """
        super().__init__()