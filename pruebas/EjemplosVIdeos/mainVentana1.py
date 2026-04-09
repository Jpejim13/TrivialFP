import sys
import os # Importante añadir esto
from PySide6 import QtCore, QtGui, QtWidgets
from PySide6.QtCore import QFile
from PySide6.QtUiTools import QUiLoader

class MainWindow(QtCore.QObject):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.contador = 0

        # Obtener la ruta absoluta del directorio donde está este script
        current_dir = os.path.dirname(__file__)
        ui_path = os.path.join(current_dir, "mainwindow.ui")

        # Cargar el archivo con la ruta completa
        ui_file = QFile(ui_path)
        if not ui_file.open(QFile.ReadOnly):
            print(f"No se pudo abrir el archivo en: {ui_path}")
            return

        loader = QUiLoader()
        self.window = loader.load(ui_file)
        ui_file.close() # Es buena práctica cerrarlo
        
        self.window.pulsador1.clicked.connect(self.on_clicked)
        self.contador = 0
        self.window.show()
        
    def on_clicked(self):

        self.window.etiqueta.setText("contador : {0}".format(self.contador))
        self.contador = self.contador + 1 

        

app = QtWidgets.QApplication(sys.argv)
window = MainWindow()
sys.exit(app.exec())