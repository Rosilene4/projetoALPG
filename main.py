#Importação da biblioteca pygame e iniciação da mesma
from turtle import Screen
import pygame
import random
from pygame.locals import *
pygame.init()

#Tamanho da janela (tela) do jogo
x = 1280
y = 720

#Código responsável por exibir a janela e o nome na tela
screen=pygame.display.set_mode((x,y))
pygame.display.set_caption("Meu jogo em Python")

#carregamento do fundo (cenário) e convertimento para alfa e tamanho da tela
bg=pygame.image.load('figuras/space.jpg').convert_alpha()
bg=pygame.transform.scale(bg, (x,y))

alien=pygame.image.load('figuras/alien.png').convert_alpha()
alien=pygame.transform.scale(alien, (50,50))

playerImg = pygame.image.load('figuras/nave.png').convert_alpha()
playerImg = pygame.transform.scale(playerImg, (50,50))
playerImg = pygame.transform.rotate(playerImg, -90)

pos_alien_x=500
pos_alien_y=360

pos_alien_x=200
pos_alien_y=300

pos_player_x=200
pos_player_y=300


rodando=True

#parte responsável por ficar atualizando a janela e impedir que o jogo feche.
while rodando:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            rodando=False
    screen.blit(bg, (0,0))

    rel_x = x % bg.get_rect().width
    screen.blit(bg, (rel_x - bg.get_rect().width,0))
    if rel_x < 1280:
        screen.blit(bg, (rel_x, 0))
    #movimento da tela
    x-=3

    screen.blit(alien,(pos_alien_y, pos_alien_y))
    screen.blit(playerImg,(pos_player_x, pos_player_y))
    
    pygame.display.update()