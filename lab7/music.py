import pygame
import os
import sys

pygame.init()
pygame.mixer.init()

SCREEN_WIDTH = 400
SCREEN_HEIGHT = 200
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Music")

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GRAY = (200, 200, 200)

font = pygame.font.SysFont(None, 24)

music_dir = 'music'
songs = [f for f in os.listdir(music_dir) if f.endswith('.mp3')]
current_song_index = 0

def play_song():
    if songs:
        pygame.mixer.music.load(os.path.join(music_dir, songs[current_song_index]))
        pygame.mixer.music.play(-1)
        print(f"Playing: {songs[current_song_index]}")

def pause_song():
    pygame.mixer.music.pause()
    print("Paused")

def unpause_song():
    pygame.mixer.music.unpause()
    print("Unpaused")

def stop_song():
    pygame.mixer.music.stop()
    print("Stopped")

def next_song():
    global current_song_index
    current_song_index = (current_song_index + 1) % len(songs)
    play_song()

def previous_song():
    global current_song_index
    current_song_index = (current_song_index - 1) % len(songs)
    play_song()

buttons = [
    {"text": "Play/Pause", "rect": pygame.Rect(50, 50, 100, 40), "action": lambda: pause_song() if pygame.mixer.music.get_busy() else unpause_song()},
    {"text": "Stop", "rect": pygame.Rect(160, 50, 60, 40), "action": stop_song},
    {"text": "Prev", "rect": pygame.Rect(230, 50, 60, 40), "action": previous_song},
    {"text": "Next", "rect": pygame.Rect(300, 50, 60, 40), "action": next_song},
]

if songs:
    play_song()

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                if pygame.mixer.music.get_busy():
                    pause_song()
                else:
                    unpause_song()
            elif event.key == pygame.K_s:
                stop_song()
            elif event.key == pygame.K_n:
                next_song()
            elif event.key == pygame.K_p:
                previous_song()
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                for button in buttons:
                    if button["rect"].collidepoint(event.pos):
                        button["action"]()

    screen.fill(WHITE)

    for button in buttons:
        pygame.draw.rect(screen, GRAY, button["rect"])
        text_surf = font.render(button["text"], True, BLACK)
        text_rect = text_surf.get_rect(center=button["rect"].center)
        screen.blit(text_surf, text_rect)

    if songs:
        song_text = font.render(f"Current: {songs[current_song_index]}", True, BLACK)
        screen.blit(song_text, (50, 120))

    pygame.display.flip()

pygame.quit()
sys.exit()

# 