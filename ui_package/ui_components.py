import sys

from PySide6 import QtWidgets, QtCore, QtGui
from __feature__ import snake_case, true_property


class FlatFrame(QtWidgets.QFrame):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.frame_shape = QtWidgets.QFrame.NoFrame
        self.frame_shadow = QtWidgets.QFrame.Plain


class FlatGroupBox(QtWidgets.QGroupBox):
    def __init__(self, parent=None, title=''):
        super().__init__(parent)
        self.title = title
        self.flat = True


class CustomTableView(QtWidgets.QTableView):
    def __init__(self, parent=None):
        super().__init__(parent)

class CustomLineEdit(QtWidgets.QLineEdit):
    def __init__(self, parent=None):
        super().__init__(parent)


class CustomComboBox(QtWidgets.QComboBox):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def load_items(self, items:list):
        for item in items:
            self.add_item(item)


class CustomButton(QtWidgets.QPushButton):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)


# class TestWindow(QtWidgets.QMainWindow):
#     def __init__(self):
#         super().__init__()
#         central_widget = QtWidgets.QWidget(self)
#         self.title = 'Testing'
#         self.frame_1 = FlatFrame(central_widget)
#         self.frame_2 = FlatFrame(central_widget)
#         self.frame_1.size_policy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Maximum)
#         self.frame_1.minimum_size = QtCore.QSize(400, 100)
#         self.frame_2.minimum_size = QtCore.QSize(400, 500)
#         self.frame_1.style_sheet = "background-color: rgb(0, 0, 255);"
#         self.frame_2.style_sheet = "background-color: rgb(255, 0, 0);"
#         self.vertical_layout = QtWidgets.QVBoxLayout(central_widget)
#         self.vertical_layout.add_widget(self.frame_1)
#         self.vertical_layout.add_widget(self.frame_2)
#         central_widget.layout = self.vertical_layout
#         print(self.children())
#         self.set_central_widget(central_widget)


# if __name__ == '__main__':
#     app = QtWidgets.QApplication()
#     window = TestWindow()
#     window.show()
#     sys.exit(app.exec())
