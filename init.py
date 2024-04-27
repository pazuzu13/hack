import pygame
from interface import Bar

def bar_init(dis, kukuruzmen):                                      #начальная расстановка шкал со сном, здоровьем и сытостью
    sleep_bar = Bar("images/bar_sleep.png", 80, 30, 5, "sleep")
    health_bar = Bar("images/bar_health.png", 80, 80, 5, "health")
    food_bar = Bar("images/bar_food.png", 80, 130, 5, "food")
    
    dis.blit(sleep_bar.image, sleep_bar.rect)
    dis.blit(health_bar.image, health_bar.rect)
    dis.blit(food_bar.image, food_bar.rect)
    
    sleep_bar.spawn_Bar(dis, 29, 30, kukuruzmen.sleep)
    health_bar.spawn_Bar(dis, 29, 80, kukuruzmen.health)
    food_bar.spawn_Bar(dis, 29, 130, kukuruzmen.food)
    
    pygame.display.update()
   
def kukuruzmen_init(dis, kukuruzmen):                   #начальная расстановка для изображения кукурузмена
    dis.blit(kukuruzmen.image, kukuruzmen.rect)

def score_init(dis, kukuruzmen):                            #начальная расстановка блока с количеством очков
    my_font = pygame.font.SysFont('Comic Sans MS', 20)
    text_surface = my_font.render('Количество очков:'+ str(kukuruzmen.score), False, (0, 0, 0))
    dis.blit(text_surface, (280,0))

def button_init(dis, buttons):                          #начальная расстановка для кнопок
    for button in buttons:
        dis.blit(button.image, button.rect)