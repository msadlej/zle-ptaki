# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'zle_ptaki.ui'
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
            MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1095, 875)
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        sizePolicy.setHeightForWidth(
            self.centralwidget.sizePolicy().hasHeightForWidth()
        )
        self.centralwidget.setSizePolicy(sizePolicy)
        self.gridLayout = QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.gridLayout_1 = QGridLayout()
        self.gridLayout_1.setObjectName("gridLayout_1")
        self.button = QPushButton(self.centralwidget)
        self.button.setObjectName("button")
        sizePolicy.setHeightForWidth(self.button.sizePolicy().hasHeightForWidth())
        self.button.setSizePolicy(sizePolicy)

        self.gridLayout_1.addWidget(self.button, 2, 0, 2, 2)

        self.AngleSpinBox = QSpinBox(self.centralwidget)
        self.AngleSpinBox.setObjectName("AngleSpinBox")
        sizePolicy.setHeightForWidth(self.AngleSpinBox.sizePolicy().hasHeightForWidth())
        self.AngleSpinBox.setSizePolicy(sizePolicy)
        self.AngleSpinBox.setReadOnly(True)
        self.AngleSpinBox.setButtonSymbols(QAbstractSpinBox.NoButtons)

        self.gridLayout_1.addWidget(self.AngleSpinBox, 1, 0, 1, 1)

        self.ForceLabel = QLabel(self.centralwidget)
        self.ForceLabel.setObjectName("ForceLabel")
        sizePolicy1 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.ForceLabel.sizePolicy().hasHeightForWidth())
        self.ForceLabel.setSizePolicy(sizePolicy1)
        font = QFont()
        font.setPointSize(12)
        self.ForceLabel.setFont(font)
        self.ForceLabel.setAlignment(Qt.AlignCenter)

        self.gridLayout_1.addWidget(self.ForceLabel, 3, 3, 1, 1)

        self.ForceSlider = QSlider(self.centralwidget)
        self.ForceSlider.setObjectName("ForceSlider")
        self.ForceSlider.setMinimum(1)
        self.ForceSlider.setMaximum(100)
        self.ForceSlider.setOrientation(Qt.Horizontal)
        self.ForceSlider.setTickPosition(QSlider.TicksBelow)
        self.ForceSlider.setTickInterval(25)

        self.gridLayout_1.addWidget(self.ForceSlider, 2, 2, 1, 2)

        self.AngleSlider = QSlider(self.centralwidget)
        self.AngleSlider.setObjectName("AngleSlider")
        self.AngleSlider.setMinimum(1)
        self.AngleSlider.setMaximum(89)
        self.AngleSlider.setOrientation(Qt.Vertical)
        self.AngleSlider.setTickPosition(QSlider.TicksAbove)
        self.AngleSlider.setTickInterval(15)

        self.gridLayout_1.addWidget(self.AngleSlider, 0, 1, 2, 1)

        self.ForceSpinBox = QSpinBox(self.centralwidget)
        self.ForceSpinBox.setObjectName("ForceSpinBox")
        sizePolicy.setHeightForWidth(self.ForceSpinBox.sizePolicy().hasHeightForWidth())
        self.ForceSpinBox.setSizePolicy(sizePolicy)
        self.ForceSpinBox.setReadOnly(True)
        self.ForceSpinBox.setButtonSymbols(QAbstractSpinBox.NoButtons)
        self.ForceSpinBox.setMaximum(100)

        self.gridLayout_1.addWidget(self.ForceSpinBox, 3, 2, 1, 1)

        self.plot = QLabel(self.centralwidget)
        self.plot.setObjectName("plot")
        sizePolicy2 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.plot.sizePolicy().hasHeightForWidth())
        self.plot.setSizePolicy(sizePolicy2)
        font1 = QFont()
        font1.setPointSize(24)
        self.plot.setFont(font1)
        self.plot.setAutoFillBackground(False)
        self.plot.setFrameShape(QFrame.Box)
        self.plot.setScaledContents(True)
        self.plot.setAlignment(Qt.AlignCenter)
        self.plot.setIndent(-1)

        self.gridLayout_1.addWidget(self.plot, 0, 2, 2, 2)

        self.AngleLabel = QLabel(self.centralwidget)
        self.AngleLabel.setObjectName("AngleLabel")
        sizePolicy3 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Expanding)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.AngleLabel.sizePolicy().hasHeightForWidth())
        self.AngleLabel.setSizePolicy(sizePolicy3)
        self.AngleLabel.setFont(font)
        self.AngleLabel.setLayoutDirection(Qt.LeftToRight)
        self.AngleLabel.setTextFormat(Qt.AutoText)
        self.AngleLabel.setAlignment(Qt.AlignCenter)

        self.gridLayout_1.addWidget(self.AngleLabel, 0, 0, 1, 1)

        self.gridLayout.addLayout(self.gridLayout_1, 0, 0, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)

    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(
            QCoreApplication.translate("MainWindow", "Zle Ptaki", None)
        )
        self.button.setText(QCoreApplication.translate("MainWindow", "Start", None))
        self.ForceLabel.setText(
            QCoreApplication.translate(
                "MainWindow",
                "<html><head/><body><p>Force 1% - 100%</p></body></html>",
                None,
            )
        )
        self.plot.setText(QCoreApplication.translate("MainWindow", "Hello", None))
        self.AngleLabel.setText(
            QCoreApplication.translate(
                "MainWindow",
                "<html><head/><body><p>Angle</p><p>1\u00b0 - 89\u00b0</p></body></html>",
                None,
            )
        )

    # retranslateUi
