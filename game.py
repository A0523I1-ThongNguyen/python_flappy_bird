import pygame
pygame.init()
screen = pygame.display.set_mode((432,768))

# vòng lặp sự kiện, lấy all event trong game diễn ra
while True:
    for event in pygame.event.get():
        # tạo phím ấn thoát game
        if event.type == pygame.QUIT:
            # phím thoát
            pygame.quit() 
        # hiện lên màng hình
    pygame.display.update()