from PyQt6.QtWidgets import QApplication

from .ui import MainWindow


class PyQtUI:
    def __init__(self):
        self.app = QApplication([])

    def init_gui(self):
        window = MainWindow()
        window.starting_window()
        window.show()

        self.app.exec()
