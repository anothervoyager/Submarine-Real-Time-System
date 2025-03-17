# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ui_main.ui'
##
## Created by: Qt User Interface Compiler version 6.8.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QFrame, QLabel, QMainWindow,
    QPushButton, QSizePolicy, QTabWidget, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(900, 600)
        MainWindow.setMinimumSize(QSize(900, 600))
        MainWindow.setMaximumSize(QSize(900, 600))
        MainWindow.setStyleSheet(u"MainWindow\n"
"{\n"
"	background-color: #38302e;\n"
"	color: ccdad1;\n"
"	\n"
"	font-family: Montserrat ExtraBold;\n"
"}")
        MainWindow.setTabShape(QTabWidget.TabShape.Rounded)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.widget_submarine_view = QWidget(self.centralwidget)
        self.widget_submarine_view.setObjectName(u"widget_submarine_view")
        self.widget_submarine_view.setGeometry(QRect(420, 10, 470, 351))
        self.widget_submarine_view.setStyleSheet(u"color: #f4f3ee;\n"
"background-color: #788585;\n"
"border-radius: 15px;                     /* <----  \u0437\u0430\u043a\u0440\u0443\u0433\u043b\u0435\u043d\u0438\u0435 \u043a\u0440\u0430\u0435\u0432  */ \n"
"/*border: 2px solid #094065; <----- \u0446\u0432\u0435\u0442 \u0433\u0440\u0430\u043d\u0438\u0446\u044b*/ ")
        self.submarine_button = QPushButton(self.widget_submarine_view)
        self.submarine_button.setObjectName(u"submarine_button")
        self.submarine_button.setGeometry(QRect(9, 10, 451, 331))
        icon = QIcon()
        icon.addFile(u"images/submarine.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.submarine_button.setIcon(icon)
        self.submarine_button.setIconSize(QSize(440, 170))
        self.button_cell_1 = QPushButton(self.widget_submarine_view)
        self.button_cell_1.setObjectName(u"button_cell_1")
        self.button_cell_1.setGeometry(QRect(240, 180, 181, 31))
        self.button_cell_1.setStyleSheet(u"color: #f4f3ee;\n"
"background-color: rgba(0, 166, 251, 0.42);\n"
"border-radius: 0px;                     /* <----  \u0437\u0430\u043a\u0440\u0443\u0433\u043b\u0435\u043d\u0438\u0435 \u043a\u0440\u0430\u0435\u0432  */ \n"
"/*border: 2px solid #094065; <----- \u0446\u0432\u0435\u0442 \u0433\u0440\u0430\u043d\u0438\u0446\u044b*/ ")
        self.button_cell_2 = QPushButton(self.widget_submarine_view)
        self.button_cell_2.setObjectName(u"button_cell_2")
        self.button_cell_2.setGeometry(QRect(80, 180, 151, 30))
        self.button_cell_2.setStyleSheet(u"color: #f4f3ee;\n"
"background-color: rgba(0, 166, 251, 0.42);\n"
"border-radius: 0px;                     /* <----  \u0437\u0430\u043a\u0440\u0443\u0433\u043b\u0435\u043d\u0438\u0435 \u043a\u0440\u0430\u0435\u0432  */ \n"
"/*border: 2px solid #094065; <----- \u0446\u0432\u0435\u0442 \u0433\u0440\u0430\u043d\u0438\u0446\u044b*/ ")
        self.button_cell_3 = QPushButton(self.widget_submarine_view)
        self.button_cell_3.setObjectName(u"button_cell_3")
        self.button_cell_3.setGeometry(QRect(230, 140, 51, 31))
        self.button_cell_3.setStyleSheet(u"color: #f4f3ee;\n"
"background-color: rgba(0, 166, 251, 0.42);\n"
"border-radius: 0px;                     /* <----  \u0437\u0430\u043a\u0440\u0443\u0433\u043b\u0435\u043d\u0438\u0435 \u043a\u0440\u0430\u0435\u0432  */ \n"
"/*border: 2px solid #094065; <----- \u0446\u0432\u0435\u0442 \u0433\u0440\u0430\u043d\u0438\u0446\u044b*/ ")
        self.label_18 = QLabel(self.widget_submarine_view)
        self.label_18.setObjectName(u"label_18")
        self.label_18.setGeometry(QRect(10, 10, 451, 31))
        self.label_18.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.label_18.setStyleSheet(u"\n"
"color: #FFFCF2;\n"
"\n"
"border-radius: 0px;                     /* <----  \u0437\u0430\u043a\u0440\u0443\u0433\u043b\u0435\u043d\u0438\u0435 \u043a\u0440\u0430\u0435\u0432  */ \n"
"font-weight: bold;\n"
"font-size: 18pt;\n"
"font-family: Montserrat ExtraBold;\n"
"border: 0px solid #38302e; /*<----- \u0446\u0432\u0435\u0442 \u0433\u0440\u0430\u043d\u0438\u0446\u044b*/\n"
"")
        self.label_18.setFrameShape(QFrame.Shape.NoFrame)
        self.label_18.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.widget_control_panel = QWidget(self.centralwidget)
        self.widget_control_panel.setObjectName(u"widget_control_panel")
        self.widget_control_panel.setGeometry(QRect(10, 370, 880, 220))
        self.widget_control_panel.setStyleSheet(u"color: #f4f3ee;\n"
"background-color: #6f6866;\n"
"border-radius: 15px;                     /* <----  \u0437\u0430\u043a\u0440\u0443\u0433\u043b\u0435\u043d\u0438\u0435 \u043a\u0440\u0430\u0435\u0432  */ \n"
"/*border: 2px solid #094065; <----- \u0446\u0432\u0435\u0442 \u0433\u0440\u0430\u043d\u0438\u0446\u044b*/ ")
        self.button_critical_oxygen = QPushButton(self.widget_control_panel)
        self.button_critical_oxygen.setObjectName(u"button_critical_oxygen")
        self.button_critical_oxygen.setGeometry(QRect(710, 70, 160, 60))
        self.button_critical_oxygen.setStyleSheet(u"QPushButton {\n"
"color: #FFFCF2;\n"
"background-color: #788585;\n"
"border-radius: 15px;                     /* <----  \u0437\u0430\u043a\u0440\u0443\u0433\u043b\u0435\u043d\u0438\u0435 \u043a\u0440\u0430\u0435\u0432  */ \n"
"font-weight: bold;\n"
"font-size: 10pt;\n"
"font-family: Montserrat ExtraBold;\n"
"border: 2px solid #38302e; /*<----- \u0446\u0432\u0435\u0442 \u0433\u0440\u0430\u043d\u0438\u0446\u044b*/\n"
"}\n"
"QPushButton:hover {\n"
"color: #e0afa0;\n"
"background-color: #9caea9;\n"
"}\n"
"QPushButton:pressed {\n"
"color: #f4f3ee;\n"
"background-color: #ccdad1;\n"
"}\n"
"")
        self.button_critical_temp = QPushButton(self.widget_control_panel)
        self.button_critical_temp.setObjectName(u"button_critical_temp")
        self.button_critical_temp.setGeometry(QRect(710, 140, 160, 60))
        self.button_critical_temp.setStyleSheet(u"QPushButton {\n"
"color: #FFFCF2;\n"
"background-color: #788585;\n"
"border-radius: 15px;                     /* <----  \u0437\u0430\u043a\u0440\u0443\u0433\u043b\u0435\u043d\u0438\u0435 \u043a\u0440\u0430\u0435\u0432  */ \n"
"font-weight: bold;\n"
"font-size: 8pt;\n"
"font-family: Montserrat ExtraBold;\n"
"border: 2px solid #38302e; /*<----- \u0446\u0432\u0435\u0442 \u0433\u0440\u0430\u043d\u0438\u0446\u044b*/\n"
"}\n"
"QPushButton:hover {\n"
"color: #e0afa0;\n"
"background-color: #9caea9;\n"
"}\n"
"QPushButton:pressed {\n"
"color: #f4f3ee;\n"
"background-color: #ccdad1;\n"
"}\n"
"")
        self.tabWidget = QTabWidget(self.widget_control_panel)
        self.tabWidget.setObjectName(u"tabWidget")
        self.tabWidget.setGeometry(QRect(0, 10, 381, 211))
        self.tabWidget.setStyleSheet(u"QTabWidget::pane\n"
"{\n"
"	border: 1px;\n"
"	border-radius: 15px; \n"
"	background: #6f6866;\n"
"	font-size: 10pt;\n"
"	font-family: Montserrat ExtraBold;\n"
"\n"
"}\n"
"QTabBar::tab\n"
"{\n"
"	background: #788585;\n"
"	min-width: 22ex;\n"
"	min-height: 5ex;\n"
"	margin-left: 15px;\n"
"	left: -5px;\n"
"	border-radius: 8px;\n"
"	color: white;\n"
"	border: 2px solid #38302e\n"
"}\n"
"\n"
"QTabBar::tab::selected\n"
"{\n"
"	background: #ccdad1;\n"
"	color: black;\n"
"}\n"
"\n"
"QTabBar::tab::hover\n"
"{\n"
"	background: #9caea9;\n"
"	color: black;\n"
"}")
        self.tab = QWidget()
        self.tab.setObjectName(u"tab")
        self.widget = QWidget(self.tab)
        self.widget.setObjectName(u"widget")
        self.widget.setGeometry(QRect(10, 10, 361, 151))
        self.widget.setStyleSheet(u"\n"
"color: #FFFCF2;\n"
"background-color: #788585;\n"
"border-radius: 15px;                     /* <----  \u0437\u0430\u043a\u0440\u0443\u0433\u043b\u0435\u043d\u0438\u0435 \u043a\u0440\u0430\u0435\u0432  */ \n"
"font-weight: bold;\n"
"font-size: 10pt;\n"
"font-family: Montserrat ExtraBold;\n"
"border: 2px solid #38302e; /*<----- \u0446\u0432\u0435\u0442 \u0433\u0440\u0430\u043d\u0438\u0446\u044b*/\n"
"")
        self.widget_indicators_cell_1 = QWidget(self.widget)
        self.widget_indicators_cell_1.setObjectName(u"widget_indicators_cell_1")
        self.widget_indicators_cell_1.setGeometry(QRect(120, 10, 71, 131))
        self.widget_indicators_cell_1.setStyleSheet(u"\n"
"color: #FFFCF2;\n"
"background-color: #38302e;\n"
"border-radius: 10px;                     /* <----  \u0437\u0430\u043a\u0440\u0443\u0433\u043b\u0435\u043d\u0438\u0435 \u043a\u0440\u0430\u0435\u0432  */ \n"
"font-weight: bold;\n"
"font-size: 10pt;\n"
"font-family: Montserrat ExtraBold;\n"
"border: 2px solid #38302e; /*<----- \u0446\u0432\u0435\u0442 \u0433\u0440\u0430\u043d\u0438\u0446\u044b*/\n"
"")
        self.label_2 = QLabel(self.widget_indicators_cell_1)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(10, 0, 51, 20))
        self.label_2.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.label_2.setStyleSheet(u"\n"
"color: #FFFCF2;\n"
"background-color: #38302e;\n"
"border-radius: 0px;                     /* <----  \u0437\u0430\u043a\u0440\u0443\u0433\u043b\u0435\u043d\u0438\u0435 \u043a\u0440\u0430\u0435\u0432  */ \n"
"font-weight: bold;\n"
"font-size: 10pt;\n"
"font-family: Montserrat ExtraBold;\n"
"border: 0px solid #38302e; /*<----- \u0446\u0432\u0435\u0442 \u0433\u0440\u0430\u043d\u0438\u0446\u044b*/\n"
"")
        self.label_2.setFrameShape(QFrame.Shape.NoFrame)
        self.label_oxygen_1 = QLabel(self.widget_indicators_cell_1)
        self.label_oxygen_1.setObjectName(u"label_oxygen_1")
        self.label_oxygen_1.setGeometry(QRect(0, 20, 71, 61))
        self.label_oxygen_1.setStyleSheet(u"font-size: 15pt;")
        self.label_oxygen_1.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.label_temperature_1 = QLabel(self.widget_indicators_cell_1)
        self.label_temperature_1.setObjectName(u"label_temperature_1")
        self.label_temperature_1.setGeometry(QRect(0, 69, 71, 61))
        font = QFont()
        font.setFamilies([u"Montserrat ExtraBold"])
        font.setPointSize(15)
        font.setBold(True)
        self.label_temperature_1.setFont(font)
        self.label_temperature_1.setStyleSheet(u"font-size: 15pt;")
        self.label_temperature_1.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.label = QLabel(self.widget)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(10, 30, 101, 61))
        self.label.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.label.setStyleSheet(u"\n"
"color: #FFFCF2;\n"
"background-color: #788585;\n"
"border-radius: 0px;                     /* <----  \u0437\u0430\u043a\u0440\u0443\u0433\u043b\u0435\u043d\u0438\u0435 \u043a\u0440\u0430\u0435\u0432  */ \n"
"font-weight: bold;\n"
"font-size: 10pt;\n"
"font-family: Montserrat ExtraBold;\n"
"border: 0px solid #38302e; /*<----- \u0446\u0432\u0435\u0442 \u0433\u0440\u0430\u043d\u0438\u0446\u044b*/\n"
"")
        self.label.setFrameShape(QFrame.Shape.NoFrame)
        self.label_8 = QLabel(self.widget)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setGeometry(QRect(10, 79, 101, 61))
        font1 = QFont()
        font1.setFamilies([u"Montserrat ExtraBold"])
        font1.setPointSize(8)
        font1.setBold(True)
        self.label_8.setFont(font1)
        self.label_8.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.label_8.setStyleSheet(u"\n"
"color: #FFFCF2;\n"
"background-color: #788585;\n"
"border-radius: 0px;                     /* <----  \u0437\u0430\u043a\u0440\u0443\u0433\u043b\u0435\u043d\u0438\u0435 \u043a\u0440\u0430\u0435\u0432  */ \n"
"font-weight: bold;\n"
"font-size: 8pt;\n"
"font-family: Montserrat ExtraBold;\n"
"border: 0px solid #38302e; /*<----- \u0446\u0432\u0435\u0442 \u0433\u0440\u0430\u043d\u0438\u0446\u044b*/\n"
"")
        self.label_8.setFrameShape(QFrame.Shape.NoFrame)
        self.widget_indicators_cell_2 = QWidget(self.widget)
        self.widget_indicators_cell_2.setObjectName(u"widget_indicators_cell_2")
        self.widget_indicators_cell_2.setGeometry(QRect(200, 10, 71, 131))
        self.widget_indicators_cell_2.setStyleSheet(u"\n"
"color: #FFFCF2;\n"
"background-color: #38302e;\n"
"border-radius: 10px;                     /* <----  \u0437\u0430\u043a\u0440\u0443\u0433\u043b\u0435\u043d\u0438\u0435 \u043a\u0440\u0430\u0435\u0432  */ \n"
"font-weight: bold;\n"
"font-size: 10pt;\n"
"font-family: Montserrat ExtraBold;\n"
"border: 2px solid #38302e; /*<----- \u0446\u0432\u0435\u0442 \u0433\u0440\u0430\u043d\u0438\u0446\u044b*/\n"
"")
        self.label_3 = QLabel(self.widget_indicators_cell_2)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(10, 0, 51, 20))
        self.label_3.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.label_3.setStyleSheet(u"\n"
"color: #FFFCF2;\n"
"background-color: #38302e;\n"
"border-radius: 0px;                     /* <----  \u0437\u0430\u043a\u0440\u0443\u0433\u043b\u0435\u043d\u0438\u0435 \u043a\u0440\u0430\u0435\u0432  */ \n"
"font-weight: bold;\n"
"font-size: 10pt;\n"
"font-family: Montserrat ExtraBold;\n"
"border: 0px solid #38302e; /*<----- \u0446\u0432\u0435\u0442 \u0433\u0440\u0430\u043d\u0438\u0446\u044b*/\n"
"")
        self.label_3.setFrameShape(QFrame.Shape.NoFrame)
        self.label_oxygen_2 = QLabel(self.widget_indicators_cell_2)
        self.label_oxygen_2.setObjectName(u"label_oxygen_2")
        self.label_oxygen_2.setGeometry(QRect(0, 20, 71, 61))
        self.label_oxygen_2.setStyleSheet(u"font-size: 15pt;")
        self.label_oxygen_2.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.label_temperature_2 = QLabel(self.widget_indicators_cell_2)
        self.label_temperature_2.setObjectName(u"label_temperature_2")
        self.label_temperature_2.setGeometry(QRect(0, 69, 71, 61))
        self.label_temperature_2.setFont(font)
        self.label_temperature_2.setStyleSheet(u"font-size: 15pt;")
        self.label_temperature_2.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.widget_indicators_cell_3 = QWidget(self.widget)
        self.widget_indicators_cell_3.setObjectName(u"widget_indicators_cell_3")
        self.widget_indicators_cell_3.setGeometry(QRect(280, 10, 71, 131))
        self.widget_indicators_cell_3.setStyleSheet(u"\n"
"color: #FFFCF2;\n"
"background-color: #38302e;\n"
"border-radius: 10px;                     /* <----  \u0437\u0430\u043a\u0440\u0443\u0433\u043b\u0435\u043d\u0438\u0435 \u043a\u0440\u0430\u0435\u0432  */ \n"
"font-weight: bold;\n"
"font-size: 10pt;\n"
"font-family: Montserrat ExtraBold;\n"
"border: 2px solid #38302e; /*<----- \u0446\u0432\u0435\u0442 \u0433\u0440\u0430\u043d\u0438\u0446\u044b*/\n"
"")
        self.label_4 = QLabel(self.widget_indicators_cell_3)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(10, 0, 51, 20))
        self.label_4.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.label_4.setStyleSheet(u"\n"
"color: #FFFCF2;\n"
"background-color: #38302e;\n"
"border-radius: 0px;                     /* <----  \u0437\u0430\u043a\u0440\u0443\u0433\u043b\u0435\u043d\u0438\u0435 \u043a\u0440\u0430\u0435\u0432  */ \n"
"font-weight: bold;\n"
"font-size: 10pt;\n"
"font-family: Montserrat ExtraBold;\n"
"border: 0px solid #38302e; /*<----- \u0446\u0432\u0435\u0442 \u0433\u0440\u0430\u043d\u0438\u0446\u044b*/\n"
"")
        self.label_4.setFrameShape(QFrame.Shape.NoFrame)
        self.label_oxygen_3 = QLabel(self.widget_indicators_cell_3)
        self.label_oxygen_3.setObjectName(u"label_oxygen_3")
        self.label_oxygen_3.setGeometry(QRect(0, 20, 71, 61))
        self.label_oxygen_3.setStyleSheet(u"font-size: 15pt;")
        self.label_oxygen_3.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.label_temperature_3 = QLabel(self.widget_indicators_cell_3)
        self.label_temperature_3.setObjectName(u"label_temperature_3")
        self.label_temperature_3.setGeometry(QRect(0, 69, 71, 61))
        self.label_temperature_3.setFont(font)
        self.label_temperature_3.setStyleSheet(u"font-size: 15pt;")
        self.label_temperature_3.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QWidget()
        self.tab_2.setObjectName(u"tab_2")
        self.widget_2 = QWidget(self.tab_2)
        self.widget_2.setObjectName(u"widget_2")
        self.widget_2.setGeometry(QRect(10, 10, 361, 151))
        self.widget_2.setStyleSheet(u"\n"
"color: #FFFCF2;\n"
"background-color: #788585;\n"
"border-radius: 15px;                     /* <----  \u0437\u0430\u043a\u0440\u0443\u0433\u043b\u0435\u043d\u0438\u0435 \u043a\u0440\u0430\u0435\u0432  */ \n"
"font-weight: bold;\n"
"font-size: 10pt;\n"
"font-family: Montserrat ExtraBold;\n"
"border: 2px solid #38302e; /*<----- \u0446\u0432\u0435\u0442 \u0433\u0440\u0430\u043d\u0438\u0446\u044b*/\n"
"")
        self.widget_indicators_cell_4 = QWidget(self.widget_2)
        self.widget_indicators_cell_4.setObjectName(u"widget_indicators_cell_4")
        self.widget_indicators_cell_4.setGeometry(QRect(10, 10, 211, 61))
        self.widget_indicators_cell_4.setStyleSheet(u"\n"
"color: #FFFCF2;\n"
"background-color: #38302e;\n"
"border-radius: 10px;                     /* <----  \u0437\u0430\u043a\u0440\u0443\u0433\u043b\u0435\u043d\u0438\u0435 \u043a\u0440\u0430\u0435\u0432  */ \n"
"font-weight: bold;\n"
"font-size: 10pt;\n"
"font-family: Montserrat ExtraBold;\n"
"border: 2px solid #38302e; /*<----- \u0446\u0432\u0435\u0442 \u0433\u0440\u0430\u043d\u0438\u0446\u044b*/\n"
"")
        self.label_5 = QLabel(self.widget_indicators_cell_4)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(10, 0, 191, 20))
        self.label_5.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.label_5.setStyleSheet(u"\n"
"color: #FFFCF2;\n"
"background-color: #38302e;\n"
"border-radius: 0px;                     /* <----  \u0437\u0430\u043a\u0440\u0443\u0433\u043b\u0435\u043d\u0438\u0435 \u043a\u0440\u0430\u0435\u0432  */ \n"
"font-weight: bold;\n"
"font-size: 10pt;\n"
"font-family: Montserrat ExtraBold;\n"
"border: 0px solid #38302e; /*<----- \u0446\u0432\u0435\u0442 \u0433\u0440\u0430\u043d\u0438\u0446\u044b*/\n"
"")
        self.label_5.setFrameShape(QFrame.Shape.NoFrame)
        self.label_5.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.label_expenses = QLabel(self.widget_indicators_cell_4)
        self.label_expenses.setObjectName(u"label_expenses")
        self.label_expenses.setGeometry(QRect(0, 20, 151, 31))
        self.label_expenses.setStyleSheet(u"font-size: 15pt;")
        self.label_expenses.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.label_rouble = QLabel(self.widget_indicators_cell_4)
        self.label_rouble.setObjectName(u"label_rouble")
        self.label_rouble.setGeometry(QRect(150, 20, 61, 31))
        self.label_rouble.setStyleSheet(u"font-size: 15pt;")
        self.label_rouble.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.widget_indicators_cell_5 = QWidget(self.widget_2)
        self.widget_indicators_cell_5.setObjectName(u"widget_indicators_cell_5")
        self.widget_indicators_cell_5.setGeometry(QRect(10, 80, 100, 61))
        self.widget_indicators_cell_5.setStyleSheet(u"\n"
"color: #FFFCF2;\n"
"background-color: #38302e;\n"
"border-radius: 10px;                     /* <----  \u0437\u0430\u043a\u0440\u0443\u0433\u043b\u0435\u043d\u0438\u0435 \u043a\u0440\u0430\u0435\u0432  */ \n"
"font-weight: bold;\n"
"font-size: 10pt;\n"
"font-family: Montserrat ExtraBold;\n"
"border: 2px solid #38302e; /*<----- \u0446\u0432\u0435\u0442 \u0433\u0440\u0430\u043d\u0438\u0446\u044b*/\n"
"")
        self.label_6 = QLabel(self.widget_indicators_cell_5)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setGeometry(QRect(10, 0, 81, 10))
        self.label_6.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.label_6.setStyleSheet(u"\n"
"color: #FFFCF2;\n"
"background-color: #38302e;\n"
"border-radius: 0px;                     /* <----  \u0437\u0430\u043a\u0440\u0443\u0433\u043b\u0435\u043d\u0438\u0435 \u043a\u0440\u0430\u0435\u0432  */ \n"
"font-weight: bold;\n"
"font-size: 10pt;\n"
"font-family: Montserrat ExtraBold;\n"
"border: 0px solid #38302e; /*<----- \u0446\u0432\u0435\u0442 \u0433\u0440\u0430\u043d\u0438\u0446\u044b*/\n"
"")
        self.label_6.setFrameShape(QFrame.Shape.NoFrame)
        self.label_6.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.label_oxygen_expenses = QLabel(self.widget_indicators_cell_5)
        self.label_oxygen_expenses.setObjectName(u"label_oxygen_expenses")
        self.label_oxygen_expenses.setGeometry(QRect(0, 28, 61, 31))
        self.label_oxygen_expenses.setStyleSheet(u"font-size: 15pt;")
        self.label_oxygen_expenses.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.label_22 = QLabel(self.widget_indicators_cell_5)
        self.label_22.setObjectName(u"label_22")
        self.label_22.setGeometry(QRect(10, 10, 81, 20))
        self.label_22.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.label_22.setStyleSheet(u"\n"
"color: #FFFCF2;\n"
"background-color: #38302e;\n"
"border-radius: 0px;                     /* <----  \u0437\u0430\u043a\u0440\u0443\u0433\u043b\u0435\u043d\u0438\u0435 \u043a\u0440\u0430\u0435\u0432  */ \n"
"font-weight: bold;\n"
"font-size: 10pt;\n"
"font-family: Montserrat ExtraBold;\n"
"border: 0px solid #38302e; /*<----- \u0446\u0432\u0435\u0442 \u0433\u0440\u0430\u043d\u0438\u0446\u044b*/\n"
"")
        self.label_22.setFrameShape(QFrame.Shape.NoFrame)
        self.label_22.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.label_rouble_5 = QLabel(self.widget_indicators_cell_5)
        self.label_rouble_5.setObjectName(u"label_rouble_5")
        self.label_rouble_5.setGeometry(QRect(60, 30, 41, 31))
        self.label_rouble_5.setStyleSheet(u"font-size: 12pt;")
        self.label_rouble_5.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.widget_indicators_cell_6 = QWidget(self.widget_2)
        self.widget_indicators_cell_6.setObjectName(u"widget_indicators_cell_6")
        self.widget_indicators_cell_6.setGeometry(QRect(230, 10, 121, 61))
        self.widget_indicators_cell_6.setStyleSheet(u"\n"
"color: #FFFCF2;\n"
"background-color: #38302e;\n"
"border-radius: 10px;                     /* <----  \u0437\u0430\u043a\u0440\u0443\u0433\u043b\u0435\u043d\u0438\u0435 \u043a\u0440\u0430\u0435\u0432  */ \n"
"font-weight: bold;\n"
"font-size: 10pt;\n"
"font-family: Montserrat ExtraBold;\n"
"border: 2px solid #38302e; /*<----- \u0446\u0432\u0435\u0442 \u0433\u0440\u0430\u043d\u0438\u0446\u044b*/\n"
"")
        self.label_7 = QLabel(self.widget_indicators_cell_6)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setGeometry(QRect(10, 0, 101, 20))
        self.label_7.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.label_7.setStyleSheet(u"\n"
"color: #FFFCF2;\n"
"background-color: #38302e;\n"
"border-radius: 0px;                     /* <----  \u0437\u0430\u043a\u0440\u0443\u0433\u043b\u0435\u043d\u0438\u0435 \u043a\u0440\u0430\u0435\u0432  */ \n"
"font-weight: bold;\n"
"font-size: 8pt;\n"
"font-family: Montserrat ExtraBold;\n"
"border: 0px solid #38302e; /*<----- \u0446\u0432\u0435\u0442 \u0433\u0440\u0430\u043d\u0438\u0446\u044b*/\n"
"")
        self.label_7.setFrameShape(QFrame.Shape.NoFrame)
        self.label_7.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.label_repair_expenses = QLabel(self.widget_indicators_cell_6)
        self.label_repair_expenses.setObjectName(u"label_repair_expenses")
        self.label_repair_expenses.setGeometry(QRect(0, 30, 81, 31))
        self.label_repair_expenses.setStyleSheet(u"font-size: 15pt;")
        self.label_repair_expenses.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.label_19 = QLabel(self.widget_indicators_cell_6)
        self.label_19.setObjectName(u"label_19")
        self.label_19.setGeometry(QRect(10, 20, 101, 10))
        self.label_19.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.label_19.setStyleSheet(u"\n"
"color: #FFFCF2;\n"
"background-color: #38302e;\n"
"border-radius: 0px;                     /* <----  \u0437\u0430\u043a\u0440\u0443\u0433\u043b\u0435\u043d\u0438\u0435 \u043a\u0440\u0430\u0435\u0432  */ \n"
"font-weight: bold;\n"
"font-size: 8pt;\n"
"font-family: Montserrat ExtraBold;\n"
"border: 0px solid #38302e; /*<----- \u0446\u0432\u0435\u0442 \u0433\u0440\u0430\u043d\u0438\u0446\u044b*/\n"
"")
        self.label_19.setFrameShape(QFrame.Shape.NoFrame)
        self.label_19.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.label_rouble_2 = QLabel(self.widget_indicators_cell_6)
        self.label_rouble_2.setObjectName(u"label_rouble_2")
        self.label_rouble_2.setGeometry(QRect(80, 30, 41, 31))
        self.label_rouble_2.setStyleSheet(u"font-size: 12pt;")
        self.label_rouble_2.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.widget_indicators_cell_7 = QWidget(self.widget_2)
        self.widget_indicators_cell_7.setObjectName(u"widget_indicators_cell_7")
        self.widget_indicators_cell_7.setGeometry(QRect(230, 80, 121, 61))
        self.widget_indicators_cell_7.setStyleSheet(u"\n"
"color: #FFFCF2;\n"
"background-color: #38302e;\n"
"border-radius: 10px;                     /* <----  \u0437\u0430\u043a\u0440\u0443\u0433\u043b\u0435\u043d\u0438\u0435 \u043a\u0440\u0430\u0435\u0432  */ \n"
"font-weight: bold;\n"
"font-size: 10pt;\n"
"font-family: Montserrat ExtraBold;\n"
"border: 2px solid #38302e; /*<----- \u0446\u0432\u0435\u0442 \u0433\u0440\u0430\u043d\u0438\u0446\u044b*/\n"
"")
        self.label_9 = QLabel(self.widget_indicators_cell_7)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setGeometry(QRect(10, 0, 101, 10))
        self.label_9.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.label_9.setStyleSheet(u"\n"
"color: #FFFCF2;\n"
"background-color: #38302e;\n"
"border-radius: 0px;                     /* <----  \u0437\u0430\u043a\u0440\u0443\u0433\u043b\u0435\u043d\u0438\u0435 \u043a\u0440\u0430\u0435\u0432  */ \n"
"font-weight: bold;\n"
"font-size: 10pt;\n"
"font-family: Montserrat ExtraBold;\n"
"border: 0px solid #38302e; /*<----- \u0446\u0432\u0435\u0442 \u0433\u0440\u0430\u043d\u0438\u0446\u044b*/\n"
"")
        self.label_9.setFrameShape(QFrame.Shape.NoFrame)
        self.label_9.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.label_support_expenses = QLabel(self.widget_indicators_cell_7)
        self.label_support_expenses.setObjectName(u"label_support_expenses")
        self.label_support_expenses.setGeometry(QRect(0, 29, 81, 31))
        self.label_support_expenses.setStyleSheet(u"font-size: 15pt;")
        self.label_support_expenses.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.label_20 = QLabel(self.widget_indicators_cell_7)
        self.label_20.setObjectName(u"label_20")
        self.label_20.setGeometry(QRect(0, 10, 120, 20))
        self.label_20.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.label_20.setStyleSheet(u"\n"
"color: #FFFCF2;\n"
"background-color: #38302e;\n"
"border-radius: 0px;                     /* <----  \u0437\u0430\u043a\u0440\u0443\u0433\u043b\u0435\u043d\u0438\u0435 \u043a\u0440\u0430\u0435\u0432  */ \n"
"font-weight: bold;\n"
"font-size: 10pt;\n"
"font-family: Montserrat ExtraBold;\n"
"border: 0px solid #38302e; /*<----- \u0446\u0432\u0435\u0442 \u0433\u0440\u0430\u043d\u0438\u0446\u044b*/\n"
"")
        self.label_20.setFrameShape(QFrame.Shape.NoFrame)
        self.label_20.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.label_rouble_3 = QLabel(self.widget_indicators_cell_7)
        self.label_rouble_3.setObjectName(u"label_rouble_3")
        self.label_rouble_3.setGeometry(QRect(80, 30, 41, 31))
        self.label_rouble_3.setStyleSheet(u"font-size: 12pt;")
        self.label_rouble_3.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.widget_indicators_cell_8 = QWidget(self.widget_2)
        self.widget_indicators_cell_8.setObjectName(u"widget_indicators_cell_8")
        self.widget_indicators_cell_8.setGeometry(QRect(120, 80, 100, 61))
        self.widget_indicators_cell_8.setStyleSheet(u"\n"
"color: #FFFCF2;\n"
"background-color: #38302e;\n"
"border-radius: 10px;                     /* <----  \u0437\u0430\u043a\u0440\u0443\u0433\u043b\u0435\u043d\u0438\u0435 \u043a\u0440\u0430\u0435\u0432  */ \n"
"font-weight: bold;\n"
"font-size: 10pt;\n"
"font-family: Montserrat ExtraBold;\n"
"border: 2px solid #38302e; /*<----- \u0446\u0432\u0435\u0442 \u0433\u0440\u0430\u043d\u0438\u0446\u044b*/\n"
"")
        self.label_21 = QLabel(self.widget_indicators_cell_8)
        self.label_21.setObjectName(u"label_21")
        self.label_21.setGeometry(QRect(10, 0, 81, 10))
        self.label_21.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.label_21.setStyleSheet(u"\n"
"color: #FFFCF2;\n"
"background-color: #38302e;\n"
"border-radius: 0px;                     /* <----  \u0437\u0430\u043a\u0440\u0443\u0433\u043b\u0435\u043d\u0438\u0435 \u043a\u0440\u0430\u0435\u0432  */ \n"
"font-weight: bold;\n"
"font-size: 10pt;\n"
"font-family: Montserrat ExtraBold;\n"
"border: 0px solid #38302e; /*<----- \u0446\u0432\u0435\u0442 \u0433\u0440\u0430\u043d\u0438\u0446\u044b*/\n"
"")
        self.label_21.setFrameShape(QFrame.Shape.NoFrame)
        self.label_21.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.label_cooling_expenses = QLabel(self.widget_indicators_cell_8)
        self.label_cooling_expenses.setObjectName(u"label_cooling_expenses")
        self.label_cooling_expenses.setGeometry(QRect(0, 35, 61, 21))
        self.label_cooling_expenses.setStyleSheet(u"font-size: 15pt;")
        self.label_cooling_expenses.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.label_23 = QLabel(self.widget_indicators_cell_8)
        self.label_23.setObjectName(u"label_23")
        self.label_23.setGeometry(QRect(0, 10, 101, 10))
        self.label_23.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.label_23.setStyleSheet(u"\n"
"color: #FFFCF2;\n"
"background-color: #38302e;\n"
"border-radius: 0px;                     /* <----  \u0437\u0430\u043a\u0440\u0443\u0433\u043b\u0435\u043d\u0438\u0435 \u043a\u0440\u0430\u0435\u0432  */ \n"
"font-weight: bold;\n"
"font-size: 8pt;\n"
"font-family: Montserrat ExtraBold;\n"
"border: 0px solid #38302e; /*<----- \u0446\u0432\u0435\u0442 \u0433\u0440\u0430\u043d\u0438\u0446\u044b*/\n"
"")
        self.label_23.setFrameShape(QFrame.Shape.NoFrame)
        self.label_23.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.label_rouble_4 = QLabel(self.widget_indicators_cell_8)
        self.label_rouble_4.setObjectName(u"label_rouble_4")
        self.label_rouble_4.setGeometry(QRect(60, 30, 41, 31))
        self.label_rouble_4.setStyleSheet(u"font-size: 12pt;")
        self.label_rouble_4.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.tabWidget.addTab(self.tab_2, "")
        self.button_cooling = QPushButton(self.widget_control_panel)
        self.button_cooling.setObjectName(u"button_cooling")
        self.button_cooling.setGeometry(QRect(540, 140, 160, 60))
        self.button_cooling.setStyleSheet(u"QPushButton {\n"
"color: #FFFCF2;\n"
"background-color: #788585;\n"
"border-radius: 15px;                     /* <----  \u0437\u0430\u043a\u0440\u0443\u0433\u043b\u0435\u043d\u0438\u0435 \u043a\u0440\u0430\u0435\u0432  */ \n"
"font-weight: bold;\n"
"font-size: 10pt;\n"
"font-family: Montserrat ExtraBold;\n"
"border: 2px solid #38302e; /*<----- \u0446\u0432\u0435\u0442 \u0433\u0440\u0430\u043d\u0438\u0446\u044b*/\n"
"}\n"
"QPushButton:hover {\n"
"color: #e0afa0;\n"
"background-color: #9caea9;\n"
"}\n"
"QPushButton:pressed {\n"
"color: #f4f3ee;\n"
"background-color: #ccdad1;\n"
"}\n"
"")
        self.button_add_oxygen = QPushButton(self.widget_control_panel)
        self.button_add_oxygen.setObjectName(u"button_add_oxygen")
        self.button_add_oxygen.setGeometry(QRect(540, 70, 160, 60))
        self.button_add_oxygen.setStyleSheet(u"QPushButton {\n"
"color: #FFFCF2;\n"
"background-color: #788585;\n"
"border-radius: 15px;                     /* <----  \u0437\u0430\u043a\u0440\u0443\u0433\u043b\u0435\u043d\u0438\u0435 \u043a\u0440\u0430\u0435\u0432  */ \n"
"font-weight: bold;\n"
"font-size: 10pt;\n"
"font-family: Montserrat ExtraBold;\n"
"border: 2px solid #38302e; /*<----- \u0446\u0432\u0435\u0442 \u0433\u0440\u0430\u043d\u0438\u0446\u044b*/\n"
"}\n"
"QPushButton:hover {\n"
"color: #e0afa0;\n"
"background-color: #9caea9;\n"
"}\n"
"QPushButton:pressed {\n"
"color: #f4f3ee;\n"
"background-color: #ccdad1;\n"
"}\n"
"")
        self.widget_3 = QWidget(self.widget_control_panel)
        self.widget_3.setObjectName(u"widget_3")
        self.widget_3.setGeometry(QRect(380, 10, 151, 201))
        self.widget_3.setStyleSheet(u"\n"
"color: #FFFCF2;\n"
"background-color: #788585;\n"
"border-radius: 15px;                     /* <----  \u0437\u0430\u043a\u0440\u0443\u0433\u043b\u0435\u043d\u0438\u0435 \u043a\u0440\u0430\u0435\u0432  */ \n"
"font-weight: bold;\n"
"font-size: 10pt;\n"
"font-family: Montserrat ExtraBold;\n"
"border: 2px solid #38302e; /*<----- \u0446\u0432\u0435\u0442 \u0433\u0440\u0430\u043d\u0438\u0446\u044b*/\n"
"")
        self.label_10 = QLabel(self.widget_3)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setGeometry(QRect(20, 10, 111, 10))
        self.label_10.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.label_10.setStyleSheet(u"\n"
"color: #FFFCF2;\n"
"\n"
"border-radius: 0px;                     /* <----  \u0437\u0430\u043a\u0440\u0443\u0433\u043b\u0435\u043d\u0438\u0435 \u043a\u0440\u0430\u0435\u0432  */ \n"
"font-weight: bold;\n"
"font-size: 8pt;\n"
"font-family: Montserrat ExtraBold;\n"
"border: 0px solid #38302e; /*<----- \u0446\u0432\u0435\u0442 \u0433\u0440\u0430\u043d\u0438\u0446\u044b*/\n"
"")
        self.label_10.setFrameShape(QFrame.Shape.NoFrame)
        self.label_10.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.label_11 = QLabel(self.widget_3)
        self.label_11.setObjectName(u"label_11")
        self.label_11.setGeometry(QRect(10, 30, 131, 10))
        self.label_11.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.label_11.setStyleSheet(u"\n"
"color: #FFFCF2;\n"
"\n"
"border-radius: 0px;                     /* <----  \u0437\u0430\u043a\u0440\u0443\u0433\u043b\u0435\u043d\u0438\u0435 \u043a\u0440\u0430\u0435\u0432  */ \n"
"font-weight: bold;\n"
"font-size: 10pt;\n"
"font-family: Montserrat ExtraBold;\n"
"border: 0px solid #38302e; /*<----- \u0446\u0432\u0435\u0442 \u0433\u0440\u0430\u043d\u0438\u0446\u044b*/\n"
"")
        self.label_11.setFrameShape(QFrame.Shape.NoFrame)
        self.label_11.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.label_12 = QLabel(self.widget_3)
        self.label_12.setObjectName(u"label_12")
        self.label_12.setGeometry(QRect(10, 40, 131, 16))
        self.label_12.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.label_12.setStyleSheet(u"\n"
"color: #FFFCF2;\n"
"\n"
"border-radius: 0px;                     /* <----  \u0437\u0430\u043a\u0440\u0443\u0433\u043b\u0435\u043d\u0438\u0435 \u043a\u0440\u0430\u0435\u0432  */ \n"
"font-weight: bold;\n"
"font-size: 10pt;\n"
"font-family: Montserrat ExtraBold;\n"
"border: 0px solid #38302e; /*<----- \u0446\u0432\u0435\u0442 \u0433\u0440\u0430\u043d\u0438\u0446\u044b*/\n"
"")
        self.label_12.setFrameShape(QFrame.Shape.NoFrame)
        self.label_12.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.label_13 = QLabel(self.widget_3)
        self.label_13.setObjectName(u"label_13")
        self.label_13.setGeometry(QRect(10, 60, 131, 10))
        self.label_13.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.label_13.setStyleSheet(u"\n"
"color: #FFFCF2;\n"
"\n"
"border-radius: 0px;                     /* <----  \u0437\u0430\u043a\u0440\u0443\u0433\u043b\u0435\u043d\u0438\u0435 \u043a\u0440\u0430\u0435\u0432  */ \n"
"font-weight: bold;\n"
"font-size: 10pt;\n"
"font-family: Montserrat ExtraBold;\n"
"border: 0px solid #38302e; /*<----- \u0446\u0432\u0435\u0442 \u0433\u0440\u0430\u043d\u0438\u0446\u044b*/\n"
"")
        self.label_13.setFrameShape(QFrame.Shape.NoFrame)
        self.label_13.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.label_14 = QLabel(self.widget_3)
        self.label_14.setObjectName(u"label_14")
        self.label_14.setGeometry(QRect(10, 71, 131, 20))
        self.label_14.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.label_14.setStyleSheet(u"\n"
"color: #FFFCF2;\n"
"\n"
"border-radius: 0px;                     /* <----  \u0437\u0430\u043a\u0440\u0443\u0433\u043b\u0435\u043d\u0438\u0435 \u043a\u0440\u0430\u0435\u0432  */ \n"
"font-weight: bold;\n"
"font-size: 10pt;\n"
"font-family: Montserrat ExtraBold;\n"
"border: 0px solid #38302e; /*<----- \u0446\u0432\u0435\u0442 \u0433\u0440\u0430\u043d\u0438\u0446\u044b*/\n"
"")
        self.label_14.setFrameShape(QFrame.Shape.NoFrame)
        self.label_14.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.label_15 = QLabel(self.widget_3)
        self.label_15.setObjectName(u"label_15")
        self.label_15.setGeometry(QRect(10, 90, 131, 20))
        self.label_15.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.label_15.setStyleSheet(u"\n"
"color: #FFFCF2;\n"
"\n"
"border-radius: 0px;                     /* <----  \u0437\u0430\u043a\u0440\u0443\u0433\u043b\u0435\u043d\u0438\u0435 \u043a\u0440\u0430\u0435\u0432  */ \n"
"font-weight: bold;\n"
"font-size: 10pt;\n"
"font-family: Montserrat ExtraBold;\n"
"border: 0px solid #38302e; /*<----- \u0446\u0432\u0435\u0442 \u0433\u0440\u0430\u043d\u0438\u0446\u044b*/\n"
"")
        self.label_15.setFrameShape(QFrame.Shape.NoFrame)
        self.label_15.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.button_easter_egg = QPushButton(self.widget_3)
        self.button_easter_egg.setObjectName(u"button_easter_egg")
        self.button_easter_egg.setGeometry(QRect(0, 110, 151, 91))
        self.button_easter_egg.setStyleSheet(u"\n"
"color: #FFFCF2;\n"
"background-color: #38302e;\n"
"border-radius: 10px;                     /* <----  \u0437\u0430\u043a\u0440\u0443\u0433\u043b\u0435\u043d\u0438\u0435 \u043a\u0440\u0430\u0435\u0432  */ \n"
"font-weight: bold;\n"
"font-size: 10pt;\n"
"font-family: Montserrat ExtraBold;\n"
"border: 2px solid #38302e; /*<----- \u0446\u0432\u0435\u0442 \u0433\u0440\u0430\u043d\u0438\u0446\u044b*/\n"
"")
        icon1 = QIcon()
        icon1.addFile(u"images/radar1.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.button_easter_egg.setIcon(icon1)
        self.button_easter_egg.setIconSize(QSize(85, 85))
        self.label_24 = QLabel(self.widget_3)
        self.label_24.setObjectName(u"label_24")
        self.label_24.setGeometry(QRect(20, 20, 111, 10))
        self.label_24.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.label_24.setStyleSheet(u"\n"
"color: #FFFCF2;\n"
"\n"
"border-radius: 0px;                     /* <----  \u0437\u0430\u043a\u0440\u0443\u0433\u043b\u0435\u043d\u0438\u0435 \u043a\u0440\u0430\u0435\u0432  */ \n"
"font-weight: bold;\n"
"font-size: 8pt;\n"
"font-family: Montserrat ExtraBold;\n"
"border: 0px solid #38302e; /*<----- \u0446\u0432\u0435\u0442 \u0433\u0440\u0430\u043d\u0438\u0446\u044b*/\n"
"")
        self.label_24.setFrameShape(QFrame.Shape.NoFrame)
        self.label_24.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.label_16 = QLabel(self.widget_control_panel)
        self.label_16.setObjectName(u"label_16")
        self.label_16.setGeometry(QRect(710, 10, 161, 51))
        self.label_16.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.label_16.setStyleSheet(u"\n"
"color: #FFFCF2;\n"
"\n"
"border-radius: 0px;                     /* <----  \u0437\u0430\u043a\u0440\u0443\u0433\u043b\u0435\u043d\u0438\u0435 \u043a\u0440\u0430\u0435\u0432  */ \n"
"font-weight: bold;\n"
"font-size: 20pt;\n"
"font-family: Montserrat ExtraBold;\n"
"border: 0px solid #38302e; /*<----- \u0446\u0432\u0435\u0442 \u0433\u0440\u0430\u043d\u0438\u0446\u044b*/\n"
"")
        self.label_16.setFrameShape(QFrame.Shape.NoFrame)
        self.label_16.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.label_17 = QLabel(self.widget_control_panel)
        self.label_17.setObjectName(u"label_17")
        self.label_17.setGeometry(QRect(540, 10, 161, 51))
        self.label_17.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.label_17.setStyleSheet(u"\n"
"color: #FFFCF2;\n"
"\n"
"border-radius: 0px;                     /* <----  \u0437\u0430\u043a\u0440\u0443\u0433\u043b\u0435\u043d\u0438\u0435 \u043a\u0440\u0430\u0435\u0432  */ \n"
"font-weight: bold;\n"
"font-size: 20pt;\n"
"font-family: Montserrat ExtraBold;\n"
"border: 0px solid #38302e; /*<----- \u0446\u0432\u0435\u0442 \u0433\u0440\u0430\u043d\u0438\u0446\u044b*/\n"
"")
        self.label_17.setFrameShape(QFrame.Shape.NoFrame)
        self.label_17.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.tab_widget = QTabWidget(self.centralwidget)
        self.tab_widget.setObjectName(u"tab_widget")
        self.tab_widget.setGeometry(QRect(10, 10, 401, 351))
        self.tab_widget.setStyleSheet(u"QTabWidget::pane\n"
"{\n"
"	border: 1px;\n"
"	background: #38302e;\n"
"}\n"
"QTabBar::tab\n"
"{\n"
"	background: #788585;\n"
"	min-width: 10ex;\n"
"	min-height: 5ex;\n"
"	margin-left: 5px;\n"
"	left: -5px;\n"
"	border-radius: 8px;\n"
"	color: white;\n"
"}\n"
"\n"
"QTabBar::tab::selected\n"
"{\n"
"	background: #ccdad1;\n"
"	color: black;\n"
"}\n"
"\n"
"QTabBar::tab::hover\n"
"{\n"
"	background: #9caea9;\n"
"	color: black;\n"
"}")
        self.tab_widget.setTabPosition(QTabWidget.TabPosition.North)
        self.tab_3 = QWidget()
        self.tab_3.setObjectName(u"tab_3")
        self.widget_graphic_1 = QWidget(self.tab_3)
        self.widget_graphic_1.setObjectName(u"widget_graphic_1")
        self.widget_graphic_1.setGeometry(QRect(0, 10, 401, 311))
        self.widget_graphic_1.setStyleSheet(u"color: #f4f3ee;\n"
"background-color: #6f6866;\n"
"border-radius: 15px;                     /* <----  \u0437\u0430\u043a\u0440\u0443\u0433\u043b\u0435\u043d\u0438\u0435 \u043a\u0440\u0430\u0435\u0432  */ \n"
"/*border: 2px solid #094065; <----- \u0446\u0432\u0435\u0442 \u0433\u0440\u0430\u043d\u0438\u0446\u044b*/ ")
        self.pushButton_9 = QPushButton(self.widget_graphic_1)
        self.pushButton_9.setObjectName(u"pushButton_9")
        self.pushButton_9.setGeometry(QRect(710, 10, 160, 60))
        self.pushButton_9.setStyleSheet(u"QPushButton {\n"
"color: #FFFCF2;\n"
"background-color: #788585;\n"
"border-radius: 15px;                     /* <----  \u0437\u0430\u043a\u0440\u0443\u0433\u043b\u0435\u043d\u0438\u0435 \u043a\u0440\u0430\u0435\u0432  */ \n"
"font-weight: bold;\n"
"font-size: 10pt;\n"
"font-family: Montserrat ExtraBold;\n"
"border: 2px solid #38302e; /*<----- \u0446\u0432\u0435\u0442 \u0433\u0440\u0430\u043d\u0438\u0446\u044b*/\n"
"}\n"
"QPushButton:hover {\n"
"color: #e0afa0;\n"
"background-color: #9caea9;\n"
"}\n"
"QPushButton:pressed {\n"
"color: #f4f3ee;\n"
"background-color: #ccdad1;\n"
"}\n"
"")
        self.pushButton_10 = QPushButton(self.widget_graphic_1)
        self.pushButton_10.setObjectName(u"pushButton_10")
        self.pushButton_10.setGeometry(QRect(710, 80, 160, 60))
        self.pushButton_10.setStyleSheet(u"QPushButton {\n"
"color: #FFFCF2;\n"
"background-color: #788585;\n"
"border-radius: 15px;                     /* <----  \u0437\u0430\u043a\u0440\u0443\u0433\u043b\u0435\u043d\u0438\u0435 \u043a\u0440\u0430\u0435\u0432  */ \n"
"font-weight: bold;\n"
"font-size: 10pt;\n"
"font-family: Montserrat ExtraBold;\n"
"border: 2px solid #38302e; /*<----- \u0446\u0432\u0435\u0442 \u0433\u0440\u0430\u043d\u0438\u0446\u044b*/\n"
"}\n"
"QPushButton:hover {\n"
"color: #e0afa0;\n"
"background-color: #9caea9;\n"
"}\n"
"QPushButton:pressed {\n"
"color: #f4f3ee;\n"
"background-color: #ccdad1;\n"
"}\n"
"")
        self.tab_widget.addTab(self.tab_3, "")
        self.tab_5 = QWidget()
        self.tab_5.setObjectName(u"tab_5")
        self.widget_graphic_2 = QWidget(self.tab_5)
        self.widget_graphic_2.setObjectName(u"widget_graphic_2")
        self.widget_graphic_2.setGeometry(QRect(0, 10, 401, 311))
        self.widget_graphic_2.setStyleSheet(u"color: #f4f3ee;\n"
"background-color: #6f6866;\n"
"border-radius: 15px;                     /* <----  \u0437\u0430\u043a\u0440\u0443\u0433\u043b\u0435\u043d\u0438\u0435 \u043a\u0440\u0430\u0435\u0432  */ \n"
"/*border: 2px solid #094065; <----- \u0446\u0432\u0435\u0442 \u0433\u0440\u0430\u043d\u0438\u0446\u044b*/ ")
        self.pushButton_11 = QPushButton(self.widget_graphic_2)
        self.pushButton_11.setObjectName(u"pushButton_11")
        self.pushButton_11.setGeometry(QRect(710, 10, 160, 60))
        self.pushButton_11.setStyleSheet(u"QPushButton {\n"
"color: #FFFCF2;\n"
"background-color: #788585;\n"
"border-radius: 15px;                     /* <----  \u0437\u0430\u043a\u0440\u0443\u0433\u043b\u0435\u043d\u0438\u0435 \u043a\u0440\u0430\u0435\u0432  */ \n"
"font-weight: bold;\n"
"font-size: 10pt;\n"
"font-family: Montserrat ExtraBold;\n"
"border: 2px solid #38302e; /*<----- \u0446\u0432\u0435\u0442 \u0433\u0440\u0430\u043d\u0438\u0446\u044b*/\n"
"}\n"
"QPushButton:hover {\n"
"color: #e0afa0;\n"
"background-color: #9caea9;\n"
"}\n"
"QPushButton:pressed {\n"
"color: #f4f3ee;\n"
"background-color: #ccdad1;\n"
"}\n"
"")
        self.pushButton_12 = QPushButton(self.widget_graphic_2)
        self.pushButton_12.setObjectName(u"pushButton_12")
        self.pushButton_12.setGeometry(QRect(710, 80, 160, 60))
        self.pushButton_12.setStyleSheet(u"QPushButton {\n"
"color: #FFFCF2;\n"
"background-color: #788585;\n"
"border-radius: 15px;                     /* <----  \u0437\u0430\u043a\u0440\u0443\u0433\u043b\u0435\u043d\u0438\u0435 \u043a\u0440\u0430\u0435\u0432  */ \n"
"font-weight: bold;\n"
"font-size: 10pt;\n"
"font-family: Montserrat ExtraBold;\n"
"border: 2px solid #38302e; /*<----- \u0446\u0432\u0435\u0442 \u0433\u0440\u0430\u043d\u0438\u0446\u044b*/\n"
"}\n"
"QPushButton:hover {\n"
"color: #e0afa0;\n"
"background-color: #9caea9;\n"
"}\n"
"QPushButton:pressed {\n"
"color: #f4f3ee;\n"
"background-color: #ccdad1;\n"
"}\n"
"")
        self.tab_widget.addTab(self.tab_5, "")
        self.tab_4 = QWidget()
        self.tab_4.setObjectName(u"tab_4")
        self.widget_graphic_3 = QWidget(self.tab_4)
        self.widget_graphic_3.setObjectName(u"widget_graphic_3")
        self.widget_graphic_3.setGeometry(QRect(0, 10, 401, 311))
        self.widget_graphic_3.setStyleSheet(u"color: #f4f3ee;\n"
"background-color: #6f6866;\n"
"border-radius: 15px;                     /* <----  \u0437\u0430\u043a\u0440\u0443\u0433\u043b\u0435\u043d\u0438\u0435 \u043a\u0440\u0430\u0435\u0432  */ \n"
"/*border: 2px solid #094065; <----- \u0446\u0432\u0435\u0442 \u0433\u0440\u0430\u043d\u0438\u0446\u044b*/ ")
        self.pushButton_13 = QPushButton(self.widget_graphic_3)
        self.pushButton_13.setObjectName(u"pushButton_13")
        self.pushButton_13.setGeometry(QRect(710, 10, 160, 60))
        self.pushButton_13.setStyleSheet(u"QPushButton {\n"
"color: #FFFCF2;\n"
"background-color: #788585;\n"
"border-radius: 15px;                     /* <----  \u0437\u0430\u043a\u0440\u0443\u0433\u043b\u0435\u043d\u0438\u0435 \u043a\u0440\u0430\u0435\u0432  */ \n"
"font-weight: bold;\n"
"font-size: 10pt;\n"
"font-family: Montserrat ExtraBold;\n"
"border: 2px solid #38302e; /*<----- \u0446\u0432\u0435\u0442 \u0433\u0440\u0430\u043d\u0438\u0446\u044b*/\n"
"}\n"
"QPushButton:hover {\n"
"color: #e0afa0;\n"
"background-color: #9caea9;\n"
"}\n"
"QPushButton:pressed {\n"
"color: #f4f3ee;\n"
"background-color: #ccdad1;\n"
"}\n"
"")
        self.pushButton_14 = QPushButton(self.widget_graphic_3)
        self.pushButton_14.setObjectName(u"pushButton_14")
        self.pushButton_14.setGeometry(QRect(710, 80, 160, 60))
        self.pushButton_14.setStyleSheet(u"QPushButton {\n"
"color: #FFFCF2;\n"
"background-color: #788585;\n"
"border-radius: 15px;                     /* <----  \u0437\u0430\u043a\u0440\u0443\u0433\u043b\u0435\u043d\u0438\u0435 \u043a\u0440\u0430\u0435\u0432  */ \n"
"font-weight: bold;\n"
"font-size: 10pt;\n"
"font-family: Montserrat ExtraBold;\n"
"border: 2px solid #38302e; /*<----- \u0446\u0432\u0435\u0442 \u0433\u0440\u0430\u043d\u0438\u0446\u044b*/\n"
"}\n"
"QPushButton:hover {\n"
"color: #e0afa0;\n"
"background-color: #9caea9;\n"
"}\n"
"QPushButton:pressed {\n"
"color: #f4f3ee;\n"
"background-color: #ccdad1;\n"
"}\n"
"")
        self.tab_widget.addTab(self.tab_4, "")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        self.tabWidget.setCurrentIndex(1)
        self.tab_widget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"\u0428\u043b\u0435\u0451\u0432 \u0420\u043e\u0434\u0438\u043e\u043d \u0412\u0430\u0434\u0438\u043c\u043e\u0432\u0438\u0447 \u041f\u0418-428\u0411 \u0421\u0438\u0441\u0442\u0435\u043c\u0430 \u0436\u0438\u0437\u043d\u0435\u043e\u0431\u0435\u0441\u043f\u0435\u0447\u0435\u043d\u0438\u0430\u044f \u043f\u043e\u0434\u0432\u043e\u0434\u043d\u043e\u0439 \u043b\u043e\u0434\u043a\u0438", None))
        self.submarine_button.setText("")
        self.button_cell_1.setText("")
        self.button_cell_2.setText("")
        self.button_cell_3.setText("")
        self.label_18.setText(QCoreApplication.translate("MainWindow", u"\u0421\u043e\u0441\u0442\u043e\u044f\u043d\u0438\u0435 \u043f\u043e\u0434\u0432\u043e\u0434\u043d\u043e\u0439 \u043b\u043e\u0434\u043a\u0438", None))
        self.button_critical_oxygen.setText(QCoreApplication.translate("MainWindow", u"\u041d\u0435\u0445\u0432\u0430\u0442\u043a\u0430 \u043a\u0438\u0441\u043b\u043e\u0440\u043e\u0434\u0430", None))
        self.button_critical_temp.setText(QCoreApplication.translate("MainWindow", u"\u041a\u0440\u0438\u0442\u0438\u0447\u0435\u0441\u043a\u0430\u044f \u0442\u0435\u043c\u043f\u0435\u0440\u0430\u0442\u0443\u0440\u0430", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"\u041e\u0442\u0441\u0435\u043a 1", None))
        self.label_oxygen_1.setText(QCoreApplication.translate("MainWindow", u"21", None))
        self.label_temperature_1.setText(QCoreApplication.translate("MainWindow", u"21", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"\u041a\u0438\u0441\u043b\u043e\u0440\u043e\u0434 (%)", None))
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"\u0422\u0435\u043c\u043f\u0435\u0440\u0430\u0442\u0443\u0440\u0430 (\u00b0\u0421)", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"\u041e\u0442\u0441\u0435\u043a 2", None))
        self.label_oxygen_2.setText(QCoreApplication.translate("MainWindow", u"21", None))
        self.label_temperature_2.setText(QCoreApplication.translate("MainWindow", u"21", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"\u041e\u0442\u0441\u0435\u043a 3", None))
        self.label_oxygen_3.setText(QCoreApplication.translate("MainWindow", u"21", None))
        self.label_temperature_3.setText(QCoreApplication.translate("MainWindow", u"21", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), QCoreApplication.translate("MainWindow", u"\u041f\u043e\u043a\u0430\u0437\u0430\u0442\u0435\u043b\u0438 \u043e\u0442\u0441\u0435\u043a\u043e\u0432", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"\u041e\u0431\u0449\u0438\u0435 \u0440\u0430\u0441\u0445\u043e\u0434\u044b ", None))
        self.label_expenses.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.label_rouble.setText(QCoreApplication.translate("MainWindow", u"\u0420\u0443\u0431.", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"\u0420\u0430\u0441\u0445\u043e\u0434\u044b", None))
        self.label_oxygen_expenses.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.label_22.setText(QCoreApplication.translate("MainWindow", u"\u043d\u0430 \u043a\u0438\u0441\u043b\u043e\u0440\u043e\u0434", None))
        self.label_rouble_5.setText(QCoreApplication.translate("MainWindow", u"\u0420\u0443\u0431.", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"\u0420\u0430\u0441\u0445\u043e\u0434\u044b ", None))
        self.label_repair_expenses.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.label_19.setText(QCoreApplication.translate("MainWindow", u"\u043d\u0430 \u043e\u0431\u0441\u043b\u0443\u0436\u0438\u0432\u0430\u043d\u0438\u0435", None))
        self.label_rouble_2.setText(QCoreApplication.translate("MainWindow", u"\u0420\u0443\u0431.", None))
        self.label_9.setText(QCoreApplication.translate("MainWindow", u"\u0420\u0430\u0441\u0445\u043e\u0434\u044b ", None))
        self.label_support_expenses.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.label_20.setText(QCoreApplication.translate("MainWindow", u"\u043d\u0430 \u0441\u043e\u0434\u0435\u0440\u0436\u0430\u043d\u0438\u0435", None))
        self.label_rouble_3.setText(QCoreApplication.translate("MainWindow", u"\u0420\u0443\u0431.", None))
        self.label_21.setText(QCoreApplication.translate("MainWindow", u"\u0420\u0430\u0441\u0445\u043e\u0434\u044b", None))
        self.label_cooling_expenses.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.label_23.setText(QCoreApplication.translate("MainWindow", u"\u043d\u0430 \u043e\u0445\u043b\u0430\u0436\u0434\u0435\u043d\u0438\u0435", None))
        self.label_rouble_4.setText(QCoreApplication.translate("MainWindow", u"\u0420\u0443\u0431.", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), QCoreApplication.translate("MainWindow", u"\u042d\u043a\u043e\u043d\u043e\u043c\u0438\u0447\u0435\u0441\u043a\u0438\u0435 \u043f\u043e\u043a\u0430\u0437\u0430\u0442\u0435\u043b\u0438", None))
        self.button_cooling.setText(QCoreApplication.translate("MainWindow", u"\u041e\u0445\u043b\u0430\u0436\u0434\u0435\u043d\u0438\u0435", None))
        self.button_add_oxygen.setText(QCoreApplication.translate("MainWindow", u"\u041f\u043e\u043f\u043e\u043b\u043d\u0438\u0442\u044c \u0437\u0430\u043f\u0430\u0441\u044b", None))
        self.label_10.setText(QCoreApplication.translate("MainWindow", u"\u0428\u043b\u0435\u0435\u0432 ", None))
        self.label_11.setText(QCoreApplication.translate("MainWindow", u"\u041f\u0418-428\u0411", None))
        self.label_12.setText(QCoreApplication.translate("MainWindow", u"\u0412\u0430\u0440\u0438\u0430\u043d\u0442:", None))
        self.label_13.setText(QCoreApplication.translate("MainWindow", u"\u0421\u0438\u0441\u0442\u0435\u043c\u0430 ", None))
        self.label_14.setText(QCoreApplication.translate("MainWindow", u"\u0416\u0438\u0437\u043d\u0435\u043e\u0431\u0435\u0441\u043f\u0435\u0447\u0435\u043d\u0438\u044f", None))
        self.label_15.setText(QCoreApplication.translate("MainWindow", u"\u041f\u043e\u0434\u0432\u043e\u0434\u043d\u043e\u0439 \u043b\u043e\u0434\u043a\u0438", None))
        self.button_easter_egg.setText("")
        self.label_24.setText(QCoreApplication.translate("MainWindow", u"\u0420\u043e\u0434\u0438\u043e\u043d \u0412\u0430\u0434\u0438\u043c\u043e\u0432\u0438\u0447", None))
        self.label_16.setText(QCoreApplication.translate("MainWindow", u"\u0410\u0432\u0430\u0440\u0438\u0438", None))
        self.label_17.setText(QCoreApplication.translate("MainWindow", u"\u0420\u0435\u0448\u0435\u043d\u0438\u044f", None))
        self.pushButton_9.setText(QCoreApplication.translate("MainWindow", u"\u0423\u0442\u0435\u0447\u043a\u0430 \u043a\u0438\u0441\u043b\u043e\u0440\u043e\u0434\u0430", None))
        self.pushButton_10.setText(QCoreApplication.translate("MainWindow", u"\u0423\u0442\u0435\u0447\u043a\u0430 \u043a\u0438\u0441\u043b\u043e\u0440\u043e\u0434\u0430", None))
        self.tab_widget.setTabText(self.tab_widget.indexOf(self.tab_3), QCoreApplication.translate("MainWindow", u"\u041e\u0442\u0441\u0435\u043a 1", None))
        self.pushButton_11.setText(QCoreApplication.translate("MainWindow", u"\u0423\u0442\u0435\u0447\u043a\u0430 \u043a\u0438\u0441\u043b\u043e\u0440\u043e\u0434\u0430", None))
        self.pushButton_12.setText(QCoreApplication.translate("MainWindow", u"\u0423\u0442\u0435\u0447\u043a\u0430 \u043a\u0438\u0441\u043b\u043e\u0440\u043e\u0434\u0430", None))
        self.tab_widget.setTabText(self.tab_widget.indexOf(self.tab_5), QCoreApplication.translate("MainWindow", u"\u041e\u0442\u0441\u0435\u043a 2", None))
        self.pushButton_13.setText(QCoreApplication.translate("MainWindow", u"\u0423\u0442\u0435\u0447\u043a\u0430 \u043a\u0438\u0441\u043b\u043e\u0440\u043e\u0434\u0430", None))
        self.pushButton_14.setText(QCoreApplication.translate("MainWindow", u"\u0423\u0442\u0435\u0447\u043a\u0430 \u043a\u0438\u0441\u043b\u043e\u0440\u043e\u0434\u0430", None))
        self.tab_widget.setTabText(self.tab_widget.indexOf(self.tab_4), QCoreApplication.translate("MainWindow", u"\u041e\u0442\u0441\u0435\u043a 3", None))
    # retranslateUi

