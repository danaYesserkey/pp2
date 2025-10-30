import pygame
import datetime
import math

pygame.init()

WIDTH, HEIGHT = 700, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Mickey")

base_image = pygame.image.load('base_micky.jpg')
minute_hand = pygame.image.load('minute.png')
second_hand = pygame.image.load('second.png')

base_image = pygame.transform.scale(base_image, (WIDTH, HEIGHT))

minute_hand = pygame.transform.scale(minute_hand, (minute_hand.get_width() // 2, minute_hand.get_height() // 2))
second_hand = pygame.transform.scale(second_hand, (second_hand.get_width() // 2, second_hand.get_height() // 2))

minute_pivot = (minute_hand.get_width() // 2, minute_hand.get_height() // 2)
second_pivot = (second_hand.get_width() // 2, second_hand.get_height() // 2)

hand_pos = (WIDTH // 2, HEIGHT // 2)

base_rect = base_image.get_rect(center=hand_pos)

running = True
clock = pygame.time.Clock()

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    now = datetime.datetime.now()
    minutes = now.minute
    seconds = now.second
    minute_angle = (minutes % 60) * 6 - 90
    second_angle = seconds * 6 - 90

    rotated_minute = pygame.transform.rotate(minute_hand, -minute_angle)
    rotated_second = pygame.transform.rotate(second_hand, -second_angle)

    minute_rect = rotated_minute.get_rect(center=hand_pos)
    second_rect = rotated_second.get_rect(center=hand_pos)

    screen.blit(base_image, base_rect)
    screen.blit(rotated_minute, minute_rect)
    screen.blit(rotated_second, second_rect)

    pygame.display.flip()
    clock.tick(1)

pygame.quit()