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
        self.gridLayout_1 = QGridLayout()
        self.gridLayout_1.setObjectName(u"gridLayout_1")
        self.AngleLabel = QLabel(self.centralwidget)
        self.AngleLabel.setObjectName(u"AngleLabel")
        sizePolicy1 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Expanding)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.AngleLabel.sizePolicy().hasHeightForWidth())
        self.AngleLabel.setSizePolicy(sizePolicy1)
        font = QFont()
        font.setPointSize(12)
        self.AngleLabel.setFont(font)
        self.AngleLabel.setLayoutDirection(Qt.LeftToRight)
        self.AngleLabel.setTextFormat(Qt.PlainText)
        self.AngleLabel.setAlignment(Qt.AlignCenter)

        self.gridLayout_1.addWidget(self.AngleLabel, 0, 0, 1, 1)

        self.AngleSlider = QSlider(self.centralwidget)
        self.AngleSlider.setObjectName(u"AngleSlider")
        self.AngleSlider.setMinimum(1)
        self.AngleSlider.setMaximum(89)
        self.AngleSlider.setOrientation(Qt.Vertical)
        self.AngleSlider.setTickPosition(QSlider.TicksAbove)
        self.AngleSlider.setTickInterval(15)

        self.gridLayout_1.addWidget(self.AngleSlider, 0, 1, 1, 1)

        self.plot = QLabel(self.centralwidget)
        self.plot.setObjectName(u"plot")
        sizePolicy.setHeightForWidth(self.plot.sizePolicy().hasHeightForWidth())
        self.plot.setSizePolicy(sizePolicy)
        font1 = QFont()
        font1.setPointSize(24)
        self.plot.setFont(font1)
        self.plot.setFrameShape(QFrame.Box)
        self.plot.setScaledContents(True)
        self.plot.setAlignment(Qt.AlignCenter)

        self.gridLayout_1.addWidget(self.plot, 0, 2, 1, 1)

        self.button = QPushButton(self.centralwidget)
        self.button.setObjectName(u"button")
        sizePolicy2 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.button.sizePolicy().hasHeightForWidth())
        self.button.setSizePolicy(sizePolicy2)

        self.gridLayout_1.addWidget(self.button, 1, 0, 2, 2)

        self.ForceSlider = QSlider(self.centralwidget)
        self.ForceSlider.setObjectName(u"ForceSlider")
        self.ForceSlider.setMinimum(1)
        self.ForceSlider.setMaximum(100)
        self.ForceSlider.setOrientation(Qt.Horizontal)
        self.ForceSlider.setTickPosition(QSlider.TicksBelow)
        self.ForceSlider.setTickInterval(25)

        self.gridLayout_1.addWidget(self.ForceSlider, 1, 2, 1, 1)

        self.ForceLabel = QLabel(self.centralwidget)
        self.ForceLabel.setObjectName(u"ForceLabel")
        sizePolicy3 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.ForceLabel.sizePolicy().hasHeightForWidth())
        self.ForceLabel.setSizePolicy(sizePolicy3)
        self.ForceLabel.setFont(font)
        self.ForceLabel.setAlignment(Qt.AlignCenter)

        self.gridLayout_1.addWidget(self.ForceLabel, 2, 2, 1, 1)


        self.gridLayout.addLayout(self.gridLayout_1, 0, 0, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Zle Ptaki", None))
        self.AngleLabel.setText(QCoreApplication.translate("MainWindow", u"Angle", None))
        self.plot.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>Level 1</p><p>Number of attempts: 1</p></body></html>", None))
        self.button.setText(QCoreApplication.translate("MainWindow", u"Start", None))
        self.ForceLabel.setText(QCoreApplication.translate("MainWindow", u"Force", None))
    # retranslateUi

