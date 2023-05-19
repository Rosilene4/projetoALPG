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

#função pro alien ficar reaparecendo na tela
def respawn():
    x = 1350
    y = random.randint(1, 640)
    return [x, y]

#função pro missel reaparecer
def respawn_missel():
    triggered = False
    respawn_missel_x = posição_nave_x
    respawn_missel_y = posição_nave_y
    velocidade_x_missel = 0
    return [respawn_missel_x, respawn_missel_y, triggered, velocidade_x_missel]

def colisões():
    global pontos
    if nave_rect.colliderect(alien_rect) or alien_rect.x == 60:
        pontos = pontos - 1
        return True
    elif missel_rect.colliderect(alien_rect):
        pontos = pontos + 1
        return True
    else:
        return False

while rodando:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            rodando = False

    scree.blit(bg, (0,0))
#parte responsável por ficar atualizando a janela e impedir que o jogo feche.

    rel_x = x % bg.get_rect().width
    scree.blit(bg, (rel_x - bg.get_rect().width, 0)) #criabg
    if rel_x < 1280:
        scree.blit(bg, (rel_x, 0))

    #teclas para mover a nave
    tecla = pygame.key.get_pressed()
    if tecla[pygame.K_UP] and posição_nave_y > 1:
        posição_nave_y -= 1
        if not triggered:
            posição_y_missel -= 1

    if tecla[pygame.K_DOWN] and posição_nave_y < 665:
        posição_nave_y += 1

        if not triggered:
          posição_y_missel += 1

    #comando para o missel ser lançado (atirar)
    if tecla[pygame.K_SPACE]:
        triggered = True
        velocidade_x_missel = 5
