#создай игру "Лабиринт"!
from pygame import *
mixer.init()
mixer.music.load('jungles.ogg')
mixer.music.play(-1)
kick = mixer.Sound('kick.ogg')
kick.play()
money = mixer.Sound('money.ogg')
money.play()
font.init()
font1 = font.Font(None, 70)
win = font1.render('ТЫ ПОБЕДИЛ', True, (0, 191, 255))
gameover = font1.render('ТЫ ПРОИГРАЛ', True, (148, 0, 211))




window = display.set_mode((700, 500))
display.set_caption('инцидент в сибуя')
bg = transform.scale(image.load('shibuya.jpg'), (700, 500))
class GameSprite(sprite.Sprite):
    def __init__(self, filename, w, h, speed, x, y):
        super().__init__()
        self.image = transform.scale(image.load(filename), (w, h))
        self.speed = speed
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

class Player(GameSprite):
    def update(self):
        keys_pressed = key.get_pressed()
        if keys_pressed[K_LEFT] and self.rect.x > 0:
            self.rect.x -= 10
        if keys_pressed[K_RIGHT] and self.rect.x < 700 - 65:
            self.rect.x += 10
        if keys_pressed[K_UP] and self.rect.y > 0:
            self.rect.y -= 10
        if keys_pressed[K_DOWN] and self.rect.y < 500 - 65:
            self.rect.y += 10
class Enemy(GameSprite):
    direction = "right"
    def update(self):
        if self.rect.x <= 470:
            self.direction = 'right'
        if self.rect.x >= 645:
            self.direction = 'left'
        if self.direction == 'left':
            self.rect.x -= 9
        else:
            self.rect.x += 9

  
class Wall(sprite.Sprite):
    def __init__(self, width, height, x, y):
        super().__init__()
        self.image = Surface((width, height))
        self.image.fill((210, 105, 30))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

    def draw_wall(self):
        window.blit(self.image, (self.rect.x, self.rect.y))



wall = Wall(220, 25, 100, 30)
wall1 = Wall(130, 25, 100, 150)
wall2 = Wall(20, 355, 215, 160)
wall3 = Wall(20, 355, 310, 50)
wall4 = Wall(20, 500, 430, 110)
walls = sprite.Group()
walls.add(wall, wall1, wall2, wall3, wall4)
player = Player('png-klev-club-92y7-p-itadori-png-2.png', 65, 65, 10, 20, 20)
ciborg = Enemy('dibgmve-aac611c1-5dfc-444b-b734-2af67a56a66b.png', 65, 65, 15, 455, 250)
treasure = GameSprite('images-Photoroom.png', 65, 65, 15, 455, 350)
finish = False
clock = time.Clock()
game = True
while game:
    if finish != True:
        window.blit(bg, (0, 0)) 
        player.update()
        player.reset()
        ciborg.update()
        ciborg.reset()
        treasure.reset()
        wall.draw_wall()
        wall1.draw_wall()
        wall2.draw_wall()
        wall3.draw_wall()
        wall4.draw_wall()
        if sprite.collide_rect(player ,treasure):
            window.blit(win, (200, 200))
            finish = True
            money.play()
        if sprite.collide_rect(player ,ciborg):
            window.blit(gameover, (200, 200))
            finish = True
            kick.play()
        if len(sprite.spritecollide(player, walls, False)) > 0:
            player.rect.x = 20
            player.rect.y = 20


    for e in event.get():
        if e.type == QUIT:
            game = False
    clock.tick(60)
    display.update()
#буду рад вам помочь этим кодом



 

