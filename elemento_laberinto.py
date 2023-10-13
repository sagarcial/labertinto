class ElementoLaberinto:
    def __init__(self, valor):
        self.valor = valor

    def obtener_valor(self):
        return self.valor

    def dibujar_elemento(self):
        # Lógica para dibujar el elemento del laberinto
        pass

class Pared(ElementoLaberinto):
    pass

class Jugador(ElementoLaberinto):
    pass

class EspacioLibre(ElementoLaberinto):
    pass

class Meta(ElementoLaberinto):
    pass
