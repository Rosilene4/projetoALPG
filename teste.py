from turtle import Screen
import pygame
import random
from pygame.locals import *
pygame.init()
import pygame.mixer
pygame.mixer.init()
#Importação da biblioteca pygame e iniciação da mesma

x = 1280
y = 720
#Tamanho da janela (tela) do jogo

cooldown=0

pygame.mixer.music.load('musicas/Orbital_som_fundo.mp3')
pygame.mixer.music.play(-1)
#Musica enquanto o jogo roda

shoot=pygame.mixer.Sound('musicas/laser.wav')
#Som do disparo da nave

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

missil_obstaculo = pygame.image.load('missel.png').convert_alpha()
missil_obstaculo = pygame.transform.scale(missel, (25, 25))
missil_obstaculo = pygame.transform.rotate(missel, 0)

meteoro = pygame.image.load('figuras/asteroid.png').convert_alpha()
meteoro = pygame.transform.scale(meteoro, (100, 100))

##teste
posição_alien_x = 500
posição_alien_y = 360

posição_meteoro_x = 500
posição_meteoro_y = 360

posição_nave_x = 200
posição_nave_y = 300

velocidade_x_missel = 0
posição_x_missel = 200
posição_y_missel = 300

posição_missil_obstaculo_x = posição_alien_x
posição_missil_obstaculo_y = posição_alien_y
velocidade_missil_obstaculo_x = 5

triggered = False

pontos = 4

velocidade_jogo = 2

rodando = True

fonte = pygame.font.SysFont('fontes/PixelGameFont.ttf', 50)

#transforma as imagens em objetos
nave_rect = nave.get_rect()
alien_rect = alien.get_rect()
missel_rect = missel.get_rect()
meteoro_rect = meteoro.get_rect()
missil_obstaculo_rect = missil_obstaculo.get_rect()
#foguete_rect = foguete.get_rect()

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

#Função para o meteoro reaparecer na tela
def respawn_meteoro():
    x = 1350
    y = random.randint(1, 640)
    return [x, y]

def respawn_missil_obstaculo():
    triggered = True
    respawn_missil_obstaculo_x = posição_alien_x
    respawn_missil_obstaculo_y = posição_alien_y
    velocidade_missil_obstaculo_x = 0
    return [respawn_missil_obstaculo_x, respawn_missil_obstaculo_y, triggered]

def colisões():
    #Som dos efeitos
    global som_nave_colisao
    #global som_missil
    #global som_explosao

    som_nave_colisao = pygame.mixer.Sound('musicas/som_de_explosao.wav')
    #som_missil = pygame.mixer.Sound("som_missil.mp3")
    #som_explosao = pygame.mixer.Sound("som_explosao.mp3")

    global pontos
    
    global velocidade_jogo
    #Se o player principal colidir com a nave inimiga ou a nave passar da tela

    if nave_rect.colliderect(alien_rect) or alien_rect.x == 60:
        pontos = pontos - 1
        som_nave_colisao.play()
        return True
    
    elif nave_rect.colliderect(meteoro_rect) or meteoro_rect.x == 60:
        pontos = pontos - 1
        return True
    
    elif missel_rect.colliderect(alien_rect):
        pontos = pontos + 1
        if pontos % 10 == 0:
            velocidade_jogo += 1
        return True
    
    elif missel_rect.colliderect(meteoro_rect):
        pontos = pontos + 1
        if pontos % 10 == 0:
            velocidade_jogo += 1
        return True
    else:
        velocidade_jogo += 0
        return False
        #som_explosao.play()

while rodando:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            rodando = False
        #condição para o som do disparo
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                shoot.play()
    keys=pygame.key.get_pressed()

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
        
    #refras da pontuação
    if pontos == 0:
        rodando = False

    #respawn do alien
    if posição_alien_x == 50:
        posição_alien_x = respawn()[0]
        posição_alien_y = respawn()[1]

    elif posição_meteoro_x == 50:
        posição_meteoro_x = respawn_meteoro()[0]
        posição_meteoro_y = respawn_meteoro()[1]

    #respawn do missel
    if posição_x_missel == 1300:
        posição_x_missel, posição_y_missel, triggered, velocidade_x_missel = respawn_missel()

    elif posição_alien_x == 50 or colisões():
        posição_alien_x = respawn()[0]
        posição_alien_y = respawn()[1]

    if posição_meteoro_x == 50 or colisões():
         posição_meteoro_x = respawn_meteoro()[0]
         posição_meteoro_y = respawn_meteoro()[1]

    if cooldown <=0:
        missil_obstaculo_x= posição_alien_x
        missil_obstaculo_y= posição_alien_y

        #atualização do cooldwon para o tempo de espera
        cooldown=60
    else:
        cooldown -=1
    
     #mover e desenhar o missel da nave inimiga
    if missil_obstaculo_x is not None and missil_obstaculo_y is not None:
        missil_obstaculo_x -=15 #mover míssil para a esquerda
        scree.blit(missil_obstaculo, (missil_obstaculo_x, missil_obstaculo_y)) #Desenha missil na tela
        
        if triggered:
            posição_missil_obstaculo_x -= velocidade_missil_obstaculo_x

        #verificar se missil saiu da tela
        if missil_obstaculo_x <0:
            missil_obstaculo_x = None
            missil_obstaculo_y = None

    


    #posição dos racts (objetos)
    nave_rect.y = posição_nave_y
    nave_rect.x = posição_nave_x

    missel_rect.x = posição_x_missel
    missel_rect.y = posição_y_missel

    alien_rect.x = posição_alien_x
    alien_rect.y = posição_alien_y

    meteoro_rect.x = posição_meteoro_x
    meteoro_rect.y = posição_meteoro_y

    missil_obstaculo_rect.x = posição_alien_x
    missil_obstaculo_rect.y = posição_alien_y
    
    x-= velocidade_jogo
    posição_alien_x -= velocidade_jogo 
    posição_meteoro_x -= velocidade_jogo
    #movimento do alien

    posição_x_missel += velocidade_x_missel

    pygame.draw.rect(scree, (0, 0, 0), nave_rect, 4)
    pygame.draw.rect(scree, (0, 0, 0), missel_rect, 4)
    pygame.draw.rect(scree, (0, 0, 0), alien_rect, 4)
    pygame.draw.rect(scree, (0, 0, 0), meteoro_rect, 4)

    #pontuação na tela
    score = fonte.render(f'Pontuação: {int(pontos)} ', True, (255, 0, 0))
    scree.blit(score, (50, 50))

    scree.blit(alien, (posição_alien_x, posição_alien_y))
    scree.blit(missel, (posição_x_missel, posição_y_missel))
    scree.blit(nave, (posição_nave_x, posição_nave_y))
    scree.blit(meteoro, (posição_meteoro_x, posição_meteoro_y))


    print(pontos)

    pygame.display.update()
#responsável por mover o fundo e atualizar o mesmo