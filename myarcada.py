from pygame import*
#akdjerngaeszrklhgofeaklugrlSA
class Game_sprite(sprite.Sprite):
    def __init__(self, imgname, x,y, w,h):
        super().__init__()
        self.image = transform.scale(image.load(imgname), (w,h))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y


class Platform(Game_sprite):
    def __init__(self, x, y):
        super().__init__('cave.png', x, y, 200, 40)
    def is_collide(self):
        if self.rect.colliderect(player.rect) and self.rect.y >= player.rect.y +90:
            return True
        return False
class Enemy(Game_sprite):
    def __init__(self, x,y):
        super().__init__('enemy.png', x,y,80,80)
    def is_collide(self): 
        global y_speed
        if self.rect.colliderect(player.rect) and y_speed > 0:
            y_speed = -14
            self.kill()
        elif self.rect.colliderect(player.rect) and y_speed <= 0:
            pass
        #тут будет проигрыш
screen = display.set_mode((700,500))
screen.fill((255,255,220))
background = transform.scale(image.load('cave.png'), (700,500))
background2 = transform.scale(image.load('cave.png'), (700,500))
player = Game_sprite('player.png', 100,100,70,100)

p1 = Platform(50, 400)
p2 = Platform(250, 250)
platforms = sprite.Group()
platforms.add(p1)
platforms.add(p2)

enemy = Enemy(300, 170)
enemy_group = sprite.Group()
enemy_group.add(enemy)

princess = Game_sprite('princess.png', 700,300,80,100)
shift_x = 0

y_speed = 0
isJump = True
clock = time.Clock()
game = True
while game:
    clock.tick(60)
    keypressed = key.get_pressed()
    for e in event.get():
        if e.type == QUIT:
            game = False
    if keypressed[K_RIGHT]:
        for platform in platforms:
            platform.rect.x -=7
        for enemy in enemy_group:
            enemy.rect.x -=7
        princess.rect.x -= 7
        shift_x +=7
    if keypressed[K_LEFT]:
        for platform in platforms:
            platform.rect.x +=7
        for enemy in enemy_group:
            enemy.rect.x +=7
        princess.rect.x += 7
        shift_x -=7
    if keypressed[K_0]:
        player.rect.y = 0
        y_speed = 0
    for p in platforms:
        if p.is_collide():
            y_speed = 0
            isJump= False
    for e in enemy_group:
        e.is_collide()
    if not(isJump) and keypressed[K_SPACE]:
        y_speed = -14
        isJump = True
    
    player.rect.y += int(y_speed)
    if y_speed < 10:
        y_speed +=0.5
    
    princess.rect.x -= 1
    screen.fill((255,255,220))
    
    screen.blit(background, (0-shift_x,0))
    screen.blit(background2, (700-shift_x,0))
    for p in platforms:
        screen.blit(p.image, p.rect)
    for e in enemy_group:
        screen.blit(e.image, e.rect)
    screen.blit(princess.image, princess.rect)
    screen.blit(player.image, player.rect)
    
    display.update()
