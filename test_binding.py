import os
import sys
from PySide6 import QtWidgets
from __feature__ import snake_case, true_property
import temporary_test.Timetable_Functions as core_funcs
from ui_package.ui_components import MainWindow


def create_root_dir():
    curr_dir = os.getcwd()
    with open("root_directory.txt", "w+") as file:
        file.write(curr_dir)
    with open("./ui_package/root_directory.txt", "w+") as file:
        file.write(curr_dir)

class FunctionalMainWindow(MainWindow):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def bind_functions(self):
        self.nav_buttons_previous.clicked.connect(self.previous_step)
        self.nav_buttons_next.clicked.connect(self.next_step)

    def set_progress(self, index):
        self.progress_bar.value = index

    def next_step(self):
        # This function is just used for showing mock GUI apps.
        # The actual function for steps is actually more complicated,
        # as it's related to data processing and multithreading stuff
        print(self.stacked_widget.current_index)
        if self.stacked_widget.current_index + 1 <= 2:
            self.stacked_widget.current_index = self.stacked_widget.current_index + 1
            self.nav_buttons_previous.set_enabled(True)
        print(self.stacked_widget.current_index)
        if self.stacked_widget.current_index == 2:
            self.nav_buttons_next.set_enabled(False)
        self.set_progress(self.stacked_widget.current_index + 1)
        self.validate_next_step()

    def previous_step(self):
        # This function is just used for showing mock GUI apps.
        # The actual function for steps is actually more complicated,
        # as it's related to data processing and multithreading stuff
        print(self.stacked_widget.current_index)
        if self.stacked_widget.current_index - 1 >= 0:
            self.stacked_widget.current_index = self.stacked_widget.current_index - 1
            self.nav_buttons_next.set_enabled(True)
        print(self.stacked_widget.current_index)
        if self.stacked_widget.current_index == 0:
            self.nav_buttons_previous.set_enabled(False)
        self.set_progress(self.stacked_widget.current_index + 1)
        self.validate_next_step()

    def validate_next_step(self):
        pass

    def validate_input_data(self):
        pass

if __name__ == '__main__':
    create_root_dir()
    app = QtWidgets.QApplication(sys.argv)
    window = FunctionalMainWindow()
    window.show()
    sys.exit(app.exec())