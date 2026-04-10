import random # Necesitaremos esta librería

preguntas_trivial = [
    {
        "pregunta": "¿En qué año llegó el hombre a la Luna?",
        "opciones": ["1965", "1969", "1972", "1958"],
        "correcta": "1969"
    },
    {
        "pregunta": "¿Cuál es el río más largo del mundo?",
        "opciones": ["Nilo", "Misisipi", "Amazonas", "Yangtsé"],
        "correcta": "Amazonas"
    },
    {
        "pregunta": "¿Qué elemento químico tiene el símbolo 'O'?",
        "opciones": ["Oro", "Osmio", "Oxígeno", "Hierro"],
        "correcta": "Oxígeno"
    },
    {
        "pregunta": "¿Quién pintó 'La última cena'?",
        "opciones": ["Picasso", "Miguel Ángel", "Leonardo da Vinci", "Dalí"],
        "correcta": "Leonardo da Vinci"
    },
    {
        "pregunta": "¿Cuál es el planeta más grande de nuestro sistema solar?",
        "opciones": ["Saturno", "Neptuno", "Júpiter", "Marte"],
        "correcta": "Júpiter"
    },
    {
        "pregunta": "¿En qué continente se encuentra el desierto del Sahara?",
        "opciones": ["Asia", "África", "América", "Oceanía"],
        "correcta": "África"
    },
    {
        "pregunta": "¿Qué país tiene forma de bota?",
        "opciones": ["España", "Grecia", "Italia", "Portugal"],
        "correcta": "Italia"
    },
    {
        "pregunta": "¿Cuántos huesos tiene el cuerpo humano adulto?",
        "opciones": ["180", "206", "215", "300"],
        "correcta": "206"
    },
    {
        "pregunta": "¿Cuál es el océano más grande del mundo?",
        "opciones": ["Atlántico", "Índico", "Ártico", "Pacífico"],
        "correcta": "Pacífico"
    },
    {
        "pregunta": "¿Quién escribió 'Don Quijote de la Mancha'?",
        "opciones": ["Lorca", "Quevedo", "Cervantes", "Góngora"],
        "correcta": "Cervantes"
    },
    {
        "pregunta": "¿Qué instrumento toca Lisa Simpson?",
        "opciones": ["Clarinete", "Violín", "Saxofón", "Flauta"],
        "correcta": "Saxofón"
    },
    {
        "pregunta": "¿Cuál es la moneda oficial de Japón?",
        "opciones": ["Yuan", "Yen", "Won", "Dólar"],
        "correcta": "Yen"
    },
    {
        "pregunta": "¿En qué país se inventó la pizza?",
        "opciones": ["Francia", "Italia", "EE.UU.", "México"],
        "correcta": "Italia"
    },
    {
        "pregunta": "¿Cuál es el animal terrestre más rápido?",
        "opciones": ["León", "Gacela", "Guepardo", "Tigre"],
        "correcta": "Guepardo"
    },
    {
        "pregunta": "¿Cómo se llama el proceso por el cual las plantas fabrican su alimento?",
        "opciones": ["Respiración", "Fotosíntesis", "Oxidación", "Transpiración"],
        "correcta": "Fotosíntesis"
    },
    {
        "pregunta": "¿Qué gas necesitan los humanos para respirar?",
        "opciones": ["Nitrógeno", "Dióxido de carbono", "Hidrógeno", "Oxígeno"],
        "correcta": "Oxígeno"
    },
    {
        "pregunta": "¿Cuál es el metal más caro del mundo?",
        "opciones": ["Oro", "Platino", "Rodio", "Paladio"],
        "correcta": "Rodio"
    },
    {
        "pregunta": "¿A qué temperatura hierve el agua a nivel del mar?",
        "opciones": ["90°C", "100°C", "120°C", "80°C"],
        "correcta": "100°C"
    },
    {
        "pregunta": "¿Quién fue el primer presidente de Estados Unidos?",
        "opciones": ["Abraham Lincoln", "Thomas Jefferson", "George Washington", "John Adams"],
        "correcta": "George Washington"
    },
    {
        "pregunta": "¿Cuál es el país más poblado del mundo?",
        "opciones": ["India", "China", "Rusia", "Brasil"],
        "correcta": "India"
    }
]

# Antes de empezar el juego, barajamos las preguntas
random.shuffle(preguntas_trivial)

print(preguntas_trivial[opciones[3]])
