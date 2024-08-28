from logic import *

def main():
    application = QApplication([])
    Calculator = calc_logic()
    Calculator.show()
    application.exec()

if __name__ == '__main__':
    main()