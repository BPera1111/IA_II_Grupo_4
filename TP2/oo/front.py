import pygame
from pygame.locals import *
import numpy as np

# Definir las dimensiones de la pantalla
w = 1500
h = 600

def graficar_pendulo(angulos_pendulo, posiciones_carrito,tiempo, fuerza,velocidad_carro):
    pygame.init()
    screen = pygame.display.set_mode((w, h))
    pygame.display.set_caption("Péndulo y Carrito")

    clock = pygame.time.Clock()

    # Bucle principal
    running = True
    index = 0
    while running:
        for event in pygame.event.get():
            if event.type == QUIT:
                running = False

        screen.fill((255, 255, 255))  # Limpia la pantalla con blanco

        # Dibujar el carrito en el centro de la pantalla
        carrito_x = w/4 + posiciones_carrito[index] * 10  # Multiplica por 10 para que se vea mejor
        pygame.draw.rect(screen, (255, 0, 0), (carrito_x - 50, 300, 100, 50)) # pygame.draw.rect(screen, color, rect (x,y,width,height)

        #dibujar debajo del carrito el valor de la fuerza
        font = pygame.font.Font(None, 36)
        text = font.render("Fuerza: " + str(fuerza[index]), True, (0, 0, 0))
        screen.blit(text, (carrito_x - 50, 350))

        #dibujar debajo del carrito el valor de la velocidad
        font = pygame.font.Font(None, 36)
        text = font.render("Velocidad: " + str(velocidad_carro[index]), True, (0, 0, 0))
        screen.blit(text, (carrito_x - 50, 400))


        # Dibujar el inicio del péndulo en la posición del carrito y que el extremo del péndulo tenga el ángulo actual respecto de una vertical hacia arriba
        pendulo_x = carrito_x
        pendulo_y = 300
        pendulo_l = 100
        pendulo_angle = angulos_pendulo[index] + 180
        pendulo_end_x = pendulo_x + pendulo_l * np.sin(pendulo_angle*np.pi/180)
        pendulo_end_y = pendulo_y + pendulo_l * np.cos(pendulo_angle*np.pi/180)
        # if abs(pendulo_angle) > 90:
        #     pendulo_end_y = pendulo_y - pendulo_l * np.cos(pendulo_angle*np.pi/180) # Corrige la posición del extremo del péndulo si el ángulo es mayor a 90 grados
        # if abs(pendulo_angle) < 180:
        #     pendulo_end_x = pendulo_x - pendulo_l * np.sin(pendulo_angle*np.pi/180)
        
        if abs(angulos_pendulo[index]) > 180:
            print("Ángulo mayor a 180 grados la re cagamos")
        
        print("Ángulo: ", angulos_pendulo[index])
        print("Posición del carrito: ", posiciones_carrito[index])
        print("Tiempo: ", tiempo[index])
        print("Fuerza: ", fuerza[index])

        pygame.draw.line(screen, (0, 0, 0), (pendulo_x, pendulo_y), (pendulo_end_x, pendulo_end_y), 5)






        

        

        pygame.display.flip()  # Actualiza la pantalla
        # clock.tick(60)  # Limita la velocidad de fotogramas a 60 FPS

        # Incrementa el índice de tiempo
        index += 1
        if index >= len(angulos_pendulo):
            input("Fin del movimiento. Presione Enter para salir.")
            running = False
            # index = 0  # Reinicia el índice cuando alcanza el final de los datos de movimiento

    pygame.quit()

