from logic import Logic
from PyQt6.QtWidgets import QApplication

def main():
    application = QApplication([])
    window = Logic()
    window.show()
    application.exec()

if __name__ == '__main__':
    main()