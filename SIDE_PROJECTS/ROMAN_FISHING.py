#ROMAN_FISHING
import os
import random
import sys
import pygame

BASE_DIR = os.path.dirname(os.path.abspath(__file__))


def roman_fishing():
    pygame.init()

    width = 1500
    height = 820
    screen = pygame.display.set_mode((width, height))
    pygame.display.set_caption('Рыбалка by Roman')

    icon_path = os.path.join(BASE_DIR, 'img', 'icon.png')
    fish_path = os.path.join(BASE_DIR, 'img', 'fish.png')
    hook_path = os.path.join(BASE_DIR, 'img', 'hook2.png')

    if os.path.exists(icon_path):
        icon = pygame.image.load(icon_path)
        pygame.display.set_icon(icon)

    font = pygame.font.Font(None, 36)

    # Рыбы
    fishes = []
    fish_surface = pygame.image.load(fish_path)

    for _ in range(8):
        x = random.randint(0, width)
        y = random.randint(350, height - 100)
        speed = random.randint(3, 10)
        fishes.append({
            'surf': fish_surface,
            'rect': fish_surface.get_rect(topleft=(x, y)),
            'speed': speed,
            'x': x,
            'y': y
        })

    fish_get = 0

    # Крюк (сохраняем оригинальное изображение для поворотов!)
    hook_original = pygame.image.load(hook_path)

    angle = -70
    xh = 930
    yh = 30
    turn = True

    lift = False
    runhook = 0
    directhook = 1

    clock = pygame.time.Clock()
    running = True

    # Главный цикл мини-игры
    while running:
        # 1. Обработка событий
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False  # Выходим из цикла, а не убиваем весь процесс!

            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    running = False  # Выход на ESC
                elif event.key in (pygame.K_SPACE, pygame.K_UP):
                    turn = False

            elif event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    turn = False

        # 2. Ход рыб
        for fish in fishes:
            fish['x'] += fish['speed']
            if fish['x'] > width:
                fish['x'] = 0
                fish['y'] = random.randint(350, height - 100)
            fish['rect'].topleft = (fish['x'], fish['y'])

        screen.fill('#0047AB')

        for fish in fishes:
            screen.blit(fish['surf'], fish['rect'])

        # 3. Ход крюка
        if turn:
            if angle > 70:
                directhook = 0
            if directhook == 1:
                angle += 1
            else:
                angle -= 1
                if angle < -70:
                    directhook = 1
        else:
            if runhook == 0:
                runhook = 1
            if runhook == 1:
                yh += 10
                xh += angle / 4
                if yh >= height + 100:
                    runhook = -1
                    lift = True
            elif runhook == -1:
                yh -= 10
                xh -= angle / 4
                if yh <= 30:
                    turn = True
                    runhook = 0
                    yh = 30
                    xh = 930
                    lift = False

        # Вращаем исходник, чтобы не копилась деформация
        hook_rotated = pygame.transform.rotate(hook_original, angle)
        hook_rect = hook_rotated.get_rect(center=(int(xh), int(yh)))
        screen.blit(hook_rotated, hook_rect)

        # 4. Проверка столкновений
        if not lift:
            for fish in fishes:
                if hook_rect.colliderect(fish['rect']):
                    fish['x'] = 0
                    fish['y'] = random.randint(350, height - 100)
                    fish['speed'] = random.randint(2, 10)
                    runhook = -1
                    fish_get += 1
                    lift = True
                    break

        # Отрисовка счета
        text = font.render(f'Поймано рыб: {fish_get}', True, (255, 255, 255))
        screen.blit(text, (10, 10))

        pygame.display.flip()
        clock.tick(60)

    # КОРРЕКТНОЕ ЗАВЕРШЕНИЕ: закрываем только окно Pygame и возвращаем управление в IMPERIVM
    pygame.quit()
    return fish_get