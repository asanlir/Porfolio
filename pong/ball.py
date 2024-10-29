import random
import pygame
from constants import ALTO, ANCHO, TAMAÑO_PELOTA, VELOCIDAD_PELOTA

class Pelota:
    def __init__(self):
        self.rect = pygame.Rect(ANCHO // 2, ALTO // 2, TAMAÑO_PELOTA, TAMAÑO_PELOTA)
        self.velocidad_inicial = VELOCIDAD_PELOTA
        self.vel_x = random.choice([-self.velocidad_inicial, self.velocidad_inicial])
        self.vel_y = random.choice([-self.velocidad_inicial, self.velocidad_inicial])
        self.incremento_velocidad = 1.05  # Incremento del 5%

    def mover(self):
        self.rect.x += self.vel_x
        self.rect.y += self.vel_y

        # Rebote con los bordes superior e inferior
        if self.rect.top <= 0 or self.rect.bottom >= ALTO:
            self.vel_y = -self.vel_y

    def reiniciar(self, aumentar_velocidad=False):
        """ Reinicia la posición de la pelota y ajusta la velocidad según quién anote """
        self.rect.center = (ANCHO // 2, ALTO // 2)
        # Si el jugador anota, aumenta la velocidad; si la IA anota, reinicia la velocidad
        if aumentar_velocidad:
            self.vel_x *= self.incremento_velocidad if self.vel_x > 0 else -self.incremento_velocidad
            self.vel_y *= self.incremento_velocidad if self.vel_y > 0 else -self.incremento_velocidad
        else:
            self.vel_x = random.choice([-self.velocidad_inicial, self.velocidad_inicial])
            self.vel_y = random.choice([-self.velocidad_inicial, self.velocidad_inicial])

    def colision_paleta(self, paleta):
        if self.rect.colliderect(paleta.rect):
            self.vel_x = -self.vel_x

    def dibujar(self, pantalla):
        pygame.draw.ellipse(pantalla, (255, 255, 255), self.rect)
