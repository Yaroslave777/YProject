import pygame as pg


# from random import randint
class MainCharacter(pg.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pg.image.load('Character.png')
        self.rect = self.image.get_rect()
        colorkey = self.image.get_at((0, 0))
        self.image.set_colorkey(colorkey)


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

    move_up, move_down, move_left, move_right = False, False, False, False
    tp_l, tp_r, tp_u, tp_d = False, False, False, False
    speed = 15

    main_char = MainCharacter()
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
            field.rect.x = 1000 * i - 1000
            field.rect.y = 1000 * j - 1000
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
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_w:
                    move_up = True
                if event.key == pg.K_a:
                    move_left = True
                if event.key == pg.K_s:
                    move_down = True
                if event.key == pg.K_d:
                    move_right = True
            if event.type == pg.KEYUP:
                if event.key == pg.K_w:
                    move_up = False
                if event.key == pg.K_a:
                    move_left = False
                if event.key == pg.K_s:
                    move_down = False
                if event.key == pg.K_d:
                    move_right = False

        for i in land:
            for j in i:
                j.rect.x -= speed * int(move_right) - speed * int(move_left)
                j.rect.y -= speed * int(move_down) - speed * int(move_up)

        screen.fill('black')
        if land[1][1].rect.x >= 1000:
            tp_l = True
        elif land[1][1].rect.x <= -1000:
            tp_r = True
        if land[1][1].rect.y >= 1000:
            tp_u = True
        elif land[1][1].rect.y <= -1000:
            tp_d = True
        for i in range(3):
            for j in range(3):
                land[i][j].rect.x += int(tp_r) * 1000 - int(tp_l) * 1000
                land[i][j].rect.y += int(tp_d) * 1000 - int(tp_u) * 1000
        tp_l, tp_r, tp_u, tp_d = False, False, False, False
        for i in land:
            for j in i:
                screen.blit(j.image, (j.rect.x, j.rect.y))
        screen.blit(main_char.image, (width // 2 - main_char.rect.width // 2, height // 2 - main_char.rect.height // 2))

        pg.display.flip()
        clock.tick(fps)
    pg.quit()
