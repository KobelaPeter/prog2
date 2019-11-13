# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'filmhozzaadas.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(327, 361)
        self.centralwidget = QtWidgets.QWidget(Dialog)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(30, 20, 55, 16))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(30, 80, 55, 16))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(30, 140, 90, 16))
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(30, 200, 71, 16))
        self.label_4.setObjectName("label_4")
        self.alkalmazGomb = QtWidgets.QPushButton(self.centralwidget)
        self.alkalmazGomb.setGeometry(QtCore.QRect(20, 230, 101, 41))
        self.alkalmazGomb.setObjectName("alkalmazGomb")
        self.megseGomb = QtWidgets.QPushButton(self.centralwidget)
        self.megseGomb.setGeometry(QtCore.QRect(130, 280, 61, 28))
        self.megseGomb.setObjectName("megseGomb")
        self.mentesGomb = QtWidgets.QPushButton(self.centralwidget)
        self.mentesGomb.setGeometry(QtCore.QRect(210, 230, 101, 41))
        self.mentesGomb.setObjectName("mentesGomb")
        self.cimhozzaadas = QtWidgets.QLineEdit(self.centralwidget)
        self.cimhozzaadas.setGeometry(QtCore.QRect(140, 10, 151, 31))
        self.cimhozzaadas.setObjectName("cimhozzaadas")
        self.mufajhozzaadas = QtWidgets.QLineEdit(self.centralwidget)
        self.mufajhozzaadas.setGeometry(QtCore.QRect(140, 71, 151, 31))
        self.mufajhozzaadas.setObjectName("mufajhozzaadas")
        self.jatekidohozzaadas = QtWidgets.QLineEdit(self.centralwidget)
        self.jatekidohozzaadas.setGeometry(QtCore.QRect(140, 130, 151, 31))
        self.jatekidohozzaadas.setObjectName("jatekidohozzaadas")
        self.foszereplohozzaadas = QtWidgets.QLineEdit(self.centralwidget)
        self.foszereplohozzaadas.setGeometry(QtCore.QRect(140, 190, 151, 31))
        self.foszereplohozzaadas.setObjectName("foszereplohozzaadas")
        # Dialog.setCentralWidget(self.centralwidget)
        # self.menubar = QtWidgets.QMenuBar(Dialog)
        # self.menubar.setGeometry(QtCore.QRect(0, 0, 327, 26))
        # self.menubar.setObjectName("menubar")
        # Dialog.setMenuBar(self.menubar)
        # self.statusbar = QtWidgets.QStatusBar(Dialog)
        # self.statusbar.setObjectName("statusbar")
        # Dialog.setStatusBar(self.statusbar)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "MainWindow"))
        self.label.setText(_translate("Dialog", "Cím:"))
        self.label_2.setText(_translate("Dialog", "Műfaj:"))
        self.label_3.setText(_translate("Dialog", "Játékidő:"))
        self.label_4.setText(_translate("Dialog", "Főszereplő:"))
        self.alkalmazGomb.setText(_translate("Dialog", "Beillesztes"))
        self.megseGomb.setText(_translate("Dialog", "Megse"))
        self.mentesGomb.setText(_translate("Dialog", "Mentes"))
