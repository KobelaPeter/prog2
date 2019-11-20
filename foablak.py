from PyQt5 import QtWidgets
import sys

from feliratosfilmek import FeliratosFilmek
from magyarfilmek import Magyarfilmek
from foablak_minta import Ui_MainWindow


class FoAblak(QtWidgets.QMainWindow, Ui_MainWindow):

    def __init__(self, parent=None):
        super(FoAblak, self).__init__(parent)
        self.setupUi(self)
        self.szinkronosfilmek.clicked.connect(self.megnyitszinkronosfilmek)
        self.feliratosfilmek.clicked.connect(self.megnyitfeliratosfilmek)

    def megnyitszinkronosfilmek(ss):
        global f
        f = Magyarfilmek()
        f.setModal(True)
        f.show()


    def megnyitfeliratosfilmek(self):
         global f
         f = FeliratosFilmek()
         f.setModal(True)
         f.show()

app = QtWidgets.QApplication(sys.argv)
form = FoAblak()
form.show()
sys.exit(app.exec_())