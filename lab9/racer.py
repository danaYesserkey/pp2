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

#9
next_speed_level = 10  # когда игрок наберёт 10 монет, енеми ускорится


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
        
        #монеты разной ценности
        self.value = random.choice([1, 2, 5])  # вес монеты

    def move(self):
        self.rect.move_ip(0, SPEED)  #SPEED 
        if self.rect.top > SCREEN_HEIGHT:  #если вышла за границей 
            self.rect.top = 0  #возвращаем наверх
            self.rect.center = (random.randint(40, SCREEN_WIDTH - 40), 0)  #случайное по горизонтали
            
            #обновляем ценность монеты после пересоздания
            self.value = random.choice([1, 2, 5])


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


while True:  # игра бесконечно
    for event in pygame.event.get():  # все события
        if event.type == INC_SPEED:  # если пришёл сигнал увеличить скорость
            SPEED += 0.5  # ускоряем енемi
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

    # Проверка столкновения с енеми
    if pygame.sprite.spritecollideany(P1, enemies):  
        pygame.mixer.Sound('crash.wav').play()  
        time.sleep(0.4)  
        button_rect = show_game_over()  

        for entity in all_sprites:  
            entity.kill()  

        waiting = True  
        while waiting:  
            for event in pygame.event.get():  
                if event.type == QUIT:  
                    pygame.quit()  
                    sys.exit()  
                if event.type == pygame.MOUSEBUTTONDOWN:  
                    if button_rect.collidepoint(event.pos):  
                        SPEED = 1  
                        SCORE = 0  
                        CSCORE = 0  

                        # >>> сбрасываем новый уровень скорости
                        next_speed_level = 10

                        P1 = Player()  
                        E1 = Enemy()  
                        C1 = Coin()  
                        enemies = pygame.sprite.Group()  
                        enemies.add(E1)  
                        all_sprites = pygame.sprite.Group()  
                        all_sprites.add(P1)  
                        all_sprites.add(E1)  
                        all_sprites.add(C1)  
                        collectables = pygame.sprite.Group()  
                        collectables.add(C1)  
                        waiting = False  
            pygame.time.Clock().tick(30)  
        continue  

    # Проверка столкновения с монетой
    collected = pygame.sprite.spritecollide(P1, collectables, True)
    if collected:  
        for coin in collected:
            CSCORE += coin.value  #добавлено: прибавляем монеты

    #Ускорение Енеми если игрок собрал N монет
    if CSCORE >= next_speed_level:
        SPEED += 1  # ускоряем Enemy
        next_speed_level += 10  # следующий порог

    if not C1.alive():  
        C1 = Coin()  
        collectables.add(C1)  

    for entity in collectables:  
        DISPLAYSURF.blit(entity.image, entity.rect)  
        entity.move()  

    pygame.display.update()  
    FramePerSec.tick(FPS)