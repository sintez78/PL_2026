import pygame

pygame.init()
screen = pygame.display.set_mode((800, 600))
clock = pygame.time.Clock()
running = True

# все цвета
C_WALL, C_FLOOR = (75, 70, 40), (110, 90, 40)
C_CAT, C_OUT = (180, 100, 60), (60, 30, 10)
C_GLASS, C_FRAME = (140, 190, 210), (220, 235, 220)
C_EYE, C_PUPIL = (100, 180, 50), (0, 0, 0)
C_YARN, C_YARN_LINE = (130, 130, 130), (50, 50, 50)

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: running = False

    # 1. стена и пол
    screen.fill(C_WALL)
    pygame.draw.rect(screen, C_FLOOR, (0, 300, 800, 300))

    # 2. окно
    pygame.draw.rect(screen, C_FRAME, (450, 50, 250, 220))
    for r in [(465, 65, 100, 60), (600, 65, 100, 60), (465, 140, 100, 115), (600, 140, 100, 115)]:
        pygame.draw.rect(screen, C_GLASS, r)

    # 3. кот
    body_parts = [
        ('poly', [(550, 380), (750, 420), (750, 480), (550, 450)]),
        ('ell', (480, 370, 140, 100)),
        ('ell', (580, 430, 50, 80)),
        ('ell', (180, 310, 420, 160)),
        ('ell', (220, 420, 100, 50))
    ]

    for type, data in body_parts:
        if type == 'poly':
            pygame.draw.polygon(screen, C_CAT, data)
            pygame.draw.polygon(screen, C_OUT, data, 1)
        else:
            pygame.draw.ellipse(screen, C_CAT, data)
            pygame.draw.ellipse(screen, C_OUT, data, 1)

    # 4. голова и уши
    ears = [[(160, 350), (150, 300), (200, 330)], [(270, 330), (310, 300), (300, 350)]]
    for ear in ears:
        pygame.draw.polygon(screen, C_CAT, ear)
        pygame.draw.polygon(screen, C_OUT, ear, 1)

    pygame.draw.ellipse(screen, C_CAT, (150, 320, 160, 130))  # Голова
    pygame.draw.ellipse(screen, C_OUT, (150, 320, 160, 130), 1)

    # 5. морда
    # глаза
    for x in [180, 250]:
        pygame.draw.ellipse(screen, C_EYE, (x, 360, 40, 30))
        pygame.draw.ellipse(screen, C_PUPIL, (x + 18, 362, 5, 26))
        pygame.draw.ellipse(screen, C_OUT, (x, 360, 40, 30), 1)

    # рот и нос
    pygame.draw.polygon(screen, (200, 150, 130), [(225, 395), (245, 395), (235, 405)])
    pygame.draw.arc(screen, C_OUT, (215, 395, 20, 20), 3.14, 6.28, 2)
    pygame.draw.arc(screen, C_OUT, (235, 395, 20, 20), 3.14, 6.28, 2)
    pygame.draw.line(screen, C_OUT, (235, 405), (235, 415), 2)

    # усы
    for i in range(3):
        offset = i * 6
        pygame.draw.line(screen, (50, 30, 0), (180, 400 + offset), (130, 395 + offset * 2), 1)
        pygame.draw.line(screen, (50, 30, 0), (290, 400 + offset), (340, 395 + offset * 2), 1)

    # 6. клубок
    pygame.draw.lines(screen, (160, 160, 160), False, [(280, 580), (350, 570), (420, 590), (490, 565)], 2)
    pygame.draw.ellipse(screen, C_YARN, (480, 520, 110, 90))
    pygame.draw.ellipse(screen, C_YARN_LINE, (480, 520, 110, 90), 1)
    pygame.draw.arc(screen, C_YARN_LINE, (500, 530, 70, 70), 0.5, 2.5, 2)

    pygame.display.flip()
    clock.tick(30)

pygame.quit()