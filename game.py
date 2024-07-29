import pygame, sys ,random
pygame.init()
# tạo hàm cho game
def double_floor():
        screen.blit(floor,(floor_x_position,650))
        screen.blit(floor,(floor_x_position+432,650))
def create_pipe():
     random_pipe_pos = random.choice(pipe_height)
     bottom_pipe = pipe.get_rect(midtop =(500, random_pipe_pos))
     top_pipe = pipe.get_rect(midtop =(500, random_pipe_pos-650))     
     return bottom_pipe,top_pipe
def move_pipe(pipes):
    for pipe in pipes :
          pipe.centerx -=5  
    return pipes
def draw_pipe(pipes):
     for p in pipes:
          if p.bottom >= 768:
               screen.blit(pipe,p)
          else:
               flip_pipe = pygame.transform.flip(pipe, False, True)
               screen.blit(flip_pipe,p)
def check_collision(pipes):
     for p in pipes:
          if bird_react.colliderect(p):
               return False
     if bird_react.top <=-75 or bird_react.bottom >= 650:
               return False
     return True
screen = pygame.display.set_mode((432,768))
clock = pygame.time.Clock() 
# tạo biến cho trò chơi
gravity = 0.25
bird_move = 0
game_active = True
# chèn background
bg = pygame.image.load('assets/background-night.png').convert()
bg = pygame.transform.scale2x(bg)
# chèn sàn
floor = pygame.image.load("assets/floor.png").convert()
floor = pygame.transform.scale2x(floor)


# lưu vị trí ban đầu 
floor_x_position = 0

# tạo con chim
bird = pygame.image.load("assets/yellowbird-midflap.png").convert()
bird = pygame.transform.scale2x(bird)
bird_react = bird.get_rect(center = (100,384))
# tạo ống
pipe = pygame.image.load("assets/pipe-green.png").convert()
pipe = pygame.transform.scale2x(pipe)
pipe_list = []
# cho ống xuất hiện 1 time nhất định : timer
spawnpipe = pygame.USEREVENT
pygame.time.set_timer(spawnpipe, 1200)
pipe_height = [200,300,400]
# vòng lặp sự kiện, lấy all event trong game diễn ra
while True:
    for event in pygame.event.get():
        # tạo phím ấn thoát game
        if event.type == pygame.QUIT:
            # phím thoát
            pygame.quit() 
            sys.exit()
        if event.type == pygame.KEYDOWN:
             if event.key == pygame.K_SPACE:
                  bird_move = 0
                  bird_move = -11
        if event.type == spawnpipe:
             pipe_list.extend(create_pipe())
             print(create_pipe)
            # thêm hình ảnh lên màng hình (0,0 là gốc tọa độ d quy định trong pygame)
    screen.blit(bg,(0,0))
    if game_active:
    # Bird       
     bird_move += gravity
     bird_react.centery += bird_move
     screen.blit(bird,bird_react) 
     game_active = check_collision(pipe_list)
     # Pipe
     pipe_list = move_pipe(pipe_list)
     draw_pipe(pipe_list)
    # Floor giảm vị trí ban đầu 1 đơn vị
    floor_x_position -=1
    double_floor()
    # sàn thứ 2 chạy xong thì sàn thứ 1 thay lên vtri sàn thứ2 và lùi ngược lại
    if floor_x_position <= -432:
         floor_x_position=0
        # hiện lên màng hình
    pygame.display.update()
    clock.tick(120)