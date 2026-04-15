import random

class Pregunta:
    def __init__(self, enunciado, correcta):
        self.enunciado = enunciado
        self.correcta = correcta

    def verificar(self, respuesta_usuario):
        return str(respuesta_usuario).strip().lower() == str(self.correcta).strip().lower()

class PreguntaOpcionMultiple(Pregunta):
    def __init__(self, enunciado, opciones, correcta):
        super().__init__(enunciado, correcta)
        self.opciones = opciones

    def obtener_opciones(self):
        lista = self.opciones.copy()
        random.shuffle(lista)
        return lista

class PreguntaVerdaderoFalso(Pregunta):
    def __init__(self, enunciado, correcta):
        super().__init__(enunciado, correcta)
        self.opciones = ["Verdadero", "Falso"]

    def obtener_opciones(self):
        return self.opciones

class PreguntaProximal(Pregunta):
    def __init__(self, enunciado, correcta, min_val, max_val):
        super().__init__(enunciado, correcta)
        self.min_val = min_val
        self.max_val = max_val

    def verificar(self, respuesta_usuario):
        diferencia = abs(int(respuesta_usuario) - int(self.correcta))
        return diferencia <= 2

preguntas_historia = [
    PreguntaOpcionMultiple("¿En qué año comenzó la Primera Guerra Mundial?", ["1914", "1918", "1939", "1912"], "1914"),
    PreguntaOpcionMultiple("¿Quién fue el primer emperador romano?", ["Julio César", "Augusto", "Nerón", "Calígula"], "Augusto"),
    PreguntaOpcionMultiple("¿Qué civilización construyó las pirámides de Giza?", ["Maya", "Inca", "Egipcia", "Griega"], "Egipcia"),
    PreguntaOpcionMultiple("¿En qué ciudad cayó el muro en 1989?", ["Praga", "Varsovia", "Berlín", "Viena"], "Berlín"),
    PreguntaOpcionMultiple("¿Quién era el rey de Macedonia que conquistó el Imperio Persa?", ["Filipo II", "Alejandro Magno", "Pericles", "Leónidas"], "Alejandro Magno"),
    PreguntaOpcionMultiple("¿Qué país regaló la Estatua de la Libertad a EE. UU.?", ["Reino Unido", "Francia", "España", "Alemania"], "Francia"),
    PreguntaOpcionMultiple("¿En qué año se descubrió América?", ["1492", "1500", "1488", "1498"], "1492"),
    PreguntaOpcionMultiple("¿Cuál era la capital del Imperio Inca?", ["Cuzco", "Lima", "Quito", "Machu Picchu"], "Cuzco"),
    PreguntaOpcionMultiple("¿Qué reina gobernó Inglaterra durante 63 años en el siglo XIX?", ["Isabel I", "Victoria", "Ana", "Isabel II"], "Victoria"),
    PreguntaOpcionMultiple("¿En qué país nació Adolf Hitler?", ["Alemania", "Austria", "Polonia", "Hungría"], "Austria"),
    PreguntaOpcionMultiple("¿Qué nombre recibían los guerreros de élite del Japón feudal?", ["Ninja", "Samurái", "Shogun", "Ronin"], "Samurái"),
    PreguntaOpcionMultiple("¿Cuál fue la moneda de España antes del Euro?", ["Peseta", "Escudo", "Real", "Doblón"], "Peseta"),
    PreguntaOpcionMultiple("¿Quién fue el líder de la Revolución Rusa de 1917?", ["Stalin", "Trotsky", "Lenin", "Nicolás II"], "Lenin"),
    PreguntaOpcionMultiple("¿Qué guerra duró realmente 116 años?", ["Guerra de los 30 años", "Guerra de los 100 años", "Guerra de Secesión", "Guerra de las Rosas"], "Guerra de los 100 años"),
    PreguntaOpcionMultiple("¿En qué ciudad se firmó la Constitución española de 1812?", ["Madrid", "Sevilla", "Cádiz", "Barcelona"], "Cádiz"),
    PreguntaVerdaderoFalso("¿Napoleón Bonaparte era extremadamente bajo para su época?", "Falso"),
    PreguntaVerdaderoFalso("¿La Revolución Francesa comenzó en 1789?", "Verdadero"),
    PreguntaVerdaderoFalso("¿Cleopatra era de origen egipcio puro?", "Falso"),
    PreguntaVerdaderoFalso("¿Los vikingos usaban cascos con cuernos?", "Falso"),
    PreguntaVerdaderoFalso("¿La peste negra mató a un tercio de la población europea?", "Verdadero"),
    PreguntaVerdaderoFalso("¿Cristóbal Colón fue el primer europeo en llegar a América?", "Falso"),
    PreguntaVerdaderoFalso("¿El Titanic se hundió en su viaje inaugural?", "Verdadero"),
    PreguntaVerdaderoFalso("¿La Gran Muralla China es visible desde la Luna a simple vista?", "Falso"),
    PreguntaVerdaderoFalso("¿Juana de Arco murió quemada en la hoguera?", "Verdadero"),
    PreguntaVerdaderoFalso("¿La Unión Soviética fue el primer país en enviar un hombre al espacio?", "Verdadero"),
    PreguntaVerdaderoFalso("¿El Imperio Romano de Oriente duró hasta 1453?", "Verdadero"),
    PreguntaVerdaderoFalso("¿La bomba atómica se usó por primera vez en la Primera Guerra Mundial?", "Falso"),
    PreguntaVerdaderoFalso("¿Atila era el líder de los Hunos?", "Verdadero"),
    PreguntaVerdaderoFalso("¿El Renacimiento comenzó en Italia?", "Verdadero"),
    PreguntaVerdaderoFalso("¿Abraham Lincoln fue asesinado en un teatro?", "Verdadero"),
    PreguntaProximal("¿En qué año cayó el Imperio Romano de Occidente?", 476, 300, 600),
    PreguntaProximal("¿En qué año llegó el hombre a la Luna?", 1969, 1900, 2020)
]

preguntas_ciencia = [
    PreguntaOpcionMultiple("¿Cuál es el planeta más cercano al Sol?", ["Venus", "Marte", "Mercurio", "Tierra"], "Mercurio"),
    PreguntaOpcionMultiple("¿Qué órgano del cuerpo humano consume más energía?", ["Corazón", "Hígado", "Cerebro", "Músculos"], "Cerebro"),
    PreguntaOpcionMultiple("¿Cuál es el animal más grande del planeta?", ["Elefante", "Ballena Azul", "Tiburón Ballena", "Calamar Gigante"], "Ballena Azul"),
    PreguntaOpcionMultiple("¿Cómo se llama la sustancia que da color verde a las plantas?", ["Hemoglobina", "Melanina", "Clorofila", "Caroteno"], "Clorofila"),
    PreguntaOpcionMultiple("¿Qué tipo de animal es una orca?", ["Pez", "Reptil", "Mamífero", "Anfibio"], "Mamífero"),
    PreguntaOpcionMultiple("¿Cuál es el elemento más abundante en el universo?", ["Oxígeno", "Helio", "Nitrógeno", "Hidrógeno"], "Hidrógeno"),
    PreguntaOpcionMultiple("¿Cuántos corazones tiene un pulpo?", ["Uno", "Dos", "Tres", "Ocho"], "Tres"),
    PreguntaOpcionMultiple("¿Qué vitamina obtenemos principalmente del Sol?", ["Vitamina C", "Vitamina A", "Vitamina D", "Vitamina B12"], "Vitamina D"),
    PreguntaOpcionMultiple("¿Cuál es el mineral más duro de la Tierra?", ["Cuarzo", "Diamante", "Grafito", "Zafiro"], "Diamante"),
    PreguntaOpcionMultiple("¿Qué gas exhalamos los humanos al respirar?", ["Oxígeno", "Dióxido de carbono", "Metano", "Ozono"], "Dióxido de carbono"),
    PreguntaOpcionMultiple("¿Cómo se llama el centro de un átomo?", ["Electrón", "Neutrón", "Núcleo", "Protón"], "Núcleo"),
    PreguntaOpcionMultiple("¿Cuál es la velocidad de la luz (aprox)?", ["300.000 km/s", "150.000 km/s", "1.000.000 km/s", "340 m/s"], "300.000 km/s"),
    PreguntaOpcionMultiple("¿Qué animal es conocido como el 'Rey de la Selva'?", ["Tigre", "Gorila", "León", "Elefante"], "León"),
    PreguntaOpcionMultiple("¿A qué grupo pertenecen las arañas?", ["Insectos", "Arácnidos", "Crustáceos", "Moluscos"], "Arácnidos"),
    PreguntaOpcionMultiple("¿Cuál es el único metal líquido a temperatura ambiente?", ["Plomo", "Mercurio", "Aluminio", "Cobre"], "Mercurio"),
    PreguntaVerdaderoFalso("¿El sonido viaja más rápido en el agua que en el aire?", "Verdadero"),
    PreguntaVerdaderoFalso("¿Los delfines duermen con un ojo abierto?", "Verdadero"),
    PreguntaVerdaderoFalso("¿Los tomates son verduras?", "Falso"),
    PreguntaVerdaderoFalso("¿Un año luz es una unidad de tiempo?", "Falso"),
    PreguntaVerdaderoFalso("¿Los tiburones no tienen huesos?", "Verdadero"),
    PreguntaVerdaderoFalso("¿El cuerpo humano tiene 4 pulmones?", "Falso"),
    PreguntaVerdaderoFalso("¿Venus es el planeta más caliente del sistema solar?", "Verdadero"),
    PreguntaVerdaderoFalso("¿Los murciélagos son ciegos?", "Falso"),
    PreguntaVerdaderoFalso("¿El ADN tiene forma de doble hélice?", "Verdadero"),
    PreguntaVerdaderoFalso("¿La luz del Sol tarda unos 8 minutos en llegar a la Tierra?", "Verdadero"),
    PreguntaVerdaderoFalso("¿Los pingüinos viven en el Polo Norte?", "Falso"),
    PreguntaVerdaderoFalso("¿El nitrógeno es el gas más abundante en la atmósfera terrestre?", "Verdadero"),
    PreguntaVerdaderoFalso("¿Las ballenas son peces?", "Falso"),
    PreguntaVerdaderoFalso("¿El cero absoluto es 0 grados Celsius?", "Falso"),
    PreguntaVerdaderoFalso("¿Las abejas pueden ver el color rojo?", "Falso"),
    PreguntaProximal("¿En qué año propuso Einstein la Teoría de la Relatividad General?", 1915, 1850, 1950)
]

preguntas_deportes = [
    PreguntaOpcionMultiple("¿Cuántos jugadores tiene un equipo de fútbol en el campo?", ["10", "11", "12", "9"], "11"),
    PreguntaOpcionMultiple("¿Cada cuántos años se celebran los Juegos Olímpicos?", ["2", "4", "5", "6"], "4"),
    PreguntaOpcionMultiple("¿En qué ciudad se juegan los partidos del Real Madrid?", ["Barcelona", "Madrid", "Valencia", "Sevilla"], "Madrid"),
    PreguntaOpcionMultiple("¿Qué deporte practica Rafael Nadal?", ["Fútbol", "Baloncesto", "Tenis", "Golf"], "Tenis"),
    PreguntaOpcionMultiple("¿Cómo se llama el premio al máximo goleador en la liga española?", ["Zamora", "Pichichi", "Balón de Oro", "Bota de Oro"], "Pichichi"),
    PreguntaOpcionMultiple("¿Cuántos tiempos tiene un partido de baloncesto NBA?", ["2", "3", "4", "1"], "4"),
    PreguntaOpcionMultiple("¿Qué país ha ganado más Mundiales de Fútbol?", ["Alemania", "Italia", "Brasil", "Argentina"], "Brasil"),
    PreguntaOpcionMultiple("¿En qué deporte se usa un 'puck'?", ["Hockey sobre hierba", "Hockey sobre hielo", "Lacrosse", "Polo"], "Hockey sobre hielo"),
    PreguntaOpcionMultiple("¿Cuánto mide una maratón?", ["21 km", "42.195 km", "10 km", "50 km"], "42.195 km"),
    PreguntaOpcionMultiple("¿Quién es considerado el mejor jugador de baloncesto de la historia?", ["Kobe Bryant", "LeBron James", "Michael Jordan", "Shaquille O'Neal"], "Michael Jordan"),
    PreguntaOpcionMultiple("¿Qué color de jersey lleva el líder del Tour de Francia?", ["Verde", "Amarillo", "Rojo", "Blanco"], "Amarillo"),
    PreguntaOpcionMultiple("¿En qué ciudad se celebraron los JJ.OO. de 1992?", ["Madrid", "Barcelona", "Atenas", "Londres"], "Barcelona"),
    PreguntaOpcionMultiple("¿Cómo se llama el estadio del FC Barcelona?", ["Santiago Bernabéu", "Camp Nou", "Metropolitano", "Mestalla"], "Camp Nou"),
    PreguntaOpcionMultiple("¿Qué selección ganó el Mundial de Catar 2022?", ["Francia", "Croacia", "Argentina", "Marruecos"], "Argentina"),
    PreguntaOpcionMultiple("¿En qué deporte se hacen 'strikes'?", ["Tenis", "Bolos", "Béisbol", "Golf"], "Bolos"),
    PreguntaVerdaderoFalso("¿Un partido de rugby dura 80 minutos?", "Verdadero"),
    PreguntaVerdaderoFalso("¿Michael Phelps es el atleta con más medallas olímpicas?", "Verdadero"),
    PreguntaVerdaderoFalso("¿En el tenis, el término 'Love' significa cero puntos?", "Verdadero"),
    PreguntaVerdaderoFalso("¿El golf es originario de Escocia?", "Verdadero"),
    PreguntaVerdaderoFalso("¿La NBA se juega con un balón blanco y negro?", "Falso"),
    PreguntaVerdaderoFalso("¿España ganó el Mundial de Fútbol en 2010?", "Verdadero"),
    PreguntaVerdaderoFalso("¿El bádminton se juega con una pelota de goma?", "Falso"),
    PreguntaVerdaderoFalso("¿Usain Bolt tiene el récord mundial de 100 metros lisos?", "Verdadero"),
    PreguntaVerdaderoFalso("¿En el béisbol, un 'home run' vale 5 puntos?", "Falso"),
    PreguntaVerdaderoFalso("¿El Giro de Italia es una competición de motociclismo?", "Falso"),
    PreguntaVerdaderoFalso("¿Un combate de boxeo profesional tiene 12 asaltos?", "Verdadero"),
    PreguntaVerdaderoFalso("¿Pelé nunca ganó un Mundial con Brasil?", "Falso"),
    PreguntaVerdaderoFalso("¿El Waterpolo se juega en una piscina?", "Verdadero"),
    PreguntaVerdaderoFalso("¿Lionel Messi ha ganado 8 Balones de Oro?", "Verdadero"),
    PreguntaVerdaderoFalso("¿El Super Bowl es la final de la liga de fútbol americano?", "Verdadero"),
    PreguntaProximal("¿En qué año se celebraron los primeros Juegos Olímpicos modernos?", 1896, 1800, 2000)
]