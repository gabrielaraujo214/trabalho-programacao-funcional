import pygame
import random
import sys

# Inicializar o pygame
pygame.init()

# Definindo cores
WHITE = (255, 255, 255)

# Dimensões da tela
larguraTela = 1000
alturaTela = 480
screen = pygame.display.set_mode((larguraTela, alturaTela))
pygame.display.set_caption("Carros Obstáculos")

# Configuração dos obstáculos
OBSTACLE_WIDTH = 140
OBSTACLE_HEIGHT = 100
velocidade_obstaculo = 5
obstacles = []

# Carregar imagem de fundo e redimensionar
background_image = pygame.image.load(r"img\cenario\cenario1.png")  # Substitua pelo caminho da sua imagem de fundo
background_image = pygame.transform.scale(background_image, (larguraTela, alturaTela))

# Carregar imagem do carro para os obstáculos
car_image = pygame.image.load(r"img\carro\carro1.png")  # Substitua pelo caminho da sua imagem
car_image = pygame.transform.scale(car_image, (OBSTACLE_WIDTH, OBSTACLE_HEIGHT))  # Redimensiona a imagem

# Posições fixas para os obstáculos (três caminhos)
fixed_positions = [615, 515, 420]  # Posições horizontais onde os obstáculos aparecerão

# Função para criar obstáculos, garantindo que um caminho fique livre
def create_obstacles():
    # Escolhe aleatoriamente qual caminho ficará livre
    free_path = random.choice(fixed_positions)
    
    for pos_x in fixed_positions:
        if pos_x != free_path:  # Só cria obstáculos nos caminhos que não estão livres
            obstacle = pygame.Rect(pos_x - OBSTACLE_WIDTH / 2, -OBSTACLE_HEIGHT, OBSTACLE_WIDTH, OBSTACLE_HEIGHT)
            obstacles.append(obstacle)
    
    return free_path  # Retorna o caminho livre

# Função para mover os obstáculos (eles vão descer)
def move_obstacles():
    for obstacle in obstacles[:]:
        obstacle.y += velocidade_obstaculo  # Move os obstáculos para baixo
        if obstacle.y > alturaTela:
            obstacles.remove(obstacle)  # Remove obstáculos que saem da tela

# Loop principal do jogo
clock = pygame.time.Clock()
running = True
while running:
    screen.blit(background_image, (0, 0))  # Exibe a imagem de fundo redimensionada

    # Eventos
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Movendo os obstáculos
    move_obstacles()

    # Criar novos obstáculos quando eles saem da tela
    if len(obstacles) == 0 or all(obstacle.y > alturaTela for obstacle in obstacles):
        create_obstacles()

    # Desenhando os obstáculos
    for obstacle in obstacles:
        screen.blit(car_image, (obstacle.x, obstacle.y))  # Desenhar imagem do carro

    pygame.display.flip()
    clock.tick(30)  # 30 FPS
