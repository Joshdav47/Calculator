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

        # Initialize the current value
        self.current_value = ''

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

        # Other Buttons
        self.decimal.clicked.connect(self.decimal_pressed)
        self.clear.clicked.connect(self.clear_display)

        # TODO: Create the functions for the buttons below:
        self.clear_entry.clicked.connect(self.clear_entry_display)
        self.delete_2.clicked.connect(self.delete)
        self.percentage.clicked.connect(self.percentage_conversion)
        self.square.cliked.connect(self.square_x)
        self.square_root.clicked.connect(self.square_root_x)
        self.divide.clicked.connect(self.division)
        self.one_div_x.connect.clicked(self.div_by_x)
        self.multiply.connect.clicked(self.multiplication)
        self.subtraction.connect.clicked.connect(self.subtract)
        self.addition.connect.clicked.connect(self.add)
        self.enter.connect.clicked.connect(self.display_answer)
        self.positive_negative.connect.clicked.connect(self.interger_conversion)

    def number_pressed(self, number):
        self.current_value += number
        self.lcdNumber.display(self.current_value)

    def decimal_pressed(self):
        if '.' not in self.current_value:
            self.current_value += '.' if self.current_value else '0.'
            self.lcdNumber.display(self.current_value)

    def clear_display(self):
        self.current_value = ''
        self.lcdNumber.display('0')