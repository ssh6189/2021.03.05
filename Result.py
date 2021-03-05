# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Result.ui',
# licensing of 'Result.ui' applies.
#
# Created: Fri Mar  5 10:59:59 2021
#      by: pyside2-uic  running on PySide2 5.13.2
#
# WARNING! All changes made in this file will be lost!

from PySide2 import QtCore, QtGui, QtWidgets

class Ui_Result(object):
    def setupUi(self, Result):
        Result.setObjectName("Result")
        Result.resize(327, 305)
        self.label = QtWidgets.QLabel(Result)
        self.label.setGeometry(QtCore.QRect(60, 32, 61, 20))
        font = QtGui.QFont()
        font.setFamily("3ds")
        font.setPointSize(16)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Result)
        self.label_2.setGeometry(QtCore.QRect(60, 80, 71, 31))
        font = QtGui.QFont()
        font.setFamily("3ds")
        font.setPointSize(16)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(Result)
        self.label_3.setGeometry(QtCore.QRect(60, 132, 61, 20))
        font = QtGui.QFont()
        font.setFamily("3ds")
        font.setPointSize(16)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(Result)
        self.label_4.setGeometry(QtCore.QRect(60, 180, 71, 31))
        font = QtGui.QFont()
        font.setFamily("3ds")
        font.setPointSize(16)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(Result)
        self.label_5.setGeometry(QtCore.QRect(60, 230, 91, 31))
        font = QtGui.QFont()
        font.setFamily("3ds")
        font.setPointSize(16)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.lineEdit = QtWidgets.QLineEdit(Result)
        self.lineEdit.setGeometry(QtCore.QRect(150, 30, 121, 31))
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit_2 = QtWidgets.QLineEdit(Result)
        self.lineEdit_2.setGeometry(QtCore.QRect(150, 80, 121, 31))
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.lineEdit_3 = QtWidgets.QLineEdit(Result)
        self.lineEdit_3.setGeometry(QtCore.QRect(150, 130, 121, 31))
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.lineEdit_4 = QtWidgets.QLineEdit(Result)
        self.lineEdit_4.setGeometry(QtCore.QRect(150, 180, 121, 31))
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.lineEdit_5 = QtWidgets.QLineEdit(Result)
        self.lineEdit_5.setGeometry(QtCore.QRect(150, 230, 121, 31))
        self.lineEdit_5.setObjectName("lineEdit_5")

        self.retranslateUi(Result)
        QtCore.QMetaObject.connectSlotsByName(Result)

    def retranslateUi(self, Result):
        Result.setWindowTitle(QtWidgets.QApplication.translate("Result", "Result", None, -1))
        self.label.setText(QtWidgets.QApplication.translate("Result", "Model", None, -1))
        self.label_2.setText(QtWidgets.QApplication.translate("Result", "Height", None, -1))
        self.label_3.setText(QtWidgets.QApplication.translate("Result", "Width", None, -1))
        self.label_4.setText(QtWidgets.QApplication.translate("Result", "Depth", None, -1))
        self.label_5.setText(QtWidgets.QApplication.translate("Result", "Number", None, -1))

