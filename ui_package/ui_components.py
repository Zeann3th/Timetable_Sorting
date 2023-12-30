import sys
import json

from PySide6 import QtWidgets, QtCore, QtGui
from PySide6.QtWidgets import QDateEdit, QSizePolicy, QHBoxLayout, QFileDialog
from datetime import datetime
from __feature__ import snake_case, true_property

# with open("settings/settings.json") as settings:
#     settings = json.load(settings)
#     theme = settings["theme"]
#
# BG_COLOR = theme["bg-color"]
# BOX_COLOR = theme["box-color"]
# NON_PRIMARY_BUTTON_COLOR = theme["non-primary-button-color"]
# PRIMARY_BUTTON_COLOR = theme["primary-button-color"]
# TEXT_COLOR_DARK_BG = theme["text-color-dark-bg"]
# TEXT_COLOR_LIGHT_BG = theme["text-color-light-bg"]
# FONT_SIZE = theme["font-size"]
# try:
#     TEXT_COLOR_PRIMARY_BUTTON = theme[theme["text-color-primary-button"]]
# except KeyError:
#     TEXT_COLOR_PRIMARY_BUTTON = theme["text-color-primary-button"]
# try:
#     TEXT_COLOR_NON_PRIMARY_BUTTON = theme[theme["text-color-non-primary-button"]]
# except KeyError:
#     TEXT_COLOR_NON_PRIMARY_BUTTON = theme["text-color-non-primary-button"]


class CustomFlatFrame(QtWidgets.QFrame):
    def __init__(self, parent=None, *args, **kwargs):
        super().__init__(parent, *args, **kwargs)
        self.parent = parent
        self.frame_shape = QtWidgets.QFrame.NoFrame
        self.frame_shadow = QtWidgets.QFrame.Plain
        self.set_custom_theme()

    def set_custom_theme(self):
        with open("../settings/settings.json") as settings:
            settings = json.load(settings)
            theme = settings["theme"]

        with open(f"../settings/themes/{theme}.json") as theme_file:
            self.theme = json.load(theme_file)

        font_size = self.theme["font-size"]
        font = QtGui.QFont()
        font.point_size = font_size
        self.font = font


class CustomFlatGroupBox(QtWidgets.QGroupBox):
    def __init__(self, parent=None, title='', *args, **kwargs):
        super().__init__(parent, *args, **kwargs)
        self.parent = parent
        self.title = title
        self.flat = True
        self.set_custom_theme()

    def set_custom_theme(self):
        with open("../settings/settings.json") as settings:
            settings = json.load(settings)
            theme = settings["theme"]

        with open(f"../settings/themes/{theme}.json") as theme_file:
            self.theme = json.load(theme_file)

        font_size = self.theme["font-size"]
        self.font_size = font_size


class CustomTableView(QtWidgets.QTableView):
    def __init__(self, parent=None, *args, **kwargs):
        super().__init__(parent, *args, **kwargs)
        self.parent = parent
        self.theme = None
        self.set_custom_theme()

    def set_custom_theme(self):
        with open("../settings/settings.json") as settings:
            settings = json.load(settings)
            theme = settings["theme"]
        
        with open(f"../settings/themes/{theme}.json") as theme_file:
            self.theme = json.load(theme_file)

        font_size = self.theme["font-size"]
        self.font_size = font_size
        box_color = self.theme["box-color"]
        border_color = self.theme["border-color"]
        border_width = self.theme["border-width"]
        border_style = self.theme["border-style"]
        border_radius = self.theme["border-radius"]
        self.style_sheet = f"""
            QTableView{{
                background-color: {box_color};
                border-top-right-radius: {border_radius};
                border-top-left-radius: {border_radius};
                border: {border_width} {border_style} {border_color};
            }}
            
            QHeaderView, QHeaderView::section{{
                background-color: {border_color};
            }}
            
            QHeaderView{{
                border-top-right-radius: {border_radius};
                border-top-left-radius: {border_radius};
            }}
            
            QHeaderView::section {{
                border-bottom: {border_width} {border_style} {border_color};
                border-right: {border_width} {border_style} {border_color};
            }}
            
            QHeaderView::section::first{{
                border-top-left-radius: {border_radius};
            }}
            
            QHeaderView::section::last{{
                border-top-right-radius: {border_radius};
                border-right: 0px;
            }}
        """

class CustomLineEdit(QtWidgets.QLineEdit):
    def __init__(self, parent=None, *args, **kwargs):
        super().__init__(parent, *args, **kwargs)
        self.theme = None
        self.set_custom_theme()

    def set_custom_theme(self):
        with open("../settings/settings.json") as settings:
            settings = json.load(settings)
            theme = settings["theme"]
            
        with open(f"../settings/themes/{theme}.json") as theme_file:
            self.theme = json.load(theme_file)
            
        box_color = self.theme["box-color"]
        border_color = self.theme["border-color"]
        border_width = self.theme["border-width"]
        border_style = self.theme["border-style"]
        border_radius = self.theme["border-radius"]

        font_size = self.theme["font-size"]

        self.style_sheet = f"""
            QLineEdit{{
                background-color: {box_color};
                border-radius: {border_radius};
                border: {border_width} {border_style} {border_color};
                font-size: {font_size}pt;
                padding: 5px;
            }}
        """


class CustomComboBox(QtWidgets.QComboBox):
    def __init__(self, parent, *args, **kwargs):
        super().__init__(parent, *args, **kwargs)
        self.parent = parent
        self.set_custom_theme()

    def load_items(self, items:list):
        for item in items:
            self.add_item(item)

    def set_custom_theme(self):
        with open("../settings/settings.json") as settings:
            settings = json.load(settings)
            theme = settings["theme"]

        font_size = theme["font-size"]
        border_width = theme["border-width"]
        border_style = theme["border-style"]
        border_color = theme["border-color"]
        border_radius = theme["border-radius"]
        box_color = theme["box-color"]
        text_color = theme["text-color-light-bg"]
        self.style_sheet = f"""
            QComboBox{{
                padding: 5px;
                border-radius: {border_radius};
                background: {box_color};
                border: {border_width} {border_style} {border_color};
                font-size: {font_size}px;
            }}
            
            QComboBox::drop-down {{
                subcontrol-origin: padding;
                subcontrol-position: top right;
                width: 20px;
                border-top-right-radius: {border_radius};
                border-bottom-right-radius: {border_radius};
            }}
            
            QComboBox::down-arrow {{
                image: url("../icons/down-arrow.png)
            }}
            
            QAbstractItemView{{
                border-radius: {border_radius};
                padding: 5px;
                background-color: {box_color};
                color: {text_color};
            }}
            
            QAbstractItemView:item{{
                border: {border_width} {border_style} {border_color};
            }}
            
            QAbstractItemView::item:focused, QAbstractItemView::item:selected{{
                border-radius: 5px;
                padding: 5px;
                color: {text_color};
                border: 0px;
            }}
            
            QAbstractItemView::item:hover{{
                
                background-color: rgb(206, 199, 191);
                color: {text_color};
                border-radius: 3px;
                padding: 5px;
                border: 0px;
            }}
        """


class CustomButton(QtWidgets.QPushButton):
    def __init__(self, parent, is_primary = True, *args, **kwargs):
        super().__init__(parent, *args, **kwargs)
        self.parent = parent
        self.is_primary = is_primary
        self.theme = None
        self.cursor = QtGui.QCursor(QtCore.Qt.PointingHandCursor)
        self.set_custom_theme()

    def set_custom_theme(self):
        with open("../settings/settings.json") as settings:
            settings = json.load(settings)
            theme = settings["theme"]
        with open(f"../settings/themes/{theme}.json") as theme_file:
            self.theme = json.load(theme_file)
        font_size = self.theme["font-size"]
        border_radius = self.theme["border-radius"]
        border_color = self.theme["border-color"]
        border_width = self.theme["border-width"]
        border_style = self.theme["border-style"]
        primary_color = self.theme["primary-button-color"]
        non_primary_color = self.theme["non-primary-button-color"]
        primary_hover = self.theme["primary-button-hover"]
        non_primary_hover = self.theme["non-primary-button-hover"]
        if self.is_primary:
            try:
                text_color = self.theme[self.theme["text-color-primary-button"]]
            except KeyError:
                text_color = self.theme["text-color-primary-button"]
            self.style_sheet = f"""
                QPushButton {{
                    border-radius: {border_radius};
                    border: {border_width} {border_style} {border_color};
                    padding: 5px;
                    background: {primary_color};
                    color: {text_color};
                    font-size: {font_size}pt;
                }}
                
                QPushButton:hover {{
                    background-color: {primary_hover};
                }}
            """
        else:
            try:
                text_color = self.theme[self.theme["text-color-non-primary-button"]]
            except KeyError:
                text_color = self.theme["text-color-non-primary-button"]
            self.style_sheet = f"""
                QPushButton {{
                    border-radius: {border_radius};
                    border: {border_width} {border_style} {border_color};
                    padding: 5px;
                    background: {non_primary_color};
                    color: {text_color};
                    font-size: {font_size}pt;
                }}
                
                QPushButton:hover {{
                    background-color: {non_primary_hover};
                }}
            """


class CustomDateEdit(QDateEdit):
    def __init__(self, parent, *args, **kwargs):
        super().__init__(parent, *args, **kwargs)
        self.parent = parent
        self.theme = None
        self.calendar_popup = True
        self.date = QtCore.QDate(datetime.today().year, datetime.today().month, datetime.today().day)
        self.set_custom_theme()

    def set_custom_theme(self):
        with open("../settings/settings.json") as settings:
            settings = json.load(settings)
            theme = settings["theme"]

        with open(f"../settings/themes/{theme}.json") as theme_file:
            self.theme = json.load(theme_file)

        box_color = self.theme["box-color"]
        border_color = self.theme["border-color"]
        border_width = self.theme["border-width"]
        border_style = self.theme["border-style"]
        border_radius = self.theme["border-radius"]

        font_size = self.theme["font-size"]

        self.style_sheet = f"""
            QDateEdit{{
                padding: 5px;
                border-radius: {border_radius};
                background: {box_color};
                border: {border_width} {border_style} {border_color};
                font-size: {font_size}pt;
            }}
            
            QDateEdit::drop-down{{
                subcontrol-origin: border;
                subcontrol-position: right;
                width: 20px;
                border-top-right-radius: {border_radius};
                border-top-left-radius: {border_radius};
            }}
            
            QDateEdit::down-arrow{{
                image: url("../icons/down-arrow.png");
            }}
        """


class CustomStepProgressBar(QtWidgets.QProgressBar):
    def __init__(self, parent=None, *args, **kwargs):
        super().__init__(parent, *args, **kwargs)
        self.parent = parent
        self.theme = None
        self.format = "Bước %v/%m"
        self.set_custom_theme()

    def set_custom_theme(self):
        with open("../settings/settings.json", "r") as settings_file:
            settings = json.load(settings_file)
            theme = settings["theme"]

        with open(f"../settings/themes/{theme}.json") as theme_file:
            self.theme = json.load(theme_file)

        primary_color = self.theme["primary-button-color"]
        non_primary_color = self.theme["non-primary-button-color"]
        text_color = self.theme["text-color-dark-bg"]
        border_radius = self.theme["border-radius"]
        border_width = self.theme["border-width"]
        border_style = self.theme["border-style"]
        border_color = self.theme["border-color"]
        font_size = self.theme["font-size"]
        self.style_sheet = f"""
            QProgressBar{{
                border: {border_width} {border_style} {border_color};
                border-radius: {border_radius};
                text-align: center;
                background: {non_primary_color};
                color: {text_color};
                font-size: {font_size}pt;
            }}
            QProgressBar::chunk{{
                background: {primary_color};
                border-radius: {border_radius};
            }}
        """

class BodyLabel(QtWidgets.QLabel):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        with open("../settings/settings.json", "r") as settings_file:
            settings = json.load(settings_file)
            theme = settings["theme"]

        with open(f"../settings/themes/{theme}.json") as theme_file:
            self.theme = json.load(theme_file)
        font = QtGui.QFont()
        font.set_point_size(self.theme["font-size"])
        self.font = font


class CustomListView(QtWidgets.QListView):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.set_custom_theme()

    def set_custom_theme(self):
        with open("../settings/settings.json", "r") as settings_file:
            settings = json.load(settings_file)
            theme = settings["theme"]

        with open(f"../settings/themes/{theme}.json") as theme_file:
            self.theme = json.load(theme_file)

        # primary_color = self.theme["primary-button-color"]
        # non_primary_color = self.theme["non-primary-button-color"]
        text_color = self.theme["text-color-dark-bg"]
        border_radius = self.theme["border-radius"]
        border_width = self.theme["border-width"]
        border_style = self.theme["border-style"]
        border_color = self.theme["border-color"]
        font_size = self.theme["font-size"]
        box_color = self.theme["box-color"]
        self.style_sheet = f"""
            QListView{{
                background: {box_color};
                border-radius: {border_radius};
                padding: 5px;
                border: {border_width} {border_style} {border_color};
            }}
        """

class LoadFile(QtWidgets.QWidget):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        with open("../settings/settings.json", "r") as settings_file:
            settings = json.load(settings_file)
            theme = settings["theme"]

        with open(f"../settings/themes/{theme}.json") as theme_file:
            self.theme = json.load(theme_file)

        self.v_layout = QtWidgets.QVBoxLayout(self)

        self.top_frame = CustomFlatFrame(self)
        self.top_frame_layout = QtWidgets.QHBoxLayout(self.top_frame)

        self.select_label = BodyLabel("Chọn file Excel thời khoá biểu", self)
        self.top_frame_layout.add_widget(self.select_label)
        self.chosen_dir = None

        self.top_frame_h_spacer = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.top_frame_layout.add_item(self.top_frame_h_spacer)

        self.choose_file_button = CustomButton(self, is_primary=True, text="Chọn file Excel từ máy tính bạn...")
        self.choose_file_button.clicked.connect(self.select_file)
        choose_file_button_size_policy = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Fixed)
        choose_file_button_size_policy.set_height_for_width(self.choose_file_button.size_policy.has_height_for_width())
        self.choose_file_button.size_policy = choose_file_button_size_policy
        self.top_frame_layout.add_widget(self.choose_file_button)

        self.top_frame.layout = self.top_frame_layout

        self.v_layout.add_widget(self.top_frame)

        self.chosen_dir_label = QtWidgets.QLabel(self)
        self.v_layout.add_widget(self.chosen_dir_label)

        self.preview_table = CustomTableView(self)
        self.v_layout.add_widget(self.preview_table)

        self.layout = self.v_layout

    def select_file(self):
        file_dialog = QtWidgets.QFileDialog()
        file_name = file_dialog.get_open_file_name(self, filter="Excel Files (*.xlsx; *.xls)")
        if file_name:
            self.chosen_dir = f"{file_name[0]}"
            self.chosen_dir_label.text = f"{file_name[0]}"
        file_dialog.fileSelected.connect(self.load_data)

    def load_data(self):
        pass

class SelectSubjectWidget(QtWidgets.QWidget):
    def __init__(self, parent=None, *args, **kwargs):
        super().__init__(parent, *args, **kwargs)
        self.parent = parent

        self.h_layout = QtWidgets.QHBoxLayout(self)

        self.left_frame = CustomFlatFrame(self)
        self.left_frame.object_name = "left_frame"

        self.left_layout = QtWidgets.QVBoxLayout(self.left_frame)
        self.left_layout.add_widget(self.left_frame)

        self.select_subject_group_box = CustomFlatGroupBox(self.left_frame)
        self.select_subject_group_box.object_name = "select_subject_group_box"
        self.select_subject_group_box.title = "Danh sách các lớp học"
        self.left_layout.add_widget(self.select_subject_group_box)

        self.select_subject_layout = QtWidgets.QVBoxLayout(self.select_subject_group_box)
        self.select_subject_layout.object_name = "select_subject_layout"

        self.class_table = CustomTableView(self.select_subject_group_box)
        self.class_table.object_name = "class_table"
        class_table_size_policy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        class_table_size_policy.set_height_for_width(self.class_table.size_policy.has_height_for_width())
        self.class_table.size_policy = class_table_size_policy
        self.select_subject_layout.add_widget(self.class_table)

        self.select_subject_search_frame = CustomFlatFrame(self.select_subject_group_box)
        self.select_subject_search_frame.object_name = "select_subject_search_frame"

        self.select_subject_search_layout = QtWidgets.QFormLayout(self.select_subject_search_frame)
        self.select_subject_search_layout.object_name = "select_subject_search_layout"

        self.select_subject_search_label = BodyLabel("Chọn học phần bạn muốn đăng ký", self.select_subject_search_frame)
        self.select_subject_search_label.object_name = "select_subject_search_label"
        self.select_subject_search_layout.set_widget(0, QtWidgets.QFormLayout.LabelRole, self.select_subject_search_label)

        self.select_subject_search_box = CustomLineEdit(self.select_subject_search_frame)
        self.select_subject_search_box.object_name = "select_subject_search_box"
        self.select_subject_search_box.placeholder_text = "Gõ mã học phần bạn muốn đăng ký"
        self.select_subject_search_layout.set_widget(0, QtWidgets.QFormLayout.FieldRole, self.select_subject_search_box)

        self.select_subject_search_frame.layout = self.select_subject_search_layout

        self.select_subject_layout.add_widget(self.select_subject_search_frame)
        self.select_subject_group_box.layout = self.select_subject_layout
        self.left_frame.layout = self.left_layout
        self.h_layout.add_widget(self.left_frame)

        self.right_frame = CustomFlatGroupBox(self)
        self.right_frame.title = "Danh sách các học phần đã chọn"
        right_frame_size_policy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Preferred)
        self.right_frame.size_policy = right_frame_size_policy

        self.right_layout = QtWidgets.QVBoxLayout(self.right_frame)

        self.selected_subjects_list = CustomListView(self.right_frame)
        self.selected_subjects_list.minimum_size = QtCore.QSize(300, 0)
        self.selected_subjects_list.maximum_size = QtCore.QSize(300, 16777215)
        self.right_layout.add_widget(self.selected_subjects_list)

        self.h_layout.add_widget(self.right_frame)

        self.layout = self.h_layout

    @QtCore.Slot(str)
    def load_data(self):
        pass


class PreviewAndExportWidget(QtWidgets.QWidget):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)


class MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.resize(1100, 800)
        self.window_title = "Sắp xếp thời khoá biểu tự động"

        self.centralwidget = QtWidgets.QWidget()
        self.centralwidget.object_name = "centralwidget"

        self.central_layout = QtWidgets.QVBoxLayout(self.centralwidget)

        self.progress_bar = CustomStepProgressBar(self.centralwidget)
        self.progress_bar.maximum = 3
        self.progress_bar.value = 1
        self.central_layout.add_widget(self.progress_bar)

        ################################################################
        # Như cái tên, đây là một widget xếp chồng
        # với các bước tạo thành từng trang, giống như một cuốn sách
        ################################################################

        self.stacked_widget = QtWidgets.QStackedWidget(self.centralwidget)
        self.stacked_widget.object_name = "stacked_widget"
        self.stacked_widget.minimum_size = QtCore.QSize(1000, 0)

        self.central_layout.add_widget(self.stacked_widget)

        ################################################################
        # Khung chọn file
        ################################################################

        self.load_file_widget = LoadFile(self.centralwidget)
        self.load_file_widget.object_name = "load_file_widget"

        self.stacked_widget.add_widget(self.load_file_widget)

        ################################################################
        # Khung chọn môn học
        ################################################################

        self.select_subjects_widget = SelectSubjectWidget(self.stacked_widget)
        self.select_subjects_widget.object_name = "select_subjects_widget"

        self.stacked_widget.add_widget(self.select_subjects_widget)

        ################################################################
        # Khung xem trước và xuất file
        ################################################################

        self.preview_and_export_widget = PreviewAndExportWidget(self.stacked_widget)
        self.preview_and_export_widget.object_name = "preview_and_export_widget"

        self.stacked_widget.add_widget(self.preview_and_export_widget)

        ################################################################
        # Khung chọn ngày
        ################################################################

        self.date_begin_choose_frame = CustomFlatFrame(self.centralwidget)
        self.date_begin_choose_frame.object_name = "date_begin_choose_frame"
        date_begin_choose_layout = QtWidgets.QFormLayout(self.date_begin_choose_frame)

        self.date_begin_choose_label = BodyLabel("Chọn ngày bắt đầu học kỳ", self.date_begin_choose_frame)
        self.date_begin_choose_label.object_name = "date_begin_choose_label"
        date_begin_choose_layout.set_widget(0, QtWidgets.QFormLayout.LabelRole, self.date_begin_choose_label)


        self.date_begin_choose_date_edit = CustomDateEdit(self.centralwidget)
        self.date_begin_choose_date_edit.object_name = "date_begin_choose_date_edit"
        self.date_selected = None
        date_begin_choose_layout.set_widget(0, QtWidgets.QFormLayout.FieldRole, self.date_begin_choose_date_edit)

        self.date_begin_choose_frame.layout = date_begin_choose_layout
        current_date = datetime.today()

        self.central_layout.add_widget(self.date_begin_choose_frame)

        ###############################################################
        # Khung nút chuyển bước
        ###############################################################

        self.nav_buttons_frame = CustomFlatFrame(self.centralwidget)
        self.nav_buttons_frame.object_name = "nav_buttons_frame"
        nav_buttons_frame_layout = QHBoxLayout(self.nav_buttons_frame)

        h_spacer_1 = QtWidgets.QSpacerItem(40, 20, QSizePolicy.Minimum, QSizePolicy.Minimum)
        nav_buttons_frame_layout.add_item(h_spacer_1)

        self.nav_buttons_previous = CustomButton(self.centralwidget, is_primary=False, text="Trở lại bước trước")
        self.nav_buttons_previous.object_name = "nav_buttons_previous"
        self.nav_buttons_previous.set_enabled(False)
        nav_buttons_frame_layout.add_widget(self.nav_buttons_previous)

        h_spacer_2 = QtWidgets.QSpacerItem(40, 20, QSizePolicy.Minimum, QSizePolicy.Minimum)
        nav_buttons_frame_layout.add_item(h_spacer_2)

        self.nav_buttons_next = CustomButton(self.centralwidget, text="Chuyển sang bước tiếp theo")
        self.nav_buttons_next.object_name = "nav_buttons_next"
        nav_buttons_frame_layout.add_widget(self.nav_buttons_next)

        h_spacer_3 = QtWidgets.QSpacerItem(40, 20, QSizePolicy.Minimum, QSizePolicy.Minimum)
        nav_buttons_frame_layout.add_item(h_spacer_3)

        self.central_layout.add_widget(self.nav_buttons_frame)


        self.centralwidget.layout = self.central_layout
        self.set_central_widget(self.centralwidget)
        self.bind_functions()

    def bind_functions(self):
        self.nav_buttons_previous.clicked.connect(self.previous_step)
        self.nav_buttons_next.clicked.connect(self.next_step)


    def set_progress(self, index):
        self.progress_bar.value = index

    def next_step(self):
        print(self.stacked_widget.current_index)
        if self.stacked_widget.current_index + 1 <= 2:
            self.stacked_widget.current_index = self.stacked_widget.current_index + 1
            self.nav_buttons_previous.set_enabled(True)
        print(self.stacked_widget.current_index)
        if self.stacked_widget.current_index == 2:
            self.nav_buttons_next.set_enabled(False)
        self.set_progress(self.stacked_widget.current_index + 1)

    def previous_step(self):
        print(self.stacked_widget.current_index)
        if self.stacked_widget.current_index - 1 >= 0:
            self.stacked_widget.current_index = self.stacked_widget.current_index - 1
            self.nav_buttons_next.set_enabled(True)
        print(self.stacked_widget.current_index)
        if self.stacked_widget.current_index == 0:
            self.nav_buttons_previous.set_enabled(False)
        self.set_progress(self.stacked_widget.current_index + 1)
