import pygame
import random
import sys

#Inicializar o pygame
pygame.init()

#Definindo cores
WHITE = (255, 255, 255)

#Dimensões da tela
larguraTela = 400
alturaTela = 600
screen = pygame.display.set_mode((larguraTela, alturaTela))
pygame.display.set_caption("Carros Obstáculos")

#Configuração dos obstáculos
OBSTACLE_WIDTH = 140
OBSTACLE_HEIGHT = 100
velocidade_obstaculo = 5
obstacles = []


#Carregar imagem do carro para os obstáculos
car_image = pygame.image.load(r"img\carro\carro1.png")  # Substitua pelo caminho da sua imagem
car_image = pygame.transform.scale(car_image, (OBSTACLE_WIDTH, OBSTACLE_HEIGHT))  # Redimensiona a imagem

#Função para criar obstáculos aleatórios
def create_obstacle():
    x = random.randint(0, larguraTela - OBSTACLE_WIDTH)
    y = -OBSTACLE_HEIGHT  # Começa fora da tela, acima
    obstacle = pygame.Rect(x, y, OBSTACLE_WIDTH, OBSTACLE_HEIGHT)
    obstacles.append(obstacle)

#Criando alguns obstáculos iniciais
for _ in range(5):
    create_obstacle()

#Função para mover os obstáculos
def move_obstacles():
    # Atualiza a posição dos obstáculos e remove os que saíram da tela
    for obstacle in obstacles[:]:
        obstacle.y += velocidade_obstaculo
        if obstacle.y > alturaTela:
            obstacles.remove(obstacle)
            create_obstacle()

#Loop principal do jogo
clock = pygame.time.Clock()
running = True
while running:
    screen.fill(WHITE)  # Fundo branco

    # Eventos
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Movendo e desenhando obstáculos
    move_obstacles()
    for obstacle in obstacles:
        screen.blit(car_image, (obstacle.x, obstacle.y))  # Desenhar imagem do carro

    pygame.display.flip()
    clock.tick(30)  # 30 FPS