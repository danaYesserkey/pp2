import pygame
import sys  #для работы с окнами и системой
from pygame.locals import *  #для константы pygame (типа QUIT, K_LEFT)
import random  #для случайностей
import time  #для пауз

pygame.init()  # апускаем
FPS = 60  #частота
FramePerSec = pygame.time.Clock()  #контроль FPS

BLUE  = (0, 0, 255)  # синий
RED   = (255, 0, 0)  # красный
GREEN = (46, 139, 87)  # зелёный
BLACK = (0, 0, 0)  # чёрный
WHITE = (255, 255, 255)  # белый
GRAY = (40, 40, 40)  # серый

SPEED = 1  #коин и енеми
SCORE = 0  # счётчик енеми
CSCORE = 0  # счётчик коин

font = pygame.font.SysFont("Verdana", 60)  #шрифт счёта
font_small = pygame.font.SysFont("Verdana", 20)  # маленький теперь

SCREEN_WIDTH = 400  #ширина
SCREEN_HEIGHT = 600  #высота
DISPLAYSURF = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))  #окно
pygame.display.set_caption("Racer")  #заголовок

background = pygame.image.load("AnimatedStreet.png")  #фон

class Enemy(pygame.sprite.Sprite):  # класс енеми
    def __init__(self):
        super().__init__()  #родак 
        self.image = pygame.image.load("Enemy.png")  #енеми пнг
        self.rect = self.image.get_rect()  #позиция 
        self.rect.center = (random.randint(40, SCREEN_WIDTH - 40), 0)  #случайно коямыз енеми

    def move(self):
        global SCORE  #переменная счет
        self.rect.move_ip(0, SPEED)  #SPEED енеми
        if self.rect.top > SCREEN_HEIGHT:  #чтобы не вышел за экран
            SCORE += 1  #+ счётчик
            self.rect.top = 0  #много енеми было
            self.rect.center = (random.randint(40, SCREEN_WIDTH - 40), 0)  #енеми по горизонтали


class Player(pygame.sprite.Sprite):  # класс игрока
    def __init__(self):
        super().__init__()  #родак иницизация
        self.image = pygame.image.load("Player.png")  #пнг игрок
        self.rect = self.image.get_rect()  #позиция
        self.rect.center = (160, 520)  #снизу по центру

    def move(self):
        pressed_keys = pygame.key.get_pressed()  #нажат клавиши
        if pressed_keys[K_LEFT] and self.rect.left > 40:  #не выходим за границей
            self.rect.move_ip(-5, 0)  #влево на 5 пикселей
        if pressed_keys[K_RIGHT] and self.rect.right < SCREEN_WIDTH - 40:  #не выходим за границу
            self.rect.move_ip(5, 0)  #вправо на 5 пикселей


class Coin(pygame.sprite.Sprite):  # класс коин
    def __init__(self):
        super().__init__()  #родакируем
        self.image = pygame.image.load("coin.png")  #коин пнг
        self.rect = self.image.get_rect()  #позиция 
        self.rect.center = (random.randint(40, SCREEN_WIDTH - 40), 0)  #случайном по горизонтали

    def move(self):
        self.rect.move_ip(0, SPEED)  #SPEED 
        if self.rect.top > SCREEN_HEIGHT:  #если вышла за границей 
            self.rect.top = 0  #возвращаем наверх
            self.rect.center = (random.randint(40, SCREEN_WIDTH - 40), 0)  #случайное по горизонтали


P1 = Player()  #игрок
E1 = Enemy()  #енеми
C1 = Coin()  #коин

enemies = pygame.sprite.Group()  #енеми груп
enemies.add(E1)  #add енеми
all_sprites = pygame.sprite.Group()  #для всех спрайтов
all_sprites.add(P1)  #игрок
all_sprites.add(E1)  #енеми
all_sprites.add(C1)  #коин
collectables = pygame.sprite.Group()  #счет коин
collectables.add(C1)  #add коин

INC_SPEED = pygame.USEREVENT + 1  #увеличения скорости
pygame.time.set_timer(INC_SPEED, 1000)  #таймер для игры

def show_game_over():  # экран конец игры
    overlay = pygame.Surface((SCREEN_WIDTH, SCREEN_HEIGHT), pygame.SRCALPHA)  # слой сверху
    overlay.fill((0, 0, 0, 180))  # чёрный с прозрачностью
    DISPLAYSURF.blit(overlay, (0, 0))  # кладём слой на экран

    title_font = pygame.font.SysFont("Verdana", 50)  # шрифт
    title = title_font.render("GAME OVER", True, (255, 90, 90))  # текст GAME OVER

    title_rect = title.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 - 100))  # по центру
    DISPLAYSURF.blit(title, title_rect)  # рисуем текст

    button_width = 200  # ширина кнопки
    button_height = 60  # высота
    button_x = (SCREEN_WIDTH - button_width) // 2  # X центр
    button_y = SCREEN_HEIGHT // 2 + 20  # чуть ниже центра
    button_rect = pygame.Rect(button_x, button_y, button_width, button_height)  # прямоугольник кнопки

    pygame.draw.rect(DISPLAYSURF, GREEN, button_rect, border_radius=10)  # кнопка зелёная
    btn_text = pygame.font.SysFont("Verdana", 28).render("Play Again", True, WHITE)  # текст кнопки
    text_rect = btn_text.get_rect(center=button_rect.center)  # центр текста
    DISPLAYSURF.blit(btn_text, text_rect)  # рисуем текст

    pygame.display.update()  # обновляем экран
    return button_rect  # возврат кнопки


# --- Главный цикл ---
while True:  # игра бесконечно
    for event in pygame.event.get():  # все события
        if event.type == INC_SPEED:  # если пришёл сигнал увеличить скорость
            SPEED += 0.5  # ускоряем енеми
        if event.type == QUIT:  # если выход
            pygame.quit()  # выключаем pygame
            sys.exit()  # завершаем

    DISPLAYSURF.blit(background, (0, 0))  # рисуем фон
    scores = font_small.render(str(SCORE), True, BLACK)  # очки енеми
    DISPLAYSURF.blit(scores, (10, 10))  # слева вверху
    coinscores = font_small.render(str(CSCORE), True, BLACK)  # очки коин
    DISPLAYSURF.blit(coinscores, (370, 10))  # справа вверху

    for entity in all_sprites:  # каждый объект
        DISPLAYSURF.blit(entity.image, entity.rect)  # рисуем
        entity.move()  # двигаем

    if pygame.sprite.spritecollideany(P1, enemies):  # если игрок столкнулся с енеми
        pygame.mixer.Sound('crash.wav').play()  # звук
        time.sleep(0.4)  # пауза
        button_rect = show_game_over()  # экран конец игры

        for entity in all_sprites:  # очищаем всех
            entity.kill()  # убираем спрайты

        waiting = True  # ждём клика
        while waiting:  # пока ждём
            for event in pygame.event.get():  # проверка событий
                if event.type == QUIT:  # выход
                    pygame.quit()  # выход
                    sys.exit()  # конец
                if event.type == pygame.MOUSEBUTTONDOWN:  # клик
                    if button_rect.collidepoint(event.pos):  # если по кнопке
                        SPEED = 1  # сброс скорости
                        SCORE = 0  # сброс счёта
                        CSCORE = 0  # сброс коин
                        P1 = Player()  # новый игрок
                        E1 = Enemy()  # новый енеми
                        C1 = Coin()  # новая коина
                        enemies = pygame.sprite.Group()  # группа енеми
                        enemies.add(E1)  # добавить енеми
                        all_sprites = pygame.sprite.Group()  # все спрайты
                        all_sprites.add(P1)  # игрок
                        all_sprites.add(E1)  # енеми
                        all_sprites.add(C1)  # коина
                        collectables = pygame.sprite.Group()  # группа коин
                        collectables.add(C1)  # добавить коину
                        waiting = False  # выходим из ожидания
            pygame.time.Clock().tick(30)  # FPS при ожидании
        continue  # продолжаем цикл

    if pygame.sprite.spritecollide(P1, collectables, True):  # если коин собрана
        CSCORE += 1  # + коин

    if not C1.alive():  # если коин исчезла
        C1 = Coin()  # новая коина
        collectables.add(C1)  # добавить коину

    for entity in collectables:  # все коины
        DISPLAYSURF.blit(entity.image, entity.rect)  # рисуем
        entity.move()  # двигаем вниз

    pygame.display.update()  # обновляем
    FramePerSec.tick(FPS)  # 60 FPS