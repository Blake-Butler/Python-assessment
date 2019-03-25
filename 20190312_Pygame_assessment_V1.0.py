#Pygame_assessment_V1.0
#By Blake

#Importing pygame
import pygame

pygame.init()

#Setting up the display window
win = pygame.display.set_mode((500, 500))
pygame.display.set_caption("pygame assessment")


#Importing images
bg = pygame.image.load('Background.png')
character = pygame.image.load('Character.png')
characterRight = pygame.image.load('Character_right.png')
characterLeft = pygame.image.load('Character_left.png')



#Setting up the variables
clock = pygame.time.Clock() #This allows me to set the frame rate
x=160
y=380
width=64
height=64
vel=5
walkCount=0
hp=3

        

#Draws the game window
def redrawGameWindow():
        
        win.fill((0,0,0))#Fills the background as black
        global walkCount #Sets walkcount as a global variable
        win.blit(bg, (0,0))    #Sets the background
    
        if walkCount + 1 >= 27:
                walkCount = 0
        if left:  #This draws the character left when left button is pushed
                win.blit(characterLeft, (x,y))
                walkCount += 1
        elif right:#This draws the character right when right button is pushed
                win.blit(characterRight, (x,y))
                walkCount += 1
        else: #This draw the character straight when no buttons are being pressed
                win.blit(character, (x,y))               
        pygame.display.flip()
        pygame.display.update()    

#Main loop
run=True
while run:
        clock.tick(27)#Sets the frame rate
        for event in pygame.event.get():
                if event.type == pygame.QUIT:
                        run=False
    
    #This is for the movement of the character
        keys=pygame.key.get_pressed()
        if keys[pygame.K_LEFT] and x > vel: 
                x -= vel
                left=True
                right=False        #This makes sure the character doesn't go off the screen
        elif keys[pygame.K_RIGHT] and x < 400 - width - vel:
                x += vel
                left=False
                right=True
        else:
                left=False
                right=False   
                walkCount=0
        
        #Draws the game window        
        redrawGameWindow()
            

#Quits the game        
pygame.quit()
    
