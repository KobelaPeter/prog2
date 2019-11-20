from PyQt5 import QtWidgets
import sys

from PyQt5.QtWidgets import QFileDialog
from PyQt5.QtWidgets import QDialog
from PyQt5.uic.properties import QtGui
from PyQt5.QtWidgets import QMessageBox

from magyarfilmek_minta import Ui_magyarfilmek
from filmhozzaadas import BeszurAblak

class Badtxt(Exception):
    pass


####################################################################################x
class Magyarfilmek(QDialog, Ui_magyarfilmek):
    def __init__(self,parent=None):
        super(Magyarfilmek, self).__init__(parent)
        self.setupUi(self)

        self.osszesfilmgomb.clicked.connect(self.osszeskiir) #kiirja az osszes filmet amiben a mellette megadott szuvegrublikas emberke a foszereplo
        self.torolGomb.clicked.connect(self.osszesfilmkiir.clear)
        self.frendezes.clicked.connect(self.rendezesFoszereplo)  #foszereplo alapjan rendezes
        self.jrendezes.clicked.connect(self.rendezesJatekido)  #jatekido alapjan rendezese
        self.ujfilmhozzaad.clicked.connect(self.hozzaadFilm)
        self.ujfilm.clicked.connect(self.fajlMegnyit) #txt bol menti be a tablazatba a filmeket
        self.kimentes.clicked.connect(self.filmekMenteseFajlba)  # kimenti txt filebe a beirt cuccokat

        self.filmek = []  #osszes filmet tarolja
        self.megnyitottfilmek = [] # ha hibas filet kerunk be kell, hogy kiszedje a listabol
#########################################################################################

    def betoltAdatok(self):
        self.tablazat.setRowCount(len(self.filmek))
        for i in range(len(self.filmek)):
            for j in range(4):
                cella = QtWidgets.QTableWidgetItem()
                cella.setText(str(self.filmek[i][j]))
                self.tablazat.setItem(i, j, cella)


###############################################################################################

    def fajlMegnyit(self):
        try:
            name, _ = QFileDialog.getOpenFileName(self, 'Open File', options=QFileDialog.DontUseNativeDialog)
            with open(name) as f:
                lines = f.readlines()
            lines = [line.rstrip('\n') for line in lines]
            for line in lines:
                while line[len(line)-1] == ' ':
                    line = line[:-1]
                if line[len(line)-1] == ';':
                    line = line[:-1]
                l = line.split(";")
                print(len(l))
                if len(l) != 4:
                    raise Badtxt
                d = ((l[0]),l[1],int((l[2])),(l[3]))
                print("Sor: ",d)
                self.megnyitottfilmek.append(d)
            self.filmek += self.megnyitottfilmek
            self.megnyitottfilmek = []
            self.betoltAdatok()

        except Badtxt:
            QMessageBox.about(self, "Hiba",
                              "Hibas txt allomany,\nvagy nem adtal meg megfelelő fájlt!")
            self.megnyitottfilmek = []

        except ValueError:
            QMessageBox.about(self, "Hiba",
                              "Hibas txt allomany,\nvagy nem adtal meg megfelelő fájlt!\n"
                              "(A Játékidő csak szám lehet!)")
            self.megnyitottfilmek = []

        except:
            pass


#######################################################################################################################

    def hozzaadFilm(self):

        ablak = BeszurAblak()
        if ablak.exec_() == QDialog.Accepted:
            uj = ablak.uj
            if uj:
                print("UJ: ",uj)
                self.tablazat.setRowCount(len(self.filmek) + 1)
                self.filmek.append(uj)
                for j in range(4):
                    cella = QtWidgets.QTableWidgetItem()
                    cella.setText(str(self.filmek[len(self.filmek)-1][j]))
                    self.tablazat.setItem(len(self.filmek)-1, j, cella)
        ablak.deleteLater()

###################################################################################################x


    def filmekMenteseFajlba(self):
        szoveg = ""
        for i in range(len(self.filmek)):
            for j in range(4):
                szoveg += self.tablazat.item(i,j).text() + ";"
            szoveg += "\n"

        with open("Output.txt", "w") as text_file:
            text_file.write(szoveg)


#######################################################################################################

    def rendezesFoszereplo(self):
        print(self.filmek)
        foszereplorendezett = sorted(self.filmek, key=lambda tup: tup[3])
        self.filmek = foszereplorendezett
        self.betoltAdatok()

######################################################################################################

    def rendezesJatekido(self):
        print(self.filmek)
        jatekidorendezett = sorted(self.filmek, key=lambda tup: tup[2])
        self.filmek = jatekidorendezett
        self.betoltAdatok()

######################################################################################################

    def osszeskiir(self):
        tmp = ""
        self.osszesfilmkiir.clear()
        foszereplo = self.osszesfilmbekeres.text()
        foszereplo = foszereplo.upper()
        foszereplo = foszereplo.replace(' ','')
        print(foszereplo)
        for i in self.filmek:
            ii = i[3].upper()
            ii = ii.replace(' ','')
            if ii == foszereplo:
                tmp += i[0] +'\n'

        if tmp == "":
            QMessageBox.about(self, "Error", "A színésznek nincs elérhető filmje HBO Go-n")
        else:
            self.osszesfilmkiir.append(tmp)

#################################################################################################

# app = QtWidgets.QApplication(sys.argv)
# form = Magyarfilmek()
# form.show()
# sys.exit(app.exec_())
