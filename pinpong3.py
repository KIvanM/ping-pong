from pygame import *

back = (200, 255, 255)
win_width = 700
win_height = 500
window = display.set_mode((win_width, win_height))

clock = time.Clock()
FPS = 60
game = True

class GameSprite(sprite.Sprite):
    def __init__(self, player_image, player_x, player_y, player_speed):
        super().__init__()
        self.image = transform.scale(image.load(player_image), (50, 50))
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

class Player(GameSprite):
    def update(self):
        keys = key.get_pressed()
        if keys[K_w] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys[K_s] and self.rect.y < win_height -50:
            self.rect.y += self.speed

    def update1(self):
        keys = key.get_pressed()
        if keys[K_UP] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys[K_DOWN] and self.rect.y < win_height -50:
            self.rect.y += self.speed

racket = Player("racket.png", 650, 250, 10)
racket1 = Player("racket.png", 0, 250, 10)
tenis = GameSprite("tenis_ball.png", 350, 250, 6)

font.init()
font1 = font.Font(None, 35)
lose1 = font1.render("PLAYER 1 LOSE!", True, (180, 0, 0))
lose2 = font1.render("PLAYER 2 LOSE!", True, (180, 0, 0))

finish = False
speed_x = 3
speed_y = 3

while game:
    for e in event.get():
        if e.type == QUIT:
            game = False

    if tenis.rect.x < 0:
        finish = True
        window.blit(lose1, (250, 230))

    if tenis.rect.x > win_width - 50:
        finish = True
        window.blit(lose2, (250, 230))

    if finish != True:
        window.fill(back)
        racket.update1()
        racket1.update()

        tenis.rect.x += speed_x
        tenis.rect.y += speed_y

        if tenis.rect.y > win_height - 50 or tenis.rect.y < 0:
            speed_y *= -1
        if sprite.collide_rect(racket, tenis) or sprite.collide_rect(racket1, tenis):
            speed_x *= -1

        racket.reset()
        racket1.reset()
        tenis.reset()

    display.update()
    clock.tick(FPS)
