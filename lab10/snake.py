from game_db import get_or_create_user, get_last_user_state, save_user_state

import sys
import random
import pygame
import json


CELL = 32
GRID_W = 20
GRID_H = 20

WIDTH = GRID_W * CELL
HEIGHT = GRID_H * CELL

WHITE = (255, 255, 255)
GREEN = (46, 139, 87)
RED = (220, 58, 58)
YELLOW = (235, 195, 35)
GRAY = (32, 32, 32)
BODY_COLOR = (38, 110, 74)
BG_COLOR = (11, 30, 11)

RUNNING = 0
PAUSED = 1
GAME_OVER = 2

START_LEN = 3
MOVE_MS = 200
MIN_MOVE = 120
LEVEL_EVERY = 40
GOLD_CHANCE = 0.15


class Snake:
    def __init__(self):
        self.reset()

    def reset(self):
        c = GRID_W // 2
        self.body = [(c, c + i) for i in range(START_LEN)]
        self.dir = (0, -1)
        self.next_dir = self.dir
        self.grow = 0

    def set_dir(self, d):
        if d != (-self.dir[0], -self.dir[1]):
            self.next_dir = d

    def step(self):
        self.dir = self.next_dir
        hx, hy = self.body[0]
        new_head = (hx + self.dir[0], hy + self.dir[1])
        self.body.insert(0, new_head)

        if self.grow > 0:
            self.grow -= 1
        else:
            self.body.pop()

    def head(self):
        return self.body[0]

    def hits_self(self):
        return self.head() in self.body[1:]

class Food:
    def __init__(self):
        self.pos = (0, 0)
        self.is_gold = False
        self.value = 1
        self.timer = 0

    def respawn(self, snake, walls):
        from collections import deque

        self.is_gold = random.random() < GOLD_CHANCE

        free = [
            (x, y)
            for x in range(GRID_W)
            for y in range(GRID_H)
            if (x, y) not in snake and (x, y) not in walls
        ]

        snake_head = snake[0]

        def reachable(target):
            q = deque([snake_head])
            visited = set([snake_head])

            while q:
                cx, cy = q.popleft()
                if (cx, cy) == target:
                    return True

                for dx, dy in [(1,0),(-1,0),(0,1),(0,-1)]:
                    nx, ny = cx + dx, cy + dy

                    if (
                        0 <= nx < GRID_W and
                        0 <= ny < GRID_H and
                        (nx, ny) not in visited and
                        (nx, ny) not in walls
                    ):
                        visited.add((nx, ny))
                        q.append((nx, ny))

            return False

        reachable_cells = [c for c in free if reachable(c)]
        if not reachable_cells:
            reachable_cells = free

        self.pos = random.choice(reachable_cells)
        self.value = random.randint(4, 6) if self.is_gold else random.randint(1, 3)
        self.timer = 240

def make_border():
    w = set()
    for x in range(GRID_W):
        w.add((x, 0))
        w.add((x, GRID_H - 1))
    for y in range(GRID_H):
        w.add((0, y))
        w.add((GRID_W - 1, y))
    return w

def make_level2_walls():
    w = make_border()
    for x in range(3, GRID_W - 3):
        w.add((x, 4))
        w.add((x, GRID_H - 5))
    return w

def make_level3_walls():
    w = make_level2_walls()
    for y in range(3, GRID_H - 3):
        w.add((3, y))
        w.add((GRID_W - 4, y))
    return w

def draw(screen, walls, food, snake, font, score, level, btn_rect=None, game_over=False):
    screen.fill(BG_COLOR)

    for (x, y) in walls:
        pygame.draw.rect(screen, GRAY, (x * CELL, y * CELL, CELL, CELL))

    fx, fy = food.pos
    pygame.draw.circle(
        screen,
        YELLOW if food.is_gold else RED,
        (fx * CELL + CELL // 2, fy * CELL + CELL // 2),
        CELL // 2 - 3,
    )

    for i, (x, y) in enumerate(snake.body):
        if i == 0:
            pygame.draw.rect(screen, GREEN, (x * CELL + 2, y * CELL + 2, CELL - 4, CELL - 4))
        else:
            pygame.draw.rect(screen, BODY_COLOR, (x * CELL + 2, y * CELL + 2, CELL - 4, CELL - 4))

    screen.blit(font.render(f"Score: {score}  Level: {level}", True, WHITE), (10, 10))

    if game_over:
        overlay = pygame.Surface((WIDTH, HEIGHT), pygame.SRCALPHA)
        overlay.fill((0, 0, 0, 160))
        screen.blit(overlay, (0, 0))

        screen.blit(font.render("GAME OVER", True, (255, 90, 90)), (WIDTH // 2 - 100, HEIGHT // 2 - 80))

        pygame.draw.rect(screen, GREEN, btn_rect, border_radius=8)
        screen.blit(font.render("Play Again", True, WHITE), btn_rect.move(40, 10))

def main():
    pygame.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Snake Game")
    clock = pygame.time.Clock()
    font = pygame.font.SysFont("Verdana", 24)

    username = input("Enter your username: ")
    user_id = get_or_create_user(username)

    saved = get_last_user_state(user_id)

    if saved:
        level, score, state_text = saved
        print(f"Welcome back {username}! Level {level}, Score {score}")

        if state_text:
            restored = json.loads(state_text)
            snake_body = restored["snake"]
            food_pos = restored["food"]
        else:
            snake_body = None
            food_pos = None
    else:
        level = 1
        score = 0
        snake_body = None
        food_pos = None

    if level == 1:
        walls = make_border()
    elif level == 2:
        walls = make_level2_walls()
    else:
        walls = make_level3_walls()

    snake = Snake()
    if snake_body:
        snake.body = snake_body

    food = Food()
    if food_pos:
        food.pos = tuple(food_pos)
    else:
        food.respawn(snake.body, walls)

    move_ms = MOVE_MS
    dir_buf = snake.dir
    state = RUNNING
    btn_rect = pygame.Rect(WIDTH // 2 - 100, HEIGHT // 2, 200, 50)

    MOVE_EVENT = pygame.USEREVENT + 1
    pygame.time.set_timer(MOVE_EVENT, move_ms)

    while True:
        for e in pygame.event.get():

            if e.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            elif e.type == pygame.KEYDOWN:

                if state == RUNNING:

                    if e.key == pygame.K_p:
                        save_user_state(
                            user_id, level, score,
                            snake.body, food.pos
                        )
                        print("Game saved!")
                        state = PAUSED
                        break

                    dirs = {
                        pygame.K_UP: (0, -1),
                        pygame.K_DOWN: (0, 1),
                        pygame.K_LEFT: (-1, 0),
                        pygame.K_RIGHT: (1, 0)
                    }
                    if e.key in dirs:
                        dir_buf = dirs[e.key]

                elif state == PAUSED:
                    if e.key == pygame.K_r:
                        state = RUNNING

                elif state == GAME_OVER:
                    if e.key == pygame.K_RETURN:
                        return main()

            elif e.type == pygame.MOUSEBUTTONDOWN and state == GAME_OVER:
                if btn_rect.collidepoint(e.pos):
                    return main()

            elif e.type == MOVE_EVENT and state == RUNNING:

                snake.set_dir(dir_buf)
                snake.step()

                food.timer -= 1
                if food.timer <= 0:
                    food.respawn(snake.body, walls)

                hx, hy = snake.head()

                if (hx, hy) in walls or snake.hits_self():
                    state = GAME_OVER

                elif (hx, hy) == food.pos:
                    score += 30 if food.is_gold else 15
                    snake.grow += food.value
                    food.respawn(snake.body, walls)

                    new_level = score // LEVEL_EVERY + 1
                    if new_level > level:
                        level = new_level

                        if level == 2:
                            walls = make_level2_walls()
                        elif level >= 3:
                            walls = make_level3_walls()

                        food.respawn(snake.body, walls)

        draw(screen, walls, food, snake, font, score, level, btn_rect, state == GAME_OVER)
        pygame.display.flip()
        clock.tick(60)


if __name__ == "__main__":
    main()