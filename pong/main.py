import pygame
from constants import ANCHO, ALTO, BLANCO, NEGRO
from paddle import Paleta
from ball import Pelota

def mostrar_pantalla_inicial(pantalla):
    fuente = pygame.font.Font(None, 36)
    texto = fuente.render("Presiona '1' para 1 jugador (IA) o '2' para 2 jugadores", True, BLANCO)
    pantalla.blit(texto, (ANCHO // 2 - texto.get_width() // 2, ALTO // 2 - texto.get_height() // 2))

def main():
    pygame.init()
    pantalla = pygame.display.set_mode((ANCHO, ALTO))
    pygame.display.set_caption("Pong")

    reloj = pygame.time.Clock()
    ejecutar = True
    modo_juego = None

    # Objetos del juego
    paleta_izquierda = Paleta(20, ALTO // 2 - 35)
    paleta_derecha = Paleta(ANCHO - 30, ALTO // 2 - 35)
    pelota = Pelota()

    # Puntaje
    puntaje_izquierda, puntaje_derecha = 0, 0
    fuente = pygame.font.Font(None, 36)

    while ejecutar:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                ejecutar = False
            if evento.type == pygame.KEYDOWN and modo_juego is None:
                if evento.key == pygame.K_1:
                    modo_juego = "IA"
                    paleta_derecha.es_ia = True
                elif evento.key == pygame.K_2:
                    modo_juego = "2P"

        pantalla.fill(NEGRO)

        if modo_juego is None:
            mostrar_pantalla_inicial(pantalla)
        else:
            teclas = pygame.key.get_pressed()

            # Movimiento de las paletas
            if modo_juego == "2P":
                paleta_izquierda.mover(teclas[pygame.K_w], teclas[pygame.K_s])
                paleta_derecha.mover(teclas[pygame.K_UP], teclas[pygame.K_DOWN])
            elif modo_juego == "IA":
                paleta_izquierda.mover(teclas[pygame.K_UP], teclas[pygame.K_DOWN])
                paleta_derecha.mover_ia(pelota)

            # Movimiento de la pelota
            pelota.mover()
            pelota.colision_paleta(paleta_izquierda)
            pelota.colision_paleta(paleta_derecha)

            # Comprobación de puntaje
            if pelota.rect.left <= 0:
                puntaje_derecha += 1
                pelota.reiniciar(aumentar_velocidad=False)  # La IA anota, restablecer velocidad
            elif pelota.rect.right >= ANCHO:
                puntaje_izquierda += 1
                pelota.reiniciar(aumentar_velocidad=True)   # El jugador anota, aumenta velocidad

            # Dibujar elementos
            paleta_izquierda.dibujar(pantalla)
            paleta_derecha.dibujar(pantalla)
            pelota.dibujar(pantalla)

            # Mostrar puntajes
            texto_izquierda = fuente.render(str(puntaje_izquierda), True, BLANCO)
            texto_derecha = fuente.render(str(puntaje_derecha), True, BLANCO)
            pantalla.blit(texto_izquierda, (ANCHO // 4, 20))
            pantalla.blit(texto_derecha, (3 * ANCHO // 4, 20))

        pygame.display.flip()
        reloj.tick(60)

    pygame.quit()

if __name__ == "__main__":
    main()
