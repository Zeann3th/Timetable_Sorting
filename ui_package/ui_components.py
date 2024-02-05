# Always run the file test_binding first

import sys
import json

from PySide6 import QtWidgets, QtCore, QtGui
from PySide6.QtWidgets import QDateEdit, QSizePolicy, QHBoxLayout, QFileDialog, QHeaderView
from datetime import datetime
from __feature__ import snake_case, true_property


class CustomFlatFrame(QtWidgets.QFrame):
    def __init__(self, parent=None, *args, **kwargs):
        super().__init__(parent, *args, **kwargs)
        self.parent = parent
        self.frame_shape = QtWidgets.QFrame.NoFrame
        self.frame_shadow = QtWidgets.QFrame.Plain
        self.set_custom_theme()

    def set_custom_theme(self):
        with open("./root_directory.txt", "r+") as file:
            root_directory = file.read()

        settings_dir = f"{root_directory}/settings"

        with open(f"{settings_dir}/settings.json") as settings:
            settings = json.load(settings)
            theme = settings["theme"]

        with open(f"{settings_dir}/themes/{theme}.json") as theme_file:
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
        self.alignment = QtCore.Qt.AlignHCenter

    def set_custom_theme(self):
        with open("./root_directory.txt", "r+") as file:
            root_directory = file.read()

        settings_dir = f"{root_directory}/settings"

        with open(f"{settings_dir}/settings.json") as settings:
            settings = json.load(settings)
            theme = settings["theme"]

        with open(f"{settings_dir}/themes/{theme}.json") as theme_file:
            self.theme = json.load(theme_file)

        font_size = self.theme["font-size"]
        font = QtGui.QFont()
        font.set_point_size(13)
        self.font = font


class CustomTableView(QtWidgets.QTableWidget):
    def __init__(self, parent=None, *args, **kwargs):
        super().__init__(parent, *args, **kwargs)
        self.parent = parent
        self.theme = None
        self.set_custom_theme()
        self.size_adjust_policy = QtWidgets.QAbstractItemView.AdjustToContents
        self.alternating_row_colors = True
        self.selection_behavior = QtWidgets.QAbstractItemView.SelectRows
        self.vertical_scroll_mode = QtWidgets.QAbstractItemView.ScrollPerItem
        self.horizontal_scroll_mode = QtWidgets.QAbstractItemView.ScrollPerPixel
        self.grid_style = QtCore.Qt.SolidLine
        self.sorting_enabled = True
        self.corner_button_enabled = False
        self.auto_scroll = False
        self.horizontal_header().set_visible(True)
        self.horizontal_header().cascading_section_resizes = True
        self.horizontal_header().highlight_sections = True
        self.horizontal_header().show_sort_indicator = True
        self.horizontal_header().stretch_last_section = True
        self.vertical_header().set_visible(False)
        self.vertical_scroll_bar_policy = QtCore.Qt.ScrollBarAlwaysOff
        self.horizontal_scroll_bar_policy = QtCore.Qt.ScrollBarAlwaysOff


    def set_custom_theme(self):
        with open("./root_directory.txt", "r+") as file:
            root_directory = file.read().replace("\\", "/")

        settings_dir = f"{root_directory}/settings"

        with open(f"{settings_dir}/settings.json") as settings:
            settings = json.load(settings)
            theme = settings["theme"]

        with open(f"{settings_dir}/themes/{theme}.json") as theme_file:
            self.theme = json.load(theme_file)

        font_size = self.theme["font-size"]
        box_color = self.theme["box-color"]
        border_color = self.theme["border-color"]
        border_width = self.theme["border-width"]
        border_style = self.theme["border-style"]
        border_radius = self.theme["border-radius"]
        alternate_color = self.theme["alternate-box-color"]
        selection_color = self.theme["box-selection-color"]
        self.style_sheet = f"""
            QTableWidget{{
                background-color: {box_color};
                alternate-background-color: {alternate_color};
                selection-background-color: {selection_color};
                border-radius: {border_radius};
                border: {border_width} {border_style} {border_color};
                font-size: {font_size}pt;
                padding-bottom: 5px;
                gridline-color: transparent;
                text-align: center;
            }}
            
            QHeaderView, QHeaderView::section{{
                background-color: transparent;
            }}
            
            QHeaderView{{
                border-top-right-radius: {border_radius};
                border-top-left-radius: {border_radius};
            }}
            
            QHeaderView::section {{
                border-right: {border_width} {border_style} {border_color};
                border-bottom: {border_width} {border_style} {border_color};
                border-top: 0px;
                border-left: 0px;
            }}
            
            QHeaderView::section::first{{
                border-top-left-radius: {border_radius};
            }}
            
            QHeaderView::section::last{{
                border-top-right-radius: {border_radius};
                border-right: 0px;
            }}
            
            QTableWidget::item::{{
                border-radius: 2px;
            }}
            QTableCornerButton::section {{
                border: 0;
                width: 0;
            }}
            """

    def create_headers(self, header_list: tuple):
        print(header_list)
        self.column_count = len(header_list)
        self.set_horizontal_header_labels(header_list)


class CustomLineEdit(QtWidgets.QLineEdit):
    def __init__(self, parent=None, *args, **kwargs):
        super().__init__(parent, *args, **kwargs)
        self.theme = None
        self.set_custom_theme()

    def set_custom_theme(self, warning = False):
        with open("./root_directory.txt", "r+") as file:
            root_directory = file.read().replace("\\", "/")

        settings_dir = f"{root_directory}/settings"

        with open(f"{settings_dir}/settings.json") as settings:
            settings = json.load(settings)
            theme = settings["theme"]

        with open(f"{settings_dir}/themes/{theme}.json") as theme_file:
            self.theme = json.load(theme_file)
            
        box_color = self.theme["box-color"]
        border_color = self.theme["border-color"]
        border_width = self.theme["border-width"]
        border_style = self.theme["border-style"]
        border_radius = self.theme["border-radius"]

        font_size = self.theme["font-size"]
        if not warning:
            self.style_sheet = f"""
                QLineEdit{{
                    background-color: {box_color};
                    border-radius: {border_radius};
                    border: {border_width} {border_style} {border_color};
                    font-size: {font_size}pt;
                    padding: 5px;
                }}
            """
        else:
            self.style_sheet = f"""
                QLineEdit{{
                    background-color: {box_color};
                    border-radius: {border_radius};
                    border: {border_width} {border_style} red;
                    font-size: {font_size}pt;
                    padding: 5px;
                }}
            """


class CustomComboBox(QtWidgets.QComboBox):
    def __init__(self, parent, *args, **kwargs):
        super().__init__(parent, *args, **kwargs)
        self.parent = parent
        self.theme = None
        self.set_custom_theme()

    def load_items(self, items:list):
        for item in items:
            self.add_item(item)

    def set_custom_theme(self):
        with open("./root_directory.txt", "r+") as file:
            root_directory = file.read().replace("\\", "/")

        settings_dir = f"{root_directory}/settings"
        icons_dir = f"{root_directory}/icons"

        with open(f"{settings_dir}/settings.json") as settings:
            settings = json.load(settings)
            theme = settings["theme"]

        with open(f"{settings_dir}/themes/{theme}.json") as theme_file:
            self.theme = json.load(theme_file)

        font_size = self.theme["font-size"]
        border_width = self.theme["border-width"]
        border_style = self.theme["border-style"]
        border_color = self.theme["border-color"]
        border_radius = self.theme["border-radius"]
        box_color = self.theme["box-color"]
        text_color = self.theme["text-color-light-bg"]
        self.style_sheet = f"""
            QComboBox{{
                padding: 5px;
                border-radius: {border_radius};
                background: {box_color};
                border: {border_width} {border_style} {border_color};
                font-size: {font_size}pt;
            }}
            
            QComboBox::drop-down {{
                subcontrol-origin: padding;
                subcontrol-position: top right;
                width: 20px;
                border-top-right-radius: {border_radius};
                border-bottom-right-radius: {border_radius};
            }}
            
            QComboBox::down-arrow {{
                image: url("{icons_dir}/down-arrow.png")
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
        with open("./root_directory.txt", "r+") as file:
            root_directory = file.read().replace("\\", "/")

        settings_dir = f"{root_directory}/settings"

        with open(f"{settings_dir}/settings.json") as settings:
            settings = json.load(settings)
            theme = settings["theme"]

        with open(f"{settings_dir}/themes/{theme}.json") as theme_file:
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
        with open("./root_directory.txt", "r+") as file:
            root_directory = file.read().replace("\\", "/")

        settings_dir = f"{root_directory}/settings"

        with open(f"{settings_dir}/settings.json") as settings:
            settings = json.load(settings)
            theme = settings["theme"]

        with open(f"{settings_dir}/themes/{theme}.json") as theme_file:
            self.theme = json.load(theme_file)

        icons_dir = f"{root_directory}/icons"

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
                image: url("{icons_dir}/down-arrow.png");
            }}
        """
        print(f""" "{icons_dir}/down-arrow.png" """)


class CustomStepProgressBar(QtWidgets.QProgressBar):
    def __init__(self, parent=None, *args, **kwargs):
        super().__init__(parent, *args, **kwargs)
        self.parent = parent
        self.theme = None
        self.format = "Bước %v/%m"
        self.set_custom_theme()

    def set_custom_theme(self):
        with open("./root_directory.txt", "r+") as file:
            root_directory = file.read()

        settings_dir = f"{root_directory}/settings"

        with open(f"{settings_dir}/settings.json") as settings:
            settings = json.load(settings)
            theme = settings["theme"]

        with open(f"{settings_dir}/themes/{theme}.json") as theme_file:
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
        with open("./root_directory.txt", "r+") as file:
            root_directory = file.read()

        settings_dir = f"{root_directory}/settings"

        with open(f"{settings_dir}/settings.json") as settings:
            settings = json.load(settings)
            theme = settings["theme"]

        with open(f"{settings_dir}/themes/{theme}.json") as theme_file:
            self.theme = json.load(theme_file)
        font = QtGui.QFont()
        font.set_point_size(self.theme["font-size"])
        self.font = font


class WarningLabel(QtWidgets.QLabel):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        with open("./root_directory.txt", "r+") as file:
            root_directory = file.read()

        settings_dir = f"{root_directory}/settings"

        with open(f"{settings_dir}/settings.json") as settings:
            settings = json.load(settings)
            theme = settings["theme"]

        with open(f"{settings_dir}/themes/{theme}.json") as theme_file:
            self.theme = json.load(theme_file)
        font = QtGui.QFont()
        font.set_point_size(self.theme["font-size"] * .8)
        self.font = font
        self.style_sheet = "color: red"

class CustomListView(QtWidgets.QListView):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.set_custom_theme()

    def set_custom_theme(self):
        with open("./root_directory.txt", "r+") as file:
            root_directory = file.read()

        settings_dir = f"{root_directory}/settings"

        with open(f"{settings_dir}/settings.json") as settings:
            settings = json.load(settings)
            theme = settings["theme"]

        with open(f"{settings_dir}/themes/{theme}.json") as theme_file:
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

        with open("./root_directory.txt", "r+") as file:
            root_directory = file.read()

        settings_dir = f"{root_directory}/settings"

        with open(f"{settings_dir}/settings.json") as settings:
            settings = json.load(settings)
            theme = settings["theme"]

        with open(f"{settings_dir}/themes/{theme}.json") as theme_file:
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
        self.preview_table.create_headers(
            ("Mã lớp", "Mã lớp kèm", "Tên môn học", "Mã môn học", "Thời gian", "Phòng học", "Loại lớp"))
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

        ####################################################################
        ## Khung trái, chứa bảng danh sách, khung tìm kiếm và tuỳ chọn giới hạn tín chỉ
        ####################################################################

        self.select_subject_left_frame = CustomFlatFrame(self)
        self.select_subject_left_frame.object_name = "select_subject_left_frame"

        self.left_layout = QtWidgets.QVBoxLayout(self.select_subject_left_frame)
        self.left_layout.add_widget(self.select_subject_left_frame)

        ####################################################################
        ## Bảng chọn mã môn học
        ####################################################################

        self.select_subject_group_box = CustomFlatGroupBox(self.select_subject_left_frame)
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
        # if (self.class_table.column_count < 7):
        #     self.class_table.column_count = 7
        self.class_table.create_headers(("Mã lớp", "Mã lớp kèm", "Tên môn học", "Mã môn học", "Thời gian", "Phòng học", "Loại lớp"))
        self.select_subject_layout.add_widget(self.class_table)

        self.guide_for_table = BodyLabel("Cuộn lên/xuống để xem hết danh sách")
        tmp_font = QtGui.QFont()
        tmp_font.set_point_size(11)
        self.guide_for_table.font = tmp_font
        self.select_subject_layout.add_widget(self.guide_for_table)
        ####################################################################
        ## Khung tìm môn học
        ####################################################################

        self.select_subject_search_frame = CustomFlatFrame(self.select_subject_group_box)
        self.select_subject_search_frame.object_name = "select_subject_search_frame"

        self.select_subject_search_layout = QtWidgets.QHBoxLayout(self.select_subject_search_frame)
        self.select_subject_search_layout.object_name = "select_subject_search_layout"

        self.select_subject_search_label = BodyLabel("Chọn học phần bạn muốn đăng ký", self.select_subject_search_frame)
        self.select_subject_search_label.object_name = "select_subject_search_label"
        self.select_subject_search_layout.add_widget(self.select_subject_search_label)

        select_subject_spacer = QtWidgets.QSpacerItem(40, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)
        self.select_subject_search_layout.add_item(select_subject_spacer)

        self.select_subject_search_box = CustomLineEdit(self.select_subject_search_frame)
        self.select_subject_search_box.object_name = "select_subject_search_box"
        self.select_subject_search_box.placeholder_text = "Gõ mã học phần bạn muốn đăng ký"
        self.select_subject_search_layout.add_widget(self.select_subject_search_box)

        self.select_subject_warning = WarningLabel(self.select_subject_search_frame)
        self.select_subject_warning.object_name = "select_subject_warning"
        self.select_subject_search_layout.add_widget(self.select_subject_warning)

        self.select_subject_search_frame.layout = self.select_subject_search_layout

        self.select_subject_layout.add_widget(self.select_subject_search_frame)
        self.select_subject_group_box.layout = self.select_subject_layout


        ####################################################################
        ## Khung giới hạn tín chỉ
        ####################################################################

        self.credits_limit_group_box = CustomFlatGroupBox(self.select_subject_left_frame)
        self.credits_limit_group_box.object_name = "credits_limit_group_box"
        self.credits_limit_group_box.title = "Giới hạn tín chỉ (theo quy chế đạo tạo 2023)"
        self.credits_limit_group_box.checkable = True
        self.credits_limit_group_box.checked = True

        self.credits_limit_layout = QtWidgets.QFormLayout(self.credits_limit_group_box)

        self.choose_program_label = BodyLabel("Chương trình học", self.credits_limit_group_box)
        self.choose_program_label.object_name = "choose_program_label"

        self.choose_program_combobox = CustomComboBox(self.credits_limit_group_box)
        self.choose_program_combobox.object_name = "choose_program_combobox"
        self.choose_program_combobox.add_item("(None)")
        self.choose_program_combobox.add_item("Chương trình chuẩn")
        self.choose_program_combobox.add_item("Chương trình ELITECH")
        self.choose_program_combobox.add_item("Chung, kì hè")
        self.choose_program_combobox.add_item("Khác/Tuỳ chỉnh")

        self.credits_limit_layout.add_row(self.choose_program_label, self.choose_program_combobox)

        self.lower_bound_label = BodyLabel("Số tín chỉ tối thiểu", self.credits_limit_group_box)
        self.lower_bound_label.object_name = "lower_bound_label"
        self.lower_bound_line_edit = CustomLineEdit(self.credits_limit_group_box)
        self.lower_bound_line_edit.object_name = "lower_bound_line_edit"
        self.lower_bound_line_edit.set_disabled(True)

        self.credits_limit_layout.add_row(self.lower_bound_label, self.lower_bound_line_edit)

        self.upper_bound_label = BodyLabel("Số tín chỉ tối đa", self.credits_limit_group_box)
        self.upper_bound_label.object_name = "upper_bound_label"
        self.upper_bound_line_edit = CustomLineEdit(self.credits_limit_group_box)
        self.upper_bound_line_edit.object_name = "upper_bound_line_edit"
        self.upper_bound_line_edit.set_disabled(True)

        self.credits_limit_layout.add_row(self.upper_bound_label, self.upper_bound_line_edit)

        self.input_warning = BodyLabel("", self.credits_limit_group_box)
        self.input_warning.object_name = "input_warning"
        warning_font = QtGui.QFont()
        warning_font.set_point_size(11)
        self.input_warning.font = warning_font
        self.input_warning.style_sheet = "color: red;"

        self.credits_limit_layout.add_row(None, self.input_warning)


        self.credits_limit_group_box.layout = self.credits_limit_layout
        self.left_layout.add_widget(self.credits_limit_group_box)

        self.select_subject_left_frame.layout = self.left_layout
        self.h_layout.add_widget(self.select_subject_left_frame)

        ####################################################################
        ## Khung phải
        ####################################################################

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

        self.choose_program_combobox.currentTextChanged.connect(self.set_credit_limit)

        self.upper_bound = None
        self.lower_bound = None

    @QtCore.Slot(str)
    def load_data(self):
        pass

    def set_credit_limit(self):
        self.lower_bound_line_edit.clear()
        self.upper_bound_line_edit.clear()
        programs = {
            "Chương trình chuẩn": {
                "lower_bound": 12,
                "upper_bound": 24,
                "non_editable": True
            },
            "Chương trình ELITECH": {
                "lower_bound": 12,
                "upper_bound": 24,
                "non_editable": True
            },
            "Chung, kì hè": {
                "lower_bound": 0,
                "upper_bound": 8,
                "non_editable": True
            },
            "Khác/Tuỳ chỉnh": {
                "lower_bound": 0,
                "upper_bound": 0,
                "non_editable": False
            }
        }
        program = programs[self.choose_program_combobox.current_text]
        self.lower_bound_line_edit.insert(str(program["lower_bound"]))
        self.upper_bound_line_edit.insert(str(program["upper_bound"]))
        self.lower_bound_line_edit.set_disabled(program["non_editable"])
        self.upper_bound_line_edit.set_disabled(program["non_editable"])
        self.lower_bound_line_edit.textEdited.connect(self.check_limit_input)
        self.upper_bound_line_edit.textEdited.connect(self.check_limit_input)

    def check_limit_input(self):
        if self.lower_bound_line_edit.text >= self.upper_bound_line_edit.text:
            self.lower_bound_line_edit.set_custom_theme(warning=True)
            self.upper_bound_line_edit.set_custom_theme(warning=True)
            self.input_warning.text = "Xin vui lòng kiểm tra lại số tín chỉ tối đa và tối thiểu"
        else:
            self.lower_bound_line_edit.set_custom_theme(warning=False)
            self.upper_bound_line_edit.set_custom_theme(warning=False)
            self.input_warning.text = ""
        try:
            self.lower_bound = int(self.lower_bound_line_edit.text)
            self.upper_bound = int(self.upper_bound_line_edit.text)
            print(self.lower_bound, self.upper_bound, sep="\n")
        except ValueError:
            print("Không phải số")

class PreviewAndExportWidget(QtWidgets.QWidget):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        h_layout = QtWidgets.QHBoxLayout(self)

        self.preview_export_left_frame = CustomFlatGroupBox(self)
        self.preview_export_left_frame.title = "Lịch học dự kiến"

        self.preview_export_left_layout = QtWidgets.QVBoxLayout(self.preview_export_left_frame)

        # As the name suggests, this calendar is just a temporary widget for mockup GUI
        # The actual widget can be:
        # - an embedded widget written with QtQuick (via QQuickWidget)
        # - or an embedded webpage with full-blown HTML, CSS and JS (via QWebEngineView)
        self.placeholder_calendar = QtWidgets.QCalendarWidget(self.preview_export_left_frame)
        self.preview_export_left_layout.add_widget(self.placeholder_calendar)

        self.preview_export_left_frame.layout = self.preview_export_left_layout

        h_layout.add_widget(self.preview_export_left_frame)

        self.preview_export_right_frame = CustomFlatFrame(self)

        preview_export_right_layout = QtWidgets.QVBoxLayout(self.preview_export_right_frame)

        self.message_frame = CustomFlatFrame(self.preview_export_right_frame)
        self.message_frame.size_policy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        message_frame_layout = QtWidgets.QVBoxLayout(self.message_frame)

        self.message_label = BodyLabel("Nếu cảm thấy lịch học vừa rồi ưng ý, bạn có thể sử dụng tuỳ chọn xuất file .ics (định dạng iCalendar) để sử dụng trong các ứng dụng lịch khác (Google Calendar hay Outlook, v.v)", self.message_frame)
        self.message_label.object_name = "message_label"
        self.message_label.word_wrap = True
        message_frame_layout.add_widget(self.message_label)

        self.manual_adjust_button = CustomButton(self.message_frame, text="Điều chỉnh lịch học thủ công (Coming soon)...", is_primary=False)
        message_frame_layout.add_widget(self.manual_adjust_button)

        preview_export_right_layout.add_widget(self.message_frame)

        preview_export_v_spacer = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        preview_export_right_layout.add_item(preview_export_v_spacer)

        self.notification_groupbox = CustomFlatGroupBox(self.preview_export_right_frame, title="Bạn muốn nhận thông báo lịch học như thế nào?")
        self.notification_groupbox.size_policy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)

        notification_groupbox_layout = QtWidgets.QVBoxLayout(self.notification_groupbox)

        self.notification_each_period_radio = QtWidgets.QRadioButton("Nhận thông báo cho từng tiết học", self.notification_groupbox)
        notification_groupbox_layout.add_widget(self.notification_each_period_radio)

        self.notification_all_radio = QtWidgets.QRadioButton("Nhận thông báo tổng hợp", self.notification_groupbox)
        notification_groupbox_layout.add_widget(self.notification_all_radio)

        self.export_to_ics_button = CustomButton(self.notification_groupbox, text="Xuất file .ics...")
        notification_groupbox_layout.add_widget(self.export_to_ics_button)

        self.ics_guide = CustomButton(self.notification_groupbox, text="Hướng dẫn sử dụng file .ics cho các ứng dụng lịch...", is_primary=False)
        self.ics_guide.clicked.connect(self.show_ics_guide)
        notification_groupbox_layout.add_widget(self.ics_guide)

        self.notification_groupbox.layout = notification_groupbox_layout

        preview_export_right_layout.add_widget(self.notification_groupbox)

        self.preview_export_right_frame.layout = preview_export_right_layout

        h_layout.add_widget(self.preview_export_right_frame)

        self.layout = h_layout

    def show_ics_guide(self):
        self.ics_guide_box = QtWidgets.QDialog(self)
        self.ics_guide_box.show()


class MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        with open("./root_directory.txt", "r+") as file:
            root_directory = file.read()

        icons_dir = f"{root_directory}/icons"

        self.resize(1100, 800)
        self.window_title = "Sắp xếp thời khoá biểu tự động (cho sinh viên Bách khoa Hà Nội)"
        self.window_icon = QtGui.QIcon(f"{icons_dir}/logo.png")

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
        date_begin_choose_layout = QtWidgets.QHBoxLayout(self.date_begin_choose_frame)

        self.date_begin_choose_label = BodyLabel("Chọn ngày bắt đầu học kỳ", self.date_begin_choose_frame)
        self.date_begin_choose_label.object_name = "date_begin_choose_label"
        date_begin_choose_layout.add_widget(self.date_begin_choose_label)

        date_pick_spacer = QtWidgets.QSpacerItem(20, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)
        date_begin_choose_layout.add_item(date_pick_spacer)


        self.date_begin_choose_date_edit = CustomDateEdit(self.centralwidget)
        self.date_begin_choose_date_edit.object_name = "date_begin_choose_date_edit"
        self.date_selected = None
        date_begin_choose_layout.add_widget(self.date_begin_choose_date_edit)

        self.date_begin_choose_frame.layout = date_begin_choose_layout
        current_date = datetime.today()

        self.central_layout.add_widget(self.date_begin_choose_frame)

        ###############################################################
        # Khung nút chuyển bước
        ###############################################################

        self.nav_buttons_frame = CustomFlatFrame(self.centralwidget)
        self.nav_buttons_frame.object_name = "nav_buttons_frame"
        nav_buttons_frame_layout = QHBoxLayout(self.nav_buttons_frame)

        h_spacer_1 = QtWidgets.QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)
        nav_buttons_frame_layout.add_item(h_spacer_1)

        self.nav_buttons_previous = CustomButton(self.centralwidget, is_primary=False, text="Trở lại bước trước")
        self.nav_buttons_previous.object_name = "nav_buttons_previous"
        self.nav_buttons_previous.minimum_size = QtCore.QSize(300, 0)
        self.nav_buttons_previous.set_enabled(False)
        nav_buttons_frame_layout.add_widget(self.nav_buttons_previous)

        h_spacer_2 = QtWidgets.QSpacerItem(40, 20, QSizePolicy.MinimumExpanding, QSizePolicy.Minimum)
        nav_buttons_frame_layout.add_item(h_spacer_2)

        self.nav_buttons_next = CustomButton(self.centralwidget, text="Chuyển sang bước tiếp theo")
        self.nav_buttons_next.object_name = "nav_buttons_next"
        self.nav_buttons_next.minimum_size = QtCore.QSize(300, 0)
        nav_buttons_frame_layout.add_widget(self.nav_buttons_next)

        h_spacer_3 = QtWidgets.QSpacerItem(20, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)
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
