import pygame  #графический интерфейс
pygame.init()  # все модули 

WIDTH, HEIGHT = 640, 480  # ширина и высота
TOOLBAR_H = 60  # высота панели
PALETTE_H = 60  # высота палитры
screen = pygame.display.set_mode((WIDTH, HEIGHT))  # создаём окно
pygame.display.set_caption("Paint")  #заголовок

clock = pygame.time.Clock()  # контроль FPS

WHITE = (255, 255, 255)  #белый
GRAY = (60, 60, 60)  #серый
LIGHTGRAY = (120, 120, 120)  #светло-серый
BLACK = (0, 0, 0)  #чёрный

tools = ["brush", "rect", "circle", "eraser"]  # список инструментов
tool_rects = []  #прямоугольник
current_tool = "brush"  # текущий
radius = 8  # радиус

palette_colors = [  #палитры
    (255, 0, 0), (0, 255, 0), (0, 0, 255),
    (255, 255, 0), (255, 0, 255), (0, 255, 255),
    (255, 255, 255), (0, 0, 0)
]
palette_rects = []  #палитра прямоугольника
current_color = (0, 0, 255)  # текущий

canvas = pygame.Surface((WIDTH, HEIGHT - TOOLBAR_H - PALETTE_H))  #поверхность для рисования
canvas.fill(BLACK)  #холст чёрный

history = [canvas.copy()]  #истории холста

def draw_gradient_line(surf, index, start, end, width, color_mode):  # функция для рисования
    c1 = max(0, min(255, 2 * index - 256))  #первый компонент цвета
    c2 = max(0, min(255, 2 * index))  #второй компонент цвета

    if color_mode == (0, 0, 255):  # если синий
        color = (c1, c1, c2)       # градиент фунция
    elif color_mode == (255, 0, 0):  # если красный
        color = (c2, c1, c1)
    elif color_mode == (0, 255, 0):  # если зелёный
        color = (c1, c2, c1)
    elif color_mode == (0, 255, 255):  #если бирюзовый
        color = (c1, c2, c2)
    elif color_mode == (255, 0, 255):  #если якро розовый 
        color = (c2, c1, c2)
    elif color_mode == (255, 255, 0):  #если желтый
        color = (c2, c2, c1)
    elif color_mode == (255, 165, 0):  #если оранжевый 
        color = (c2, int(c2*0.65), 0)
    elif color_mode == (128, 0, 128):  #если фиолетовый
        color = (int(c2*0.5), 0, int(c2*0.5))
    elif color_mode == (255, 192, 203):  #если розовый
        color = (c2, int(c2*0.75), int(c2*0.8))
    elif color_mode == (255, 255, 255):  #если белый
        color = (c2, c2, c2)
    else:
        color = color_mode  # используем исходный цвет

    dx = start[0] - end[0]  #по X
    dy = start[1] - end[1]  #по Y
    iterations = max(abs(dx), abs(dy))  #количество шагов
    if iterations == 0:  # начальная и конечная точка 
        pygame.draw.circle(surf, color, start, width)  #круговое рисование
        return  #все бытты рисование 

    for i in range(iterations):  # цикл точками 
        progress = i / iterations  #от 0 до 1 
        aprogress = 1 - progress  # обратно 
        x = int(aprogress * start[0] + progress * end[0])  #X
        y = int(aprogress * start[1] + progress * end[1])  #Y
        pygame.draw.circle(surf, color, (x, y), width)  #на текущей точке рисуем

def draw_toolbar():  #панель инструментов
    pygame.draw.rect(screen, GRAY, (0, 0, WIDTH, TOOLBAR_H))  #фон
    tool_rects.clear()  #прямоугольние кнопок
    font = pygame.font.SysFont("Verdana", 16)  #шрифт
    button_width = 55  # ширина
    button_height = 40  #высота
    button_spacing = 5  # отступ
    for i, tool in enumerate(tools):  #инструменты по индексом
        rect = pygame.Rect(10 + i * (button_width + button_spacing), 10, button_width, button_height)  #позиция и размер
        pygame.draw.rect(screen, LIGHTGRAY 
                         if tool == current_tool 
                         else WHITE, rect)  #кнопка текущая
        pygame.draw.rect(screen, BLACK, rect, 2)  #рамку
        text = font.render(tool.capitalize(), True, BLACK)  #текст
        text_rect = text.get_rect(center=rect.center)  #в центре
        screen.blit(text, text_rect)  #на экране
        tool_rects.append((rect, tool))  #добавляем кнопку

    font2 = pygame.font.SysFont("Verdana", 14)  #шрифт размера
    size_text = font2.render(f"Size: {radius}", True, WHITE)  #размер размераааа
    size_rect = size_text.get_rect()  #прямоугольник текст
    size_rect.topleft = (WIDTH - 280, 20)  #текст с слева

    screen.blit(size_text, size_rect)  #текст размера

    plus_rect = pygame.Rect(WIDTH - 240, 15, 30, 30)  #add +
    minus_rect = pygame.Rect(WIDTH - 210, 15, 30, 30)  #-
    pygame.draw.rect(screen, LIGHTGRAY, plus_rect)
    pygame.draw.rect(screen, BLACK, plus_rect, 2)  #рамка
    pygame.draw.rect(screen, LIGHTGRAY, minus_rect)
    pygame.draw.rect(screen, BLACK, minus_rect, 2)

    plus_text = font2.render("+", True, BLACK)  #текст
    minus_text = font2.render("−", True, BLACK)
    plus_text_rect = plus_text.get_rect(center=plus_rect.center)  #центр
    minus_text_rect = minus_text.get_rect(center=minus_rect.center)
    screen.blit(plus_text, plus_text_rect)
    screen.blit(minus_text, minus_text_rect)

    undo_width = 55  #ширина
    clear_width = 55
    undo_height = 30  #высота
    clear_height = 30
    button_spacing2 = 15  #отступ
    right_margin = 60
    total_width = undo_width + clear_width + button_spacing2  #суммарная ширина
    undo_x = WIDTH - right_margin - total_width + 20  # позиция
    clear_x = undo_x + undo_width + button_spacing2
    undo_rect = pygame.Rect(undo_x, 15, undo_width, undo_height)  #Undo
    clear_rect = pygame.Rect(clear_x, 15, clear_width, clear_height)  #Clear
    pygame.draw.rect(screen, LIGHTGRAY, undo_rect)
    pygame.draw.rect(screen, BLACK, undo_rect, 2)
    pygame.draw.rect(screen, LIGHTGRAY, clear_rect)
    pygame.draw.rect(screen, BLACK, clear_rect, 2)

    undo_text = font2.render("Undo", True, BLACK)  #текст
    clear_text = font2.render("Clear", True, BLACK)
    undo_text_rect = undo_text.get_rect(center=undo_rect.center)  #центр
    clear_text_rect = clear_text.get_rect(center=clear_rect.center)
    screen.blit(undo_text, undo_text_rect)
    screen.blit(clear_text, clear_text_rect)

    return plus_rect, minus_rect, undo_rect, clear_rect  #кнопоки

def draw_palette():  #палитры
    pygame.draw.rect(screen, GRAY, (0, HEIGHT - PALETTE_H, WIDTH, PALETTE_H))  #фон
    palette_rects.clear()  #список цветов
    cell_size = 50  #размер
    padding = 10  #отступ
    for i, color in enumerate(palette_colors):  #индекс
        x = padding + i * (cell_size + 10)  #X для ячейки
        y = HEIGHT - PALETTE_H + padding  #и для этого Yка
        rect = pygame.Rect(x, y, cell_size, cell_size)  #прямоугольники
        pygame.draw.rect(screen, color, rect)  #цвета
        pygame.draw.rect(screen, WHITE if color == current_color else BLACK, rect, 2)  #рамка
        palette_rects.append((rect, color))  #в список add

points = []  #точки линии
drawing = False  #флаг draw
start_pos = None  #начало позиции
running = True  #флаг работат

while running:  #цикл бежуши
    screen.fill(BLACK)  #экран чёрный
    screen.blit(canvas, (0, TOOLBAR_H))  #холст на экране
    plus_rect, minus_rect, undo_rect, clear_rect = draw_toolbar()  #гет тулс
    draw_palette()  #палитра

    for event in pygame.event.get():  #все события
        if event.type == pygame.QUIT:  # если окно энд
            running = False  #делаем энд

        elif event.type == pygame.MOUSEBUTTONDOWN:  #нажамкаем
            pos = event.pos  #позиция для мыши

            for rect, tool in tool_rects:  #чек тулс
                if rect.collidepoint(pos):  #если клик
                    current_tool = tool  #чандже тулс
                    break
            else:
                for rect, color in palette_rects:  #чек палитра
                    if rect.collidepoint(pos):  #клик
                        current_color = color  #то чандже цвет
                        break
                else:
                    if plus_rect.collidepoint(pos):  #кнопка +
                        radius = min(100, radius + 1)  #радиус +
                    elif minus_rect.collidepoint(pos):  #кнопка -
                        radius = max(1, radius - 1)  #радиус -
                    elif undo_rect.collidepoint(pos):  #кнопка назад
                        if len(history) > 1:  #исторя коремыз
                            history.pop()  #дел последний
                            canvas.blit(history[-1], (0, 0))  #предыдущий холст
                    elif clear_rect.collidepoint(pos):  #кнопка очистка
                        canvas.fill(BLACK)  #очищаем
                        history.append(canvas.copy())  #сейф состояние
                    else:
                        if TOOLBAR_H < pos[1] < HEIGHT - PALETTE_H:  #если клик холста
                            drawing = True  #рисуем
                            start_pos = (pos[0], pos[1] - TOOLBAR_H)  #сейф позицию
                            points = [start_pos]  #список точек

        elif event.type == pygame.MOUSEBUTTONUP:  #мышка нот тоуч
            if drawing:  # если рисуем
                end_pos = (event.pos[0], event.pos[1] - TOOLBAR_H)  #позицию начинаем
                if current_tool == "rect":  # если прямоугольник
                    rect = pygame.Rect(min(start_pos[0], end_pos[0]),
                                       min(start_pos[1], end_pos[1]),
                                       abs(end_pos[0] - start_pos[0]),
                                       abs(end_pos[1] - start_pos[1]))  #создаём прямоугольник
                    pygame.draw.rect(canvas, current_color, rect, 2)  #рисуем прямоугольник
                    history.append(canvas.copy())  #сохраняем
                elif current_tool == "circle":  # если круг
                    r = int(((end_pos[0]-start_pos[0])**2 + (end_pos[1]-start_pos[1])**2)**0.5)  #радиус
                    pygame.draw.circle(canvas, current_color, start_pos, r, 2)  #рисуем круг
                    history.append(canvas.copy())  #сохраняем тоже
                drawing = False  #кончается рисовка

        elif event.type == pygame.MOUSEMOTION and drawing:  #мышка движется
            pos = (event.pos[0], event.pos[1] - TOOLBAR_H)  #гет позицию
            if current_tool == "brush":  # если кисть
                points.append(pos)  #add точку в список
                points = points[-256:]  #ограничиваем точки
                for i in range(len(points) - 1):  #рисуем градиент
                    draw_gradient_line(canvas, i, points[i], points[i + 1], radius, current_color)  #функция рисования
                history.append(canvas.copy())  #сохраняем
            elif current_tool == "eraser":  #если ластик
                pygame.draw.circle(canvas, BLACK, pos, radius)  #чёрный круг для стирания
                history.append(canvas.copy())  #сохраняем опять про еасер

    pygame.display.flip()  # обновляем
    clock.tick(60)  #ограничиваем FPS

pygame.quit()  #the end