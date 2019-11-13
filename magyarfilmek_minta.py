# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'magyarfilmek.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_magyarfilmek(object):
    def setupUi(self, magyarfilmek):
        magyarfilmek.setObjectName("magyarfilmek")
        magyarfilmek.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(magyarfilmek)
        self.centralwidget.setObjectName("centralwidget")
        self.tablazat = QtWidgets.QTableWidget(self.centralwidget)
        self.tablazat.setGeometry(QtCore.QRect(10, 370, 561, 171))
        self.tablazat.setObjectName("tablazat")
        self.tablazat.setColumnCount(4)
        self.tablazat.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tablazat.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tablazat.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tablazat.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tablazat.setHorizontalHeaderItem(3, item)
        self.osszesfilmgomb = QtWidgets.QPushButton(self.centralwidget)
        self.osszesfilmgomb.setGeometry(QtCore.QRect(580, 280, 161, 41))
        self.osszesfilmgomb.setObjectName("osszesfilmgomb")
        self.osszesfilmkiir = QtWidgets.QTextBrowser(self.centralwidget)
        self.osszesfilmkiir.setGeometry(QtCore.QRect(510, 20, 256, 192))
        self.osszesfilmkiir.setObjectName("osszesfilmkiir")
        self.frendezes = QtWidgets.QPushButton(self.centralwidget)
        self.frendezes.setGeometry(QtCore.QRect(10, 250, 191, 41))
        self.frendezes.setObjectName("frendezes")
        self.jrendezes = QtWidgets.QPushButton(self.centralwidget)
        self.jrendezes.setGeometry(QtCore.QRect(10, 310, 191, 41))
        self.jrendezes.setObjectName("jrendezes")
        self.kimentes = QtWidgets.QPushButton(self.centralwidget)
        self.kimentes.setGeometry(QtCore.QRect(590, 470, 191, 41))
        self.kimentes.setObjectName("kimentes")
        self.ujfilm = QtWidgets.QPushButton(self.centralwidget)
        self.ujfilm.setGeometry(QtCore.QRect(590, 370, 191, 41))
        self.ujfilm.setObjectName("ujfilm")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(410, 20, 101, 41))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(470, 240, 111, 16))
        self.label_2.setObjectName("label_2")
        self.ujfilmhozzaad = QtWidgets.QPushButton(self.centralwidget)
        self.ujfilmhozzaad.setGeometry(QtCore.QRect(590, 420, 191, 41))
        self.ujfilmhozzaad.setObjectName("ujfilmhozzaad")
        self.textBrowser = QtWidgets.QTextBrowser(self.centralwidget)
        self.textBrowser.setGeometry(QtCore.QRect(10, 10, 311, 221))
        self.textBrowser.setObjectName("textBrowser")
        self.osszesfilmbekeres = QtWidgets.QLineEdit(self.centralwidget)
        self.osszesfilmbekeres.setGeometry(QtCore.QRect(570, 230, 181, 41))
        self.osszesfilmbekeres.setObjectName("osszesfilmbekeres")
        self.torolGomb = QtWidgets.QPushButton(self.centralwidget)
        self.torolGomb.setGeometry(QtCore.QRect(430, 170, 71, 41))
        self.torolGomb.setObjectName("torolGomb")
        # magyarfilmek.setCentralWidget(self.centralwidget)
        # self.menubar = QtWidgets.QMenuBar(magyarfilmek)
        # self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 26))
        # self.menubar.setObjectName("menubar")
        # magyarfilmek.setMenuBar(self.menubar)
        # self.statusbar = QtWidgets.QStatusBar(magyarfilmek)
        # self.statusbar.setObjectName("statusbar")
        # magyarfilmek.setStatusBar(self.statusbar)

        self.retranslateUi(magyarfilmek)
        QtCore.QMetaObject.connectSlotsByName(magyarfilmek)

    def retranslateUi(self, magyarfilmek):
        _translate = QtCore.QCoreApplication.translate
        magyarfilmek.setWindowTitle(_translate("magyarfilmek", "MainWindow"))
        item = self.tablazat.horizontalHeaderItem(0)
        item.setText(_translate("magyarfilmek", "Cím"))
        item = self.tablazat.horizontalHeaderItem(1)
        item.setText(_translate("magyarfilmek", "Műfaj"))
        item = self.tablazat.horizontalHeaderItem(2)
        item.setText(_translate("magyarfilmek", "Játékidő"))
        item = self.tablazat.horizontalHeaderItem(3)
        item.setText(_translate("magyarfilmek", "Főszereplő"))
        self.osszesfilmgomb.setText(_translate("magyarfilmek", "Főszereplő összes filmje"))
        self.osszesfilmkiir.setHtml(_translate("magyarfilmek", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:7.8pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))
        self.frendezes.setText(_translate("magyarfilmek", "Foszereplo alapjan rendezes"))
        self.jrendezes.setText(_translate("magyarfilmek", "Jatekido alapjan rendezes"))
        self.kimentes.setText(_translate("magyarfilmek", "Kimentes .TXT fileba"))
        self.ujfilm.setText(_translate("magyarfilmek", "Uj Filmek beszurasa .TXT-ből"))
        self.label.setText(_translate("magyarfilmek", "Összes Filmje:"))
        self.label_2.setText(_translate("magyarfilmek", "Főszereplő neve:"))
        self.ujfilmhozzaad.setText(_translate("magyarfilmek", "Uj Film hozzaadasa"))
        self.textBrowser.setHtml(_translate("magyarfilmek", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:7.8pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:26pt; font-weight:600;\">HBO GO</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:26pt; font-style:italic;\">Magyar Szinkronos Filmek</span></p></body></html>"))
        self.torolGomb.setText(_translate("magyarfilmek", "Torles"))
