import pygame, classGame, classBaloon


game = classGame.Game()

pygame.time.set_timer(pygame.USEREVENT, 400)
TIMESPEED = pygame.USEREVENT + 1
pygame.time.set_timer(TIMESPEED, 7000)





while not game.over:
    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            game.over = True
        if e.type == pygame.USEREVENT:
            game.spawnbaloon()
        if e.type == pygame.MOUSEBUTTONDOWN:
            game.checkclick(e.pos)
        if e.type == TIMESPEED:
            game.speedup()
    game.update()
