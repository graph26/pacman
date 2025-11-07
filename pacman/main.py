from library import *

pygame.init()

screenX=900
screenY=600
screen = pygame.display.set_mode([screenX,screenY])
pygame.display.set_caption('Пакмен')
pygame.display.set_icon(pygame.image.load('gallery/pacman_icon.png'))

running = True
menu_true = True


def menu():
    global menu_true, screen
    screen.fill([0, 0, 0])
    screen.blit(pygame.image.load('gallery/tabl_pacman.png'), [50, 10])
    font = pygame.font.Font(None, 50)
    text_start = font.render(f'Начать', 1, [255, 255, 255])
    screen.blit(text_start, [824 // 2 - 20, 340])
    text_setting = font.render(f'Настройки', 1, [255, 255, 255])
    screen.blit(text_setting, [824 // 2 - 50, 400])
    menu_true = False


while running:
    if menu_true:
        menu()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    pygame.time.delay(50)
    pygame.display.flip()

pygame.quit()