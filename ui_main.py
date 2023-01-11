# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1095, 875)
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        sizePolicy.setHeightForWidth(self.centralwidget.sizePolicy().hasHeightForWidth())
        self.centralwidget.setSizePolicy(sizePolicy)
        self.gridLayout = QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.stack = QStackedWidget(self.centralwidget)
        self.stack.setObjectName(u"stack")
        sizePolicy.setHeightForWidth(self.stack.sizePolicy().hasHeightForWidth())
        self.stack.setSizePolicy(sizePolicy)
        self.page_1 = QWidget()
        self.page_1.setObjectName(u"page_1")
        sizePolicy.setHeightForWidth(self.page_1.sizePolicy().hasHeightForWidth())
        self.page_1.setSizePolicy(sizePolicy)
        self.gridLayout_8 = QGridLayout(self.page_1)
        self.gridLayout_8.setObjectName(u"gridLayout_8")
        self.gridLayout_1 = QGridLayout()
        self.gridLayout_1.setObjectName(u"gridLayout_1")
        self.AngleLabel_1 = QLabel(self.page_1)
        self.AngleLabel_1.setObjectName(u"AngleLabel_1")
        sizePolicy1 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Expanding)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.AngleLabel_1.sizePolicy().hasHeightForWidth())
        self.AngleLabel_1.setSizePolicy(sizePolicy1)
        font = QFont()
        font.setPointSize(12)
        self.AngleLabel_1.setFont(font)
        self.AngleLabel_1.setLayoutDirection(Qt.LeftToRight)
        self.AngleLabel_1.setTextFormat(Qt.PlainText)
        self.AngleLabel_1.setAlignment(Qt.AlignCenter)

        self.gridLayout_1.addWidget(self.AngleLabel_1, 0, 0, 1, 1)

        self.AngleSlider_1 = QSlider(self.page_1)
        self.AngleSlider_1.setObjectName(u"AngleSlider_1")
        self.AngleSlider_1.setMinimum(1)
        self.AngleSlider_1.setMaximum(89)
        self.AngleSlider_1.setOrientation(Qt.Vertical)
        self.AngleSlider_1.setTickPosition(QSlider.TicksAbove)
        self.AngleSlider_1.setTickInterval(15)

        self.gridLayout_1.addWidget(self.AngleSlider_1, 0, 1, 1, 1)

        self.plot_1 = QLabel(self.page_1)
        self.plot_1.setObjectName(u"plot_1")
        sizePolicy.setHeightForWidth(self.plot_1.sizePolicy().hasHeightForWidth())
        self.plot_1.setSizePolicy(sizePolicy)
        font1 = QFont()
        font1.setPointSize(24)
        self.plot_1.setFont(font1)
        self.plot_1.setFrameShape(QFrame.Box)
        self.plot_1.setScaledContents(True)
        self.plot_1.setAlignment(Qt.AlignCenter)

        self.gridLayout_1.addWidget(self.plot_1, 0, 2, 1, 1)

        self.button_1 = QPushButton(self.page_1)
        self.button_1.setObjectName(u"button_1")
        sizePolicy2 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.button_1.sizePolicy().hasHeightForWidth())
        self.button_1.setSizePolicy(sizePolicy2)

        self.gridLayout_1.addWidget(self.button_1, 1, 0, 2, 2)

        self.ForceSlider_1 = QSlider(self.page_1)
        self.ForceSlider_1.setObjectName(u"ForceSlider_1")
        self.ForceSlider_1.setMinimum(1)
        self.ForceSlider_1.setMaximum(100)
        self.ForceSlider_1.setOrientation(Qt.Horizontal)
        self.ForceSlider_1.setTickPosition(QSlider.TicksBelow)
        self.ForceSlider_1.setTickInterval(25)

        self.gridLayout_1.addWidget(self.ForceSlider_1, 1, 2, 1, 1)

        self.ForceLabel_1 = QLabel(self.page_1)
        self.ForceLabel_1.setObjectName(u"ForceLabel_1")
        sizePolicy3 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.ForceLabel_1.sizePolicy().hasHeightForWidth())
        self.ForceLabel_1.setSizePolicy(sizePolicy3)
        self.ForceLabel_1.setFont(font)
        self.ForceLabel_1.setAlignment(Qt.AlignCenter)

        self.gridLayout_1.addWidget(self.ForceLabel_1, 2, 2, 1, 1)


        self.gridLayout_8.addLayout(self.gridLayout_1, 0, 0, 1, 1)

        self.stack.addWidget(self.page_1)
        self.page_2 = QWidget()
        self.page_2.setObjectName(u"page_2")
        self.gridLayout_7 = QGridLayout(self.page_2)
        self.gridLayout_7.setObjectName(u"gridLayout_7")
        self.gridLayout_2 = QGridLayout()
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.AngleLabel_2 = QLabel(self.page_2)
        self.AngleLabel_2.setObjectName(u"AngleLabel_2")
        sizePolicy1.setHeightForWidth(self.AngleLabel_2.sizePolicy().hasHeightForWidth())
        self.AngleLabel_2.setSizePolicy(sizePolicy1)
        self.AngleLabel_2.setFont(font)
        self.AngleLabel_2.setLayoutDirection(Qt.LeftToRight)
        self.AngleLabel_2.setTextFormat(Qt.PlainText)
        self.AngleLabel_2.setAlignment(Qt.AlignCenter)

        self.gridLayout_2.addWidget(self.AngleLabel_2, 0, 0, 1, 1)

        self.AngleSlider_2 = QSlider(self.page_2)
        self.AngleSlider_2.setObjectName(u"AngleSlider_2")
        self.AngleSlider_2.setMinimum(1)
        self.AngleSlider_2.setMaximum(89)
        self.AngleSlider_2.setOrientation(Qt.Vertical)
        self.AngleSlider_2.setTickPosition(QSlider.TicksAbove)
        self.AngleSlider_2.setTickInterval(15)

        self.gridLayout_2.addWidget(self.AngleSlider_2, 0, 1, 1, 1)

        self.plot_2 = QLabel(self.page_2)
        self.plot_2.setObjectName(u"plot_2")
        sizePolicy.setHeightForWidth(self.plot_2.sizePolicy().hasHeightForWidth())
        self.plot_2.setSizePolicy(sizePolicy)
        self.plot_2.setFont(font1)
        self.plot_2.setFrameShape(QFrame.Box)
        self.plot_2.setScaledContents(True)
        self.plot_2.setAlignment(Qt.AlignCenter)

        self.gridLayout_2.addWidget(self.plot_2, 0, 2, 1, 1)

        self.button_2 = QPushButton(self.page_2)
        self.button_2.setObjectName(u"button_2")
        sizePolicy2.setHeightForWidth(self.button_2.sizePolicy().hasHeightForWidth())
        self.button_2.setSizePolicy(sizePolicy2)

        self.gridLayout_2.addWidget(self.button_2, 1, 0, 2, 2)

        self.ForceSlider_2 = QSlider(self.page_2)
        self.ForceSlider_2.setObjectName(u"ForceSlider_2")
        self.ForceSlider_2.setMinimum(1)
        self.ForceSlider_2.setMaximum(100)
        self.ForceSlider_2.setOrientation(Qt.Horizontal)
        self.ForceSlider_2.setTickPosition(QSlider.TicksBelow)
        self.ForceSlider_2.setTickInterval(25)

        self.gridLayout_2.addWidget(self.ForceSlider_2, 1, 2, 1, 1)

        self.ForceLabel_2 = QLabel(self.page_2)
        self.ForceLabel_2.setObjectName(u"ForceLabel_2")
        sizePolicy3.setHeightForWidth(self.ForceLabel_2.sizePolicy().hasHeightForWidth())
        self.ForceLabel_2.setSizePolicy(sizePolicy3)
        self.ForceLabel_2.setFont(font)
        self.ForceLabel_2.setAlignment(Qt.AlignCenter)

        self.gridLayout_2.addWidget(self.ForceLabel_2, 2, 2, 1, 1)


        self.gridLayout_7.addLayout(self.gridLayout_2, 0, 0, 1, 1)

        self.stack.addWidget(self.page_2)
        self.exit_page = QWidget()
        self.exit_page.setObjectName(u"exit_page")
        self.gridLayout_4 = QGridLayout(self.exit_page)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.gridLayout_6 = QGridLayout()
        self.gridLayout_6.setObjectName(u"gridLayout_6")
        self.plot_exit = QLabel(self.exit_page)
        self.plot_exit.setObjectName(u"plot_exit")
        sizePolicy.setHeightForWidth(self.plot_exit.sizePolicy().hasHeightForWidth())
        self.plot_exit.setSizePolicy(sizePolicy)
        self.plot_exit.setFont(font1)
        self.plot_exit.setFrameShape(QFrame.Box)
        self.plot_exit.setScaledContents(True)
        self.plot_exit.setAlignment(Qt.AlignCenter)

        self.gridLayout_6.addWidget(self.plot_exit, 0, 2, 1, 1)

        self.button_exit = QPushButton(self.exit_page)
        self.button_exit.setObjectName(u"button_exit")
        sizePolicy2.setHeightForWidth(self.button_exit.sizePolicy().hasHeightForWidth())
        self.button_exit.setSizePolicy(sizePolicy2)

        self.gridLayout_6.addWidget(self.button_exit, 1, 0, 2, 2)

        self.ForceLabel_exit = QLabel(self.exit_page)
        self.ForceLabel_exit.setObjectName(u"ForceLabel_exit")
        sizePolicy3.setHeightForWidth(self.ForceLabel_exit.sizePolicy().hasHeightForWidth())
        self.ForceLabel_exit.setSizePolicy(sizePolicy3)
        self.ForceLabel_exit.setFont(font)
        self.ForceLabel_exit.setAlignment(Qt.AlignCenter)

        self.gridLayout_6.addWidget(self.ForceLabel_exit, 2, 2, 1, 1)

        self.ForceSlider_exit = QSlider(self.exit_page)
        self.ForceSlider_exit.setObjectName(u"ForceSlider_exit")
        self.ForceSlider_exit.setMinimum(1)
        self.ForceSlider_exit.setMaximum(100)
        self.ForceSlider_exit.setOrientation(Qt.Horizontal)
        self.ForceSlider_exit.setTickPosition(QSlider.TicksBelow)
        self.ForceSlider_exit.setTickInterval(25)

        self.gridLayout_6.addWidget(self.ForceSlider_exit, 1, 2, 1, 1)

        self.AngleSlider_exit = QSlider(self.exit_page)
        self.AngleSlider_exit.setObjectName(u"AngleSlider_exit")
        self.AngleSlider_exit.setMinimum(1)
        self.AngleSlider_exit.setMaximum(89)
        self.AngleSlider_exit.setOrientation(Qt.Vertical)
        self.AngleSlider_exit.setTickPosition(QSlider.TicksAbove)
        self.AngleSlider_exit.setTickInterval(15)

        self.gridLayout_6.addWidget(self.AngleSlider_exit, 0, 1, 1, 1)

        self.AngleLabel_exit = QLabel(self.exit_page)
        self.AngleLabel_exit.setObjectName(u"AngleLabel_exit")
        sizePolicy1.setHeightForWidth(self.AngleLabel_exit.sizePolicy().hasHeightForWidth())
        self.AngleLabel_exit.setSizePolicy(sizePolicy1)
        self.AngleLabel_exit.setFont(font)
        self.AngleLabel_exit.setLayoutDirection(Qt.LeftToRight)
        self.AngleLabel_exit.setTextFormat(Qt.PlainText)
        self.AngleLabel_exit.setAlignment(Qt.AlignCenter)

        self.gridLayout_6.addWidget(self.AngleLabel_exit, 0, 0, 1, 1)


        self.gridLayout_4.addLayout(self.gridLayout_6, 0, 0, 1, 1)

        self.stack.addWidget(self.exit_page)

        self.gridLayout.addWidget(self.stack, 0, 0, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        self.stack.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Zle Ptaki", None))
        self.AngleLabel_1.setText(QCoreApplication.translate("MainWindow", u"Angle", None))
        self.plot_1.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>Level 1</p><p>Number of attempts: 1</p></body></html>", None))
        self.button_1.setText(QCoreApplication.translate("MainWindow", u"Start", None))
        self.ForceLabel_1.setText(QCoreApplication.translate("MainWindow", u"Force", None))
        self.AngleLabel_2.setText(QCoreApplication.translate("MainWindow", u"Angle", None))
        self.plot_2.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>Level 2</p><p>Number of attempts: 3</p></body></html>", None))
        self.button_2.setText(QCoreApplication.translate("MainWindow", u"Start", None))
        self.ForceLabel_2.setText(QCoreApplication.translate("MainWindow", u"Force", None))
        self.plot_exit.setText(QCoreApplication.translate("MainWindow", u"The End", None))
        self.button_exit.setText(QCoreApplication.translate("MainWindow", u"Exit", None))
        self.ForceLabel_exit.setText(QCoreApplication.translate("MainWindow", u"Force", None))
        self.AngleLabel_exit.setText(QCoreApplication.translate("MainWindow", u"Angle", None))
    # retranslateUi

