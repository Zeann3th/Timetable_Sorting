# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main.ui'
##
## Created by: Qt User Interface Compiler version 6.6.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

################################################################################
## A/N: Run this file will only show the mock UI, nothing else
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QAbstractItemView, QAbstractScrollArea, QAbstractSpinBox, QApplication,
    QCalendarWidget, QComboBox, QDateEdit, QFormLayout,
    QFrame, QGroupBox, QHBoxLayout, QHeaderView,
    QLabel, QLineEdit, QListView, QMainWindow,
    QMenuBar, QPushButton, QRadioButton, QSizePolicy,
    QSpacerItem, QStackedWidget, QStatusBar, QTableWidget,
    QTableWidgetItem, QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1053, 810)
        MainWindow.setStyleSheet(u"QMainWindow > QWidget {\n"
"	background: #FFFBF5;\n"
"}")
        MainWindow.setUnifiedTitleAndToolBarOnMac(False)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout_9 = QVBoxLayout(self.centralwidget)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.label_7 = QLabel(self.centralwidget)
        self.label_7.setObjectName(u"label_7")
        font = QFont()
        font.setPointSize(16)
        self.label_7.setFont(font)

        self.verticalLayout_9.addWidget(self.label_7)

        self.stackedWidget = QStackedWidget(self.centralwidget)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.stackedWidget.setMinimumSize(QSize(1000, 0))
        self.stackedWidget.setMaximumSize(QSize(16777215, 16777215))
        self.page = QWidget()
        self.page.setObjectName(u"page")
        self.verticalLayout_2 = QVBoxLayout(self.page)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.frame_3 = QFrame(self.page)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setMaximumSize(QSize(16777215, 16777215))
        font1 = QFont()
        font1.setPointSize(13)
        self.frame_3.setFont(font1)
        self.frame_3.setFrameShape(QFrame.NoFrame)
        self.frame_3.setFrameShadow(QFrame.Plain)
        self.verticalLayout_4 = QVBoxLayout(self.frame_3)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.frame_1 = QFrame(self.frame_3)
        self.frame_1.setObjectName(u"frame_1")
        self.frame_1.setFont(font1)
        self.frame_1.setFrameShape(QFrame.NoFrame)
        self.frame_1.setFrameShadow(QFrame.Plain)
        self.horizontalLayout = QHBoxLayout(self.frame_1)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.label = QLabel(self.frame_1)
        self.label.setObjectName(u"label")
        self.label.setFont(font1)

        self.horizontalLayout.addWidget(self.label)

        self.horizontalSpacer = QSpacerItem(20, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.pushButton = QPushButton(self.frame_1)
        self.pushButton.setObjectName(u"pushButton")
        sizePolicy = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton.sizePolicy().hasHeightForWidth())
        self.pushButton.setSizePolicy(sizePolicy)
        self.pushButton.setFont(font1)
        self.pushButton.setCursor(QCursor(Qt.PointingHandCursor))
        self.pushButton.setStyleSheet(u"QPushButton {\n"
"	border-radius: 10px;\n"
"	padding: 5px;\n"
"	background: #7743DB;\n"
"	color: white;\n"
"}")
        icon = QIcon(QIcon.fromTheme(u"document-open"))
        self.pushButton.setIcon(icon)
        self.pushButton.setCheckable(False)
        self.pushButton.setChecked(False)
        self.pushButton.setFlat(True)

        self.horizontalLayout.addWidget(self.pushButton)


        self.verticalLayout_4.addWidget(self.frame_1)

        self.groupBox = QGroupBox(self.frame_3)
        self.groupBox.setObjectName(u"groupBox")
        self.groupBox.setFont(font1)
        self.groupBox.setFlat(True)
        self.groupBox.setCheckable(False)
        self.verticalLayout_3 = QVBoxLayout(self.groupBox)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.tableWidget = QTableWidget(self.groupBox)
        if (self.tableWidget.columnCount() < 7):
            self.tableWidget.setColumnCount(7)
        __qtablewidgetitem = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(4, __qtablewidgetitem4)
        __qtablewidgetitem5 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(5, __qtablewidgetitem5)
        __qtablewidgetitem6 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(6, __qtablewidgetitem6)
        self.tableWidget.setObjectName(u"tableWidget")
        sizePolicy1 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.tableWidget.sizePolicy().hasHeightForWidth())
        self.tableWidget.setSizePolicy(sizePolicy1)
        self.tableWidget.setFont(font1)
        self.tableWidget.setStyleSheet(u"QTableView{\n"
"	background-color: #F7EFE5;\n"
"	border-top-right-radius: 10px;\n"
"	border-top-left-radius: 10px;\n"
"	border: 1px solid black;\n"
"}\n"
"\n"
"QHeaderView, QHeaderView::section{\n"
"	background-color: #F7EFE5;\n"
"}\n"
"\n"
"QHeaderView{\n"
"	border-top-right-radius: 10px;\n"
"	border-top-left-radius: 10px;\n"
"}\n"
"\n"
"QHeaderView::section {\n"
"	border-bottom: 1px solid black;\n"
"	border-right: 1px solid black;\n"
"}\n"
"\n"
"QHeaderView::section::first{\n"
"	border-top-left-radius: 10px;\n"
"}\n"
"\n"
"QHeaderView::section::last{\n"
"	border-top-right-radius: 10px;\n"
"	border-right: 0px;\n"
"}\n"
"\n"
"QScrollArea{\n"
"	border-radius: 10px;\n"
"}")
        self.tableWidget.setFrameShape(QFrame.NoFrame)
        self.tableWidget.setFrameShadow(QFrame.Plain)
        self.tableWidget.setSizeAdjustPolicy(QAbstractScrollArea.AdjustToContents)
        self.tableWidget.setAutoScroll(True)
        self.tableWidget.setAlternatingRowColors(True)
        self.tableWidget.setGridStyle(Qt.SolidLine)
        self.tableWidget.setSortingEnabled(True)
        self.tableWidget.horizontalHeader().setCascadingSectionResizes(True)
        self.tableWidget.horizontalHeader().setHighlightSections(True)
        self.tableWidget.horizontalHeader().setProperty("showSortIndicator", True)
        self.tableWidget.horizontalHeader().setStretchLastSection(True)
        self.tableWidget.verticalHeader().setCascadingSectionResizes(False)

        self.verticalLayout_3.addWidget(self.tableWidget)


        self.verticalLayout_4.addWidget(self.groupBox)


        self.verticalLayout_2.addWidget(self.frame_3)

        self.stackedWidget.addWidget(self.page)
        self.page_2 = QWidget()
        self.page_2.setObjectName(u"page_2")
        self.horizontalLayout_3 = QHBoxLayout(self.page_2)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.frame_5 = QFrame(self.page_2)
        self.frame_5.setObjectName(u"frame_5")
        self.frame_5.setFrameShape(QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QFrame.Raised)
        self.verticalLayout_6 = QVBoxLayout(self.frame_5)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.frame_6 = QFrame(self.frame_5)
        self.frame_6.setObjectName(u"frame_6")
        self.frame_6.setFrameShape(QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QFrame.Raised)
        self.verticalLayout_8 = QVBoxLayout(self.frame_6)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.groupBox_4 = QGroupBox(self.frame_6)
        self.groupBox_4.setObjectName(u"groupBox_4")
        self.groupBox_4.setFont(font1)
        self.groupBox_4.setFlat(True)
        self.groupBox_4.setCheckable(False)
        self.verticalLayout_7 = QVBoxLayout(self.groupBox_4)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.tableWidget_2 = QTableWidget(self.groupBox_4)
        if (self.tableWidget_2.columnCount() < 6):
            self.tableWidget_2.setColumnCount(6)
        __qtablewidgetitem7 = QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(0, __qtablewidgetitem7)
        __qtablewidgetitem8 = QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(1, __qtablewidgetitem8)
        __qtablewidgetitem9 = QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(2, __qtablewidgetitem9)
        __qtablewidgetitem10 = QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(3, __qtablewidgetitem10)
        __qtablewidgetitem11 = QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(4, __qtablewidgetitem11)
        __qtablewidgetitem12 = QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(5, __qtablewidgetitem12)
        self.tableWidget_2.setObjectName(u"tableWidget_2")
        sizePolicy2 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.tableWidget_2.sizePolicy().hasHeightForWidth())
        self.tableWidget_2.setSizePolicy(sizePolicy2)
        self.tableWidget_2.setFont(font1)
        self.tableWidget_2.setStyleSheet(u"QTableView{\n"
"	background-color: #F7EFE5;\n"
"	border-top-left-radius: 10px;\n"
"	border-top-right-radius: 10px;\n"
"	border: 1px solid black;\n"
"}\n"
"\n"
"QHeaderView, QHeaderView::section{\n"
"	background-color: #F7EFE5;\n"
"}\n"
"\n"
"QHeaderView{\n"
"	border-top-right-radius: 10px;\n"
"	border-top-left-radius: 10px;\n"
"}\n"
"\n"
"QHeaderView::section {\n"
"	border-bottom: 1px solid black;\n"
"	border-right: 1px solid black;\n"
"}\n"
"\n"
"QHeaderView::section::first{\n"
"	border-top-left-radius: 10px;\n"
"}\n"
"\n"
"QHeaderView::section::last{\n"
"	border-top-right-radius: 10px;\n"
"	border-right: 0px;\n"
"}\n"
"\n"
"QScrollArea{\n"
"	border-radius: 10px;\n"
"}")
        self.tableWidget_2.setFrameShape(QFrame.NoFrame)
        self.tableWidget_2.setFrameShadow(QFrame.Plain)
        self.tableWidget_2.setSizeAdjustPolicy(QAbstractScrollArea.AdjustToContents)
        self.tableWidget_2.setAutoScroll(False)
        self.tableWidget_2.setAlternatingRowColors(True)
        self.tableWidget_2.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.tableWidget_2.setVerticalScrollMode(QAbstractItemView.ScrollPerItem)
        self.tableWidget_2.setHorizontalScrollMode(QAbstractItemView.ScrollPerPixel)
        self.tableWidget_2.setGridStyle(Qt.SolidLine)
        self.tableWidget_2.setSortingEnabled(True)
        self.tableWidget_2.setCornerButtonEnabled(False)
        self.tableWidget_2.horizontalHeader().setVisible(True)
        self.tableWidget_2.horizontalHeader().setCascadingSectionResizes(True)
        self.tableWidget_2.horizontalHeader().setHighlightSections(True)
        self.tableWidget_2.horizontalHeader().setProperty("showSortIndicator", True)
        self.tableWidget_2.horizontalHeader().setStretchLastSection(True)

        self.verticalLayout_7.addWidget(self.tableWidget_2)

        self.frame = QFrame(self.groupBox_4)
        self.frame.setObjectName(u"frame")
        sizePolicy3 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.frame.sizePolicy().hasHeightForWidth())
        self.frame.setSizePolicy(sizePolicy3)
        self.frame.setFont(font1)
        self.formLayout = QFormLayout(self.frame)
        self.formLayout.setObjectName(u"formLayout")
        self.label_2 = QLabel(self.frame)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setFont(font1)

        self.formLayout.setWidget(1, QFormLayout.LabelRole, self.label_2)

        self.pushButton_3 = QPushButton(self.frame)
        self.pushButton_3.setObjectName(u"pushButton_3")
        sizePolicy.setHeightForWidth(self.pushButton_3.sizePolicy().hasHeightForWidth())
        self.pushButton_3.setSizePolicy(sizePolicy)
        self.pushButton_3.setFont(font1)
        self.pushButton_3.setCursor(QCursor(Qt.PointingHandCursor))
        self.pushButton_3.setStyleSheet(u"QPushButton {\n"
"	border-radius: 10px;\n"
"	padding: 5px;\n"
"	background: #7743DB;\n"
"	color: white;\n"
"}")
        self.pushButton_3.setIcon(icon)
        self.pushButton_3.setCheckable(False)
        self.pushButton_3.setChecked(False)
        self.pushButton_3.setFlat(True)

        self.formLayout.setWidget(2, QFormLayout.FieldRole, self.pushButton_3)

        self.lineEdit_3 = QLineEdit(self.frame)
        self.lineEdit_3.setObjectName(u"lineEdit_3")
        self.lineEdit_3.setFont(font1)
        self.lineEdit_3.setStyleSheet(u"QLineEdit{\n"
"	background: #F7EFE5;\n"
"	border-radius: 10px;\n"
"	padding: 5px;\n"
"	border: 1px solid black;\n"
"}\n"
"")
        self.lineEdit_3.setReadOnly(True)

        self.formLayout.setWidget(1, QFormLayout.FieldRole, self.lineEdit_3)


        self.verticalLayout_7.addWidget(self.frame)


        self.verticalLayout_8.addWidget(self.groupBox_4)


        self.verticalLayout_6.addWidget(self.frame_6)

        self.groupBox_3 = QGroupBox(self.frame_5)
        self.groupBox_3.setObjectName(u"groupBox_3")
        self.groupBox_3.setFont(font1)
        self.groupBox_3.setFlat(True)
        self.groupBox_3.setCheckable(True)
        self.formLayout_2 = QFormLayout(self.groupBox_3)
        self.formLayout_2.setObjectName(u"formLayout_2")
        self.label_4 = QLabel(self.groupBox_3)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setFont(font1)

        self.formLayout_2.setWidget(0, QFormLayout.LabelRole, self.label_4)

        self.comboBox_2 = QComboBox(self.groupBox_3)
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.setObjectName(u"comboBox_2")
        self.comboBox_2.setFont(font1)
        self.comboBox_2.setStyleSheet(u"QComboBox{\n"
"	padding: 5px;\n"
"	border-radius: 10px;\n"
"	background: #F7EFE5;\n"
"	border: 1px solid black;\n"
"}\n"
"\n"
"QComboBox::drop-down {\n"
"	subcontrol-origin: padding;\n"
"	subcontrol-position: top right;\n"
"	width: 20px;\n"
"	border-top-right-radius: 10px;\n"
"	border-bottom-right-radius: 10px;\n"
"}\n"
"\n"
"QComboBox::down-arrow {\n"
"	image: url(\"C:/Users/quang_mkkjeym/PycharmProjects/\\Timetable_Sorting/icons/down-arrow.png\")\n"
"}\n"
"\n"
"QAbstractItemView{\n"
"	border-radius: 15px;\n"
"	padding: 5px;\n"
"	background-color: #F7EFE5;\n"
"	color: black;\n"
"}\n"
"\n"
"QAbstractItemView:item{\n"
"	border: 1px solid black;\n"
"}\n"
"\n"
"QAbstractItemView::item:focused, QAbstractItemView::item:selected{\n"
"	border-radius: 5px;\n"
"	padding: 5px;\n"
"	color: black;\n"
"	border: 0px;\n"
"}\n"
"\n"
"QAbstractItemView::item:hover{\n"
"	\n"
"	background-color: rgb(206, 199, 191);\n"
"	color: black;\n"
"	border-radius: 3px;\n"
"	padding: 5px;\n"
"	border: 0px;\n"
"}")
        self.comboBox_2.setEditable(False)

        self.formLayout_2.setWidget(0, QFormLayout.FieldRole, self.comboBox_2)

        self.label_5 = QLabel(self.groupBox_3)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setFont(font1)

        self.formLayout_2.setWidget(1, QFormLayout.LabelRole, self.label_5)

        self.lineEdit = QLineEdit(self.groupBox_3)
        self.lineEdit.setObjectName(u"lineEdit")
        self.lineEdit.setFont(font1)
        self.lineEdit.setStyleSheet(u"QLineEdit{\n"
"	background: #F7EFE5;\n"
"	border-radius: 10px;\n"
"	padding: 5px;\n"
"	border: 1px solid black;\n"
"}\n"
"")
        self.lineEdit.setReadOnly(True)

        self.formLayout_2.setWidget(1, QFormLayout.FieldRole, self.lineEdit)

        self.label_6 = QLabel(self.groupBox_3)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setFont(font1)

        self.formLayout_2.setWidget(2, QFormLayout.LabelRole, self.label_6)

        self.lineEdit_2 = QLineEdit(self.groupBox_3)
        self.lineEdit_2.setObjectName(u"lineEdit_2")
        self.lineEdit_2.setFont(font1)
        self.lineEdit_2.setStyleSheet(u"QLineEdit{\n"
"	background: #F7EFE5;\n"
"	border-radius: 10px;\n"
"	padding: 5px;\n"
"	border: 1px solid black;\n"
"}\n"
"")
        self.lineEdit_2.setReadOnly(True)

        self.formLayout_2.setWidget(2, QFormLayout.FieldRole, self.lineEdit_2)


        self.verticalLayout_6.addWidget(self.groupBox_3)


        self.horizontalLayout_3.addWidget(self.frame_5)

        self.groupBox_2 = QGroupBox(self.page_2)
        self.groupBox_2.setObjectName(u"groupBox_2")
        sizePolicy4 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Preferred)
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(self.groupBox_2.sizePolicy().hasHeightForWidth())
        self.groupBox_2.setSizePolicy(sizePolicy4)
        self.groupBox_2.setFont(font1)
        self.groupBox_2.setFlat(True)
        self.verticalLayout_5 = QVBoxLayout(self.groupBox_2)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.chosen_subjects = QListView(self.groupBox_2)
        self.chosen_subjects.setObjectName(u"chosen_subjects")
        self.chosen_subjects.setMinimumSize(QSize(300, 0))
        self.chosen_subjects.setMaximumSize(QSize(300, 16777215))
        self.chosen_subjects.setFont(font1)
        self.chosen_subjects.setStyleSheet(u"QListView{\n"
"	background-color: #F7EFE5;\n"
"	border-radius: 10px;\n"
"	border: 1px solid black;\n"
"}")
        self.chosen_subjects.setFrameShape(QFrame.NoFrame)
        self.chosen_subjects.setFrameShadow(QFrame.Plain)

        self.verticalLayout_5.addWidget(self.chosen_subjects)


        self.horizontalLayout_3.addWidget(self.groupBox_2)

        self.stackedWidget.addWidget(self.page_2)
        self.page_3 = QWidget()
        self.page_3.setObjectName(u"page_3")
        self.horizontalLayout_4 = QHBoxLayout(self.page_3)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.frame_4 = QFrame(self.page_3)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setMaximumSize(QSize(450, 16777215))
        self.frame_4.setFont(font1)
        self.frame_4.setMouseTracking(True)
        self.frame_4.setTabletTracking(True)
        self.frame_4.setFrameShape(QFrame.NoFrame)
        self.frame_4.setFrameShadow(QFrame.Plain)
        self.verticalLayout = QVBoxLayout(self.frame_4)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.frame_2 = QFrame(self.frame_4)
        self.frame_2.setObjectName(u"frame_2")
        sizePolicy3.setHeightForWidth(self.frame_2.sizePolicy().hasHeightForWidth())
        self.frame_2.setSizePolicy(sizePolicy3)
        self.frame_2.setFont(font1)
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.formLayout_4 = QFormLayout(self.frame_2)
        self.formLayout_4.setObjectName(u"formLayout_4")
        self.label_3 = QLabel(self.frame_2)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setFont(font1)

        self.formLayout_4.setWidget(0, QFormLayout.LabelRole, self.label_3)

        self.dateEdit = QDateEdit(self.frame_2)
        self.dateEdit.setObjectName(u"dateEdit")
        self.dateEdit.setFont(font1)
        self.dateEdit.setStyleSheet(u"QDateEdit{\n"
"	padding: 5px;\n"
"	border-radius: 10px;\n"
"	background: #F7EFE5;\n"
"	border: 1px solid black;\n"
"}\n"
"\n"
"QDateEdit::drop-down{\n"
"	subcontrol-origin: border;\n"
"    subcontrol-position: right;\n"
"	width: 20px;\n"
"	border-top-right-radius: 10px;\n"
"	border-top-left-radius: 10px;\n"
"}\n"
"\n"
"QDateEdit::down-arrow{\n"
"	image: url(\"C:/Users/quang_mkkjeym/PycharmProjects/\\Timetable_Sorting/icons/down-arrow.png\");\n"
"}")
        self.dateEdit.setReadOnly(False)
        self.dateEdit.setButtonSymbols(QAbstractSpinBox.UpDownArrows)
        self.dateEdit.setAccelerated(False)
        self.dateEdit.setProperty("showGroupSeparator", True)
        self.dateEdit.setCalendarPopup(True)

        self.formLayout_4.setWidget(0, QFormLayout.FieldRole, self.dateEdit)


        self.verticalLayout.addWidget(self.frame_2)


        self.horizontalLayout_4.addWidget(self.frame_4)

        self.groupBox_9 = QGroupBox(self.page_3)
        self.groupBox_9.setObjectName(u"groupBox_9")
        sizePolicy4.setHeightForWidth(self.groupBox_9.sizePolicy().hasHeightForWidth())
        self.groupBox_9.setSizePolicy(sizePolicy4)
        self.groupBox_9.setFont(font1)
        self.groupBox_9.setFlat(True)
        self.verticalLayout_18 = QVBoxLayout(self.groupBox_9)
        self.verticalLayout_18.setObjectName(u"verticalLayout_18")
        self.chosen_subjects_4 = QListView(self.groupBox_9)
        self.chosen_subjects_4.setObjectName(u"chosen_subjects_4")
        self.chosen_subjects_4.setMinimumSize(QSize(300, 0))
        self.chosen_subjects_4.setMaximumSize(QSize(300, 16777215))
        self.chosen_subjects_4.setFont(font1)
        self.chosen_subjects_4.setStyleSheet(u"QListView{\n"
"	background-color: #F7EFE5;\n"
"	border-radius: 10px;\n"
"	border: 1px solid black;\n"
"}")
        self.chosen_subjects_4.setFrameShape(QFrame.NoFrame)
        self.chosen_subjects_4.setFrameShadow(QFrame.Plain)

        self.verticalLayout_18.addWidget(self.chosen_subjects_4)


        self.horizontalLayout_4.addWidget(self.groupBox_9)

        self.stackedWidget.addWidget(self.page_3)
        self.page_4 = QWidget()
        self.page_4.setObjectName(u"page_4")
        self.horizontalLayout_5 = QHBoxLayout(self.page_4)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.calendarWidget = QCalendarWidget(self.page_4)
        self.calendarWidget.setObjectName(u"calendarWidget")

        self.horizontalLayout_5.addWidget(self.calendarWidget)

        self.frame_8 = QFrame(self.page_4)
        self.frame_8.setObjectName(u"frame_8")
        self.frame_8.setMinimumSize(QSize(50, 0))
        self.frame_8.setFrameShape(QFrame.NoFrame)
        self.frame_8.setFrameShadow(QFrame.Plain)
        self.verticalLayout_10 = QVBoxLayout(self.frame_8)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.frame_9 = QFrame(self.frame_8)
        self.frame_9.setObjectName(u"frame_9")
        self.frame_9.setFrameShape(QFrame.StyledPanel)
        self.frame_9.setFrameShadow(QFrame.Raised)
        self.verticalLayout_12 = QVBoxLayout(self.frame_9)
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.label_8 = QLabel(self.frame_9)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setFont(font1)
        self.label_8.setWordWrap(True)

        self.verticalLayout_12.addWidget(self.label_8)

        self.pushButton_7 = QPushButton(self.frame_9)
        self.pushButton_7.setObjectName(u"pushButton_7")
        sizePolicy5 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        sizePolicy5.setHorizontalStretch(0)
        sizePolicy5.setVerticalStretch(0)
        sizePolicy5.setHeightForWidth(self.pushButton_7.sizePolicy().hasHeightForWidth())
        self.pushButton_7.setSizePolicy(sizePolicy5)
        self.pushButton_7.setFont(font1)
        self.pushButton_7.setStyleSheet(u"QPushButton {\n"
"	border-radius: 10px;\n"
"	padding: 5px;\n"
"	background: #C3ACD0;\n"
"	color: white;\n"
"}")

        self.verticalLayout_12.addWidget(self.pushButton_7)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Minimum)

        self.verticalLayout_12.addItem(self.verticalSpacer)


        self.verticalLayout_10.addWidget(self.frame_9)

        self.groupBox_5 = QGroupBox(self.frame_8)
        self.groupBox_5.setObjectName(u"groupBox_5")
        sizePolicy3.setHeightForWidth(self.groupBox_5.sizePolicy().hasHeightForWidth())
        self.groupBox_5.setSizePolicy(sizePolicy3)
        self.groupBox_5.setFont(font1)
        self.groupBox_5.setFlat(True)
        self.verticalLayout_11 = QVBoxLayout(self.groupBox_5)
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.radioButton_2 = QRadioButton(self.groupBox_5)
        self.radioButton_2.setObjectName(u"radioButton_2")
        self.radioButton_2.setFont(font1)

        self.verticalLayout_11.addWidget(self.radioButton_2)

        self.radioButton = QRadioButton(self.groupBox_5)
        self.radioButton.setObjectName(u"radioButton")
        self.radioButton.setFont(font1)

        self.verticalLayout_11.addWidget(self.radioButton)

        self.pushButton_2 = QPushButton(self.groupBox_5)
        self.pushButton_2.setObjectName(u"pushButton_2")
        sizePolicy5.setHeightForWidth(self.pushButton_2.sizePolicy().hasHeightForWidth())
        self.pushButton_2.setSizePolicy(sizePolicy5)
        self.pushButton_2.setFont(font1)
        self.pushButton_2.setStyleSheet(u"QPushButton {\n"
"	border-radius: 10px;\n"
"	padding: 5px;\n"
"	background: #7743DB;\n"
"	color: white;\n"
"}")

        self.verticalLayout_11.addWidget(self.pushButton_2)

        self.pushButton_6 = QPushButton(self.groupBox_5)
        self.pushButton_6.setObjectName(u"pushButton_6")
        sizePolicy5.setHeightForWidth(self.pushButton_6.sizePolicy().hasHeightForWidth())
        self.pushButton_6.setSizePolicy(sizePolicy5)
        self.pushButton_6.setFont(font1)
        self.pushButton_6.setStyleSheet(u"QPushButton {\n"
"	border-radius: 10px;\n"
"	padding: 5px;\n"
"	background: #C3ACD0;\n"
"	color: white;\n"
"}")

        self.verticalLayout_11.addWidget(self.pushButton_6)


        self.verticalLayout_10.addWidget(self.groupBox_5)


        self.horizontalLayout_5.addWidget(self.frame_8)

        self.stackedWidget.addWidget(self.page_4)

        self.verticalLayout_9.addWidget(self.stackedWidget)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Minimum)

        self.verticalLayout_9.addItem(self.verticalSpacer_2)

        self.frame_7 = QFrame(self.centralwidget)
        self.frame_7.setObjectName(u"frame_7")
        self.frame_7.setFont(font1)
        self.frame_7.setStyleSheet(u"QPushButton {\n"
"	border-radius: 10px;\n"
"	padding: 5px;\n"
"	background: #C3ACD0;\n"
"	color: white;\n"
"}")
        self.frame_7.setFrameShape(QFrame.StyledPanel)
        self.frame_7.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.frame_7)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Minimum, QSizePolicy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_3)

        self.pushButton_5 = QPushButton(self.frame_7)
        self.pushButton_5.setObjectName(u"pushButton_5")
        sizePolicy.setHeightForWidth(self.pushButton_5.sizePolicy().hasHeightForWidth())
        self.pushButton_5.setSizePolicy(sizePolicy)
        self.pushButton_5.setFont(font1)

        self.horizontalLayout_2.addWidget(self.pushButton_5)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Minimum, QSizePolicy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_2)

        self.pushButton_4 = QPushButton(self.frame_7)
        self.pushButton_4.setObjectName(u"pushButton_4")
        sizePolicy.setHeightForWidth(self.pushButton_4.sizePolicy().hasHeightForWidth())
        self.pushButton_4.setSizePolicy(sizePolicy)
        self.pushButton_4.setFont(font1)
        self.pushButton_4.setStyleSheet(u"QPushButton {\n"
"	border-radius: 10px;\n"
"	padding: 5px;\n"
"	background: #7743DB;\n"
"	color: white;\n"
"}")

        self.horizontalLayout_2.addWidget(self.pushButton_4)

        self.horizontalSpacer_4 = QSpacerItem(40, 20, QSizePolicy.Minimum, QSizePolicy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_4)


        self.verticalLayout_9.addWidget(self.frame_7)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 1053, 22))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        self.stackedWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"[Step]", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Ch\u1ecdn file Excel th\u1eddi kho\u00e1 bi\u1ec3u", None))
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"Ch\u1ecdn file...", None))
        self.groupBox.setTitle(QCoreApplication.translate("MainWindow", u"Danh s\u00e1ch l\u1edbp h\u1ecdc", None))
        ___qtablewidgetitem = self.tableWidget.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("MainWindow", u"M\u00e3 l\u1edbp", None));
        ___qtablewidgetitem1 = self.tableWidget.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("MainWindow", u"M\u00e3 l\u1edbp k\u00e8m", None));
        ___qtablewidgetitem2 = self.tableWidget.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("MainWindow", u"T\u00ean m\u00f4n h\u1ecdc", None));
        ___qtablewidgetitem3 = self.tableWidget.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("MainWindow", u"M\u00e3 m\u00f4n h\u1ecdc", None));
        ___qtablewidgetitem4 = self.tableWidget.horizontalHeaderItem(4)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("MainWindow", u"Th\u1eddi gian", None));
        ___qtablewidgetitem5 = self.tableWidget.horizontalHeaderItem(5)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("MainWindow", u"Ph\u00f2ng h\u1ecdc", None));
        ___qtablewidgetitem6 = self.tableWidget.horizontalHeaderItem(6)
        ___qtablewidgetitem6.setText(QCoreApplication.translate("MainWindow", u"Lo\u1ea1i l\u1edbp", None));
        self.groupBox_4.setTitle(QCoreApplication.translate("MainWindow", u"Danh s\u00e1ch c\u00e1c l\u1edbp h\u1ecdc", None))
        ___qtablewidgetitem7 = self.tableWidget_2.horizontalHeaderItem(0)
        ___qtablewidgetitem7.setText(QCoreApplication.translate("MainWindow", u"M\u00e3 l\u1edbp", None));
        ___qtablewidgetitem8 = self.tableWidget_2.horizontalHeaderItem(1)
        ___qtablewidgetitem8.setText(QCoreApplication.translate("MainWindow", u"T\u00ean m\u00f4n h\u1ecdc", None));
        ___qtablewidgetitem9 = self.tableWidget_2.horizontalHeaderItem(2)
        ___qtablewidgetitem9.setText(QCoreApplication.translate("MainWindow", u"M\u00e3 m\u00f4n h\u1ecdc", None));
        ___qtablewidgetitem10 = self.tableWidget_2.horizontalHeaderItem(3)
        ___qtablewidgetitem10.setText(QCoreApplication.translate("MainWindow", u"Th\u1eddi gian", None));
        ___qtablewidgetitem11 = self.tableWidget_2.horizontalHeaderItem(4)
        ___qtablewidgetitem11.setText(QCoreApplication.translate("MainWindow", u"Ph\u00f2ng h\u1ecdc", None));
        ___qtablewidgetitem12 = self.tableWidget_2.horizontalHeaderItem(5)
        ___qtablewidgetitem12.setText(QCoreApplication.translate("MainWindow", u"Lo\u1ea1i l\u1edbp", None));
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Ch\u1ecdn h\u1ecdc ph\u1ea7n b\u1ea1n mu\u1ed1n h\u1ecdc", None))
        self.pushButton_3.setText(QCoreApplication.translate("MainWindow", u"Ch\u1ecdn", None))
        self.lineEdit_3.setPlaceholderText(QCoreApplication.translate("MainWindow", u"G\u00f5 m\u00e3 h\u1ecdc ph\u1ea7n b\u1ea1n mu\u1ed1n h\u1ecdc v\u00e0o \u0111\u00e2y", None))
        self.groupBox_3.setTitle(QCoreApplication.translate("MainWindow", u"Gi\u1edbi h\u1ea1n t\u00edn ch\u1ec9", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"Ch\u01b0\u01a1ng tr\u00ecnh h\u1ecdc", None))
        self.comboBox_2.setItemText(0, QCoreApplication.translate("MainWindow", u"(none)", None))
        self.comboBox_2.setItemText(1, QCoreApplication.translate("MainWindow", u"Ch\u01b0\u01a1ng tr\u00ecnh chu\u1ea9n", None))
        self.comboBox_2.setItemText(2, QCoreApplication.translate("MainWindow", u"Ch\u01b0\u01a1ng tr\u00ecnh ELITECH", None))
        self.comboBox_2.setItemText(3, QCoreApplication.translate("MainWindow", u"Kh\u00e1c/Tu\u1ef3 ch\u1ec9nh", None))

        self.label_5.setText(QCoreApplication.translate("MainWindow", u"S\u1ed1 t\u00edn ch\u1ec9 t\u1ed1i thi\u1ec3u", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"S\u1ed1 t\u00edn ch\u1ec9 t\u1ed1i \u0111a", None))
        self.groupBox_2.setTitle(QCoreApplication.translate("MainWindow", u"Danh s\u00e1ch c\u00e1c h\u1ecdc ph\u1ea7n \u0111\u00e3 ch\u1ecdn", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Ch\u1ecdn ng\u00e0y b\u1eaft \u0111\u1ea7u h\u1ecdc k\u1ef3", None))
        self.groupBox_9.setTitle(QCoreApplication.translate("MainWindow", u"Danh s\u00e1ch c\u00e1c h\u1ecdc ph\u1ea7n \u0111\u00e3 ch\u1ecdn", None))
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"N\u1ebfu c\u1ea3m th\u1ea5y l\u1ecbch h\u1ecdc v\u1eeba r\u1ed3i \u01b0ng \u00fd, b\u1ea1n c\u00f3 th\u1ec3 s\u1eed d\u1ee5ng tu\u1ef3 ch\u1ecdn xu\u1ea5t file .ics (\u0111\u1ecbnh d\u1ea1ng iCalendar) \u0111\u1ec3 s\u1eed d\u1ee5ng trong c\u00e1c \u1ee9ng d\u1ee5ng l\u1ecbch kh\u00e1c (Google Calendar hay Outlook, v.v)", None))
        self.pushButton_7.setText(QCoreApplication.translate("MainWindow", u"\u0110i\u1ec1u ch\u1ec9nh l\u1ecbch h\u1ecdc th\u1ee7 c\u00f4ng...", None))
        self.groupBox_5.setTitle(QCoreApplication.translate("MainWindow", u"B\u1ea1n mu\u1ed1n nh\u1eadn th\u00f4ng b\u00e1o l\u1ecbch h\u1ecdc nh\u01b0 th\u1ebf n\u00e0o?", None))
        self.radioButton_2.setText(QCoreApplication.translate("MainWindow", u"Nh\u1eadn th\u00f4ng b\u00e1o -cho t\u1eebng ti\u1ebft h\u1ecdc", None))
        self.radioButton.setText(QCoreApplication.translate("MainWindow", u"Nh\u1eadn th\u00f4ng b\u00e1o t\u1ed5ng h\u1ee3p", None))
        self.pushButton_2.setText(QCoreApplication.translate("MainWindow", u"Xu\u1ea5t file .ics...", None))
        self.pushButton_6.setText(QCoreApplication.translate("MainWindow", u"H\u01b0\u1edbng d\u1eabn s\u1eed d\u1ee5ng file .ics cho c\u00e1c \u1ee9ng d\u1ee5ng l\u1ecbch...", None))
        self.pushButton_5.setText(QCoreApplication.translate("MainWindow", u"Tr\u1edf l\u1ea1i b\u01b0\u1edbc tr\u01b0\u1edbc", None))
        self.pushButton_4.setText(QCoreApplication.translate("MainWindow", u"\u0110i \u0111\u1ebfn b\u01b0\u1edbc ti\u1ebfp theo", None))
    # retranslateUi

if __name__ == "__main__":
        import sys
        app = QApplication(sys.argv)
        MainWindow = QMainWindow()
        ui = Ui_MainWindow()
        ui.setupUi(MainWindow)
        MainWindow.show()
        sys.exit(app.exec())
