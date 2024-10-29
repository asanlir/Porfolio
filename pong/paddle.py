import random
import pygame
from constants import ALTO, ANCHO_PALETA, ALTO_PALETA, VELOCIDAD_PALETA

class Paleta:
    def __init__(self, x, y, es_ia=False):
        self.rect = pygame.Rect(x, y, ANCHO_PALETA, ALTO_PALETA)
        self.es_ia = es_ia
        self.probabilidad_seguir = 0.90  # 90% de probabilidad de seguir la bola

    def mover(self, arriba, abajo):
        if arriba and self.rect.top > 0:
            self.rect.y -= VELOCIDAD_PALETA
        if abajo and self.rect.bottom < ALTO:
            self.rect.y += VELOCIDAD_PALETA

    def mover_ia(self, pelota):
        # Determina si la IA seguirá la bola basado en la probabilidad
        if random.random() < self.probabilidad_seguir:
            objetivo_y = pelota.rect.centery  # Objetivo es la posición Y de la bola

            # La IA se mueve hacia el objetivo
            if objetivo_y < self.rect.centery and self.rect.top > 0:
                self.rect.y -= VELOCIDAD_PALETA
            elif objetivo_y > self.rect.centery and self.rect.bottom < ALTO:
                self.rect.y += VELOCIDAD_PALETA

    def dibujar(self, pantalla):
        pygame.draw.rect(pantalla, (255, 255, 255), self.rect)
