import pygame

from constants import SERPIENTE, ANCHO, ALTO

class Serpiente:
    def __init__(self):
        self.cuerpo = [[100, 100], [80, 100], [60, 100]]  # Posición inicial de la serpiente
        self.direccion = 'DERECHA'
        self.creciendo = False
        self.color = SERPIENTE # Define el color de la serpiente

    def mover(self):
        cabeza_x, cabeza_y = self.cuerpo[0]
        if self.direccion == 'DERECHA':
            cabeza_x += 20
        elif self.direccion == 'IZQUIERDA':
            cabeza_x -= 20
        elif self.direccion == 'ARRIBA':
            cabeza_y -= 20
        elif self.direccion == 'ABAJO':
            cabeza_y += 20

        # Inserta la nueva cabeza
        self.cuerpo.insert(0, [cabeza_x, cabeza_y])

        # Si no está creciendo, elimina la última parte
        if not self.creciendo:
            self.cuerpo.pop()
        else:
            self.creciendo = False

    def cambiar_direccion(self, nueva_direccion):
        if (nueva_direccion == 'DERECHA' and self.direccion != 'IZQUIERDA') or \
           (nueva_direccion == 'IZQUIERDA' and self.direccion != 'DERECHA') or \
           (nueva_direccion == 'ARRIBA' and self.direccion != 'ABAJO') or \
           (nueva_direccion == 'ABAJO' and self.direccion != 'ARRIBA'):
            self.direccion = nueva_direccion

    def crecer(self):
        self.creciendo = True

    def dibujar(self, pantalla):
        for segmento in self.cuerpo:
            pygame.draw.rect(pantalla, self.color, pygame.Rect(segmento[0], segmento[1], 20, 20))

    def colision(self):
        # Verifica si la cabeza de la serpiente colisiona con las paredes o consigo misma
        cabeza = self.cuerpo[0]
        return (cabeza[0] < 0 or cabeza[0] >= ANCHO or cabeza[1] < 0 or cabeza[1] >= ALTO or
                self.cuerpo[0] in self.cuerpo[1:])  # Colisión con sí misma
