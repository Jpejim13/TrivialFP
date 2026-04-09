from PySide6.QtWidgets import QApplication, QMainWindow, QStackedWidget, QPushButton, QVBoxLayout, QWidget, QLabel

class PantallaInicio(QWidget):
    def __init__(self, controlador):
        super().__init__()
        layout = QVBoxLayout()
        layout.addWidget(QLabel("ESTÁS EN EL INICIO"))
        
        btn = QPushButton("Ir a Configuración")
        # Usamos una función del controlador para cambiar de pantalla
        btn.clicked.connect(lambda: controlador.setCurrentIndex(1))
        
        layout.addWidget(btn)
        self.setLayout(layout)

class PantallaAjustes(QWidget):
    def __init__(self, controlador):
        super().__init__()
        layout = QVBoxLayout()
        layout.addWidget(QLabel("AJUSTES DEL SISTEMA"))
        
        btn = QPushButton("Volver al Inicio")
        btn.clicked.connect(lambda: controlador.setCurrentIndex(0))
        
        layout.addWidget(btn)
        self.setLayout(layout)

class VentanaPrincipal(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setFixedSize(300, 200)

        # El contenedor mágico
        self.stacked_widget = QStackedWidget()
        
        # Instanciamos las pantallas pasándoles el controlador (el stacked_widget)
        self.pantalla_1 = PantallaInicio(self.stacked_widget)
        self.pantalla_2 = PantallaAjustes(self.stacked_widget)

        # Añadimos las pantallas al stack
        self.stacked_widget.addWidget(self.pantalla_1) # Índice 0
        self.stacked_widget.addWidget(self.pantalla_2) # Índice 1

        self.setCentralWidget(self.stacked_widget)

app = QApplication([])
ventana = VentanaPrincipal()
ventana.show()
app.exec()