from laberinto import Laberinto
from elemento_laberinto import Pared, Jugador, EspacioLibre, Meta

class LaberintoManager:
    def __init__(self):
        self.laberinto = None

    def cargar_laberinto_desde_archivo(self, archivo):
        """Lógica para cargar el laberinto desde un archivo."""
        with open(archivo, "r") as f:
            lineas = f.readlines()

        # Crear el laberinto
        self.laberinto = Laberinto()

        # Agregar las paredes
        for linea in lineas:
            for caracter in linea:
                if caracter == "1":
                    self.laberinto.agregar_elemento(Pared(caracter))
                elif caracter == "0":
                    self.laberinto.agregar_elemento(EspacioLibre(caracter))
                elif caracter == "X":
                    self.laberinto.agregar_elemento(Jugador(caracter))
                elif caracter == "W":
                    self.laberinto.agregar_elemento(Meta(caracter))

        # Establecer el tamaño del laberinto
        self.laberinto.establecer_tamano(len(lineas), len(lineas[0]))

    def dibujar_laberinto(self):
        """Lógica para dibujar el laberinto."""
        for fila in self.laberinto.obtener_filas():
            for elemento in fila:
                print(elemento.obtener_caracter(), end="")
            print()

  