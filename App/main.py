import sys
import os
from PySide6 import QtCore, QtGui, QtWidgets
from PySide6.QtCore import QFile
from PySide6.QtUiTools import QUiLoader

class MainWindow(QtCore.QObject):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        
        current_dir = os.path.dirname(__file__)
        ui_path = os.path.join(current_dir, "juego.ui")

        ui_file = QFile(ui_path)
        if not ui_file.open(QFile.ReadOnly):
            print(f"No se pudo abrir el archivo en: {ui_path}")
            return

        loader = QUiLoader()
        self.window = loader.load(ui_file)
        ui_file.close()

        self.pantallas = self.window.pantallas
        self.pantallas.setCurrentIndex(0)

        # Conexiones de botones
        self.window.BotonJugar.clicked.connect(lambda: self.on_clicked_cambio_pantalla("elegirModo"))
        self.window.botonKahoot.clicked.connect(lambda: self.on_clicked_cambio_pantalla("pantallaKahoot"))

        #se lo pasamos como la lambda pq por defecto la funcion on clicked pasa true o false entonces no podriamos meterle el argumento "elegir modo", la funcion
        #lambda nos permite pasarle el string 

        self.window.show()
        
        
    def on_clicked_cambio_pantalla(self,pantalla):
        minuscula = pantalla.lower()
        match minuscula: # Sin paréntesis aquí
            case "elegirmodo": # Importante: comparamos contra minúsculas
                self.pantallas.setCurrentIndex(1)
            case "pantallakahoot":
                 self.pantallas.setCurrentIndex(2)
            case "salir":
                print("Cerrando aplicación.")
            case _:
                print("Comando no reconocido.")
        

app = QtWidgets.QApplication(sys.argv)
window = MainWindow()
sys.exit(app.exec())