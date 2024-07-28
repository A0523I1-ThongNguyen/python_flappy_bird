import pygame, sys ,random
pygame.init()
# method for game
def double_floor():
        screen.blit(floor,(floor_x_position,600))
        screen.blit(floor,(floor_x_position+432,600))
def create_pipe():
     random_pipe_pos = random.choice(pipe_height)
     new_pipe = pipe.get_rect(midtop =(500, random_pipe_pos))
     return new_pipe
def move_pipe(pipes):
    for pipe in pipes :
          pipe.centerx -=5
    return pipes
def draw_pipe(pipes):
     for p in pipes:
          screen.blit(pipe,p)
screen = pygame.display.set_mode((432,768))
clock = pygame.time.Clock() 
# ariables for game
gravity = 0.25
bird_move = 0
#  background
bg = pygame.image.load('assets/background-night.png').convert()
bg = pygame.transform.scale2x(bg)
# floor
floor = pygame.image.load("assets/floor.png").convert()
floor = pygame.transform.scale2x(floor)
# original location 
floor_x_position = 0

# bird
bird = pygame.image.load("assets/yellowbird-midflap.png").convert()
bird = pygame.transform.scale2x(bird)
bird_react = bird.get_rect(center = (100,384))
# pipe
pipe = pygame.image.load("assets/pipe-green.png").convert()
pipe = pygame.transform.scale2x(pipe)
pipe_list = []
# timer
spawnpipe = pygame.USEREVENT
pygame.time.set_timer(spawnpipe, 1200)
pipe_height = [200,300,400]
# loop event 
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
             pipe_list.append(create_pipe())
             print(create_pipe)
            
    screen.blit(bg,(0,0))
    # Bird
    bird_move += gravity
    bird_react.centery += bird_move
    screen.blit(bird,bird_react)
    # Pipe
    pipe_list = move_pipe(pipe_list)
    draw_pipe(pipe_list)
    # Floor
    floor_x_position -=1
    double_floor()
    
    if floor_x_position <= -432:
         floor_x_position=0
       
    pygame.display.update()
    clock.tick(120)