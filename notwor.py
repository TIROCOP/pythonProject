import pygame

class Board:
    def __init__(self, x, y, cell_size):
        self.sphd = []
        self.spstan = []
        self.x_cart = x
        self.y_cart = y

        self.spv1_xy = (0, 0)
        self.spe2_xy = (0, 3)

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
        print(self.sp_vil)

        self.sp_en = []
        k = 0
        for _ in range(2):
            f = []
            for _ in range(4):
                f.append([0, spen2[k]])
                k += 1
            self.sp_en.append(f)
        self.sp_en[self.spe2_xy[0]][self.spe2_xy[1]] = [2, spen2[0]]
        print(self.sp_en)

        self.board = []
        for _ in range(self.y_cart):
            f = []
            for _ in range(self.x_cart):
                f.append([0, '', ''])
            self.board.append(f)
        self.board[self.bo1_xy[1]][self.bo1_xy[0]] = [1, '', '']
        self.board[self.bo2_xy[1]][self.x_cart - 1] = [2, '', '']
        for i in self.board:
            print(i)

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
                if self.board[y][x][0] == 0:
                    pygame.draw.rect(
                        screen,
                        pygame.Color('white'),
                        (x * self.cell_size + self.left,
                         self.cell_size * y + self.top,
                         self.cell_size, self.cell_size),
                        1
                    )
                else:
                    if self.board[y][x][0] == 1:
                        self.bo1_xy = (y, x)
                    else:
                        self.bo2_xy = (y, x)
                    pygame.draw.rect(
                        screen,
                        pygame.Color('red'),
                        (x * self.cell_size + self.left,
                         self.cell_size * y + self.top,
                         self.cell_size, self.cell_size),
                        1
                    )
                if self.board[y][x][1] != '':
                    fil = pygame.image.load(self.board[y][x][1][0])
                    screen.blit(fil, (x * self.cell_size + self.left,
                                      self.cell_size * y + self.top))

                if self.board[y][x][2] != '':
                    fil = pygame.image.load(self.board[y][x][2][0])
                    screen.blit(fil, (x * self.cell_size + self.left,
                                      self.cell_size * y + self.top))
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
                    screen.blit(fil, (x * self.cell_size + self.cell_size * 0.5,
                                      self.cell_size * y + self.cell_size * 7.5))
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

    '''    def get_click(self, mouse_pos):
        cell = self.get_cell(mouse_pos)
        self.on_click(cell)

    def get_cell(self, mouse_pos):
        for y in range(self.y_cart):
            for x in range(self.x_cart):
                if x * self.cell_size + self.left <= mouse_pos[0] <= x * self.cell_size + self.left + self.cell_size \
                        and self.cell_size * y + self.top <= mouse_pos[1] <= self.cell_size * y \
                        + self.top + self.cell_size:
                    print((x, y))
                    return (x, y)

        print(None)
        return None

    def on_click(self, cell):
        if type(cell) is tuple:
            if self.board[cell[0]][cell[1]][0] == 0:
                self.board[cell[0]][cell[1]][0] = 1
            else:
                self.board[cell[0]][cell[1]][0] = 0
    '''

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
                self.board[(y - k[1]) % self.y_cart][(self.x_cart // 2 + (x - k[0])) % self.x_cart][0] = \
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

    def prithp(self, fl):
        if fl == 1:
            print(self.board[0])
            self.board[self.bo1_xy[0]][self.bo1_xy[1]][1] = self.board[self.bo1_xy[0]][self.bo1_xy[1]][2]
            self.board[self.bo1_xy[0]][self.bo1_xy[1]][2] = ''
            print(self.board[0])

        if fl == 2:
            print(self.sp_vil[self.spv1_xy[0]][self.spv1_xy[1]][1])
            self.board[self.bo2_xy[0]][self.bo2_xy[1]][1] = self.board[self.bo2_xy[0]][self.bo2_xy[1]][2]
            self.board[self.bo2_xy[0]][self.bo2_xy[1]][2] = ''
        print(self.board[0])

    def game_checker(self):
        for y in range(self.y_cart):
            for x in range(self.x_cart):
                if self.board[y][x][1] != '':
                    if self.board[y][x][1][1][0] == 1:
                        self.sphd.append(self.board[y][x][1])
                        self.board[y][x][1] = ''
                else:
                    self.spstan.append(self.board[y][x][1])

    def gameprocess(self):
        pass


if __name__ == '__main__':
    spvil1 = [['mario.png', (0, 50, 25, ())], ['mario.png', (1, 50, 25, ())],
              ['mario.png', (0, 50, 25, ())], ['mario.png', (1, 50, 25, ())],
              ['mario.png', (0, 50, 25, ())], ['mario.png', (1, 50, 25, ())],
              ['mario.png', (0, 50, 25, ())], ['mario.png', (1, 50, 25, ())]]
#(walk 1\ 0 no, hp, dmg, (x, y))
    spen2 = [['king_wait/king1.png', (0, 50, 25, ())], ['mario.png', (0, 50, 25, ())],
             ['mario.png', (0, 50, 25, ())], ['mario.png', (0, 50, 25, ())],
             ['mario.png', (0, 50, 25, ())], ['mario.png', (0, 50, 25, ())],
             ['mario.png', (0, 50, 25, ())], ['mario.png', (0, 50, 25, ())]]
    pygame.init()
    width, height = 1600, 1000
    bg = pygame.image.load("fon_1.png")

    size = width, height
    screen = pygame.display.set_mode(size)
    board = Board(12, 5, 100)
    running = True
    target_vil = False
    target_enem = False
    while running:
        for event in pygame.event.get():

            if event.type == pygame.MOUSEBUTTONDOWN:
                pass
                # board.get_click(event.pos)

            if event.type == pygame.QUIT:
                running = False

            if event.type == pygame.KEYDOWN:
                if event.type == pygame.QUIT:
                    running = False
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
                        board.prithp(2)
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
                        board.prithp(1)
                        target_vil = False
                    if event.key == pygame.K_f:
                        target_vil = False

        screen.fill(pygame.Color('black'))
        screen.blit(bg, (0, 0))
        board.render(screen)
        pygame.display.flip()
