from PyQt5 import QtWidgets
import sys
import datetime

from PyQt5.QtWidgets import QDialog, QFileDialog
from PyQt5.uic.properties import QtGui

from feliratosfilmek_minta import Ui_feliratosablak

class FeliratosFilmek(QDialog, Ui_feliratosablak):

    def __init__(self,parent=None):
        super(FeliratosFilmek, self).__init__(parent)
        self.setupUi(self)
        self.leirasGomb.clicked.connect(self.leiras)
        self.torlesGomb.clicked.connect(self.torles)


    def leiras(self):
        print(self.filmeklista.currentItem().text())
        if self.filmeklista.currentItem().text() == "A remény rabjai":
            self.textEdit.clear()
            self.textEdit.append("{}: \n\nAmerikai filmdráma \n137 perc\n1994\nFőszereplők:\nTim Robbins, Morgan Freeman, Bob Gunton ".format(self.filmeklista.currentItem().text()))
        if self.filmeklista.currentItem().text() == "Forrest Gump":
            self.textEdit.clear()
            self.textEdit.append("{}: \n\nAmerikai filmszatíra \n141 perc\n1994\nFőszereplők:\nTom Hnaks, Sally Field, Robin Wright".format(self.filmeklista.currentItem().text()))
        if self.filmeklista.currentItem().text() == "Halálsoron":
            self.textEdit.clear()
            self.textEdit.append("{}: \n\nAmerikai fantasztikus thriller \n188 perc\n1999\nFőszereplők:\nTom Hanks, Michael Clarke Duncan, David Morse".format(self.filmeklista.currentItem().text()))
        if self.filmeklista.currentItem().text() == "Szerelmünk lapjai":
            self.textEdit.clear()
            self.textEdit.append("{}: \n\nAmerikai romantikus film \n123 perc\n2004\nFőszereplők:\nRachel McAdams, Ryan Gosling, Gena Rowlands".format(self.filmeklista.currentItem().text()))
        if self.filmeklista.currentItem().text() == "Életrevalók":
            self.textEdit.clear()
            self.textEdit.append("{}: \n\nFrancia vígjáték \n107perc\n2011\nFőszereplők:\nFrancois Cluzet, Omar Sy, Anne Le Ny ".format(self.filmeklista.currentItem().text()))


    def torles(self):
        torol = self.filmeklista.takeItem(self.filmeklista.currentRow())
        torol = None


# app = QtWidgets.QApplication(sys.argv)
# form = FeliratosFilmek()
# form.show()
# sys.exit(app.exec_())