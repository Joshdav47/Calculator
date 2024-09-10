from logic import *

def main():
    application = QApplication([])
    Calculator = Calc_Logic()
    Calculator.show()
    application.exec()

if __name__ == '__main__':
    main()