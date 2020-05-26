'''Shoot-em-up Python Game.

Author: Hasib Sarvari  
Version: 1.4 
Website: http://githib.com/

'''

import pygame  # import the pygame module
import random  # import the random
import sys  # import the systems module


# game setup ################ only runs once
pygame.init()  # starts the game engine
clock = pygame.time.Clock()  # creates clock to limit frames per second
FPS = 60  # sets max speed of main loop
SCREENSIZE = SCREENWIDTH, SCREENHEIGHT = 1360, 800  # sets size of screen/window
screen = pygame.display.set_mode(SCREENSIZE)  # creates awindow and game screen
start_ticks = pygame.time.get_ticks() #starter tick

"""Initalise audio mixer and caption for pygame window. """
pygame.mixer.pre_init()
pygame.mixer.init()
pygame.display.set_caption('Shoot\'em up game') # Display 'Shoot'em up game'

# set variables for colors RGB (0-255)
white = (255, 255, 255)
black = (0, 0, 0)
red = (255, 0, 0)
yellow = (255, 255, 0)
green = (0, 255, 0)

enemySpeed = 5
score = 0
movement = 5

font = pygame.font.Font(None, 45) #setup to use graphics fonts

# start playing the background music
pygame.mixer.music.load("sound/background.mp3")
pygame.mixer.music.set_volume(0.3)   # set background music volume
pygame.mixer.music.play(loops=-1)  # loop forever

#background image
bg = pygame.image.load('img/bgMountain.png')


player1Image = pygame.image.load('img/crosshair.png') #load crosshair image
player1ImageSizeXY =  [64, 64]
player1XY = [100, 100]
pygame.mouse.set_visible(False) #Removes the cursoer from the game

enemy1Image = pygame.image.load('img/bird.png') #load in enermy bird
enemy1XY = [0 , 0]

def scoreboard(): 
    """
    Score board functions which draws the scoreboard.
    
    Function returns everything in the function that is callable

    Returns:
        Background: draws the background of the scoreboard
        Time: time in seconds
        Score: score in the events that has been clicked
    """
    pygame.draw.rect(screen, white, (0, 750, 1360, 50)) 

    text_time = font.render('Time: ' + str(round((30 - seconds),1)), 3, black)
    screen.blit(text_time, (520, 760))

    text_score = font.render('Score: ' +  str(score), 3, black)
    screen.blit(text_score, (730,760))
        
def shootingSound(): 
    """Shooting the hit sounds"""
    pygame.mixer.Channel(0).play(pygame.mixer.Sound("sound/gunshot.ogg"), maxtime=600)
   
gameState = "running"  # controls which state the games is in

# game loop #################### runs 60 times a second!
while gameState != "exit":# game loop - note:  everything in the mainloop is indented one tab
    """Main gmae loop. 

    Retruns: 
        Screen: background iamge of the mountains. 
        Enemey Player
        Player 1 
        Second IF statement
        Mouse potition for player 1
        Enermy Movement 
        Scoreboard initialiation

    """
    fireLock = 0
    for event in pygame.event.get():  # get user interaction events
        if event.type == pygame.QUIT:  # tests if window's X (close) has been clicked
            gameState = "exit"  # causes exit of game loop
    # your code starts here ##############################

    screen.blit(bg, (0, 0))#fill screen with background image

    #calculate how many seconds
    seconds = (pygame.time.get_ticks()-start_ticks)/1000
    if seconds > 30 :  # if more than 30 seconds close the game
        break
    # print(seconds) #print how many seconds

    enemy1 = screen.blit(enemy1Image, enemy1XY)  #set varibale enermy1
    player1 = screen.blit(player1Image, player1XY) #set variable player 1

    #setup the mousepostions
    mousePosition = pygame.mouse.get_pos()
    newXPostiion = mousePosition[0] - (player1ImageSizeXY[0] / 2) #centring the mouse positio and image
    newYPosition = mousePosition[1] - (player1ImageSizeXY[1] / 2)
    player1XY = newXPostiion, newYPosition

    for i in range(enemySpeed):
        enemy1XY[0] += movement # enemy movemtn left to right 
        if pygame.mouse.get_pressed()[0] == 1 and fireLock == 0:
            fireLock = 1
            if player1.colliderect(enemy1):
                shootingSound()          
                # print("Hit!")
                score += 1
                enemy1XY[0] = -150
                enemy1XY[1] = random.randint(0,700)
        
        #Check if enermy goes off screen
        if enemy1XY[0] >= SCREENWIDTH:
            enemy1XY[0] = -150  
            enemy1XY[1] = random.randint(0,700)

    scoreboard()#display scoreboard
    # your code ends here ###############################
    pygame.display.flip()  # transfers build screen to human visable screen
    clock.tick(FPS)  # limits game to frame per second, FPS value

# out of game loop ###############
print("The game has closed")  # notifies user the game has ended
pygame.quit()   # stops the game engine
sys.exit()  # close operating system window

