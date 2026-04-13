import sys
import os
import random
from PySide6 import QtCore, QtGui, QtWidgets
from PySide6.QtCore import QFile
from PySide6.QtUiTools import QUiLoader

# Import de preguntas y clases
from preguntas import preguntas_historia, preguntas_ciencia, preguntas_deportes, PreguntaVerdaderoFalso, PreguntaOpcionMultiple

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
        
        # Lista de botones de la pantalla Kahoot
        self.botones_kahoot = [
            self.window.kahootB1, 
            self.window.kahootB2, 
            self.window.kahootB3, 
            self.window.kahootB4
        ]

        # --- Conexiones de Botones Principales ---
        self.window.BotonJugar.clicked.connect(lambda: self.on_clicked_cambio_pantalla("elegirModo"))
        
        # Botón Modo Kahoot (Opción Múltiple)
        self.window.botonKahoot.clicked.connect(lambda: self.preparar_juego("kahoot"))
        
        # Botón Verdadero o Falso
        self.window.botonExamen.clicked.connect(lambda: self.preparar_juego("vf"))

        # Conectar todos los botones de respuesta a la misma función de verificación
        for btn in self.botones_kahoot:
            btn.clicked.connect(self.verificar_respuesta)

        self.window.show()
        
    def on_clicked_cambio_pantalla(self, pantalla):
        minuscula = pantalla.lower()
        match minuscula:
            case "elegirmodo":
                self.pantallas.setCurrentIndex(1)
            case "salir":
                QtWidgets.QApplication.quit()
            case _:
                print("Comando no reconocido.")

    def preparar_juego(self, modo):
        """
        Filtra las preguntas según el tema del ComboBox y el modo elegido.
        """
        tema = self.window.comboBox.currentText()
        
        # 1. Seleccionar el pool de preguntas por tema
        if tema == "Deportes":
            pool = preguntas_deportes
        elif tema == "Historia":
            pool = preguntas_historia
        else: 
            pool = preguntas_ciencia

        # 2. Filtrar preguntas según el modo (isinstance ayuda a separar las clases)
        if modo == "kahoot":
            self.preguntas_partida = [p for p in pool if isinstance(p, PreguntaOpcionMultiple)]
        elif modo == "vf":
            self.preguntas_partida = [p for p in pool if isinstance(p, PreguntaVerdaderoFalso)]

        # Mezclar y resetear contadores
        random.shuffle(self.preguntas_partida)
        self.indice_pregunta = 0
        self.puntuacion = 0
        
        # Cambiar a la pantalla de juego (pantallaKahoot es la 2)
        if self.preguntas_partida:
            self.pantallas.setCurrentIndex(2)
            self.cargar_pregunta_en_ui()
        else:
            QtWidgets.QMessageBox.warning(self.window, "Aviso", f"No hay preguntas de tipo {modo} para este tema.")

    def cargar_pregunta_en_ui(self):
        pregunta_actual = self.preguntas_partida[self.indice_pregunta]
        
        # Actualizar textos
        self.window.numeroPregunta.setText(f"Pregunta {self.indice_pregunta + 1}")
        self.window.EnunciadoKahoot.setText(pregunta_actual.enunciado)
        
        opciones = pregunta_actual.obtener_opciones()
        
        # Gestionar botones: si hay 2 opciones (V/F), esconde los otros 2 automáticamente
        for i, btn in enumerate(self.botones_kahoot):
            btn.setStyleSheet("") # Limpiar colores de la pregunta anterior
            btn.setEnabled(True)
            
            if i < len(opciones):
                btn.show()
                btn.setText(opciones[i])
            else:
                btn.hide() 

    def verificar_respuesta(self):
        boton_pulsado = self.sender()
        texto_elegido = boton_pulsado.text()
        pregunta_obj = self.preguntas_partida[self.indice_pregunta]
        
        # Desactivar botones para evitar doble clic
        for btn in self.botones_kahoot:
            btn.setEnabled(False)

        if pregunta_obj.verificar(texto_elegido):
            boton_pulsado.setStyleSheet("background-color: #27ae60; color: white; font-weight: bold;")
            self.puntuacion += 10
        else:
            boton_pulsado.setStyleSheet("background-color: #e74c3c; color: white; font-weight: bold;")
            
        self.indice_pregunta += 1
        QtCore.QTimer.singleShot(1200, self.siguiente_paso)

    def siguiente_paso(self):
        if self.indice_pregunta < len(self.preguntas_partida):
            self.cargar_pregunta_en_ui()
        else:
            msg = QtWidgets.QMessageBox(self.window)
            msg.setWindowTitle("Fin de la partida")
            msg.setText(f"¡Juego Terminado!\nPuntuación final: {self.puntuacion}")
            msg.exec()
            self.pantallas.setCurrentIndex(0) # Volver al inicio

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MainWindow()
    sys.exit(app.exec())