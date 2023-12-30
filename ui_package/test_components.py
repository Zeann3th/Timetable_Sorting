import sys

from PySide6 import QtWidgets, QtCore, QtGui
from __feature__ import snake_case, true_property
from ui_components import *

# class TestWindow(QtWidgets.QMainWindow):
#     def __init__(self):
#         super().__init__()
#         central_widget = QtWidgets.QWidget(self)
#         self.window_title = 'Testing'
#         self.frame_1 = CustomFlatFrame(central_widget)
#         self.frame_2 = CustomFlatFrame(central_widget)
#         self.frame_1.size_policy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Maximum)
#         self.frame_1.minimum_size = QtCore.QSize(400, 100)
#         self.frame_2.minimum_size = QtCore.QSize(400, 500)
#         self.frame_1.style_sheet = "background-color: rgb(0, 0, 255);"
#         self.frame_2.style_sheet = "background-color: rgb(255, 0, 0);"
#         self.group_box = CustomFlatGroupBox(self.frame_1, "ComboBox1")
#
#         self.vertical_layout = QtWidgets.QVBoxLayout(central_widget)
#         self.vertical_layout.add_widget(self.frame_1)
#         self.vertical_layout.add_widget(self.frame_2)
#         central_widget.layout = self.vertical_layout
#         print(self.children())
#         self.set_central_widget(central_widget)


if __name__ == '__main__':
    app = QtWidgets.QApplication()
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
