import pygame
import random
from const import *
from classes import *
from interface import *
from init import *
from audiofiles import *

pygame.init()

#функция для проверки коллизий c платформой
def check_collision_platforms(object, platform_list):
    #перебираем все платформы из списка (не группы спрайтов)
    for platform in platform_list:
        if object.rect.colliderect(platform.rect):
            if object.y_velocity > 0: # Если спрайт падает
                #меняем переменную-флаг
                object.on_ground = True
                #ставим его поверх платформы и сбрасываем скорость по оси Y
                object.rect.bottom = platform.rect.top
                object.y_velocity = 0
            elif object.y_velocity < 0: # Если спрайт движется вверх
                #ставим спрайт снизу платформы
                object.rect.top = platform.rect.bottom
                object.y_velocity = 0
            elif object.x_velocity > 0: # Если спрайт движется вправо
                #ставим спрайт слева от платформы
                object.rect.right = platform.rect.left
            elif object.x_velocity < 0: # Если спрайт движется влево
                #ставим спрайт справа от платформы
                object.rect.left = platform.rect.right

#функция проверки коллизии выбранного объекта с объектами Enemies
def check_collision_enemies(object, enemies_list):
    #running делаем видимой внутри функции чтобы было возможно
    #завершить игру
    global running
    #в списке проверяем
    for enemy in enemies_list:
        #при коллизии
        if object.rect.colliderect(enemy.rect):
            #объект пропадает из всех групп спрайтов и игра заканчивается
            object.kill()
            running = False

#проверка 
def check_collision_collectibles(Player, collectibles_list):
    #если object касается collictible 
    for collectible in collectibles_list:
        if Player.rect.colliderect(collectible.rect):
            #убираем этот объект из всех групп
            collectible.kill()
            #убираем этот объект из списка (чтобы не было проверки коллизии)
            collectibles_list.remove(collectible)
            #прибавляем одно очко
            return(True)
        else:
            return(False)
            

def restart_game(dis):
    pygame.mixer.music.stop() 
    gameover_sound.play() 

    #кнопки в меню проигрыша\рестарта
    yes_button = Button("images/yes.png", 450, 420)
    no_button = Button("images/no.png", 650, 420)
    
    dis.blit(background_the_end, (0, 0))
    button_init(dis, [yes_button, no_button])

    while True:    #игровой цикл во время выбора продолжить\выйти при рестарте
        pygame.display.update()                                        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                #нажатие на крестик
                return(False)
            if event.type == pygame.MOUSEBUTTONDOWN:   #проверка клика
                x,y = event.pos
                if yes_button.rect.collidepoint(x,y):  #кнока Да перезапускает игру
                    click.play() 
                    playorpause() 
                    return(True)
                elif no_button.rect.collidepoint(x,y): #кнопка Нет возвращает в меню
                    click.play() 
                    return(False)

def main_menu(screen):
    screen.blit(blur_menu, (0, 0))
    global is_music_playing
    pygame.mixer.music.rewind() #!!!!        #перезапуск музыки, если играет
    playorpause()               #!!!!        #включение либо выключение музыки
    screen.blit(background_menu, (0, 0))   #отрисовка фона меню
   
    #кнопки в главном меню
    start_button = Button("images/start_button.png", 550, 205)
    quit_button = Button("images/quit_button.png", 550, 350)

    #кнопки управления музыкой, зависят от переменной is_music_playing
    if is_music_playing == True:
        msc_off_button = Button("images/music_off.png", 591, 280)
        msc_on_button = Button("images/music_on_selected.png", 511, 280)
    else:
        msc_off_button = Button("images/music_off_selected.png", 290, 175)
        msc_on_button = Button("images/music_on.png", 209, 175)
   
    #группа кнопок меню
    buttons = [start_button, quit_button, msc_on_button, msc_off_button]


    #отрисовка и печать всех кнопок
    button_init(screen, buttons)
    pygame.display.update()
    global running
    #игровой цикл при нахождении в главном меню
    while True:
        button_init(screen, buttons)
        pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:               #выход при нажатии на крестик
                pygame.quit()
                quit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                x, y = event.pos
                if start_button.rect.collidepoint(x, y):    #нажатие на кнопку начала игры
                    click.play() 
                    return True
                elif quit_button.rect.collidepoint(x, y):   #нажатие на кнопку выхода из игры
                    click.play() 
                    pygame.quit()
                    quit()
                elif msc_off_button.rect.collidepoint(x,y): #нажатие на кнопку выключения музыки
                    click.play()
                    pygame.mixer_music.set_volume(0.0)
                    msc_off_button.change_img("images/music_off_selected.png")  #меняем изображение кнопок чтобы было ясно какая выбрана
                    msc_on_button.change_img("images/music_on.png")
                    is_music_playing = False                                    #меняем статус воспроизведения музыки

                elif msc_on_button.rect.collidepoint(x,y):  #нажатие на кнопку включения музыки
                    click.play()
                    pygame.mixer_music.set_volume(0.4)
                    msc_on_button.change_img("images/music_on_selected.png")
                    msc_off_button.change_img("images/music_off.png")
                    is_music_playing = True

        pygame.time.delay(10)


def play_game(screen):          
    screen.blit(background_image, (0, 0))
    global score_count
    #создаем счетчик частоты кадров и очков
    clock = pygame.time.Clock()
    #создаем игрока, платформы, врагов и то, что будем собирать в игре
    player = Player(400, 235)
    platforms_list = [Platform(0, HEIGHT-25), Platform(700, 355), Platform(100, 350), Platform(400, 235), Platform(950, 223)]
    enemies_list = [Enemy(120, 315)]
    collectibles_list = [Collectible(970, 210), Collectible(670, 335)]

    #создаем групп спрайтов
    player_and_platforms = pygame.sprite.Group()
    enemies = pygame.sprite.Group()
    collectibles = pygame.sprite.Group()

    #в трех циклах добавляем объекты в соответствующие группы
    for i in enemies_list:
        enemies.add(i)

    for i in platforms_list:
        player_and_platforms.add(i)

    for i in collectibles_list:
        collectibles.add(i)

    #отдельно добавляем игрока
    player_and_platforms.add(player)

    global running
    running == True
    start = pygame.time.get_ticks()
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        new_time = pygame.time.get_ticks()      #заканчиваем отсчёт 10 секунд
        if (new_time - start) > 2000:          #каждые 10 секунд выполняем следующие команды
            platforms_list[0].kill
            platforms_list.pop(0)
            platforms_list.append(Platform(random.randint(0, WIDTH), random.randint(0, HEIGHT)))
            player_and_platforms.remove(platforms_list[0])
            player_and_platforms.add(platforms_list[-1])
            #hundred_points_sound.play()     
            pygame.display.update()
            start = pygame.time.get_ticks()     #начинаем отсчёт 10 секунд заново
            
        #проверяем нажатие на клавиши для перемещения
        keys = pygame.key.get_pressed()
        player.x_velocity = 0
        if keys[pygame.K_LEFT]:
            player.x_velocity = -5
        if keys[pygame.K_RIGHT]:
            player.x_velocity = 5
        #условие прыжка более сложное
        if keys[pygame.K_SPACE] and player.on_ground == True:
            player.y_velocity = -9
            player.on_ground = False

        #гравитация для игрока
        player.y_velocity += 0.3 

        #обновляем значения атрибутов игрока и врагов
        player.update()
        enemies.update()

        #отрисовываем фон, платформы, врагов и собираемые предметы
        screen.blit(background_image, (0, 0))
        player_and_platforms.draw(screen)
        enemies.draw(screen)
        collectibles.draw(screen)
        global score_count
        #проверяем все возможные коллизии
        check_collision_platforms(player, platforms_list)
        check_collision_enemies(player, enemies_list)
        if check_collision_collectibles(player, collectibles_list):
            score_count += 1
        #счёт игры
        font = pygame.font.Font(None, 36) # создание объекта, выбор размера шрифта
        #обновление счёта на экране
        score_text = font.render("Счёт: " + str(score_count), True, BLACK)
        score_rect = score_text.get_rect() # создание хитбокса текста
        score_rect.topleft = (511, 40) # расположение хитбокса\текста на экране
        screen.blit(score_text, score_rect)
        
        #обновление экрана и установка частоты кадров
        pygame.display.update()
        clock.tick(60)
    return(restart_game(screen))

#игровой цикл
running = True
menu = True
score_count = 0
is_music_playing = True
#создаем экран
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Тапок')
while True:
    if menu:
        if main_menu(screen) == False:
            break
    if play_game(screen):
        running = True
        menu = False
    else:
        menu = True
        running = True

pygame.quit()