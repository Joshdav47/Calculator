from PyQt6.QtWidgets import *
from ui_calculator import *

class calc_logic(QMainWindow, Ui_UI_Calculator):
    def __init__(self) -> None:
        """
        Method to initialize the Calculator controls
        """
        super().__init__()
        self.setupUi(self)

        # Initialize the LCD display
        self.lcdNumber.setDigitCount(10)  # Set the number of digits to display

        # Connect number buttons
        self.zero.clicked.connect(lambda: self.number_pressed('0'))
        self.one.clicked.connect(lambda: self.number_pressed('1'))
        self.two.clicked.connect(lambda: self.number_pressed('2'))
        self.three.clicked.connect(lambda: self.number_pressed('3'))
        self.four.clicked.connect(lambda: self.number_pressed('4'))
        self.five.clicked.connect(lambda: self.number_pressed('5'))
        self.six.clicked.connect(lambda: self.number_pressed('6'))
        self.seven.clicked.connect(lambda: self.number_pressed('7'))
        self.eight.clicked.connect(lambda: self.number_pressed('8'))
        self.nine.clicked.connect(lambda: self.number_pressed('9'))

        # Initialize the current value
        self.current_value = ''

    def number_pressed(self, number):
        self.current_value += number
        self.lcdNumber.display(self.current_value)