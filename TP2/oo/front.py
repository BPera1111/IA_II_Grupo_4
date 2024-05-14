import pygame
from pygame.locals import *
import numpy as np
import sys

# Definir las dimensiones de la pantalla
w = 1250
h = 500

def graficar_pendulo(angulos_pendulo, posiciones_carrito,tiempo, fuerza,velocidad_carro, titulo):
    pygame.mixer.quit()
    pygame.init()
    screen = pygame.display.set_mode((w, h))
    pygame.display.set_caption(titulo)

    clock = pygame.time.Clock()

    play_button = Button((0, 255, 0), (w/2)-50, (h/2)-25, 100, 50, 'Play')

    # Bucle principal
    running = False
    index = 0
    draw_button = True
    while True:
        for event in pygame.event.get():
            pos = pygame.mouse.get_pos()
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if play_button.isOver(pos):
                    running = True
                    draw_button = False

        screen.fill((255, 255, 255))  # Limpia la pantalla con blanco
        if draw_button:
            play_button.draw(screen, (0, 0, 0))

        if running:
            
            y_obj = 170
            # Dibujar el carrito en la centro de la pantalla
            carrito_x = w/2 + posiciones_carrito[index] * 50 # Multiplica por 10 para que se vea mejor
            carrito_y = y_obj
            pygame.draw.rect(screen, (255, 0, 0), (carrito_x - 50, carrito_y - 25, 100, 50)) # pygame.draw.rect(screen, color, rect (x,y,width,height)

            # Dibujar las ruedas del carrito
            pygame.draw.circle(screen, (0, 0, 0), (carrito_x - 25, carrito_y+25), 15) # pygame.draw.circle(screen, color, pos, radius)
            pygame.draw.circle(screen, (0, 0, 0), (carrito_x + 25, carrito_y+25), 15) # pygame.draw.circle(screen, color, pos, radius)

            # Dibujar el inicio del péndulo en la posición del carrito y que el extremo del péndulo tenga el ángulo actual respecto de una vertical hacia arriba
            pendulo_x = carrito_x
            pendulo_y = carrito_y - 25
            pendulo_l = 100
            pendulo_angle = angulos_pendulo[index] + 180
            pendulo_end_x = pendulo_x + pendulo_l * np.sin(pendulo_angle*np.pi/180)
            pendulo_end_y = pendulo_y + pendulo_l * np.cos(pendulo_angle*np.pi/180)
            # if abs(pendulo_angle) > 90:
            #     pendulo_end_y = pendulo_y - pendulo_l * np.cos(pendulo_angle*np.pi/180) # Corrige la posición del extremo del péndulo si el ángulo es mayor a 90 grados
            # if abs(pendulo_angle) < 180:
            #     pendulo_end_x = pendulo_x - pendulo_l * np.sin(pendulo_angle*np.pi/180)
            
            pygame.draw.line(screen, (0, 0, 0), (pendulo_x, pendulo_y), (pendulo_end_x, pendulo_end_y), 5)

            #dibujar debajo el valor del tiempo
            font = pygame.font.Font(None, 36)
            text = font.render("Tiempo: " + str(tiempo[index]), True, (0, 0, 0))
            screen.blit(text, (50, 270))

            #dibujar debajo del carrito el valor de la fuerza
            font = pygame.font.Font(None, 36)
            text = font.render("Fuerza: " + str(fuerza[index]), True, (0, 0, 0))
            screen.blit(text, (50, 310))

            #dibujar debajo del carrito el valor de la velocidad
            font = pygame.font.Font(None, 36)
            text = font.render("Velocidad: " + str(velocidad_carro[index]), True, (0, 0, 0))
            screen.blit(text, (50, 350))

            #dibujar debajo el valor de la posición
            font = pygame.font.Font(None, 36)
            text = font.render("Posición: " + str(posiciones_carrito[index]), True, (0, 0, 0))
            screen.blit(text, (50, 390))

    
            # dibujar una línea que represente el suelo con marcas cada 100 unidades
            for i in range(-w//2, w//2, 50): # Dibuja una línea cada 100 unidades
                pygame.draw.line(screen, (0, 0, 0), (w//2 + i, 210), (w//2 + i, 220), 1) # pygame.draw.line(screen, color, start_pos, end_pos, width)
                #dibujar debajo el valor de la posición
                font = pygame.font.Font(None, 36) # pygame.font.Font(None, size)
                text = font.render(str(int(i/50)), True, (0, 0, 0)) # pygame.font.Font.render(text, antialias, color, background=None) hace 
                text_width = text.get_width()
                screen.blit(text, (w//2 + i - text_width//2, 220)) # pygame.Surface.blit(source, dest, area=None, special_flags = 0) Hace que el texto se vea centrado en la línea
            #dibujar una linea horizontal en la posición 205
            pygame.draw.line(screen, (0, 0, 0), (0, 210), (w, 210), 2)



            

            index += 1
            if index >= len(angulos_pendulo):
                running = False
                index = 0
                while True:
                    for event in pygame.event.get():
                        if event.type == pygame.QUIT:
                            pygame.quit()
                            sys.exit()

        pygame.display.flip()  # Actualiza la pantalla


    pygame.quit()



class Button:
    def __init__(self, color, x, y, width, height, text=''):
        self.color = color
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.text = text

    def draw(self, screen, outline=None):
        if outline:
            pygame.draw.rect(screen, outline, (self.x-2, self.y-2, self.width+4, self.height+4), 0)
        pygame.draw.rect(screen, self.color, (self.x, self.y, self.width, self.height), 0)
        if self.text != '':
            font = pygame.font.SysFont('comicsans', 50)
            text = font.render(self.text, 1, (0, 0, 0))
            screen.blit(text, (self.x + (self.width/2 - text.get_width()/2), self.y + (self.height/2 - text.get_height()/2)))

    def isOver(self, pos):
        if self.x < pos[0] < self.x + self.width:
            if self.y < pos[1] < self.y + self.height:
                return True
        return False