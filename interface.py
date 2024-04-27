import pygame

class Rec_Bar(pygame.sprite.Sprite):                                 #реализация маленького квадратика в шкалах
    def __init__(self, filename):
        pygame.sprite.Sprite.__init__(self)                          #наследуем конструктор класса-родителя
        self.image = pygame.image.load(filename).convert_alpha()     #загружаем изображение
    
    def place_rec_bar(self,x,y):
        self.rect = self.image.get_rect(center=(x, y))

class Bar(pygame.sprite.Sprite):                                        #реализация шкалы и заполнение квадратиками
    def __init__(self, filename, x,y, start_param, type):
        pygame.sprite.Sprite.__init__(self)                             #наследуем конструктор класса-родителя
        self.image = pygame.image.load(filename).convert_alpha()        #изобаржение самой шкалы
        self.rect = self.image.get_rect(center=(x, y))                  #хитбокс шкалы
        self.recbars = []                                               #список для хранения иконок
        self.param = start_param                                        #стартовое количество иконок
        if type == "sleep":
            rec_bar_img = "images/rec_bar_sleep.png"
        elif type == "health":
            rec_bar_img = "images/rec_bar_health.png"
        elif type == "food":
            rec_bar_img = "images/rec_bar_meal.png"
        for i in range(start_param):
            self.recbars.append(Rec_Bar(rec_bar_img))
            
    def spawn_Bar(self, dis, start_x, start_y, param):
        for i in range(param):                                         
            self.recbars[i].place_rec_bar(start_x,start_y)              #создаем хитбокс иконки в нужных координатах
            dis.blit(self.recbars[i].image, self.recbars[i].rect)       #отрисовываем ее изображение на хитбоксе
            start_x+=26                                               #сдвигаемся вправо

class Button(pygame.sprite.Sprite):                             #реализация кнопки
    def __init__(self, filename, x,y):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(filename).convert_alpha()
        self.rect = self.image.get_rect(center=(x, y))

    def change_img(self, filename):
        self.image = pygame.image.load(filename).convert_alpha()