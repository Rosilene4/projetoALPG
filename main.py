from turtle import Screen
import pygame
import random
from pygame.locals import *
pygame.init()
#Importação da biblioteca pygame e iniciação da mesma

x = 1280
y = 720
#Tamanho da janela (tela) do jogo

scree = pygame.display.set_mode((x, y))
pygame.display.set_caption('INVASORES DO ESPAÇO')
#Código responsável por exibir a janela e o nome na tela

bg = pygame.image.load('figuras/space.jpg').convert_alpha()
bg = pygame.transform.scale(bg, (x, y))
#carregamento do fundo (cenário) e convertimento para alfa e tamanho da tela

alien = pygame.image.load('figuras/alien.png').convert_alpha()
alien = pygame.transform.scale(alien, (50, 50))

nave = pygame.image.load('figuras/nave.png').convert_alpha()
nave = pygame.transform.scale(nave, (50, 50))
nave = pygame.transform.rotate(nave, -90)

missel = pygame.image.load('figuras/missel.png').convert_alpha()
missel = pygame.transform.scale(missel, (25, 25))
missel = pygame.transform.rotate(missel, 0)

posição_alien_x = 500
posição_alien_y = 360

posição_nave_x = 200
posição_nave_y = 300

velocidade_x_missel = 0
posição_x_missel = 200
posição_y_missel = 300

triggered = False

pontos = 4

rodando = True

fonte = pygame.font.SysFont('fontes/PixelGameFont.ttf', 50)

#transforma as imagens em objetos
nave_rect = nave.get_rect()
alien_rect = alien.get_rect()
missel_rect = missel.get_rect()