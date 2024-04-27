import pygame
import random
from const import *

#класс для игрока
class Player(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()

        #создание изображения для спрайта
        self.image = pygame.image.load("images/spider-man.png")
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
class Enemy(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()

        #создание изображения для спрайта
        #self.image = pygame.Surface((32, 32))
        #self.image.fill(RED)
        self.image = pygame.image.load("images/tapok.png")

        #начальная позиция по Х, нужна для патрулирования
        self.x_start = x
        #выбор направления начального движения
        self.direction = random.choice([-1, 1])

        #создание хитбокса для спрайта
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y-10

        #компоненты скорости по оси Х и Y
        self.x_velocity = 1
        self.y_velocity = 0
    
    def update(self):
        #если расстояние от начальной точки превысило 50
        #то меняем направление
        if abs(self.x_start - self.rect.x) > 50:
            self.direction *= -1

        #движение спрайта по оси Х
        self.rect.x += self.x_velocity * self.direction

#класс для поднимаемых предметов
class Collectible(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()

        #создание изображения для спрайта
        self.image = pygame.image.load("images/muh.png")
        #self.image = pygame.Surface((16, 16))
        #self.image.fill(GOLD)

        #создание хитбокса для спрайта
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y-30

#класс для платформы
class Platform(pygame.sprite.Sprite):
    def __init__(self, x, y, width, height):
        super().__init__()
        #создание изображения для спрайта
        self.image = pygame.Surface((width, height))
        self.image.fill(BLUE)

        #создание хитбокса для спрайта
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y