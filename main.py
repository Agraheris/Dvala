import pygame

pygame.init()
screen = pygame.display.set_mode((800, 600))
running = True
clock = pygame.time.Clock()
while running:
    fps = round(clock.get_fps())
    pygame.display.set_caption(f"POKEMON Dvala, fps : {fps}")

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    screen.fill([70, 50, 26])

    pygame.display.flip()
    clock.tick(60)
pygame.quit()