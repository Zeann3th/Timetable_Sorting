# Always run the file test_binding first

import sys

from PySide6 import QtWidgets, QtCore, QtGui
from __feature__ import snake_case, true_property
from ui_components import *

if __name__ == '__main__':
    app = QtWidgets.QApplication()
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
