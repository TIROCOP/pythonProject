import pygame
import pygame as pygame

COLOR = (255, 100, 98)
SURFACE_COLOR = (167, 255, 100)
width, height = 1600, 1000
pygame.init()

paused_image = pygame.image.load('paused.jpg')
pause_button = pygame.image.load('pausa_batton.png')
vil_win = pygame.image.load('vil_win.jpg')
en_win = pygame.image.load('en_win.jpg')
screen = pygame.display.set_mode((640, 480))
IMAGE_wait = pygame.image.load('tomatomet_wait/tomatomet_wait.png').convert_alpha()
IMAGE_wait1 = pygame.image.load('tomatomet_wait/tomatomet_wait1.png').convert_alpha()
IMAGE1 = pygame.image.load('tomatomet_wait/tomatomet.png').convert_alpha()
IMAGE2 = pygame.image.load('tomatomet_fier/tomatomet1.png').convert_alpha()
IMAGE3 = pygame.image.load('tomatomet_fier/tomatomet3.png').convert_alpha()
IMAGE4 = pygame.image.load('tomatomet_fier/tomatomet4.png').convert_alpha()
IMAGE5 = pygame.image.load('tomatomet_fier/tomatomet5.png').convert_alpha()
sp_of_sp = [IMAGE1, IMAGE2, IMAGE3, IMAGE4, IMAGE5]
sp_of_sp_wait = [IMAGE1, IMAGE_wait, IMAGE_wait1]
k = 0
Fie_boll = pygame.image.load('tomat/tomat1.png').convert_alpha()
Fie_boll1 = pygame.image.load('tomat/tomat2.png').convert_alpha()
Fie_boll2 = pygame.image.load('tomat/tomat3.png').convert_alpha()
Fie_boll3 = pygame.image.load('tomat/tomat4.png').convert_alpha()
Fie_boll4 = pygame.image.load('tomat/tomat5.png').convert_alpha()
Fie_boll5 = pygame.image.load('tomat/tomat6.png').convert_alpha()
Fie_boll6 = pygame.image.load('tomat/tomat7.png').convert_alpha()
Fie_boll7 = pygame.image.load('tomat/tomat.png').convert_alpha()

sp_of_fi = [Fie_boll, Fie_boll1, Fie_boll2, Fie_boll3, Fie_boll4, Fie_boll5, Fie_boll6, Fie_boll7]

size = (width, height)

Image_king = pygame.image.load('king_wait/king1.png').convert_alpha()
Image_king_wait = pygame.image.load('king_wait/king2.png').convert_alpha()
Image_king_wait1 = pygame.image.load('king_wait/king3.png').convert_alpha()

Image_king1 = pygame.image.load('king_fie/king1.png').convert_alpha()
Image_king2 = pygame.image.load('king_fie/king2.png').convert_alpha()
Image_king3 = pygame.image.load('king_fie/king3.png').convert_alpha()
Image_king4 = pygame.image.load('king_fie/king4.png').convert_alpha()

shot_king = pygame.image.load('death_king/death.png').convert_alpha()

shoots_king = [shot_king]
sp_king_wait = [Image_king, Image_king_wait, Image_king_wait1]
sp_king = [Image_king, Image_king1, Image_king2, Image_king3, Image_king4]

dr_fruit = pygame.image.load('dragonfruit/dragonfruit.png').convert_alpha()
dr_fruit1 = pygame.image.load('dragonfruit/dragonfruit1.png').convert_alpha()
dr_fruit2 = pygame.image.load('dragonfruit/dragonfruit2.png').convert_alpha()
dr_fruit3 = pygame.image.load('dragonfruit/dragonfruit3.png').convert_alpha()

sp_dragon_fr = [dr_fruit, dr_fruit1, dr_fruit2, dr_fruit3]


sp_bomb_wait = []
sp_bomb_att = []
en_bomb = ['bomberman', 'bomberman1', 'bomberman2', 'bomberman3']
nom = ['bomber', 'bomber1', 'bomber2', 'bomber3', 'bomber4', 'bomber5']
final_attak = pygame.image.load('bomb/final_attak.png').convert_alpha()

for i in en_bomb:
    sp_bomb_wait.append(pygame.image.load('bomb_wait/' + i +'.png').convert_alpha())
for i in nom:
    sp_bomb_att.append(pygame.image.load('bomb/' + i +'.png').convert_alpha())


corn_boy = pygame.image.load('corn_boy.png').convert_alpha()
corn = pygame.image.load('corn.png')
sp_peas = []
sp_peas_att = []
vil_peas = ['peas']
vil_peas1 = ['peas', 'peas1', 'peas2', 'peas3', 'peas4', 'peas5']

for i in vil_peas:
    sp_peas.append(pygame.image.load('aggressivepeas/' + i +'.png').convert_alpha())
for i in vil_peas1:
    sp_peas_att.append(pygame.image.load('aggressivepeas/' + i +'.png').convert_alpha())

kossa1 = pygame.image.load('kossa.png').convert_alpha()
kossa2 = pygame.image.load('kossa_rev.png').convert_alpha()
