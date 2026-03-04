import pygame
from pygame.draw import *

pygame.init()
FPS = 30
screen = pygame.display.set_mode((400, 400))

# === ЦВЕТА (как на картинке) ===
GRAY = (200, 200, 200)      # Светло-серый фон
YELLOW = (255, 255, 0)      # Жёлтое лицо
BLACK = (0, 0, 0)           # Чёрный (контуры, рот, брови)
RED = (255, 0, 0)           # Красные глаза

# === ФОН ===
screen.fill(GRAY)

# === ЛИЦО ===
# Жёлтый круг
circle(screen, YELLOW, (200, 200), 100)
# Чёрная обводка лица
circle(screen, BLACK, (200, 200), 100, 3)

# === ГЛАЗА ===
# Белки (красные круги)
circle(screen, RED, (165, 170), 18)   # Левый
circle(screen, RED, (235, 170), 18)   # Правый

# Зрачки (чёрные точки внутри)
circle(screen, BLACK, (165, 170), 8)  # Левый
circle(screen, BLACK, (235, 170), 8)  # Правый

# === БРОВИ (злые, наклонные) ===
# Левая бровь (слева-сверху вниз-вправо)
line(screen, BLACK, (140, 145), (185, 165), 8)
# Правая бровь (справа-сверху вниз-влево)
line(screen, BLACK, (260, 145), (215, 165), 8)

# === РОТ (прямой, чёрный прямоугольник) ===
rect(screen, BLACK, (150, 240, 100, 15))

# === ОБНОВЛЕНИЕ ЭКРАНА ===
pygame.display.update()

clock = pygame.time.Clock()
finished = False

while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True

pygame.quit()