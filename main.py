from loop import *

pygame.init()
res = (200, 400)
screen = pygame.display.set_mode(res)
color = (255, 255, 255)
color_light = (170, 170, 170)
color_dark = (100, 100, 100)
width = screen.get_width()
height = screen.get_height()
font = pygame.font.SysFont('Corbel', 35)
text = font.render('quit', True, color)
text1 = font.render('run', True, color)
pos = width / 2 - width / 3
image = pygame.image.load("img/bg.png")

while True:
    sc.fill("black")
    screen.blit(image, (0, 0))
    for ev in pygame.event.get():
        if ev.type == pygame.QUIT:
            pygame.quit()
        if ev.type == pygame.MOUSEBUTTONDOWN:
            if pos <= mouse[0] <= pos + 140 and height / 2 <= mouse[1] <= height / 2 + 40:
                pygame.quit()
            if pos <= mouse[0] <= pos + 140 and height / 3 <= mouse[1] <= height / 3 + 40:
                main()
                exit()
    mouse = pygame.mouse.get_pos()
    if pos <= mouse[0] <= pos + 140 and height / 2 <= mouse[1] <= height / 2 + 40:
        pygame.draw.rect(screen, color_light, [pos, height / 2, 140, 40])
    else:
        pygame.draw.rect(screen, color_dark, [pos, height / 2, 140, 40])
    if pos <= mouse[0] <= pos + 140 and height / 3 <= mouse[1] <= height / 3 + 40:
        pygame.draw.rect(screen, color_light, [pos, height / 3, 140, 40])
    else:
        pygame.draw.rect(screen, color_dark, [pos, height / 3, 140, 40])

    screen.blit(text, (pos + 50, height / 2))
    screen.blit(text1, (pos + 50, height / 3))
    pygame.display.update()
