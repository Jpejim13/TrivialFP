import sys
import os
import random
from PySide6 import QtCore, QtGui, QtWidgets
from PySide6.QtCore import QFile
from PySide6.QtUiTools import QUiLoader

# Importaciones de tus clases de preguntas (asumo que están en preguntas.py)
from preguntas import preguntas_historia, preguntas_ciencia, preguntas_deportes, PreguntaVerdaderoFalso, PreguntaOpcionMultiple, PreguntaProximal

class MainWindow(QtCore.QObject):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        
        # --- CARGA DE UI ---
        current_dir = os.path.dirname(__file__)
        ui_path = os.path.join(current_dir, "juego.ui")
        ui_file = QFile(ui_path)
        if not ui_file.open(QFile.ReadOnly):
            print("No se pudo abrir el archivo UI")
            return
        loader = QUiLoader()
        self.window = loader.load(ui_file)
        ui_file.close()

        # --- VARIABLES DE ESTADO ---
        self.pantallas = self.window.pantallas
        self.pantallas.setCurrentIndex(0)
        
        self.preguntas_partida = []
        self.indice_pregunta = 0
        self.puntuacion = 0
        self.aciertos = 0
        self.fallos = 0
        self.modo_actual = ""
        
        self.botones_kahoot = [
            self.window.kahootB1, 
            self.window.kahootB2, 
            self.window.kahootB3, 
            self.window.kahootB4
        ]

        # --- CONEXIONES DE BOTONES (PANTALLA INICIO Y MODOS) ---
        self.window.BotonJugar.clicked.connect(lambda: self.on_clicked_cambio_pantalla("elegirModo"))
        self.window.botonKahoot.clicked.connect(lambda: self.preparar_juego("kahoot"))
        self.window.botonExamen.clicked.connect(lambda: self.preparar_juego("vf"))
        self.window.BotonAcercarse.clicked.connect(lambda: self.preparar_juego("proximal"))

        # --- CONEXIONES JUEGO ---
        for btn in self.botones_kahoot:
            btn.clicked.connect(self.verificar_respuesta)

        self.window.botonResponderProximal.clicked.connect(self.verificar_respuesta_proximal)
        self.window.sliderProximal.valueChanged.connect(self.actualizar_label_slider)

        # --- CONEXIONES PANTALLA ESTADÍSTICAS ---
        # Botón "Guardar Estadísticas" (pushButton en tu .ui)
        self.window.pushButton.clicked.connect(self.guardar_estadisticas_dialogo)
        # Botón "Volver a jugar" (pushButton_2 en tu .ui)
        self.window.pushButton_2.clicked.connect(lambda: self.pantallas.setCurrentIndex(0))

        self.window.show()
        
    def on_clicked_cambio_pantalla(self, pantalla):
        minuscula = pantalla.lower()
        if minuscula == "elegirmodo":
            self.pantallas.setCurrentIndex(1)
        elif minuscula == "salir":
            QtWidgets.QApplication.quit()

    def preparar_juego(self, modo):
        tema = self.window.comboBox.currentText()
        
        if tema == "Deportes":
            pool = preguntas_deportes
        elif tema == "Historia":
            pool = preguntas_historia
        else: 
            pool = preguntas_ciencia

        self.modo_actual = modo
        
        if modo == "kahoot":
            self.preguntas_partida = [p for p in pool if isinstance(p, PreguntaOpcionMultiple)]
        elif modo == "vf":
            self.preguntas_partida = [p for p in pool if isinstance(p, PreguntaVerdaderoFalso)]
        elif modo == "proximal":
            self.preguntas_partida = [p for p in pool if isinstance(p, PreguntaProximal)]

        random.shuffle(self.preguntas_partida)
        
        # Reiniciar contadores para nueva partida
        self.indice_pregunta = 0
        self.puntuacion = 0
        self.aciertos = 0
        self.fallos = 0
        
        if self.preguntas_partida:
            if modo == "proximal":
                self.pantallas.setCurrentIndex(3)
                self.cargar_pregunta_proximal()
            else:
                self.pantallas.setCurrentIndex(2)
                self.cargar_pregunta_en_ui()
        else:
            QtWidgets.QMessageBox.warning(self.window, "Aviso", f"No hay preguntas de tipo {modo} para este tema.")

    def cargar_pregunta_en_ui(self):
        pregunta_actual = self.preguntas_partida[self.indice_pregunta]
        self.window.numeroPregunta.setText(f"Pregunta {self.indice_pregunta + 1}")
        self.window.EnunciadoKahoot.setText(pregunta_actual.enunciado)
        
        opciones = pregunta_actual.obtener_opciones()
        for i, btn in enumerate(self.botones_kahoot):
            btn.setStyleSheet("")
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
        
        for btn in self.botones_kahoot:
            btn.setEnabled(False)

        if pregunta_obj.verificar(texto_elegido):
            boton_pulsado.setStyleSheet("background-color: #27ae60; color: white; font-weight: bold;")
            self.puntuacion += 10
            self.aciertos += 1
        else:
            boton_pulsado.setStyleSheet("background-color: #e74c3c; color: white; font-weight: bold;")
            self.fallos += 1
            
        self.indice_pregunta += 1
        QtCore.QTimer.singleShot(1000, self.siguiente_paso)

    def siguiente_paso(self):
        if self.indice_pregunta < len(self.preguntas_partida):
            self.cargar_pregunta_en_ui()
        else:
            self.mostrar_fin_partida()

    def cargar_pregunta_proximal(self):
        pregunta_actual = self.preguntas_partida[self.indice_pregunta]
        self.window.botonResponderProximal.setEnabled(True)
        self.window.botonResponderProximal.setStyleSheet("background-color: #46178F; color: white; border-radius: 10px;")
        
        self.window.EnunciadoProximal.setText(pregunta_actual.enunciado)
        self.window.sliderProximal.setMinimum(pregunta_actual.min_val)
        self.window.sliderProximal.setMaximum(pregunta_actual.max_val)
        
        valor_medio = (pregunta_actual.min_val + pregunta_actual.max_val) // 2
        self.window.sliderProximal.setValue(valor_medio)
        self.actualizar_label_slider(valor_medio)

    def actualizar_label_slider(self, valor):
        self.window.valorSlider.setText(f"Año seleccionado: {valor}")

    def verificar_respuesta_proximal(self):
        self.window.botonResponderProximal.setEnabled(False)
        pregunta_obj = self.preguntas_partida[self.indice_pregunta]
        respuesta_usuario = self.window.sliderProximal.value()
        
        if pregunta_obj.verificar(respuesta_usuario):
            self.window.botonResponderProximal.setStyleSheet("background-color: #27ae60; color: white; border-radius: 10px;")
            self.puntuacion += 10
            self.aciertos += 1
        else:
            self.window.botonResponderProximal.setStyleSheet("background-color: #e74c3c; color: white; border-radius: 10px;")
            self.fallos += 1
            
        self.indice_pregunta += 1
        QtCore.QTimer.singleShot(1500, self.siguiente_paso_proximal)

    def siguiente_paso_proximal(self):
        if self.indice_pregunta < len(self.preguntas_partida):
            self.cargar_pregunta_proximal()
        else:
            self.mostrar_fin_partida()

    def mostrar_fin_partida(self):
        # 1. Actualizar textos en la pantalla de estadísticas (Índice 4)
        total = self.aciertos + self.fallos
        self.window.NumeroTotalPreguntas.setText(f"Preguntas respondidas: {total}")
        self.window.PreguntasAcertadas.setText(f"Aciertos: {self.aciertos}")
        self.window.PreguntasFalladas.setText(f"Fallos: {self.fallos}")
        self.window.PuntuacionFinal.setText(f"Puntuación final: {self.puntuacion}")

        # 2. Cambiar a la pantalla de estadísticas
        self.pantallas.setCurrentIndex(4)

    def guardar_estadisticas_dialogo(self):
        # Cuadro de diálogo para guardar archivo
        nombre_archivo, _ = QtWidgets.QFileDialog.getSaveFileName(
            self.window,
            "Guardar mis estadísticas",
            "",
            "Archivo de Texto (*.txt);;Todos los archivos (*)"
        )

        if nombre_archivo:
            # Si no tiene extensión .txt, se la ponemos
            if not nombre_archivo.lower().endswith(".txt"):
                nombre_archivo += ".txt"

            try:
                with open(nombre_archivo, "w", encoding="utf-8") as f:
                    f.write("--- RESUMEN DE PARTIDA CLICKTHON ---\n")
                    f.write(f"Modo jugado: {self.modo_actual.capitalize()}\n")
                    f.write(f"Total preguntas: {self.aciertos + self.fallos}\n")
                    f.write(f"Aciertos: {self.aciertos}\n")
                    f.write(f"Fallos: {self.fallos}\n")
                    f.write(f"PUNTUACIÓN TOTAL: {self.puntuacion}\n")
                
                QtWidgets.QMessageBox.information(self.window, "Éxito", "Estadísticas guardadas correctamente.")
            except Exception as e:
                QtWidgets.QMessageBox.critical(self.window, "Error", f"No se pudo guardar: {e}")

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MainWindow()
    sys.exit(app.exec())