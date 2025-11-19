import pygame  #графический интерфейс
pygame.init()  # все модули 

WIDTH, HEIGHT = 740, 480  # ширина и высота
TOOLBAR_H = 60  # высота панели
PALETTE_H = 60  # высота палитры
screen = pygame.display.set_mode((WIDTH, HEIGHT))  # создаём окно
pygame.display.set_caption("Paint")  #заголовок

clock = pygame.time.Clock()  # контроль FPS

WHITE = (255, 255, 255)  #белый
GRAY = (60, 60, 60)  #серый
LIGHTGRAY = (120, 120, 120)  #светло-серый
BLACK = (0, 0, 0)  #чёрный

tools = [
    "brush", "eraser", "rect", "square",
    "circle", "right_triangle", "equil_triangle", "rhombus"
]
tool_rects = []  #прямоугольники
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

def draw_icon(surf, rect, tool):
    cx = rect.centerx
    cy = rect.centery
    w = rect.width - 16
    h = rect.height - 16

    # Brush – короткая линия
    if tool == "brush":
        pygame.draw.line(surf, BLACK, (cx - 12, cy), (cx + 12, cy), 4)

    # Eraser – белый квадрат
    elif tool == "eraser":
        pygame.draw.rect(surf, WHITE, (cx - 10, cy - 10, 20, 20))

    # Rect – прямоугольник
    elif tool == "rect":
        pygame.draw.rect(surf, BLACK, (cx - 14, cy - 10, 28, 20), 2)

    # Square – квадрат
    elif tool == "square":
        pygame.draw.rect(surf, BLACK, (cx - 12, cy - 12, 24, 24), 2)

    # Circle – круг
    elif tool == "circle":
        pygame.draw.circle(surf, BLACK, (cx, cy), 12, 2)

    # Right Triangle – прямоугольный треугольник
    elif tool == "right_triangle":
        pts = [(cx - 12, cy - 12), (cx - 12, cy + 12), (cx + 12, cy + 12)]
        pygame.draw.polygon(surf, BLACK, pts, 2)

    # Equilateral Triangle – равносторонний
    elif tool == "equil_triangle":
        pts = [(cx, cy - 14), (cx - 12, cy + 10), (cx + 12, cy + 10)]
        pygame.draw.polygon(surf, BLACK, pts, 2)

    # Rhombus – ромб
    elif tool == "rhombus":
        pts = [(cx, cy - 14), (cx - 14, cy), (cx, cy + 14), (cx + 14, cy)]
        pygame.draw.polygon(surf, BLACK, pts, 2)


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
    pygame.draw.rect(screen, GRAY, (0, 0, WIDTH, TOOLBAR_H))
    tool_rects.clear()

    button_size = 40
    padding = 10

    x = padding
    y = 10

    for tool in tools:
        rect = pygame.Rect(x, y, button_size, button_size)
        pygame.draw.rect(screen, LIGHTGRAY if tool == current_tool else WHITE, rect)
        pygame.draw.rect(screen, BLACK, rect, 2)
        draw_icon(screen, rect, tool)
        tool_rects.append((rect, tool))
        x += button_size + 8

    font2 = pygame.font.SysFont("Verdana", 14)

    size_text = font2.render(f"Size: {radius}", True, WHITE)
    screen.blit(size_text, (WIDTH - 280, 20))

    plus_rect = pygame.Rect(WIDTH - 240, 15, 30, 30)
    minus_rect = pygame.Rect(WIDTH - 210, 15, 30, 30)
    pygame.draw.rect(screen, LIGHTGRAY, plus_rect)
    pygame.draw.rect(screen, BLACK, plus_rect, 2)
    pygame.draw.rect(screen, LIGHTGRAY, minus_rect)
    pygame.draw.rect(screen, BLACK, minus_rect, 2)

    plus_txt = font2.render("+", True, BLACK)
    minus_txt = font2.render("-", True, BLACK)
    screen.blit(plus_txt, plus_txt.get_rect(center=plus_rect.center))
    screen.blit(minus_txt, minus_txt.get_rect(center=minus_rect.center))

    undo_rect = pygame.Rect(WIDTH - 160, 15, 60, 30)
    clear_rect = pygame.Rect(WIDTH - 90, 15, 60, 30)
    pygame.draw.rect(screen, LIGHTGRAY, undo_rect)
    pygame.draw.rect(screen, BLACK, undo_rect, 2)
    pygame.draw.rect(screen, LIGHTGRAY, clear_rect)
    pygame.draw.rect(screen, BLACK, clear_rect, 2)

    screen.blit(font2.render("Undo", True, BLACK), undo_rect.move(10, 5))
    screen.blit(font2.render("Clear", True, BLACK), clear_rect.move(10, 5))

    return plus_rect, minus_rect, undo_rect, clear_rect


def draw_palette():
    pygame.draw.rect(screen, GRAY, (0, HEIGHT - PALETTE_H, WIDTH, PALETTE_H))
    palette_rects.clear()

    cell = 50
    pad = 10

    for i, color in enumerate(palette_colors):
        x = pad + i * (cell + 10)
        y = HEIGHT - PALETTE_H + pad
        rect = pygame.Rect(x, y, cell, cell)
        pygame.draw.rect(screen, color, rect)
        pygame.draw.rect(screen, WHITE if color == current_color else BLACK, rect, 2)
        palette_rects.append((rect, color))


points = []
drawing = False
start_pos = None
running = True

while running:
    screen.fill(BLACK)
    screen.blit(canvas, (0, TOOLBAR_H))
    plus_rect, minus_rect, undo_rect, clear_rect = draw_toolbar()
    draw_palette()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        elif event.type == pygame.MOUSEBUTTONDOWN:
            pos = event.pos

            for rect, tool in tool_rects:
                if rect.collidepoint(pos):
                    current_tool = tool
                    break
            else:
                for rect, color in palette_rects:
                    if rect.collidepoint(pos):
                        current_color = color
                        break
                else:
                    if plus_rect.collidepoint(pos):
                        radius = min(100, radius + 1)
                    elif minus_rect.collidepoint(pos):
                        radius = max(1, radius - 1)
                    elif undo_rect.collidepoint(pos):
                        if len(history) > 1:
                            history.pop()
                            canvas.blit(history[-1], (0, 0))
                    elif clear_rect.collidepoint(pos):
                        canvas.fill(BLACK)
                        history.append(canvas.copy())
                    else:
                        if TOOLBAR_H < pos[1] < HEIGHT - PALETTE_H:
                            drawing = True
                            start_pos = (pos[0], pos[1] - TOOLBAR_H)
                            points = [start_pos]

        elif event.type == pygame.MOUSEBUTTONUP:
            if drawing:
                end_pos = (event.pos[0], event.pos[1] - TOOLBAR_H)

                if current_tool == "rect":
                    rect = pygame.Rect(min(start_pos[0], end_pos[0]),
                                       min(start_pos[1], end_pos[1]),
                                       abs(end_pos[0] - start_pos[0]),
                                       abs(end_pos[1] - start_pos[1]))
                    pygame.draw.rect(canvas, current_color, rect, 2)
                    history.append(canvas.copy())

                elif current_tool == "square":
                    side = max(abs(end_pos[0] - start_pos[0]),
                               abs(end_pos[1] - start_pos[1]))
                    rect = pygame.Rect(start_pos[0], start_pos[1], side, side)
                    pygame.draw.rect(canvas, current_color, rect, 2)
                    history.append(canvas.copy())

                elif current_tool == "circle":
                    r = int(((end_pos[0] - start_pos[0]) ** 2 +
                             (end_pos[1] - start_pos[1]) ** 2) ** 0.5)
                    pygame.draw.circle(canvas, current_color, start_pos, r, 2)
                    history.append(canvas.copy())

                elif current_tool == "right_triangle":
                    pts = [start_pos,
                           (start_pos[0], end_pos[1]),
                           end_pos]
                    pygame.draw.polygon(canvas, current_color, pts, 2)
                    history.append(canvas.copy())

                elif current_tool == "equil_triangle":
                    sx, sy = start_pos
                    ex, ey = end_pos
                    h = abs(ey - sy)
                    pts = [(sx, sy), (sx - h, sy + h), (sx + h, sy + h)]
                    pygame.draw.polygon(canvas, current_color, pts, 2)
                    history.append(canvas.copy())

                elif current_tool == "rhombus":
                    sx, sy = start_pos
                    ex, ey = end_pos
                    pts = [(sx, sy - 20), (sx - 30, sy), (sx, sy + 20), (sx + 30, sy)]
                    pygame.draw.polygon(canvas, current_color, pts, 2)
                    history.append(canvas.copy())

                drawing = False

        elif event.type == pygame.MOUSEMOTION and drawing:
            pos = (event.pos[0], event.pos[1] - TOOLBAR_H)


            if current_tool == "brush":
                points.append(pos)
                points = points[-256:]
                for i in range(len(points) - 1):
                    draw_gradient_line(canvas, i, points[i], points[i + 1], radius, current_color)
                history.append(canvas.copy())


            elif current_tool == "eraser":
                points.append(pos)
                points = points[-256:]
                for i in range(len(points) - 1):
                    draw_gradient_line(canvas, i, points[i], points[i + 1], radius, BLACK)
                history.append(canvas.copy())

    pygame.display.flip()
    clock.tick(60)
pygame.quit()