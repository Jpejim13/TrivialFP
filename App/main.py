import sys
import os
import random
from PySide6 import QtCore, QtGui, QtWidgets
from PySide6.QtCore import QFile
from PySide6.QtUiTools import QUiLoader

#import de preguntas
from preguntas import preguntas_historia, preguntas_ciencia, preguntas_deportes, PreguntaVerdaderoFalso

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
        self.preguntas_partida = []
        self.indice_pregunta = 0
        self.puntuacion = 0
        
        # Guardado de bototnes 
        self.botones_kahoot = [
            self.window.kahootB1, 
            self.window.kahootB2, 
            self.window.kahootB3, 
            self.window.kahootB4
        ]

        self.window.BotonJugar.clicked.connect(lambda: self.on_clicked_cambio_pantalla("elegirModo"))
        self.window.botonKahoot.clicked.connect(lambda: self.on_clicked_cambio_pantalla("pantallaKahoot"))
        #debemos poner el lambda para poder pasar un argumento
        

        for btn in self.botones_kahoot:
            btn.clicked.connect(self.verificar_respuesta)

        self.window.show()
        
    def on_clicked_cambio_pantalla(self, pantalla):
        minuscula = pantalla.lower()
        match minuscula:
            case "elegirmodo":
                self.pantallas.setCurrentIndex(1)
            case "pantallakahoot":
                self.preparar_juego()
                self.pantallas.setCurrentIndex(2)
            case "salir":
                QtWidgets.QApplication.quit()
            case _:
                print("Comando no reconocido.")

    def preparar_juego(self):

        tema = self.window.comboBox.currentText()
        

        if tema == "Deportes":
            self.preguntas_partida = preguntas_deportes.copy()
        elif tema == "Historia":
            self.preguntas_partida = preguntas_historia.copy()
        else: 
            self.preguntas_partida = preguntas_ciencia.copy()
        

        random.shuffle(self.preguntas_partida)
        self.indice_pregunta = 0
        self.puntuacion = 0
        

        self.cargar_pregunta_en_ui()

    def cargar_pregunta_en_ui(self):

        pregunta_actual = self.preguntas_partida[self.indice_pregunta]
        

        self.window.numeroPregunta.setText(f"Pregunta {self.indice_pregunta + 1}")
        self.window.EnunciadoKahoot.setText(pregunta_actual.enunciado)
        
 
        opciones = pregunta_actual.obtener_opciones()
        

        for i, btn in enumerate(self.botones_kahoot):
            btn.setStyleSheet("") 
            if i < len(opciones):
                btn.show()
                btn.setText(opciones[i])
            else:
                btn.hide() 

    def verificar_respuesta(self):
        boton_pulsado = self.sender()
        texto_elegido = boton_pulsado.text()
        pregunta_obj = self.preguntas_partida[self.indice_pregunta]
        
        if pregunta_obj.verificar(texto_elegido):
            boton_pulsado.setStyleSheet("background-color: green; color: white;")
            self.puntuacion += 10
        else:
            boton_pulsado.setStyleSheet("background-color: red; color: white;")
            

        self.indice_pregunta += 1
        QtCore.QTimer.singleShot(1500, self.siguiente_paso)#delay para q el user vea el resultado

    def siguiente_paso(self):
        if self.indice_pregunta < len(self.preguntas_partida):
            self.cargar_pregunta_en_ui()
        else:
            msg = QtWidgets.QMessageBox()
            msg.setText(f"¡Juego Terminado!\nPuntuación final: {self.puntuacion}")
            msg.exec()
            self.pantallas.setCurrentIndex(0)

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MainWindow()
    sys.exit(app.exec())