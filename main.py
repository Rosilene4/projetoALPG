from turtle import Screen
import pygame
import random
from pygame.locals import *
pygame.init()
x = 1280
y = 720

screen=pygame.display.set_mode((x,y))
pygame.display.set_caption("Meu jogo em Python")

bg=pygame.image.load('figuras/space.jpg').convert_alpha()
bg=pygame.transform.scale(bg, (x,y))

rodando=True

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
    
    pygame.display.update()