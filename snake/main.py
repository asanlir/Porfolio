import random
import pygame
import time
from constants import ANCHO, ALTO, VELOCIDAD, FONDO
from snake import Serpiente
from food import Comida, ComidaEspecial

# Inicializa Pygame
pygame.init()

# Configura la pantalla
pantalla = pygame.display.set_mode((ANCHO, ALTO))
pygame.display.set_caption("Snake")

# Inicializa el reloj y la velocidad de la serpiente
reloj = pygame.time.Clock()
velocidad = VELOCIDAD

def mostrar_puntaje(puntuacion):
    fuente = pygame.font.Font(None, 36)
    texto = fuente.render(f"Puntuación: {puntuacion}", True, (255, 255, 255))
    pantalla.blit(texto, (10, 10))

def mostrar_mensaje_fin():
    """ Muestra un mensaje cuando el jugador pierde, permitiendo elegir entre reiniciar o salir. """
    fuente = pygame.font.Font(None, 48)
    mensaje1 = fuente.render("¡Juego terminado!", True, (255, 0, 0))
    mensaje2 = pygame.font.Font(None, 36).render("Pulsa 'R' para reiniciar o 'Q' para salir", True, (255, 255, 255))

    pantalla.blit(mensaje1, (ANCHO // 2 - mensaje1.get_width() // 2, ALTO // 2 - 40))
    pantalla.blit(mensaje2, (ANCHO // 2 - mensaje2.get_width() // 2, ALTO // 2 + 20))
    pygame.display.flip()

    # Espera hasta que el jugador pulse 'R' para reiniciar o 'Q' para salir
    esperando = True
    while esperando:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                pygame.quit()
                return False
            elif evento.type == pygame.KEYDOWN:
                if evento.key == pygame.K_r:
                    return True  # Reinicia el juego
                elif evento.key == pygame.K_q:
                    pygame.quit()
                    return False  # Salir del juego

def bucle_principal():
    global velocidad

    # Reinicializar variables de juego
    serpiente = Serpiente()
    comida = Comida()
    comida_especial = ComidaEspecial()
    puntuacion = 0
    mostrar_comida_especial = False
    tiempo_ultima_comida_especial = time.time()
    intervalo_comida_especial = random.randint(15, 20)

    while True:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                pygame.quit()
                return

        # Controles de la serpiente
        teclas = pygame.key.get_pressed()
        if teclas[pygame.K_UP]:
            serpiente.cambiar_direccion('ARRIBA')
        elif teclas[pygame.K_DOWN]:
            serpiente.cambiar_direccion('ABAJO')
        elif teclas[pygame.K_LEFT]:
            serpiente.cambiar_direccion('IZQUIERDA')
        elif teclas[pygame.K_RIGHT]:
            serpiente.cambiar_direccion('DERECHA')

        serpiente.mover()

        # Comprobar colisión con la comida normal
        if serpiente.cuerpo[0] == comida.posicion:
            serpiente.crecer()
            puntuacion += 1
            comida.generar()
            velocidad *= 1.02  # Aumenta la velocidad en un 2%

        # Aparición de la comida especial en intervalos de 15-20 segundos
        tiempo_actual = time.time()
        if not mostrar_comida_especial and (tiempo_actual - tiempo_ultima_comida_especial >= intervalo_comida_especial):
            comida_especial.generar()
            mostrar_comida_especial = True
            tiempo_aparicion_comida_especial = tiempo_actual
            tiempo_ultima_comida_especial = tiempo_actual
            intervalo_comida_especial = random.randint(15, 20)

        # Comprobar colisión con la comida especial
        if mostrar_comida_especial:
            if serpiente.cuerpo[0] == comida_especial.posicion:
                serpiente.crecer()
                puntuacion += 5
                mostrar_comida_especial = False
            elif tiempo_actual - tiempo_aparicion_comida_especial >= 3:
                mostrar_comida_especial = False

        # Comprobar colisión con los límites o el propio cuerpo
        if serpiente.colision():
            if not mostrar_mensaje_fin():
                return  # Sale del juego si elige 'Q'
            else:
                velocidad = VELOCIDAD
                bucle_principal()  # Reinicia el juego si elige 'R'
                return

        # Dibujar elementos en pantalla
        pantalla.fill(FONDO)
        serpiente.dibujar(pantalla)
        comida.dibujar(pantalla)

        if mostrar_comida_especial:
            comida_especial.dibujar(pantalla)

        mostrar_puntaje(puntuacion)

        pygame.display.flip()
        reloj.tick(velocidad)

if __name__ == "__main__":
    bucle_principal()
