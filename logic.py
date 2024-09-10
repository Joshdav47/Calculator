from PyQt6.QtWidgets import *
from ui_calculator import *
import math
from decimal import Decimal, getcontext

class Calc_Logic(QMainWindow, Ui_UI_Calculator):
    def __init__(self) -> None:
        """
        Method to initialize the Calculator controls
        """
        super().__init__()
        self.setupUi(self)

        # Initialize the LCD display
        self.lcdNumber.setDigitCount(10)  # Set the number of digits to display

        # Initialize values
        self.current_value = ''
        self.previous_value = ''
        self.current_operator = None

        # Sets precision to 10 decimal places
        getcontext().prec = 10

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
        self.square.clicked.connect(self.square_x)
        self.square_root.clicked.connect(self.square_root_x)
        self.divide.clicked.connect(self.division)
        self.one_div_x.clicked.connect(self.div_by_x)
        self.multiply.clicked.connect(self.multiplication)
        self.subtraction.clicked.connect(self.subtract)
        self.addition.clicked.connect(self.add)
        self.enter.clicked.connect(self.display_answer)
        self.positive_negative.clicked.connect(self.integer_conversion)

    def clear_entry_display(self):
        pass

    def delete(self):
        pass

    def percentage_conversion(self):
        pass
    # TODO: Fix both square functions
    def square_x(self):
        self.current_operator = 'square_x'
        if self.current_value:
            result = math.pow(Decimal(self.current_value), 2)
            self.previous_value = str(result)
            return result
        elif self.current_value:
            self.previous_value = self.current_value
            self.current_value = ''
            return None

    def square_root_x(self):
        self.current_operator = 'square_root_x'
        if self.current_value:
            result = Decimal(self.current_value).sqrt()
            self.previous_value = str(result)
            return result
        elif self.current_value:
            self.previous_value = self.current_value
            self.current_value = ''
            return None

    def division(self):
        self.current_operator = 'divide'
        if self.current_value and self.previous_value:
            if self.current_value == '0':
                return "ERROR"
            else:
                result = Decimal(self.previous_value) / Decimal(self.current_value)
                self.previous_value = str(result)
                return result
        elif self.current_value:
            self.previous_value = self.current_value
            self.current_value = ''
            return None

    def div_by_x(self):
        pass

    def multiplication(self):
        self.current_operator = 'multiply'
        if self.current_value and self.previous_value:
            result = Decimal(self.previous_value) * Decimal(self.current_value)
            self.previous_value = str(result)
            return result
        elif self.current_value:
            self.previous_value = self.current_value
            self.current_value = ''
            return None

    def subtract(self):
        self.current_operator = 'subtract'
        if self.current_value and self.previous_value:
            result = Decimal(self.previous_value) - Decimal(self.current_value)
            self.previous_value = str(result)
            return result
        elif self.current_value:
            self.previous_value = self.current_value
            self.current_value = ''
            return None

    def add(self):
            self.current_operator = 'add'
            if self.current_value and self.previous_value:
                    result = Decimal(self.previous_value) + Decimal(self.current_value)
                    self.previous_value = str(result)
                    return result
            elif self.current_value:
                self.previous_value = self.current_value
                self.current_value = ''
                return None

    def display_answer(self):
        result = 0
        if self.current_operator and self.previous_value and self.current_value:
            if self.current_operator == 'add':
                result = self.add()
            elif self.current_operator == 'subtract':
                result = self.subtract()
            elif self.current_operator == 'multiply':
                result = self.multiplication()
            elif self.current_operator == 'divide':
                result = self.division()
            elif self.current_operator == 'square':
                result = self.square_x()
            elif self.current_operator == 'square_root':
                result = self.square_root_x()
            elif self.current_operator == 'div_by_x':
                result = self.div_by_x()
            elif self.current_operator == 'percentage':
                result = self.percentage_conversion()

            self.lcdNumber.display(str(result))
            self.previous_value = str(result)
            self.current_value = ''
            self.current_operator = None

    def integer_conversion(self):
        pass

    def number_pressed(self, number):
        self.current_value += number
        self.lcdNumber.display(self.current_value)

    def decimal_pressed(self):
        if '.' not in self.current_value:
            self.current_value += '.' if self.current_value else '0.'
            self.lcdNumber.display(self.current_value)

    def clear_display(self):
        self.current_value = ''
        self.previous_value = ''
        self.current_operator = None
        self.lcdNumber.display('0')