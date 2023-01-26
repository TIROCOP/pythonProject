import sys
import sprites
from sprites import *
import pygame


class Board:
    def __init__(self, x, y, cell_size):
        self.sphd = []
        self.spstan = []
        self.x_cart = x
        self.y_cart = y

        self.spv1_xy = (0, 0)
        self.spe2_xy = (0, 0)

        self.bo1_xy = (0, 0)
        self.bo2_xy = (self.x_cart, 0)

        self.sp_vil = []
        k = 0
        for _ in range(2):
            f = []
            for _ in range(4):
                f.append([0, spvil1[k]])
                k += 1
            self.sp_vil.append(f)
        self.sp_vil[self.spv1_xy[0]][self.spv1_xy[1]] = [1, spvil1[0]]

        self.sp_en = []
        k = 0
        for _ in range(2):
            f = []
            for _ in range(4):
                f.append([0, spen2[k]])
                k += 1
            self.sp_en.append(f)
        self.sp_en[self.spe2_xy[0]][self.spe2_xy[1]] = [2, spen2[0]]

        self.board = []
        for _ in range(self.y_cart):
            f = []
            for _ in range(self.x_cart):
                f.append([0, '', ''])
            self.board.append(f)
        self.board[self.bo1_xy[1]][self.bo1_xy[0]] = [1, '', '']
        self.board[self.bo2_xy[1]][self.x_cart - 1] = [2, '', '']

        self.left = cell_size * 2
        self.top = cell_size * 2
        self.cell_size = cell_size

    def set_view(self, left, top, cell_size):
        self.left = left
        self.top = top
        self.cell_size = cell_size

    def render(self, screen):
        for y in range(self.y_cart):
            for x in range(self.x_cart):
                if self.board[y][x][0] == 1:
                    self.bo1_xy = (y, x)
                    pygame.draw.rect(
                        screen,
                        pygame.Color('red'),
                        (x * self.cell_size + self.left,
                         self.cell_size * y + self.top,
                         self.cell_size, self.cell_size),
                        1
                    )

                if self.board[y][x][0] == 2:
                    self.bo2_xy = (y, x)
                    pygame.draw.rect(
                        screen,
                        pygame.Color('red'),
                        (x * self.cell_size + self.left,
                         self.cell_size * y + self.top,
                         self.cell_size, self.cell_size),
                        1
                    )

        # отрисовка выборки персов
        for y in range(len(self.sp_vil)):
            for x in range(len(self.sp_vil[0])):
                if self.sp_vil[y][x][0] == 0:
                    pygame.draw.rect(
                        screen,
                        pygame.Color('white'),
                        (x * self.cell_size + self.cell_size * 0.5,
                         self.cell_size * y + self.cell_size * 7.5,
                         self.cell_size, self.cell_size),
                        1
                    )
                else:
                    self.spv1_xy = (y, x)
                    pygame.draw.rect(
                        screen,
                        pygame.Color('red'),
                        (x * self.cell_size + self.cell_size * 0.5,
                         self.cell_size * y + self.cell_size * 7.5,
                         self.cell_size, self.cell_size),
                        1
                    )
                if self.sp_vil[y][x][1] != '':
                    fil = pygame.image.load(self.sp_vil[y][x][1][0])
                    screen.blit(fil, (
                        x * self.cell_size + self.cell_size * 0.5, self.cell_size * y + self.cell_size * 7.5
                    ))
        # зомби
        for y in range(len(self.sp_en)):
            for x in range(len(self.sp_en[0])):
                if self.sp_en[y][x][0] == 0:
                    pygame.draw.rect(
                        screen,
                        pygame.Color('white'),
                        (x * self.cell_size + self.cell_size * 11.5,
                         self.cell_size * y + self.cell_size * 7.5,
                         self.cell_size, self.cell_size),
                        1
                    )
                else:
                    self.spe2_xy = (y, x)
                    pygame.draw.rect(
                        screen,
                        pygame.Color('red'),
                        (x * self.cell_size + self.cell_size * 11.5,
                         self.cell_size * y + self.cell_size * 7.5,
                         self.cell_size, self.cell_size),
                        1
                    )
                if self.sp_en[y][x][1] != '':
                    fil = pygame.image.load(self.sp_en[y][x][1][0])
                    screen.blit(fil, (x * self.cell_size + self.cell_size * 11.5,
                                      self.cell_size * y + self.cell_size * 7.5))

    def change_pos(self, k, fl):
        if fl == 1:
            y, x = self.bo1_xy
        else:
            y, x = self.bo2_xy
        if self.board[y][x][0] == fl:
            if x == 6 and event.key == pygame.K_LEFT and fl == 2:
                self.board[(y - k[1]) % self.y_cart][x + (x - k[0]) % self.x_cart][0] = fl
                self.board[y][x][0] = 0
                self.board[(y - k[1]) % self.y_cart][x + (x - k[0]) % self.x_cart][2] = self.board[y][x][2]
                self.board[y][x][2] = ''
            elif x == 11 and event.key == pygame.K_RIGHT and fl == 2:
                self.board[(y - k[1]) % self.y_cart][(self.x_cart // 2 + (x - k[0])) % self.x_cart][0] = fl
                self.board[y][x][0] = 0
                self.board[(y - k[1]) % self.y_cart][(self.x_cart // 2 + (x - k[0])) % self.x_cart][2] = \
                    self.board[y][x][2]
                self.board[y][x][2] = ''

            elif x == 0 and event.key == pygame.K_a:
                self.board[(y - k[1]) % self.y_cart][(self.x_cart // 2 + (x - k[0])) % self.x_cart][0] = fl
                self.board[y][x][0] = 0
                self.board[(y - k[1]) % self.y_cart][(self.x_cart // 2 + (x - k[0])) % self.x_cart][1] = \
                    self.board[y][x][2]
                self.board[y][x][2] = ''

            elif x == 5 and event.key == pygame.K_d:
                self.board[(y - k[1]) % self.y_cart][(self.x_cart // 2 + (x - k[0])) % self.x_cart][0] = fl
                self.board[y][x][0] = 0
                self.board[(y - k[1]) % self.y_cart][(self.x_cart // 2 + (x - k[0])) % self.x_cart][2] = \
                    self.board[y][x][2]
                self.board[y][x][2] = ''
            else:
                self.board[(y - k[1]) % self.y_cart][(x - k[0]) % self.x_cart][0] = fl
                self.board[y][x][0] = 0
                self.board[(y - k[1]) % self.y_cart][(x - k[0]) % self.x_cart][2] = self.board[y][x][2]
                self.board[y][x][2] = ''

    def take(self, k, fl):
        for y in range(len(self.sp_vil)):  # 2
            for x in range(len(self.sp_vil[0])):  # 4
                if fl == 2:
                    if self.sp_en[y][x][0] == fl:
                        self.sp_en[(y - k[1]) % len(self.sp_en)][(x - k[0]) % len(self.sp_en[0])][0] = fl
                        self.sp_en[y][x][0] = 0
                        return 0
                if fl == 1:
                    if self.sp_vil[y][x][0] == fl:
                        self.sp_vil[(y - k[1]) % len(self.sp_vil)][(x - k[0]) % len(self.sp_vil[0])][0] = fl
                        self.sp_vil[y][x][0] = 0
                        return 0
        return 1

    def check(self, fl):

        if fl == 1:
            print(self.sp_vil[self.spv1_xy[0]][self.spv1_xy[1]][1])
            self.board[self.bo1_xy[0]][self.bo1_xy[1]][2] = self.sp_vil[self.spv1_xy[0]][self.spv1_xy[1]][1]
        if fl == 2:
            print(self.sp_vil[self.spv1_xy[0]][self.spv1_xy[1]][1])
            self.board[self.bo2_xy[0]][self.bo2_xy[1]][2] = self.sp_en[self.spe2_xy[0]][self.spe2_xy[1]][1]
        print(self.board[0])

    def dieingsprite(self, b_pos):
        print(self.board)
        self.board[b_pos[0]][b_pos[1]][1] = ''
        print(self.board[b_pos[0]][b_pos[1]][1], 11111)

    def prithp(self, fl):
        print(1)
        if fl == 1:
            name1 = self.sp_vil[self.spv1_xy[0]][self.spv1_xy[1]][1][1]
            print(self.board[self.bo1_xy[0]][self.bo1_xy[1]][1])
            print(name1)
            for vil_sprite in vil_sprites_list:
                if vil_sprite.b_pos == self.bo2_xy:
                    return 1
            if name1 == 'tom':
                tom = Toma((self.bo1_xy[1] * self.cell_size + self.left + 50,
                            self.cell_size * self.bo1_xy[0] + self.top + 50), self.bo1_xy)
                vil_sprites_list.add(tom)
                print(self.board[self.bo1_xy[0]][self.bo1_xy[1]])
                self.board[self.bo1_xy[0]][self.bo1_xy[1]][1] = self.board[self.bo1_xy[0]][self.bo1_xy[1]][2]
                self.board[self.bo1_xy[0]][self.bo1_xy[1]][2] = ''
                print(self.board)
                return 0

            if name1 == 'drag':
                dr = DragonFruit((self.bo1_xy[1] * self.cell_size + self.left + 50,
                                  self.cell_size * self.bo1_xy[0] + self.top + 50), self.bo1_xy)
                vil_sprites_list.add(dr)
                print(self.board[self.bo1_xy[0]][self.bo1_xy[1]])
                self.board[self.bo1_xy[0]][self.bo1_xy[1]][1] = self.board[self.bo1_xy[0]][self.bo1_xy[1]][2]
                self.board[self.bo1_xy[0]][self.bo1_xy[1]][2] = ''
                print(self.board[self.bo1_xy[0]][self.bo1_xy[1]])
                return 0

            '''print(self.board[0])
            self.board[self.bo1_xy[0]][self.bo1_xy[1]][1] = self.board[self.bo1_xy[0]][self.bo1_xy[1]][2]
            self.board[self.bo1_xy[0]][self.bo1_xy[1]][2] = ''
            print(self.board[0])'''

        if fl == 2:

            name2 = self.sp_en[self.spe2_xy[0]][self.spe2_xy[1]][1][1]
            for en_sprite in en_sprites_list:
                if en_sprite.b_pos == self.bo2_xy:
                    return 1
            if name2 == 'king':
                king = King((self.bo2_xy[1] * self.cell_size + self.left + 50,
                             self.cell_size * self.bo2_xy[0] + self.top + 50), self.bo2_xy)
                en_sprites_list.add(king)
                self.board[self.bo2_xy[0]][self.bo2_xy[1]][1] = self.board[self.bo2_xy[0]][self.bo2_xy[1]][2]
                self.board[self.bo2_xy[0]][self.bo2_xy[1]][2] = ''
                return 0
            if name2 == 'bm':
                bomb = Bomb((self.bo2_xy[1] * self.cell_size + self.left + 50,
                             self.cell_size * self.bo2_xy[0] + self.top + 50))
                en_shoot_list.add(bomb)

                return 0

        return 1

    def game_checker(self):
        for y in range(self.y_cart):
            for x in range(self.x_cart):
                if self.board[y][x][1] != '':
                    if self.board[y][x][1][1][0] == 1:
                        self.sphd.append(self.board[y][x][1])
                        self.board[y][x][1] = ''
                else:
                    self.spstan.append(self.board[y][x][1])


def chek_win():
    for i in [en_sprites_list,
              vil_sprites_list,
              vil_shoot_list,
              en_shoot_list]:
        for sprite in i:
            if sprite.pos[0] >= 1550:
                paused(1)
                return 'end'
            if sprite.pos[0] <= 60:
                paused(2)
                return 'end'
    return 0


def kiker_chek():
    for en_sprite in en_sprites_list:
        for vil_at in vil_shoot_list:
            if pygame.sprite.collide_mask(vil_at, en_sprite):
                print(en_sprite, 1111, vil_at)
                print(*vil_shoot_list)
                print(*en_sprites_list)
                print(*en_sprites_list)
                en_sprite.damage(vil_at.how_dmg())
                vil_at.impr()
    for vi_sprite in vil_sprites_list:
        for en_at in en_shoot_list:
            if pygame.sprite.collide_mask(vi_sprite, en_at):
                print(vi_sprite, 1111, en_at)
                print(*en_shoot_list)
                print(*vil_sprites_list)
                vi_sprite.damage(en_at.how_dmg())
                en_at.impr()
    for vil_at in vil_shoot_list:
        for en_at in en_shoot_list:
            if pygame.sprite.collide_mask(vil_at, en_at):
                vil_at.damage(en_at.how_dmg())
                en_at.damage(en_at.how_dmg())
                vil_at.drr()
                en_at.drr()


def paused(fl):
    pause = True
    while pause:
        if fl == 1:
            for event in pygame.event.get():
                if event.type == pygame.MOUSEBUTTONDOWN:
                    pause = False

            screen.blit(vil_win, (550, 450))
            pygame.display.flip()
        elif fl == 2:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    pause = False

            screen.blit(en_win, (550, 450))
            pygame.display.flip()
        else:
            for event in pygame.event.get():
                if event.type == pygame.MOUSEBUTTONDOWN:
                    pause = False

                    # board.get_click(event.pos)
                if event.type == pygame.QUIT:
                    pause = False
                    sys.exit()

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_p:
                        pause = False
            screen.blit(paused_image, (550, 450))
            pygame.display.flip()


spvil1 = [['tomatomet_veiv.png', 'tom'], ['dragonfruit/dragonfruit.png', 'drag'],
          ['mario.png', ''], ['mario.png', ''],
          ['mario.png', ''], ['mario.png', ''],
          ['mario.png', ''], ['mario.png', '']]
spen2 = [['king_veiv.png', 'king'], ['bomb/bomber.png', 'bm'],
         ['mario.png', ''], ['mario.png', ''],
         ['mario.png', ''], ['mario.png', ''],
         ['mario.png', ''], ['mario.png', '']]

board_chek = []
board = Board(12, 5, 100)
rstart = 0


if __name__ == '__main__':
    pygame.init()
    bg = pygame.image.load("fon_1.png")
    screen = pygame.display.set_mode(size)

    pygame.display.set_caption("PVZ")

    running = True
    clock = pygame.time.Clock()
    target_vil = False
    target_enem = False
    for i in range(len(board.board)):
        kos = kossa((120, i * 100 + 250), kossa1, 15)
        vil_shoot_list.add(kos)

    for i in range(len(board.board)):
        kos = kossa((1500, i * 100 + 250), kossa2, -15)
        en_shoot_list.add(kos)

    while running:
        for event in pygame.event.get():

            if event.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()
                if pos[0] > 760 and pos[0] < 840 and pos[1] < 30:
                    paused()

            if event.type == pygame.QUIT:
                running = False
                sys.exit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_p:
                    paused()
                    print('pausa')

            # main
            if event.type == pygame.KEYDOWN:
                # управление зомби
                if event.key == pygame.K_DOWN and target_enem == False:
                    board.take((0, -1), 2)
                if event.key == pygame.K_UP and target_enem == False:
                    board.take((0, 1), 2)
                if event.key == pygame.K_LEFT and target_enem == False:
                    board.take((1, 0), 2)
                if event.key == pygame.K_RIGHT and target_enem == False:
                    board.take((-1, 0), 2)
                if event.key == pygame.K_KP_0 and target_enem == False:
                    board.check(2)
                    target_enem = True
                elif target_enem == True:
                    if event.key == pygame.K_DOWN:
                        board.change_pos((0, -1), 2)
                    if event.key == pygame.K_UP:
                        board.change_pos((0, 1), 2)
                    if event.key == pygame.K_LEFT:
                        board.change_pos((1, 0), 2)
                    if event.key == pygame.K_RIGHT:
                        board.change_pos((-1, 0), 2)
                    if event.key == pygame.K_p:
                        target_enem = False
                    if event.key == pygame.K_KP_0:
                        re = board.prithp(2)
                        if re == 0:
                            target_enem = False

            if event.type == pygame.KEYDOWN:
                # управление растениями
                if event.key == pygame.K_s and target_vil == False:
                    board.take((0, -1), 1)
                if event.key == pygame.K_w and target_vil == False:
                    board.take((0, 1), 1)
                if event.key == pygame.K_a and target_vil == False:
                    board.take((1, 0), 1)
                if event.key == pygame.K_d and target_vil == False:
                    board.take((-1, 0), 1)
                if event.key == pygame.K_SPACE and target_vil == False:

                    board.check(1)
                    target_vil = True
                elif target_vil == True:
                    if event.key == pygame.K_s:
                        board.change_pos((0, -1), 1)
                    if event.key == pygame.K_w:
                        board.change_pos((0, 1), 1)
                    if event.key == pygame.K_a:
                        board.change_pos((1, 0), 1)
                    if event.key == pygame.K_d:
                        board.change_pos((-1, 0), 1)
                    if event.key == pygame.K_SPACE:
                        ed = board.prithp(1)
                        if ed == 0:
                            target_vil = False
                    if event.key == pygame.K_f:
                        target_vil = False

        screen.fill(pygame.Color('black'))
        if chek_win() == 'end':
            sys.exit()
        screen.blit(bg, (0, 0))

        board.render(screen)
        en_sprites_list.update()
        vil_sprites_list.update()
        vil_shoot_list.update()
        en_shoot_list.update()
        kiker_chek()
        vil_sprites_list.draw(screen)
        en_sprites_list.draw(screen)
        vil_shoot_list.draw(screen)
        en_shoot_list.draw(screen)
        screen.blit(pause_button, (763, 10))
        pygame.display.flip()
        clock.tick(12)

    pygame.quit()


