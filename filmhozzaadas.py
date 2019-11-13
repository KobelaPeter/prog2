from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QDialog, QMessageBox
import sys

from filmhozzaadas_minta import Ui_Dialog


class BeszurAblak(QDialog, Ui_Dialog):

    def __init__(self,parent=None):
        super(BeszurAblak, self).__init__(parent)
        self.setupUi(self)

        self.alkalmazGomb.clicked.connect(self.accept)
        self.megseGomb.clicked.connect(self.close)
        self.mentesGomb.clicked.connect(self.mentes)

        self.uj = ()

    def mentes(self):
        try:
            cim = (self.cimhozzaadas.text())
            print("cim: ",cim)
            mufaj = self.mufajhozzaadas.text()
            print("mufaj: ",mufaj)
            jatekido = self.jatekidohozzaadas.text()
            print("jatekido: ",jatekido)
            foszereplo = self.foszereplohozzaadas.text()
            print("foszereplo: ",foszereplo)

            self.uj = (cim,mufaj,int(jatekido),foszereplo)
        except:
            QMessageBox.about(self, "Error", "Hibas adatot adtal meg!")

        # print(self.uj)

# app = QtWidgets.QApplication(sys.argv)
# form = Ui_Dialog()
# form.show()
# sys.exit(app.exec_())
