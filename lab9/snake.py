import os  # работа с ОС
import sys  # системные функции
import random  # случайные числа
import pygame  # графика и события

CELL = 32  # размер клетки
GRID_W = 20  # ширина
GRID_H = 20  # высота

WIDTH = GRID_W * CELL  # ширина окна
HEIGHT = GRID_H * CELL  # высота окна

WHITE = (255, 255, 255)  # белый
GREEN = (46, 139, 87)  # зеленый
RED = (220, 58, 58)  # красный
YELLOW = (235, 195, 35)  # желтый
GRAY = (32, 32, 32)  # серый
BODY_COLOR = (38, 110, 74)  # тела змеи
BG_COLOR = (11, 30, 11)  # фон

START_LEN = 3  # начальная длина змеи
MOVE_MS = 200  # скорость движения (мс)
MIN_MOVE = 120  # минимальная скорость
LEVEL_EVERY = 40  # очки для повышения уровня
GOLD_CHANCE = 0.15  # шанс золотой еды

RUNNING = 0  # состояние игры - играем
GAME_OVER = 2  # состояние игры - конец игры


class Snake:  # класс змеи
    def __init__(self):
        self.reset()  # сброс змеи

    def reset(self):  # сброс змеи
        c = GRID_W // 2  # центр по x
        self.body = [(c, c + i) for i in range(START_LEN)]  # тело змеи
        self.dir = (0, -1)  # направление вверх
        self.next_dir = self.dir  # следующее направление
        self.grow = 0  # сколько расти

    def set_dir(self, d):  # задать направление
        if d != (-self.dir[0], -self.dir[1]):  # не разворот назад
            self.next_dir = d  # обновляем направление

    def step(self):  # двигаем змею
        self.dir = self.next_dir  # обновляем направление
        hx, hy = self.body[0]  # голова
        new_head = (hx + self.dir[0], hy + self.dir[1])  # новая позиция головы
        self.body.insert(0, new_head)  # добавляем голову

        if self.grow > 0:  # если надо расти
            self.grow -= 1  # уменьшаем счетчик роста
        else:
            self.body.pop()  # удаляем хвост

    def head(self):  # получить голову
        return self.body[0]  # возвращаем координаты головы

    def hits_self(self):  # проверка столкновения с собой
        return self.head() in self.body[1:]  # есть ли голова в теле


class Food:  # класс еды
    def __init__(self):
        self.pos = (0, 0)  # позиция еды
        self.is_gold = False  # золотая ли еда

        #еды и таймер исчезновения
        self.value = 1   # сколько очков / роста дает еда
        self.timer = 0   # время жизни еды в кадрах

    def respawn(self, snake, walls):  # появление еды
        self.is_gold = random.random() < GOLD_CHANCE  # шанс золотой еды

        free = [  # свободные клетки
            (x, y)
            for x in range(GRID_W)
            for y in range(GRID_H)
            if (x, y) not in snake and (x, y) not in walls  # не заняты
        ]
        self.pos = random.choice(free)  # новая позиция еды

        # >>> добавлено Lab 9: назначаем вес еды
        if self.is_gold:
            self.value = random.randint(4, 6)     # золотая — тяжелее
        else:
            self.value = random.randint(1, 3)     # обычная — слабее

        #таймер жизни еды (примерно 4 секунды)
        self.timer = 60 * 4


def make_border():  # создаем стены по краям
    w = set()  # множество стен
    for x in range(GRID_W):  # верх и низ
        w.add((x, 0))  # верхняя стена
        w.add((x, GRID_H - 1))  # нижняя стена
    for y in range(GRID_H):  # левый и правый край
        w.add((0, y))  # левая стена
        w.add((GRID_W - 1, y))  # правая стена
    return w  # возвращаем стены


def draw(screen, walls, food, snake, font, score, level, over_rect=None, game_over=False):
    # фон
    screen.fill(BG_COLOR)  # заливаем фон

    # стены
    for (x, y) in walls:  # рисуем стены
        pygame.draw.rect(screen, GRAY, (x * CELL, y * CELL, CELL, CELL))  # квадрат стены

    # еда
    x, y = food.pos  # позиция еды
    px, py = x * CELL, y * CELL  # пиксели
    color = YELLOW if food.is_gold else RED  # еды
    pygame.draw.circle(screen, color, (px + CELL // 2, py + CELL // 2), CELL // 2 - 3)  # рисуем еду

    # змейка
    for i, (x, y) in enumerate(snake.body):  # рисуем тело змеи
        px, py = x * CELL, y * CELL  # пиксели клетки
        if i == 0:  # голова
            pygame.draw.rect(screen, GREEN, (px + 2, py + 2, CELL - 4, CELL - 4), border_radius=6)  # зеленый квадрат
        else:
            pygame.draw.rect(screen, BODY_COLOR, (px + 2, py + 2, CELL - 4, CELL - 4), border_radius=4)  # тело змеи

    # текст
    text = font.render(f"Score: {score}  Level: {level}", True, WHITE)  # счет и уровень
    screen.blit(text, (10, 10))  # рисуем текст

    # экран Game Over
    if game_over:  # если конец игры
        overlay = pygame.Surface((WIDTH, HEIGHT), pygame.SRCALPHA)  # полупрозрачный фон
        overlay.fill((0, 0, 0, 160))  # черный с прозрачностью
        screen.blit(overlay, (0, 0))  # накладываем

        t = font.render("GAME OVER", True, (255, 90, 90))  # текст Game Over
        screen.blit(t, (WIDTH // 2 - 100, HEIGHT // 2 - 80))  # рисуем текст

        pygame.draw.rect(screen, GREEN, over_rect, border_radius=8)  # кнопка заново
        screen.blit(font.render("Play Again", True, WHITE), over_rect.move(40, 10))  # текст кнопки


def main():
    pygame.init()  # запуск pygame
    screen = pygame.display.set_mode((WIDTH, HEIGHT))  # окно игры
    pygame.display.set_caption("Змейка")  # заголовок окна

    clock = pygame.time.Clock()  # часы для FPS
    font = pygame.font.SysFont("Verdana", 24)  # шрифт

    snake = Snake()  # создаем змею
    walls = make_border()  # создаем стены
    food = Food()  # создаем еду
    food.respawn(snake.body, walls)  # ставим еду

    score = 0  # счет
    level = 1  # уровень
    move_ms = MOVE_MS  # скорость

    MOVE_EVENT = pygame.USEREVENT + 1  # событие движения змеи
    pygame.time.set_timer(MOVE_EVENT, move_ms)  # таймер движения

    state = RUNNING  # состояние игры
    btn_rect = pygame.Rect(WIDTH // 2 - 100, HEIGHT // 2, 200, 50)  # кнопка игры заново
    dir_buf = snake.dir  # буфер направления

    while True:  # главный цикл
        for e in pygame.event.get():  # перебираем события
            if e.type == pygame.QUIT:  # выход из игры
                pygame.quit()  # закрываем pygame
                sys.exit()  # выходим из программы

            elif e.type == pygame.KEYDOWN:  # клавиша нажата
                k = e.key  # какая клавиша
                if state == RUNNING:  # если игра идет
                    key_dir = {  # словарь направлений
                        pygame.K_UP: (0, -1),  # вверх
                        pygame.K_w: (0, -1),  # вверх (W)
                        pygame.K_DOWN: (0, 1),  # вниз
                        pygame.K_s: (0, 1),  # вниз (S)
                        pygame.K_LEFT: (-1, 0),  # влево
                        pygame.K_a: (-1, 0),  # влево (A)
                        pygame.K_RIGHT: (1, 0),  # вправо
                        pygame.K_d: (1, 0),  # вправо (D)
                    }
                    if k in key_dir:  # если направление есть
                        dir_buf = key_dir[k]  # меняем буфер направления

                elif state == GAME_OVER and k == pygame.K_RETURN:  # если конец игры и нажали Enter
                    snake.reset()  # сброс змеи
                    score = 0  # сброс счета
                    level = 1  # сброс уровня
                    move_ms = MOVE_MS  # сброс скорости
                    food.respawn(snake.body, walls)  # новая еда
                    state = RUNNING  # играем снова

            elif e.type == pygame.MOUSEBUTTONDOWN and state == GAME_OVER and btn_rect.collidepoint(e.pos):
                # клик по кнопке "Play Again"
                snake.reset()  # сброс змеи
                score = 0  # сброс счета
                level = 1  # сброс уровня
                move_ms = MOVE_MS  # сброс скорости
                food.respawn(snake.body, walls)  # новая еда
                state = RUNNING  # играем снова

            elif e.type == MOVE_EVENT and state == RUNNING:  # событие движения змеи
                snake.set_dir(dir_buf)  # задаем направление
                snake.step()  # двигаем змею

                #уменьшение таймера еды
                food.timer -= 1
                if food.timer <= 0:
                    food.respawn(snake.body, walls)

                hx, hy = snake.head()  # голова змеи

                if (hx, hy) in walls or not (0 <= hx < GRID_W and 0 <= hy < GRID_H) or snake.hits_self():
                    # проверка столкновения со стеной, границами или собой
                    state = GAME_OVER  # конец игры

                elif (hx, hy) == food.pos:  # если съели еду
                    #очки зависят от веса еды
                    if food.is_gold:
                        score += random.randint(30, 50)
                    else:
                        score += random.randint(10, 20)

                    snake.grow += food.value  # рост зависит от веса еды
                    food.respawn(snake.body, walls)  # новая еда

                    new_level = score // LEVEL_EVERY + 1  # вычисляем уровень
                    if new_level > level:  # если уровень повысился
                        level = new_level  # обновляем уровень
                        move_ms = max(MIN_MOVE, int(move_ms * 0.96))  # ускоряем игру
                        pygame.time.set_timer(MOVE_EVENT, move_ms)  # новый таймер

        draw(screen, walls, food, snake, font, score, level, btn_rect, state == GAME_OVER)  # рисуем все
        pygame.display.flip()  # обновляем экран
        clock.tick(60)  # FPS


if __name__ == "__main__":
    main()  # запускаем игру