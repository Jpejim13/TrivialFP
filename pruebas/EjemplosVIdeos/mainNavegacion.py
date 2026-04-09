import sys
import os
from PySide6 import QtCore, QtGui, QtWidgets
from PySide6.QtCore import QFile
from PySide6.QtUiTools import QUiLoader

class MainWindow(QtCore.QObject):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        
        current_dir = os.path.dirname(__file__)
        ui_path = os.path.join(current_dir, "Navegacion.ui")

        ui_file = QFile(ui_path)
        if not ui_file.open(QFile.ReadOnly):
            print(f"No se pudo abrir el archivo en: {ui_path}")
            return

        loader = QUiLoader()
        self.window = loader.load(ui_file)
        ui_file.close()

        # IMPORTANTE: En tu UI se llama "Mazo"
        self.mazo = self.window.Mazo
        self.mazo.setCurrentIndex(0)

        # Conexiones de botones
        self.window.sig.clicked.connect(self.on_clicked_siguiente)
        self.window.sig2.clicked.connect(self.on_clicked_siguiente)
        self.window.ant.clicked.connect(self.on_clicked_atras)
        self.window.ant2.clicked.connect(self.on_clicked_atras)
        
        self.window.show()
        
    def on_clicked_siguiente(self):
        # Obtenemos el índice actual directamente del Mazo
        idx = self.mazo.currentIndex()
        # Solo avanzamos si no es la última página
        if idx < self.mazo.count() - 1:
            self.mazo.setCurrentIndex(idx + 1)

    def on_clicked_atras(self):
        idx = self.mazo.currentIndex()
        # Solo retrocedemos si no es la primera página (0)
        if idx > 0:
            self.mazo.setCurrentIndex(idx - 1)

app = QtWidgets.QApplication(sys.argv)
window = MainWindow()
sys.exit(app.exec())