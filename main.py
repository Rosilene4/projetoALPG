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

#controle do tempo de disparo da nave inimiga
cooldown=0

pygame.mixer.music.load('musicas/Orbital_som_fundo.mp3')
pygame.mixer.music.play(-1)
#Musica enquanto o jogo roda

shoot=pygame.mixer.Sound('musicas/laser.wav')
#Som do disparo da nave

screen = pygame.display.set_mode((x, y))
pygame.display.set_caption('INVASORES DO ESPAÇO')
#Código responsável por exibir a janela e o nome na tela

bg = pygame.image.load('fundo11.jpeg').convert_alpha()
bg = pygame.transform.scale(bg, (x, y))
#carregamento do fundo (cenário) e convertimento para alfa e tamanho da tela

alien = pygame.image.load('figuras/alien.png').convert_alpha()
alien = pygame.transform.scale(alien, (70, 70))

nave = pygame.image.load('figuras/nave.png').convert_alpha()
nave = pygame.transform.scale(nave, (90, 90))
nave = pygame.transform.rotate(nave, -90)

missel = pygame.image.load('figuras/missel.png').convert_alpha()
missel = pygame.transform.scale(missel, (50, 50))
missel = pygame.transform.rotate(missel, 0)

'''missil_obstaculo = pygame.image.load('imagens_novo_nivel/missil_pequeno.png').convert_alpha()
missil_obstaculo = pygame.transform.scale(missel, (50, 50))
missil_obstaculo = pygame.transform.rotate(missel, 0)'''

alien2= pygame.image.load('asteroid_fogo.png').convert_alpha()
alien2= pygame.transform.scale(alien2, (100,100))

meteoro_fogo = pygame.image.load('fogo.png').convert_alpha()
meteoro_fogo = pygame.transform.scale(meteoro_fogo, (100, 100))

explosão = pygame.image.load('explosion.png').convert_alpha()
explosão = pygame.transform.scale(explosão, (100, 100))

velocidade_alien2_x= 0
velocidade_alien2_y= 0

alien2_speed= 2
posição_alien2_x = 1350
posição_alien2_y = random.randint(1, 640)

posição_alien_x = 500
posição_alien_y = 360

meteoro_fogo_speed = 2
posição_meteoro_fogo_x = 1350
posição_meteoro_fogo_y = random.randint(1, 640)

posição_nave_x = 200
posição_nave_y = 300

velocidade_x_missel =0
posição_x_missel = 200
posição_y_missel = 300

'''posição_missil_obstaculo_x = posição_alien_x
posição_missil_obstaculo_y = posição_alien_y
velocidade_missil_obstaculo_x = 2'''

triggered = False

pontos = 6
velocidade_pontos = 2

rodando = True

fonte = pygame.font.SysFont('fontes/PixelGameFont.ttf', 50)

#transforma as imagens em objetos
nave_rect = nave.get_rect()
alien_rect = alien.get_rect()
missel_rect = missel.get_rect()
#missil_obstaculo_rect = missil_obstaculo.get_rect()
alien2_rect = alien2.get_rect()
meteoro_fogo_rect = meteoro_fogo.get_rect()

def reiniciar_jogo():
    global posição_alien2_x, posição_alien2_y, velocidade_alien2_x, velocidade_alien2_y
    global alien2_speed, posição_alien_x, posição_alien_y, posição_nave_x, posição_nave_y
    global velocidade_x_missel, posição_x_missel, posição_y_missel
    global posição_missil_obstaculo_x, posição_missil_obstaculo_y, velocidade_missil_obstaculo_x
    global triggered, pontos, velocidade_pontos, rodando
    global meteoro_fogo_speed, posição_meteoro_fogo_x, posição_meteoro_fogo_y, velocidade_meteoro_fogo_x, velocidade_meteoro_fogo_y

    posição_alien2_x = 13500
    posição_alien2_y = random.randint(1, 640)
    
    velocidade_alien2_x= 0
    velocidade_alien2_y= 0
    
    alien2_speed= 2
    posição_alien2_x = 1350
    posição_alien2_y = random.randint(1, 640)

    velocidade_meteoro_fogo_x= 0
    velocidade_meteoro_fogo_y= 0

    meteoro_fogo_speed = 2
    posição_meteoro_fogo_x = 1350
    posição_meteoro_fogo_y = random.randint(1, 640)
    
    posição_alien_x = 500
    posição_alien_y = 360
    
    posição_nave_x = 200
    posição_nave_y = 300
    
    velocidade_x_missel =0
    posição_x_missel = 200
    posição_y_missel = 300
    
    '''posição_missil_obstaculo_x = posição_alien_x
    posição_missil_obstaculo_y = posição_alien_y
    velocidade_missil_obstaculo_x = 2'''
    
    triggered = False
    pontos = 4
    velocidade_pontos = 2
    rodando = True
    
    

def exibe_mensagem(msg, tamanho, cor):
    fonte= pygame.font.SysFont('comicsansms', tamanho, True, False)
    mensagem = f'{msg}'
    texto_formatado = fonte.render(mensagem, True, cor)
    return texto_formatado

def pausar_jogo():
    paused = True
    while paused:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                paused = False
# Se apertado a tecla " c " o jogo continua de onde parou
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_c:
                    paused = False

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
    global som_explosao
    global pontos
    global velocidade_pontos

    som_nave_colisao = pygame.mixer.Sound('musicas/explosion01.wav')
    #som_missil = pygame.mixer.Sound("som_missil.mp3")
    som_explosao = pygame.mixer.Sound("musicas/explosion04.wav")

    #Se o player principal colidir com a nave inimiga ou a nave passar da tela

    if nave_rect.colliderect(alien_rect) or alien_rect.x == 60:
        pontos -=1
        som_nave_colisao.play()
        screen.blit(explosão, (posição_alien_x, posição_alien_y))
        return True
    
    if nave_rect.colliderect(alien2_rect) or alien2_rect.x == 60:
        pontos =0     
        som_explosao.play()
        screen.blit(explosão, (posição_alien2_x, posição_alien2_y))
        return True
    
    if nave_rect.colliderect(meteoro_fogo_rect) or meteoro_fogo_rect.x == 60:
        pontos =0      
        som_explosao.play()
        screen.blit(explosão, (posição_meteoro_fogo_x, posição_meteoro_fogo_y))
        return True
    
    if missel_rect.colliderect(alien_rect):
        pontos +=1
        som_explosao.play()
        screen.blit(explosão, (posição_alien_x, posição_alien_y))
        if pontos % 10 == 0:
            velocidade_pontos +1
        return True
    '''if missil_obstaculo_rect.colliderect(nave_rect):
        pontos -=1
        som_explosao.play()
        screen.blit(explosão, (posição_nave_x, posição_nave_y))
        return True'''
    
    #if missel_rect.colliderect(alien2_rect):
    #    pontos = pontos + 1
    #    som_explosao.play()
    #    return True
    
    if pontos >= 10:
        velocidade_pontos=4
        
    else:
        velocidade_pontos += 0
        return False   
 
game_over_exibindo= False
rodando= True
while rodando:
    for events in pygame.event.get():
        if events.type == pygame.QUIT:
            rodando = False
        screen.blit(bg, (0,0))
    
    #parte responsável por ficar atualizando a janela e impedir que o jogo feche.
    rel_x = x % bg.get_rect().width
    screen.blit(bg, (rel_x - bg.get_rect().width, 0)) #criabg
    if rel_x < 1280:
        screen.blit(bg, (rel_x, 0))

    elif events.type == pygame.KEYDOWN:  #condição para o som do disparo
        if events.key == pygame.K_SPACE:
            shoot.play()
    keys=pygame.key.get_pressed()
    
    #teclas para mover a nave
    tecla = pygame.key.get_pressed()
    #reinicia o jogo se apertar na tecla espace
    if tecla[pygame.K_a]:
        reiniciar_jogo()

    if tecla[pygame.K_p]:
        pausar_jogo()
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
        
    #refras da pontuação / exibir game over
    if pontos == 0:
        game_over = exibe_mensagem("GAME OVER" , 50, (255, 255, 255))
        screen.blit(game_over, (544 ,300) )
        pygame.display.update()
        game_over_exibindo= True
        pygame.time.wait(2000)
        rodando = False
        pausar_jogo()

    

    #respawn do alien
    if posição_alien_x == 50:
        posição_alien_x = respawn()[0]
        posição_alien_y = respawn()[1]

    # Alien 2
    if posição_alien2_x == 50:
        posição_alien2_x= 1350
        posição_alien2_y= random.randint(1, 640)
    posição_alien2_x -=3

    if posição_meteoro_fogo_x == 50:
        posição_meteoro_fogo_x = 1350
        posição_meteoro_fogo_y = random.randint(1, 640)
    posição_meteoro_fogo_x -=3

    alien2_rect= screen.blit(alien2, (posição_alien2_x, posição_alien2_y))
    meteoro_fogo_rect = screen.blit(meteoro_fogo, (posição_meteoro_fogo_x, posição_meteoro_fogo_y))
    
    screen.blit(alien, (posição_alien_x, posição_alien_y))
    screen.blit(alien2, (posição_alien2_x, posição_alien2_y))
    
    #respawn do missel
    if posição_x_missel == 1300:
        posição_x_missel, posição_y_missel, triggered, velocidade_x_missel = respawn_missel()

    if posição_alien_x == 50 or colisões():
        posição_alien_x = respawn()[0]
        posição_alien_y = respawn()[1]

    alien2_rect.x= posição_alien2_x
    alien2_rect.y= posição_alien2_y

    meteoro_fogo_rect.x = posição_meteoro_fogo_x
    meteoro_fogo_rect.y = posição_meteoro_fogo_y

    posição_alien2_x -= 2
    posição_meteoro_fogo_x -= 1

    #desenhar foguete
    screen.blit(alien2, alien2_rect)
    screen.blit(meteoro_fogo, meteoro_fogo_rect)

#Controle do tempo de espera entre os disparos da nave inimiga
    '''if cooldown <=0:
        missil_obstaculo_x= posição_alien_x
        missil_obstaculo_y= posição_alien_y

        #atualização do cooldwon para o tempo de espera
        cooldown=60
    else:
        cooldown -=1

    #mover e desenhar o missel da nave inimiga
    if missil_obstaculo_x is not None and missil_obstaculo_y is not None:
        missil_obstaculo_x -=15 #mover míssil para a esquerda
        screen.blit(missil_obstaculo, (missil_obstaculo_x, missil_obstaculo_y)) #Desenha missil na tela
        
        if triggered:
            posição_missil_obstaculo_x -= velocidade_missil_obstaculo_x

        #verificar se missil saiu da tela
        if missil_obstaculo_x <0:
            missil_obstaculo_x = None
            missil_obstaculo_y = None'''
             
        #if pontos>=15:
        #    nave=pygame.image.load('nave_pequena.png').convert_alpha()
        #    nave = pygame.transform.scale(nave, (90, 90))
        #    screen.blit(nave, (posição_nave_x, posição_nave_y))
        #    velocidade_pontos=8


    #posição dos racts (objetos)
    nave_rect.y = posição_nave_y
    nave_rect.x = posição_nave_x

    missel_rect.x = posição_x_missel
    missel_rect.y = posição_y_missel

    alien_rect.x = posição_alien_x
    alien_rect.y = posição_alien_y

    #missil_obstaculo_rect.x = posição_alien_x
    #missil_obstaculo_rect.y = posição_alien_y
    
    x-= velocidade_pontos
    posição_alien_x -= velocidade_pontos
    #movimento do alien

    posição_x_missel += velocidade_x_missel

    #pontuação na tela
    score = fonte.render(f'PONTUAÇÃO : {int(pontos)} ', True, (255, 255, 255))
    screen.blit(score, (50, 50))

    screen.blit(alien, (posição_alien_x, posição_alien_y))
    screen.blit(missel, (posição_x_missel, posição_y_missel))
    screen.blit(nave, (posição_nave_x, posição_nave_y))
    screen.blit(alien2, (posição_alien2_x, posição_alien2_y))
    screen.blit(meteoro_fogo, (posição_meteoro_fogo_x, posição_meteoro_fogo_y))

    pygame.display.update()
#responsável por mover o fundo e atualizar o mesmo
