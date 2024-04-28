import pygame
import random
from const import *

#класс для игрока
class Player(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()

        #создание изображения для спрайта
        self.image = pygame.image.load("images/spider-man.png").convert_alpha()
        #self.image = pygame.Surface((32, 32))
        #self.image.fill(GREEN)

        #создание хитбокса для спрайта
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y-10

        #компоненты скорости по оси X и Y
        self.x_velocity = 0
        self.y_velocity = 0

        #переменная-флаг для отслеживания в прыжке ли спрайт
        self.on_ground = False

    def update(self):
        # Обновление позиции игрока
        self.rect.x += self.x_velocity
        self.rect.y += self.y_velocity

#класс для патрулирующих врагов
import random

class Enemy(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.image.load("images/tapok.png").convert_alpha()
        
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y - 10
        
        self.velocity = [random.randint(-3, 3), random.randint(-3, 3)]
    
    def update(self):
        self.rect.move_ip(self.velocity)
        if self.rect.left < 0 or self.rect.right > WIDTH:
            self.velocity[0] *= -1
        if self.rect.top < 0 or self.rect.bottom > HEIGHT:
            self.velocity[1] *= -1


#класс для поднимаемых предметов
class Collectible(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()

        #создание изображения для спрайта
        self.image = pygame.image.load("images/muh.png").convert_alpha()
        #self.image = pygame.Surface((16, 16))
        #self.image.fill(GOLD)

        #создание хитбокса для спрайта
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y-30

#класс для платформы
class Platform(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        #создание изображения для спрайта
        #self.image = pygame.Surface((width, height))
        #self.image.fill(BLUE)
        self.image = pygame.image.load("images/cloud.png").convert_alpha()

        #создание хитбокса для спрайта
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        
        self.velocity = [random.randint(-3, 3), random.randint(-3, 3)]
    def update(self):
        self.rect.move_ip(self.velocity)
        if self.rect.left < 0 or self.rect.right > WIDTH:
            self.velocity[0] *= -1
        if self.rect.top < 0 or self.rect.bottom > HEIGHT:
            self.velocity[1] *= -1