from sprites import *
sprite = Sprites()


def main():
    while sprite.running:
        sprite.draw()
        pygame.display.flip()
        clock.tick(fps)
