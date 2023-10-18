import pygame
import sys

# Colores
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Tamaño de la ventana y celda
WIDTH, HEIGHT = 800, 600
CELL_SIZE = 40

# Define la clase Laberinto
class Laberinto:
    def __init__(self, filename):
        # Carga el laberinto desde el archivo
        self.maze = self.load_maze(filename)
        self.rows = len(self.maze)
        self.cols = len(self.maze[0])

    def load_maze(self, filename):
        # Carga el laberinto desde el archivo de texto
        with open(filename, "r") as file:
            maze = [list(line.strip()) for line in file]
        return maze

    def draw(self, screen):
        for row in range(self.rows):
            for col in range(self.cols):
                if self.maze[row][col] == '1':
                    pygame.draw.rect(screen, BLACK, (col * CELL_SIZE, row * CELL_SIZE, CELL_SIZE, CELL_SIZE))
                elif self.maze[row][col] == '0':
                    pygame.draw.rect(screen, WHITE, (col * CELL_SIZE, row * CELL_SIZE, CELL_SIZE, CELL_SIZE))
                # Agregar más condiciones para dibujar 'X' y 'W' si lo deseas

# Define la clase Personaje
class Personaje:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def draw(self, screen):
        pygame.draw.rect(screen, (255, 0, 0), (self.x * CELL_SIZE, self.y * CELL_SIZE, CELL_SIZE, CELL_SIZE))

# Define la clase Meta
class Meta:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def draw(self, screen):
        pygame.draw.rect(screen, (0, 255, 0), (self.x * CELL_SIZE, self.y * CELL_SIZE, CELL_SIZE, CELL_SIZE))

# Define la clase Juego
class Juego:
    def __init__(self, laberinto, personaje, meta):
        self.laberinto = laberinto
        self.personaje = personaje
        self.meta = meta

    def run(self):
        pygame.init()
        screen = pygame.display.set_mode((WIDTH, HEIGHT))
        pygame.display.set_caption("Laberinto Pygame")

        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

            keys = pygame.key.get_pressed()
            if keys[pygame.K_LEFT]:
                # Mueve al personaje hacia la izquierda
                pass  # Agrega la lógica de movimiento
            elif keys[pygame.K_RIGHT]:
                # Mueve al personaje hacia la derecha
                pass  # Agrega la lógica de movimiento
            elif keys[pygame.K_UP]:
                # Mueve al personaje hacia arriba
                pass  # Agrega la lógica de movimiento
            elif keys[pygame.K_DOWN]:
                # Mueve al personaje hacia abajo
                pass  # Agrega la lógica de movimiento

            screen.fill((255, 255, 255))
            self.laberinto.draw(screen)
            self.personaje.draw(screen)
            self.meta.draw(screen)
            pygame.display.update()

if __name__ == "__main__":
    laberinto = Laberinto("laberinto.txt")
    personaje = Personaje(1, 1)  # Inicializa con la posición inicial del personaje
    meta = Meta(5, 5)  # Cambia las coordenadas según tu laberinto
    juego = Juego(laberinto, personaje, meta)
    juego.run()
