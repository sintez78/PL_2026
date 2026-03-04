import pygame

pygame.init()
screen = pygame.display.set_mode((800, 600))
clock = pygame.time.Clock()

# Цвета (подобраны пипеткой с картинки)
C_WALL, C_FLOOR = (65, 50, 10), (100, 80, 20)  # Темно-коричневый и оливковый
C_WIN_FRAME, C_WIN_GLASS = (220, 240, 240), (130, 200, 220)
C_ORANGE, C_GREY = (200, 100, 50), (100, 90, 85)
C_YARN, C_LINES = (150, 150, 150), (60, 60, 60)
C_EYE_G, C_EYE_B = (100, 200, 50), (50, 180, 250)


def draw_yarn(surf, x, y, r):
    pygame.draw.ellipse(surf, C_YARN, (x, y, r, r * 0.9))
    pygame.draw.ellipse(surf, C_LINES, (x, y, r, r * 0.9), 1)
    # полоски ниток
    rect = (x + 5, y + 5, r - 10, r * 0.9 - 10)
    pygame.draw.arc(surf, C_LINES, rect, 0, 3.14, 2)
    pygame.draw.arc(surf, C_LINES, (x, y + 10, r, r * 0.6), 3.2, 6.0, 2)
    pygame.draw.line(surf, C_LINES, (x + 5, y + r // 2), (x + r - 5, y + r // 2), 2)


def draw_cat(surf, color, x, y, w, facing_right):
    h = w // 2.5
    head_sz = h * 0.9
    eye_color = C_EYE_B if color == C_GREY else C_EYE_G

    # координаты зависят от направления
    if facing_right:
        head_x, tail_x = x + w - head_sz * 0.8, x
        tail_end = x - 40
    else:
        head_x, tail_x = x - head_sz * 0.2, x + w
        tail_end = x + w + 40

    # хвост
    pygame.draw.line(surf, color, (tail_x, y + h // 1.5), (tail_end, y + h // 2), 15)
    # лапы (задние)
    leg_x = x + 20 if facing_right else x + w - 50
    pygame.draw.ellipse(surf, color, (leg_x, y + h * 0.7, 40, 30))
    pygame.draw.ellipse(surf, (0, 0, 0), (leg_x, y + h * 0.7, 40, 30), 1)
    # тело
    pygame.draw.ellipse(surf, color, (x, y, w, h))
    pygame.draw.ellipse(surf, (0, 0, 0), (x, y, w, h), 1)
    # голова
    pygame.draw.ellipse(surf, color, (head_x, y - 10, head_sz, head_sz))
    pygame.draw.ellipse(surf, (0, 0, 0), (head_x, y - 10, head_sz, head_sz), 1)
    # уши
    ear_x1 = head_x + 5 if not facing_right else head_x + head_sz - 25
    ear_x2 = head_x + 25 if not facing_right else head_x + 5
    pygame.draw.polygon(surf, color, [(ear_x1, y), (ear_x1 + 10, y - 15), (ear_x1 + 20, y + 5)])
    pygame.draw.polygon(surf, (220, 150, 150),
                        [(ear_x1 + 2, y), (ear_x1 + 10, y - 10), (ear_x1 + 18, y + 5)])  # Розовое внутри
    pygame.draw.polygon(surf, color, [(ear_x2, y + 5), (ear_x2 + 10, y - 15), (ear_x2 + 20, y)])
    # глаза
    ex = head_x + 10 if not facing_right else head_x + head_sz - 35
    pygame.draw.ellipse(surf, eye_color, (ex, y + 15, 10, 15))
    pygame.draw.ellipse(surf, (0, 0, 0), (ex + 4, y + 20, 2, 8))  # Зрачок
    pygame.draw.ellipse(surf, eye_color, (ex + 15, y + 15, 10, 15))
    pygame.draw.ellipse(surf, (0, 0, 0), (ex + 19, y + 20, 2, 8))


running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: running = False

    # 1. фон
    screen.fill(C_WALL)
    pygame.draw.rect(screen, C_FLOOR, (0, 280, 800, 320))

    # 2. окна (3 штуки)
    for i in range(3):
        wx = -50 + i * 280
        pygame.draw.rect(screen, C_WIN_FRAME, (wx, 40, 220, 200))  # Рама
        # стекла (4 части)
        pygame.draw.rect(screen, C_WIN_GLASS, (wx + 10, 50, 95, 85))
        pygame.draw.rect(screen, C_WIN_GLASS, (wx + 115, 50, 95, 85))
        pygame.draw.rect(screen, C_WIN_GLASS, (wx + 10, 145, 95, 85))
        pygame.draw.rect(screen, C_WIN_GLASS, (wx + 115, 145, 95, 85))

    # 3.клубки (фон)
    draw_yarn(screen, 220, 290, 50)  # У малого кота
    draw_yarn(screen, 630, 400, 60)  # Справа средний
    draw_yarn(screen, 150, 470, 55)  # Слева средний
    draw_yarn(screen, 550, 540, 50)  # Внизу маленький

    # 4. коты
    # Большой Рыжий (Справа, смотрит влево)
    draw_cat(screen, C_ORANGE, 400, 300, 300, False)
    # Большой Серый (Слева, смотрит вправо)
    draw_cat(screen, C_GREY, 50, 380, 300, True)

    # котята
    draw_cat(screen, C_ORANGE, 80, 300, 100, False)  # Верх лево
    draw_cat(screen, C_ORANGE, 650, 420, 100, False)  # Сред право
    draw_cat(screen, C_GREY, 100, 540, 100, True)  # Низ лево
    draw_cat(screen, C_ORANGE, 500, 490, 100, False)  # Низ центр
    draw_cat(screen, C_GREY, 660, 530, 100, True)  # Низ право

    # 5. большие клубы
    draw_yarn(screen, 460, 430, 110)  # Центр (самый большой)
    draw_yarn(screen, 280, 480, 160)  # Центр-низ (самый большой)
    draw_yarn(screen, 620, 480, 120)  # Справа большой

    pygame.display.flip()
    clock.tick(30)

pygame.quit()#