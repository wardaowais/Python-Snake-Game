import pygame
import time
import random
pygame.init()

display_width = 800
display_height = 600

burly_wood=(95, 137, 110)
white = (255,255,255)
black = (0,0,0)
red = (175,0,0)
green = (0,199,140)
yellow = (175,175,0)
blue = (30,144,255)
light_green = (0,255,0)
light_red = (255,0,0)
light_yellow = (255,255,0)
light_blue = (0,191,255)
dark_golden=(184,134,11)
dark_olive_green=(85,107,47)
dark_violet=(6, 66, 45)
navy_blue=(24, 31, 45)

clock = pygame.time.Clock()
 
snake_block = 10
snake_speed = 10

smallFont = pygame.font.SysFont("Comicsansms", 20)
medFont = pygame.font.SysFont("Comicsansms", 45)
largeFont = pygame.font.SysFont("Verdana", 55)



gameDisplay = pygame.display.set_mode((display_width, display_height))
pygame.display.set_caption("Worm Snake Game")
font_style = pygame.font.SysFont("bahnschrift", 25)
score_font = pygame.font.SysFont("Helvetica", 35)

def Your_score(score):
    f=open("snakefile.txt","w")
    value = score_font.render("Your Score: " + str(score), True, black)
    f.write(str(score)+'\n')
    gameDisplay.blit(value, [0 , 0])
    button("Back",260,500,120,35,light_red,green,action = "main")
    button("Quit",400,500,120,35,light_red,green,action = "quit")
    messageToScreen("Press Space to stop", navy_blue,-260,size="small")
    f.close()
def display_scores():
    display_scores = True
    while display_scores:
        gameDisplay.fill(burly_wood)
        messageToScreen("PYTHON SNAKE GAME",navy_blue,-250,size="large")
        messageToScreen("Have a great  scores? ",dark_violet,-100,size="medium")
        messageToScreen("Your Score is: ",black,-24,size="small")
        button("Back",200, 500,150,50, light_yellow, yellow, action = "main")
        button("Quit",450,500,150,50,light_red,red,action = "quit")
        g=open("snakefile.txt",'r')
        for i in g:
            i.rstrip('\n')
        messageToScreen(i,black,15,size="small")
        messageToScreen("Thank you! for play my snake game",dark_violet,40,size="small")
        messageToScreen("Give the feed back about my game",dark_violet,60,size="small")
        messageToScreen("Hope you like my brilliant game",dark_violet,80,size="small")
        
        
        
        pygame.display.update()
        g.close()
        for event in pygame.event.get():
            try:
                if event.type == pygame.QUIT:
                    display_scores = False
                    pygame.quit()
                    quit()
            except Exception:
                messageToScreen("Please press quit  if you don't wants to play again",black)
def our_snake(snake_block, snake_list):
    for x in snake_list:
        pygame.draw.rect(gameDisplay, black, [x[0], x[1], snake_block, snake_block])
 
 
def message(msg, color):
    mesg = font_style.render(msg, True, color)
    gameDisplay.blit(mesg, [display_width / 6, display_height / 3])
    
def text_objects(text, font):
    textSurface = font.render(text, True, black)
    return textSurface, textSurface.get_rect()
 
def isPause():
    loop = 1
    message("PAUSED,Press Space to continue", red)
    while loop:
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    gameDisplay.fill((0, 0, 0))
                    loop = 0
        pygame.display.update()
        
def gameLoop1():
    pause=False
    game_over = False
    game_close = False
    
    x1 = display_width / 2
    y1 = display_height / 2
 
    x1_change = 0
    y1_change = 0
 
    snake_List = []
    Length_of_snake = 1
 
    foodx = round(random.randrange(0, display_width - snake_block) / 10.0) * 10.0
    foody = round(random.randrange(0, display_height - snake_block) / 10.0) * 10.0
 
    while not game_over:
 
        while game_close == True:
            gameDisplay.fill(burly_wood)
            message("You Lost! Press C-Play Again ", red)
            button("Choose levls",60, 500,140,35, light_yellow, yellow, action = "lvl")
            button("Scores",600,500,140,35,light_yellow, yellow, action = "scores")
            Your_score(Length_of_snake - 1)
            pygame.display.update()
 
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_c:
                        gameLoop1()     
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x1_change = -snake_block
                    y1_change = 0
                elif event.key == pygame.K_RIGHT:
                    x1_change = snake_block
                    y1_change = 0     
                elif event.key == pygame.K_UP:
                    y1_change = -snake_block
                    x1_change = 0
                elif event.key == pygame.K_DOWN:
                    y1_change = snake_block
                    x1_change = 0
                if event.key == pygame.K_SPACE:
                    isPause()
        if x1 >= display_width or x1 < 0 or y1 >= display_height or y1 < 0:
            game_close = True
        x1 += x1_change
        y1 += y1_change
        gameDisplay.fill(burly_wood)
        pygame.draw.rect(gameDisplay, green, [foodx, foody, snake_block, snake_block])
        snake_Head = []
        snake_Head.append(x1)
        snake_Head.append(y1)
        snake_List.append(snake_Head)
        if len(snake_List) > Length_of_snake:
            del snake_List[0]
 
        our_snake(snake_block, snake_List)
        Your_score(Length_of_snake - 1)
 
        pygame.display.update()
 
        if x1 == foodx and y1 == foody:
            foodx = round(random.randrange(0, display_width - snake_block) / 10.0) * 10.0
            foody = round(random.randrange(0, display_height - snake_block) / 10.0) * 10.0
            Length_of_snake += 1
 
        clock.tick(snake_speed)
 
    pygame.quit()
    quit()
    
def gameLoop():
    pause=False
    game_over = False
    game_close = False
    
    x1 = display_width / 2
    y1 = display_height / 2
 
    x1_change = 0
    y1_change = 0
 
    snake_List = []
    Length_of_snake = 1
 
    foodx = round(random.randrange(0, display_width - snake_block) / 10.0) * 10.0
    foody = round(random.randrange(0, display_height - snake_block) / 10.0) * 10.0
 
    while not game_over:
 
        while game_close == True:
            gameDisplay.fill(burly_wood)
            message("You Lost! Press C-Play Again", red)
            button("Choose levls",60, 500,140,35, light_yellow, yellow, action = "lvl")
            button("Scores",600,500,140,35,light_yellow, yellow, action = "scores")
            Your_score(Length_of_snake - 1)
            pygame.display.update()
 
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_c:
                        gameLoop()     
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x1_change = -snake_block
                    y1_change = 0
                elif event.key == pygame.K_RIGHT:
                    x1_change = snake_block
                    y1_change = 0     
                elif event.key == pygame.K_UP:
                    y1_change = -snake_block
                    x1_change = 0
                elif event.key == pygame.K_DOWN:
                    y1_change = snake_block
                    x1_change = 0
                if event.key == pygame.K_SPACE:
                    isPause()
        if x1 >= display_width or x1 < 0 or y1 >= display_height or y1 < 0:
            game_close = True
        x1 += x1_change
        y1 += y1_change
        gameDisplay.fill(burly_wood)
        pygame.draw.rect(gameDisplay, green, [foodx, foody, snake_block, snake_block])
        snake_Head = []
        snake_Head.append(x1)
        snake_Head.append(y1)
        snake_List.append(snake_Head)
        if len(snake_List) > Length_of_snake:
            del snake_List[0]
 
        for x in snake_List[:-1]:
            if x == snake_Head:
                game_close = True
        our_snake(snake_block, snake_List)
        Your_score(Length_of_snake - 1)
 
        pygame.display.update()
 
        if x1 == foodx and y1 == foody:
            foodx = round(random.randrange(0, display_width - snake_block) / 10.0) * 10.0
            foody = round(random.randrange(0, display_height - snake_block) / 10.0) * 10.0
            Length_of_snake += 1
 
        clock.tick(snake_speed)
 
    pygame.quit()
    quit()

def text_objects(text, color, size):
    if size == "small":
        textSurf = smallFont.render(text, True, color)
    elif size == "medium":
        textSurf = medFont.render(text, True, color)
    elif size == "large":
        textSurf = largeFont.render(text, True, color)

    return textSurf, textSurf.get_rect()


def messageToScreen(msg, color, y_displace = 0, size = "small"):
    textSurface, textRect = text_objects(msg, color, size)
    textRect.center = (display_width/2), (display_height/2) + y_displace
    gameDisplay.blit(textSurface, textRect)

def text_to_button(msg, color, buttonX, buttonY, buttonWidth, buttonHeight, size = "small"):
    textSurface, textRect = text_objects(msg, color, size)
    textRect.center = ((buttonX + (buttonWidth/2), buttonY + (buttonHeight/2)))
    gameDisplay.blit(textSurface, textRect)

def button(text, x, y, width, height, inactiveColor , activeColor,textColor = black, action = None):
    cur = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()

    if x+ width > cur[0] > x and y + height > cur[1] > y:
        pygame.draw.rect(gameDisplay, activeColor, (x,y,width,height))
        if click[0] == 1 and action != None:
            if action == "quit":
                pygame.quit()
                quit()
            if action == "directions":
                gameDisplay.fill(burly_wood)
                pygame.display.update()
                directions()
            if action == "lvl":
                gameDisplay.fill(burly_wood)
                pygame.display.update()
                levelScreen()
            if action == "main":
                gameDisplay.fill(burly_wood)
                pygame.display.update()
                startScreen()
            if action == "gameLoop1":
                gameDisplay.fill(burly_wood)
                pygame.display.update()
                gameLoop1()
            if action == "gameLoop":
                gameDisplay.fill(burly_wood)
                pygame.display.update()
                gameLoop()
            if action == "scores":
                gameDisplay.fill(burly_wood)
                pygame.display.update()
                display_scores()
          


    else:
        pygame.draw.rect(gameDisplay, inactiveColor, (x,y,width,height))

    text_to_button(text,textColor,x,y,width,height)



def levelScreen():
    level = True

    while level:
        try:
            global levelnumber
            levelnumber = 1 
            gameDisplay.fill(burly_wood)
            messageToScreen("Choose The Levels",  dark_violet, -250, size = "large")
            messageToScreen("Press hard : if you have good experince with snake game ",  dark_violet, -180, size = "small")
            messageToScreen("Press Easy : if you  don't have any  experince with snake game",  dark_violet, -140, size = "small")
            messageToScreen("Press Back : to go to previous page",  dark_violet, -100, size = "small")
            messageToScreen("Press Quit : to destroy your game",  dark_violet, -50, size = "small")
            button("Back",250,500,150,50,light_green, green,action="main")
            button("EASY",250, 390,150,50, light_yellow, yellow, action = "gameLoop1")
            button("QUIT",450,500,150,50,light_green, green,action = "quit")
            button("HARD",450,390,150,50,light_yellow,yellow,action = "gameLoop")
            pygame.display.update()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    level = False
                    pygame.quit()
                    quit()
        except Exception:
            messageToScreen("PLEASE QUIT THE PROGRAM AND START AGAIN",  dark_violet, -30, size = "large")
            
                
def directions():
    directions = True

    while directions:

        gameDisplay.fill(burly_wood)
        messageToScreen("Directions", navy_blue, -200, size = "large")
        messageToScreen("Click The Buttons To Navigate",black,-140)
        messageToScreen("Select Level Buttons To Start The Level",black,-120)
        messageToScreen("The snake can move in any direction according to the user",black,-100)
        messageToScreen("with the help of the keys(LEFT,RIGHT,UP,DOWN ARROW keys).",black,-80)
        messageToScreen("When the snake eats a fruit ",black,-60)
        messageToScreen("the score will increase by 1 points.",black,-40)
        messageToScreen("The block will generate automatically within the boundaries",black,-20)

        messageToScreen("Have Fun!!!",blue,100, size = "medium")
        button("Back",150, 500,150,50, light_yellow, yellow, action = "main")
        button("Quit",550,500,150,50,light_red,red,action = "quit")
        pygame.display.update()

        for event in pygame.event.get():
            try:
                if event.type == pygame.QUIT:
                    directions = False
                    pygame.quit()
                    quit()
            except Exception:
                messageToScreen("Please press quit  if you don't wants to play again",black)
                                
def startScreen():
    try:
        game = True
        while game:
            gameDisplay.fill(burly_wood)
            messageToScreen("Welcome To The", dark_violet, -200, size = "medium")
            messageToScreen("Worm Snake Game", dark_violet, -100, size = "medium")
            messageToScreen("Press direction button if you don't know how to play!", dark_violet, -20, size = "small",)
            button("PLAY GAME",150, 350,150,50, light_green, green, action = "lvl")
            button("Directions",350, 350,150,50, light_yellow, yellow, action = "directions")
            button("Quit Game",550, 350,150,50, light_red, red, action = "quit")


            pygame.display.update()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    game = False
                    pygame.quit()
                    quit()
    except Exception:
        messageToScreen("error occur ", dark_violet, -200, size = "medium")
        

startScreen()
            
            
        
    
    
    


    
          
        
            
            
            
            
            


            
        
        

        
    

        
      

            

        
    


        
        







            
            
    

    
    

               
    
                      
            
        
        
        

       
      


