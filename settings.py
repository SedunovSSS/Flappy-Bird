import pygame
from random import randrange
import json
pygame.init()
width = 200
height = 400
score = 0
fps = 40
x, y = 80, 310
n = randrange(-40, 140, 10)
cx, cy = 400, 0
game_over = False
running = True
clock = pygame.time.Clock()
sc = pygame.display.set_mode([width, height])
font_score = pygame.font.SysFont('Arial', 15, bold=True)
font_best = pygame.font.SysFont('Arial', 15, bold=True)
font_game_over = pygame.font.SysFont('Arial', 35, bold=True)
pygame.display.set_caption("FlappyBird")

with open("bests.json", "r", encoding='utf-8') as content:
    data = json.load(content)
