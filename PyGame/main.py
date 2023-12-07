import pygame

# Инициализация Pygame
pygame.init()

# Определение размеров окна
WIDTH = 800
HEIGHT = 600

# Создание окна
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Простой платформер")

# Загрузка изображений для игрока и платформы
player_img = pygame.image.load("player.gif")
platform_img = pygame.image.load("platform.png")

# Определение размеров игрока и платформы
player_width = 50
player_height = 50
platform_width = 200
platform_height = 20

# Определение начальных координат для игрока и платформы
player_x = 400
player_y = 500
platform_x = 300
platform_y = 400

# Определение скорости игрока
player_speed = 5

# Определение состояния игры (продолжается или завершена)
running = True

# Основной игровой цикл
while running:
    # Обработка событий
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Получение состояний клавиш
    keys = pygame.key.get_pressed()

    # Перемещение игрока влево или вправо
    if keys[pygame.K_LEFT] and player_x > 0:
        player_x -= player_speed
    if keys[pygame.K_RIGHT] and player_x < WIDTH-100:
        player_x += player_speed
    if keys[pygame.K_UP]:
        player_y -= player_speed
    if keys[pygame.K_DOWN]:
        player_y += player_speed
    print(player_x, player_y)
    # Отрисовка игровых объектов
    screen.fill((0, 0, 0))
    screen.blit(player_img, (player_x, player_y))
    screen.blit(platform_img, (platform_x, platform_y))

    # Обновление экрана
    pygame.display.update()

# Завершение игры
pygame.quit()
