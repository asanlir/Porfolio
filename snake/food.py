import pygame
import random
from constants import TAM_CELDA, COMIDA, ESPECIAL

class Comida:
    def __init__(self):
        self.posicion = [0, 0]
        self.generar()

    def generar(self):
        self.posicion = [
            random.randint(0, (800 - TAM_CELDA) // TAM_CELDA) * TAM_CELDA,
            random.randint(0, (600 - TAM_CELDA) // TAM_CELDA) * TAM_CELDA
        ]

    def dibujar(self, pantalla):
        pygame.draw.rect(pantalla, COMIDA, pygame.Rect(self.posicion[0], self.posicion[1], TAM_CELDA, TAM_CELDA))

class ComidaEspecial:
    def __init__(self):
        self.posicion = [0, 0]
        self.esta_activo = False
        self.timer = 0

    def generar(self):
        self.posicion = [
            random.randint(0, (800 - TAM_CELDA) // TAM_CELDA) * TAM_CELDA,
            random.randint(0, (600 - TAM_CELDA) // TAM_CELDA) * TAM_CELDA
        ]
        self.esta_activo = True
        self.timer = pygame.time.get_ticks()  # Iniciar el temporizador

    def comprobar_tiempo(self):
        if self.esta_activo and (pygame.time.get_ticks() - self.timer > 5000):  # 5 segundos
            self.esta_activo = False

    def dibujar(self, pantalla):
        if self.esta_activo:
            pygame.draw.circle(pantalla, ESPECIAL, (self.posicion[0] + TAM_CELDA // 2, self.posicion[1] + TAM_CELDA // 2), TAM_CELDA // 2)