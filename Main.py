from pygame import *

font.init()
font2 = font.Font(None, 33)
win_width = 700
win_height = 500
window = display.set_mode((win_width, win_height))
window.fill((130,200, 230))
class GameSprite(sprite.Sprite):
    def __init__(self, player_image, player_x, player_y, player_speed, w=65, h=65):
        super().__init__()
        self.image = transform.scale(image.load(player_image), (w, h))
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y

    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

class Player(GameSprite):
    def update_R(self):
        keys_pressed = key.get_pressed()
        if keys_pressed[K_DOWN] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys_pressed[K_UP] and self.rect.y < 635:
            self.rect.y += self.speed

    def update_L(self):
        keys_pressed = key.get_pressed()
        if keys_pressed[K_w] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys_pressed[K_s] and self.rect.y < 635:
            self.rect.y += self.speed


game = True
finish = False
clock = time.Clock()
FPS = 60
lose1 = font2.render("Пропуск!", 1, (255, 255, 255))
rocket_1 = Player('Ворота.jpg', 30, 200, 4, 50, 150)
rocket_2 = Player('Ворота.jpg', 650, 200, 4, 50, 150)

ball = Player('Ball.png', 200, 200, 2, 20, 20 )

speed_x = 3
speed_y = 5

while game:
    for e in event.get():
        if e.type == QUIT:
            game = False


    if not finish:
        window.fill((130, 200, 230))

        rocket_1.update_R()
        rocket_2.update_L()

        ball.reset()

        ball.rect.x += speed_x
        ball.rect.y += speed_y

        if sprite.collide_rect(rocket_1, ball) or sprite.collide_rect(rocket_2, ball):
            speed_x *= -1

        if ball.rect.y > win_height - 50 or ball.rect.y < 0:
            speed_y *= -1

        if ball.rect.x < 3 or ball.rect.x > 700:
            finish = True
            window.blit(lose1, (200, 200))


        rocket_1.reset()
        rocket_2.reset()

    display.update()
    clock.tick(FPS)