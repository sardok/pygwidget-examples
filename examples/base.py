import logging
import pygame


logger = logging.getLogger()
logging.basicConfig()
pygame.init()
screen = pygame.display.set_mode((800, 600))


def run_sprites(sprites, size=None, title=None):
    global screen
    if size:
        screen = pygame.display.set_mode(size)
    if title is not None:
        pygame.display.set_caption(title)
    clock = pygame.time.Clock()
    group = pygame.sprite.Group()
    for sprite in sprites:
        group.add(sprite)

    inputs = []
    key_buffer = []
    exit = False

    while not exit:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit = True
            if event.type == pygame.locals.KEYUP:
                if event.key == pygame.locals.K_RETURN:
                    key_comb = ''.join(key_buffer)
                    logging.info('Processing input: {}'.format(key_comb))
                    inputs.append(key_comb)
                    key_buffer = []
                elif pygame.locals.K_0 <= event.key <= pygame.locals.K_9:
                    value = str(event.key - ord('0'))
                    key_buffer.append(value)

        try:
            input_ = inputs.pop()
        except IndexError:
            input_ = ''
        group.update(input_)
        group.draw(screen)
        pygame.display.flip()
        clock.tick(60)

    pygame.quit()


def run_sprite(sprite, *a, **kw):
    return run_sprites([sprite], *a, **kw)
