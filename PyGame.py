import pygame as pg


# from random import randint

def movement(key):
    if chr(key) in move_letters.keys():
        return move_letters[chr(key)]
    else:
        return [0, 0]


if __name__ == '__main__':
    pg.init()

    width = 1000
    height = 1000
    screen = pg.display.set_mode((width, height))

    char_image = pg.image.load('Character.png')
    character = pg.sprite.Sprite()
    character.image = char_image
    character.rect = character.image.get_rect()

    move_letters = {'w': [0, -5], 'a': [-5, 0], 's': [0, 5], 'd': [5, 0]}

    land = [[], [], []]
    la_x = 0
    la_y = 0
    for i in range(3):
        a = []
        for j in range(3):
            field = pg.sprite.Sprite()
            field_image = pg.image.load('check_field.png')
            field.image = field_image
            field.rect = field.image.get_rect()
            a.append(field)
        land[i] = a

    fps = 50
    count = 1
    clock = pg.time.Clock()
    running = True
    while running:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                running = False
            klav = pg.key.get_pressed()
            x, y = movement(pg.K_w)
            la_x -= x * klav[pg.K_w]
            la_y -= y * klav[pg.K_w]

            x, y = movement(pg.K_a)
            la_x -= x * klav[pg.K_a]
            la_y -= y * klav[pg.K_a]

            x, y = movement(pg.K_s)
            la_x -= x * klav[pg.K_s]
            la_y -= y * klav[pg.K_s]

            x, y = movement(pg.K_d)
            la_x -= x * klav[pg.K_d]
            la_y -= y * klav[pg.K_d]
        screen.fill('black')
        screen.blit(land[1][1].image, (la_x, la_y))
        screen.blit(character.image, (width // 2 - character.rect.width // 2, height // 2 - character.rect.height // 2))

        pg.display.flip()
        clock.tick(fps)
    pg.quit()
