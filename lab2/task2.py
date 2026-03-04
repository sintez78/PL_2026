import pygame

# Инициализация
pygame.init()

# Цвета
C_WALL, C_FLOOR = (75, 70, 40), (110, 90, 40)
C_CAT, C_OUT = (180, 100, 60), (60, 30, 10)
C_GLASS, C_FRAME = (140, 190, 210), (220, 235, 220)
C_EYE, C_PUPIL = (100, 180, 50), (0, 0, 0)
C_YARN, C_YARN_LINE = (130, 130, 130), (50, 50, 50)
C_NOSE = (200, 150, 130)
C_WHISKER = (50, 30, 0)


def draw_background(screen):
    screen.fill(C_WALL)
    pygame.draw.rect(screen, C_FLOOR, (0, 300, 800, 300))

def draw_window(screen):
    pygame.draw.rect(screen, C_FRAME, (450, 50, 250, 220))
    glass_rects = [
        (465, 65, 100, 60), (600, 65, 100, 60),
        (465, 140, 100, 115), (600, 140, 100, 115)
    ]
    for r in glass_rects:
        pygame.draw.rect(screen, C_GLASS, r)


def draw_cat_body(screen):
    # Части тела: тип (полигон или эллипс) и координаты
    body_parts = [
        ('poly', [(550, 380), (750, 420), (750, 480), (550, 450)]),  # Хвост
        ('ell', (480, 370, 140, 100)),  # Бедро
        ('ell', (580, 430, 50, 80)),  # Лапа
        ('ell', (180, 310, 420, 160)),  # Туловище
        ('ell', (220, 420, 100, 50))  # Передняя лапа
    ]

    for type, data in body_parts:
        if type == 'poly':
            pygame.draw.polygon(screen, C_CAT, data)
            pygame.draw.polygon(screen, C_OUT, data, 1)
        else:
            pygame.draw.ellipse(screen, C_CAT, data)
            pygame.draw.ellipse(screen, C_OUT, data, 1)

    # Уши
    ears = [[(160, 350), (150, 300), (200, 330)], [(270, 330), (310, 300), (300, 350)]]
    for ear in ears:
        pygame.draw.polygon(screen, C_CAT, ear)
        pygame.draw.polygon(screen, C_OUT, ear, 1)

    # Голова (основа)
    pygame.draw.ellipse(screen, C_CAT, (150, 320, 160, 130))
    pygame.draw.ellipse(screen, C_OUT, (150, 320, 160, 130), 1)

def draw_cat_face(screen):
    # Глаза
    for x in [180, 250]:
        pygame.draw.ellipse(screen, C_EYE, (x, 360, 40, 30))
        pygame.draw.ellipse(screen, C_PUPIL, (x + 18, 362, 5, 26))
        pygame.draw.ellipse(screen, C_OUT, (x, 360, 40, 30), 1)

    # Нос
    pygame.draw.polygon(screen, C_NOSE, [(225, 395), (245, 395), (235, 405)])

    # Рот
    pygame.draw.arc(screen, C_OUT, (215, 395, 20, 20), 3.14, 6.28, 2)
    pygame.draw.arc(screen, C_OUT, (235, 395, 20, 20), 3.14, 6.28, 2)
    pygame.draw.line(screen, C_OUT, (235, 405), (235, 415), 2)

    # Усы
    for i in range(3):
        offset = i * 6
        pygame.draw.line(screen, C_WHISKER, (180, 400 + offset), (130, 395 + offset * 2), 1)
        pygame.draw.line(screen, C_WHISKER, (290, 400 + offset), (340, 395 + offset * 2), 1)


def draw_yarn(screen):
    # Нитка на полу
    points = [(280, 580), (350, 570), (420, 590), (490, 565)]
    pygame.draw.lines(screen, (160, 160, 160), False, points, 2)

    # Сам клубок
    ball_rect = (480, 520, 110, 90)
    pygame.draw.ellipse(screen, C_YARN, ball_rect)
    pygame.draw.ellipse(screen, C_YARN_LINE, ball_rect, 1)
    pygame.draw.arc(screen, C_YARN_LINE, (500, 530, 70, 70), 0.5, 2.5, 2)


def main():
    screen = pygame.display.set_mode((800, 600))
    clock = pygame.time.Clock()
    running = True

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # Вызов всех функций отрисовки по порядку
        draw_background(screen)
        draw_window(screen)
        draw_cat_body(screen)
        draw_cat_face(screen)
        draw_yarn(screen)

        pygame.display.flip()
        clock.tick(30)

    pygame.quit()


if __name__ == "__main__":
    main()