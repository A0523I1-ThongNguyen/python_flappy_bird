import pygame, sys ,random
# set sound are more suitable for pygame
pygame.mixer.pre_init(frequency=44100, size=-16, channels=2, buffer=512)
pygame.init()
# method game
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
          if p.bottom >= 600:
               screen.blit(pipe,p)
          else:
               flip_pipe = pygame.transform.flip(pipe, False, True)
               screen.blit(flip_pipe,p)
def check_collision(pipes):
     for p in pipes:
          if bird_react.colliderect(p):
               hit_sound.play()
               return False
     if bird_react.top <=-75 or bird_react.bottom >= 650:
               return False
     return True
# method of creating effects for birds
def rotate_bird(parBird):
     new_bird = pygame.transform.rotozoom(parBird,-bird_move*3,1)
     return new_bird
def bird_animation():
     new_bird = bird_list[bird_index]
     new_bird_rect = new_bird.get_rect(center = (100,bird_react.centery))
     return new_bird, new_bird_rect
def score_display(game_state):
     if game_state == 'main game':
          score_surface = game_font.render(str(int(score)),True,(255,255,255))
          score_rect = score_surface.get_rect(center = (216,100))
          screen.blit(score_surface, score_rect)
     if game_state == "game_over":
          score_surface = game_font.render(f'Your score: {int(score)}',True,(255,255,255))
          score_rect = score_surface.get_rect(center = (216  ,100))
          screen.blit(score_surface, score_rect)

          high_score_surface = game_font.render(f'High score: {int(high_score)}',True,(242, 145, 17))
          high_score_rect = high_score_surface.get_rect(center = (216,620))
          screen.blit(high_score_surface, high_score_rect)
def update_score(score, high_score):
     if score > high_score:
          high_score = score
     return high_score
screen = pygame.display.set_mode((432,768))
clock = pygame.time.Clock() 
game_font = pygame.font.Font("04B_19.ttf", 40)
# variable for game
gravity = 0.25
bird_move = 0
game_active = True
score = 0
high_score = 0
#  background
bg = pygame.image.load('assets/background-night.png').convert()
bg = pygame.transform.scale2x(bg)
# floor
floor = pygame.image.load("assets/floor.png").convert()
floor = pygame.transform.scale2x(floor)


# original location
floor_x_position = 0

#create bird
bird_down = pygame.transform.scale2x(pygame.image.load("assets/yellowbird-downflap.png")).convert_alpha()
bird_mid = pygame.transform.scale2x(pygame.image.load("assets/yellowbird-midflap.png")).convert_alpha()
bird_up = pygame.transform.scale2x(pygame.image.load("assets/yellowbird-upflap.png")).convert_alpha()
bird_list = [bird_down,bird_mid,bird_up]
bird_index = 2   
bird = bird_list[bird_index]
# bird = pygame.image.load("assets/yellowbird-midflap.png").convert_alpha()
# bird = pygame.transform.scale2x(bird)
bird_react = bird.get_rect(center = (100,384))

# create time for bird
birdflap = pygame.USEREVENT + 1
pygame.time.set_timer(birdflap,200)

# create pipe
pipe = pygame.image.load("assets/pipe-green.png").convert()
pipe = pygame.transform.scale2x(pipe)
pipe_list = []
#create timer
spawnpipe = pygame.USEREVENT
pygame.time.set_timer(spawnpipe, 1200)
pipe_height = [200,300,400]
# create end screen
var_game_over =  pygame.image.load("assets/message.png").convert_alpha()
game_over_rect = var_game_over.get_rect(center=(216,384))

# insert sound 
flap_sound = pygame.mixer.Sound("sound/sfx_wing.wav")
hit_sound = pygame.mixer.Sound("sound/sfx_hit.wav")
score_sound = pygame.mixer.Sound("sound/sfx_point.wav")
score_sound_countdown = 100
# while loop event of game
while True:
    for event in pygame.event.get():
        # game exit key
        if event.type == pygame.QUIT: 
            pygame.quit() 
            sys.exit()
        if event.type == pygame.KEYDOWN:
               if event.key == pygame.K_SPACE and game_active:
                  bird_move = 0
                  bird_move = -6
                  flap_sound.play()
               if event.key == pygame.K_SPACE and game_active==False:
                    game_active = True
                    pipe_list.clear()
                    bird_react.center = (100 , 384)
                    bird_move = 0
                    score = 0
        if event.type == spawnpipe:
             pipe_list.extend(create_pipe())
             print(create_pipe)
        if event.type == birdflap:
             if bird_index < 2:
                  bird_index +=1
             else:
                  bird_index =0
             bird,bird_react = bird_animation()
            # add image to screen
    screen.blit(bg,(0,0))
    if game_active:
          # Bird       
          bird_move += gravity
          # effects in motion
          rotated_bird = rotate_bird(bird)
          bird_react.centery += bird_move
          screen.blit(rotated_bird,bird_react) 
          game_active = check_collision(pipe_list)
          # Pipe
          pipe_list = move_pipe(pipe_list)
          draw_pipe(pipe_list)
          score += 0.01
          score_display('main game')
          score_sound_countdown -= 1
          if score_sound_countdown <= 0:
               score_sound.play()
               score_sound_countdown = 100
    else:
          screen.blit(var_game_over,game_over_rect)
          high_score = update_score(score,high_score)
          score_display('game_over')
    # Floor decreases the original position by 1 unit
    floor_x_position -=1
    double_floor()
    # When the second floor is depleted, the first welder moves up to replace it and then returns back.
    if floor_x_position <= -432:
          floor_x_position=0
        # display on the screen
    pygame.display.update()
    clock.tick(120)