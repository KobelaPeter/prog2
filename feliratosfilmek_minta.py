# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'feliratosfilmek.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_feliratosablak(object):
    def setupUi(self, feliratosablak):
        feliratosablak.setObjectName("feliratosablak")
        feliratosablak.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(feliratosablak)
        self.centralwidget.setObjectName("centralwidget")
        self.textEdit = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit.setGeometry(QtCore.QRect(360, 130, 361, 321))
        self.textEdit.setObjectName("textEdit")
        self.filmeklista = QtWidgets.QListWidget(self.centralwidget)
        self.filmeklista.setGeometry(QtCore.QRect(30, 130, 211, 321))
        self.filmeklista.setObjectName("filmeklista")
        item = QtWidgets.QListWidgetItem()
        self.filmeklista.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.filmeklista.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.filmeklista.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.filmeklista.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.filmeklista.addItem(item)
        self.leirasGomb = QtWidgets.QPushButton(self.centralwidget)
        self.leirasGomb.setGeometry(QtCore.QRect(60, 460, 131, 51))
        self.leirasGomb.setObjectName("leirasGomb")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(30, 80, 101, 41))
        self.label.setObjectName("label")
        self.torlesGomb = QtWidgets.QPushButton(self.centralwidget)
        self.torlesGomb.setGeometry(QtCore.QRect(470, 460, 131, 51))
        self.torlesGomb.setObjectName("torlesGomb")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(360, 100, 55, 16))
        self.label_2.setObjectName("label_2")
        self.textBrowser = QtWidgets.QTextBrowser(self.centralwidget)
        self.textBrowser.setGeometry(QtCore.QRect(140, 10, 511, 61))
        self.textBrowser.setObjectName("textBrowser")
        # feliratosablak.setCentralWidget(self.centralwidget)
        # self.menubar = QtWidgets.QMenuBar(feliratosablak)
        # self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 26))
        # self.menubar.setObjectName("menubar")
        # feliratosablak.setMenuBar(self.menubar)
        # self.statusbar = QtWidgets.QStatusBar(feliratosablak)
        # self.statusbar.setObjectName("statusbar")
        # feliratosablak.setStatusBar(self.statusbar)

        self.retranslateUi(feliratosablak)
        QtCore.QMetaObject.connectSlotsByName(feliratosablak)

    def retranslateUi(self, feliratosablak):
        _translate = QtCore.QCoreApplication.translate
        feliratosablak.setWindowTitle(_translate("feliratosablak", "MainWindow"))
        __sortingEnabled = self.filmeklista.isSortingEnabled()
        self.filmeklista.setSortingEnabled(False)
        item = self.filmeklista.item(0)
        item.setText(_translate("feliratosablak", "A remény rabjai"))
        item = self.filmeklista.item(1)
        item.setText(_translate("feliratosablak", "Forrest Gump"))
        item = self.filmeklista.item(2)
        item.setText(_translate("feliratosablak", "Halálsoron"))
        item = self.filmeklista.item(3)
        item.setText(_translate("feliratosablak", "Szerelmünk lapjai"))
        item = self.filmeklista.item(4)
        item.setText(_translate("feliratosablak", "Életrevalók"))
        self.filmeklista.setSortingEnabled(__sortingEnabled)
        self.leirasGomb.setText(_translate("feliratosablak", "Leírás"))
        self.label.setText(_translate("feliratosablak", "Feliratos Filmek:"))
        self.torlesGomb.setText(_translate("feliratosablak", "Film Törlése"))
        self.label_2.setText(_translate("feliratosablak", "Leírás:"))
        self.textBrowser.setHtml(_translate("feliratosablak", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:7.8pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:18pt; font-weight:600;\">HBO GO Magyar Feliratos Filmek</span></p></body></html>"))
