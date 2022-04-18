import os
import sys
import PyQt5
import webbrowser
from PyPDF2 import PdfFileReader



from PyQt5 import uic, QtWidgets, QtGui
from PyQt5.QtWidgets import QApplication, QWidget, QInputDialog, QLineEdit, QFileDialog, QMessageBox

Ui_MainWindow, QtBaseClass = uic.loadUiType('contafolio.ui')


class MyApp(QtWidgets.QMainWindow, Ui_MainWindow):

    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)
        self.setWindowTitle("Contador de folios GIGHA")
        self.pushButton.clicked.connect(self.moreskia)
        self.lcdNumber
        self.textBrowser
        
        
             
       
        """self.commandLinkButton.clicked.connect(lambda: webbrowser.open('https://github.com/normanagudelo/ContaFolios'))"""
       
    def moreskia(self):
        self.dir_path = QFileDialog.getExistingDirectory(self, "Elige una ruta de descarga", "E:\\")
        print(self.dir_path)
        contenido = os.listdir(f"{self.dir_path}")
        print(contenido)
        numeropaginas=0
                
        for documento in contenido:
           
            try:
                reader = PdfFileReader(f"{self.dir_path}"+"/"+f"{documento}",'rb')
                self.textBrowser.append(f"{documento}"+"   --->   "+f"paginas:{reader.numPages}")
                numeropaginas += reader.numPages
                print(numeropaginas)
                self.lcdNumber.display(numeropaginas)

            except:
                self.textBrowser.append(f"{documento}   --->   esta averiado, encriptado o no es tipo PDF.")

                
            
        
        
        
    
            

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MyApp()
    window.show()
    app.exec_()
