import pygame
pygame.mixer.init()

heal_sound = pygame.mixer.Sound("sounds/heal.mp3")   #звук лечения
sleep_sound = pygame.mixer.Sound("sounds/sleep.mp3") #звук сна
food_sound = pygame.mixer.Sound("sounds/eating.mp3") #звук еды
click = pygame.mixer.Sound("sounds/click.mp3") #звук клика
hundred_points_sound = pygame.mixer.Sound("sounds/100points.mp3")  #звук воспроизводящийся каждые 100 очков
pause_sound = pygame.mixer.Sound("sounds/pause.mp3")               #звук кнопки "пауза"
gameover_sound = pygame.mixer.Sound("sounds/game_over.mp3")        #звук проигрыша

playlist = ["music/st1.mp3"]  #плейлист с музыкой игры

pygame.mixer.music.set_volume(0.4)        #установка громкости
pygame.mixer.music.load(playlist[0])      #выбор трека st1.mp3

def playorpause():                        #функция, запускающая, ставящая\снимающая с паузы фоновую музыку
    if pygame.mixer.music.get_pos() == -1:
        pygame.mixer.music.play(-1)

    elif pygame.mixer.music.get_busy() == True:
        pygame.mixer.music.pause()

    else:
        pygame.mixer.music.unpause()