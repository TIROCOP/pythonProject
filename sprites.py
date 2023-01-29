import sys

import pygame

import pygame
import random
from constant import *

en_sprites_list = pygame.sprite.Group()
vil_sprites_list = pygame.sprite.Group()
vil_shoot_list = pygame.sprite.Group()
en_shoot_list = pygame.sprite.Group()


def set_up():
    global en_sprites_list, vil_sprites_list, vil_shoot_list, en_shoot_list
    en_sprites_list = pygame.sprite.Group()
    vil_sprites_list = pygame.sprite.Group()
    vil_shoot_list = pygame.sprite.Group()
    en_shoot_list = pygame.sprite.Group()


class kossa(pygame.sprite.Sprite):
    def __init__(self, pos, image, go):
        super().__init__()
        self.image = image
        self.rect = self.image.get_rect(center=pos)
        self.images = [image, image]
        self.hp = 10000000000
        self.dmg = 100000
        self.b_pos = (-50, -50)
        self.pos = pos
        self.game_wait = 0
        self.go = 0
        self.g = go
        self.ifa = 0
        self.k = 0

        self.index = 0

        self.image = self.images[self.index]

    def damage(self, dmg):
        self.hp -= dmg

    def how_dmg(self):
        return self.dmg

    def impr(self):
        pass

    def drr(self):
        self.go = self.g

    def update(self):
        if self.pos[0] > 1400 and self.image == kossa1:
            self.kill()
        if self.pos[0] < 250 and self.image == kossa2:
            self.kill()

        self.image = self.images[self.index]
        self.pos = self.pos[0] + self.go, self.pos[1]
        self.rect = self.image.get_rect(center=(self.pos[0] + self.go, self.pos[1]))


class DragonFruit(pygame.sprite.Sprite):
    def __init__(self, pos, b_pos):
        super().__init__()
        self.image = sp_dragon_fr[k]
        self.rect = self.image.get_rect(center=pos)
        self.images = sp_dragon_fr
        self.b_pos = b_pos
        self.hp = 1000
        self.pos = pos
        self.k = 0

        self.index = 0

        # self.image = self.images[self.index]

    def damage(self, dmg):
        self.hp -= dmg

    def update(self):
        self.index += 1

        if self.index >= len(self.images):
            self.index = 0
        # self.k += 1
        if self.hp <= 0:
            self.kill()

        self.image = self.images[self.index]


class Bomb(pygame.sprite.Sprite):
    def __init__(self, pos):
        super().__init__()
        self.image = sp_bomb_wait[k]
        self.rect = self.image.get_rect(center=pos)
        self.images = sp_bomb_wait
        self.hp = 100
        self.dmg = 10000
        self.b_pos = (-50, -50)
        self.pos = pos
        self.game_wait = 0
        self.ifa = 0
        self.k = 0

        self.index = 0

        self.image = self.images[self.index]

    def damage(self, dmg):
        self.hp -= dmg

    def how_dmg(self):
        return self.dmg

    def drr(self):
        pass

    def impr(self):
        self.kill()

    def update(self):
        if self.game_wait == 0:
            self.k += 1
        self.index += 1

        if self.index >= len(self.images):
            self.index = 0

        if self.k == 40:  # как долго ждёт
            self.k = 0
            self.game_wait = 1
            self.index = 0
            self.images = sp_bomb_att
            self.image = self.images[0]

        if self.pos[0] < 50 or self.hp <= 0:
            self.kill()

        if sp_bomb_att == self.images:
            self.pos = self.pos[0] - 5, self.pos[1]
            self.rect = self.image.get_rect(center=(self.pos[0] - 5, self.pos[1]))

        self.image = self.images[self.index]


class Peas(pygame.sprite.Sprite):
    def __init__(self, pos):
        super().__init__()
        self.image = sp_peas[0]
        self.rect = self.image.get_rect(center=pos)
        self.images = sp_peas
        self.hp = 100
        self.dmg = 10000
        self.b_pos = (-50, -50)
        self.pos = pos
        self.game_wait = 0
        self.ifa = 0
        self.k = 0

        self.index = 0

        self.image = self.images[self.index]

    def damage(self, dmg):
        self.hp -= dmg

    def how_dmg(self):
        return self.dmg

    def drr(self):
        pass

    def impr(self):
        self.kill()

    def update(self):
        if self.game_wait == 0:
            self.k += 1
        self.index += 1

        if self.index >= len(self.images):
            self.index = 0

        if self.k == 40:  # как долго ждёт
            self.k = 0
            self.game_wait = 1
            self.index = 0
            self.images = sp_peas_att
            self.image = self.images[0]

        if self.pos[0] < 50 or self.hp <= 0:
            self.kill()

        if sp_peas_att == self.images:
            self.pos = self.pos[0] + 5, self.pos[1]
            self.rect = self.image.get_rect(center=(self.pos[0] + 5, self.pos[1]))

        self.image = self.images[self.index]

class King(pygame.sprite.Sprite):
    def __init__(self, pos, b_pos):
        super().__init__()
        self.image = sp_king_wait[k]
        self.rect = self.image.get_rect(center=pos)
        self.images = sp_king_wait
        self.b_pos = b_pos
        self.hp = 100
        self.pos = pos
        self.k = 0

        self.index = 0

        self.image = self.images[self.index]

    def damage(self, dmg):
        self.hp -= dmg

    def update(self):
        self.index += 1

        if self.index == len(self.images) and self.images != sp_king_wait:
            en_shot = EnemyShoot(self.pos, shoots_king, 50, 50)
            en_shoot_list.add(en_shot)
            self.images = sp_king_wait

        if self.index >= len(self.images):
            self.index = 0
        self.k += 1
        if self.k == 40:  # как часто вылетает
            self.k = 0
            self.index = 0
            self.images = sp_king
            self.image = self.images[0]
            return
        if self.hp <= 0:
            self.kill()

        self.image = self.images[self.index]


class Toma(pygame.sprite.Sprite):
    def __init__(self, pos, b_pos):
        super().__init__()
        self.image = sp_of_sp[k]
        self.rect = self.image.get_rect(center=pos)
        self.images = sp_of_sp_wait
        self.pos = pos
        self.b_pos = b_pos
        self.hp = 100
        self.k = 0

        self.index = 0

        self.image = self.images[self.index]

    def damage(self, dmg):
        self.hp -= dmg

    def update(self):
        self.index += 1

        if self.index == len(self.images) and self.images != sp_of_sp_wait:
            shot = Shoot(self.pos, sp_of_fi, 50, 50)
            vil_shoot_list.add(shot)
            self.images = sp_of_sp_wait

        if self.index >= len(self.images):
            self.index = 0
        self.k += 1
        if self.k == 40:  # как часто вылетает
            self.k = 0
            self.index = 0
            self.images = sp_of_sp
            self.image = self.images[0]
            return

        if self.hp <= 0:
            self.kill()

        self.image = self.images[self.index]



class Corn_boy(pygame.sprite.Sprite):
    def __init__(self, pos, b_pos):
        super().__init__()
        self.image = corn_boy
        self.rect = self.image.get_rect(center=pos)
        self.images = [corn_boy]
        self.check = 0
        self.kk = 0
        self.pos = pos
        self.b_pos = b_pos
        self.hp = 100
        self.k = 0

        self.index = 0

        self.image = self.images[self.index]

    def damage(self, dmg):
        self.hp -= dmg

    def update(self):
        self.index += 1

        if self.index == len(self.images) and self.check != 4 and self.check % 2 == 0:
            self.check += 1
            shot = Shoot(self.pos, [corn], 5, 5)
            vil_shoot_list.add(shot)

        elif self.check != 4 and self.check % 2 != 0:
            self.check += 1

        elif self.check == 4 and self.kk != 1:
            self.k = 0
            self.kk = 1


        if self.index >= len(self.images):
            self.index = 0

        self.k += 1

        if self.k > 20 and self.kk == 1:
            self.kk = 0
            self.check = 0


        if self.hp <= 0:
            self.kill()

        self.image = self.images[self.index]


class EnemyShoot(pygame.sprite.Sprite):  # томат
    def __init__(self, pos, sp, dmg,hp):
        super().__init__()
        self.image = sp[k]
        self.rect = self.image.get_rect(center=(pos[0] - 10, pos[1]))
        self.images = sp
        self.hp = hp
        self.dmg = dmg
        self.pos = pos

        self.index = 0

        self.image = self.images[self.index]

    def drr(self):
        pass

    def how_dmg(self):
        return self.dmg

    def damage(self, dmg):
        self.hp -= dmg

    def update(self):
        self.index += 1

        if self.index >= len(self.images):
            self.index = 0

        if self.pos[0] < 50:
            self.impr()
        if self.hp <= 0:
            self.kill()
        self.image = self.images[self.index]
        self.pos = self.pos[0] - 10, self.pos[1]
        self.rect = self.image.get_rect(center=(self.pos[0] - 10, self.pos[1]))

    def impr(self):
        self.kill()


class Shoot(pygame.sprite.Sprite):  # томат
    def __init__(self, pos, sp, dmg, hp):
        super().__init__()
        self.image = sp[k]
        self.rect = self.image.get_rect(center=(pos[0] + 10, pos[1]))
        self.images = sp
        self.dmg = dmg
        self.hp = hp
        self.pos = pos

        self.index = 0

        self.image = self.images[self.index]

    def how_dmg(self):
        return self.dmg

    def damage(self, dmg):
        self.hp -= dmg

    def drr(self):
        pass

    def update(self):
        self.index += 1

        if self.index >= len(self.images):
            self.index = 0

        if self.pos[0] > size[0]:
            self.impr()

        if self.hp <= 0:
            self.kill()

        self.image = self.images[self.index]
        self.pos = self.pos[0] + 10, self.pos[1]
        self.rect = self.image.get_rect(center=(self.pos[0] + 10, self.pos[1]))

    def impr(self):
        self.kill()
