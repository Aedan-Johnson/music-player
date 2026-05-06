from PyQt6 import QtWidgets
import sys

def run_app():
    app = QtWidgets.QApplication(sys.argv)
    window = QtWidgets.QMainWindow()
    window.setWindowTitle("USB Music Player")
    window.resize(800, 600)
    window.show()
    sys.exit(app.exec())
