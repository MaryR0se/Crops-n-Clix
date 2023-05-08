import pygame
import os
import random
import plants as A
import farm_animals as M


pygame.font.init()

#caption
pygame.display.set_caption("Prototype 0!")
#window
WIDTH = 1200 #825
HEIGHT = 800 #WIDTH / 1.61803398875 #thought a golden(-ish) rectangle would be cute here
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
#primary colors
DARK_BROWN = ( 70,  40,  30)
BROWN = (185, 165, 130)
YELLOW = (235, 250, 200)
GREEN = (185, 250, 190)
CYAN = (140, 235, 245)
BLUE = (165, 195, 245)
MAGENTA = (240, 190, 230)
RED = (218, 119, 175)  #""""""red""""""
#frames per second (the one I chose is arbitrary)
FPS = 60
#windows
CROPS = pygame.Rect(10, 10, HEIGHT - 20, HEIGHT / 2 - 20)
ANIMALS = pygame.Rect(10, HEIGHT / 2 + 30, HEIGHT - 20, HEIGHT / 2 - 15)
NEWS = pygame.Rect(HEIGHT + 10, 10, WIDTH - HEIGHT, HEIGHT / 3 - 15)
INVENTORY = pygame.Rect(HEIGHT + 10, HEIGHT / 3 + 20, WIDTH - HEIGHT, HEIGHT / 3 - 15)
SHOP = pygame.Rect(HEIGHT + 10, HEIGHT / 3 * 2 + 30, WIDTH - HEIGHT, HEIGHT / 3 - 15)
#animal pens
PEN_SIZE = (HEIGHT - 60, HEIGHT / 2 - 60)



WHITE = (255, 255, 255)
DARK_BROWN = (70,40,30)
MEDIUM_BROWN = (185, 165, 130)
LIGHT_BROWN = (235, 250, 200)
LIGHT_GREEN = (185, 250, 190)
DARK_GREEN = (40, 140, 10)
LIGHT_PURPLE = (240, 190, 230)
DARK_PURPLE = (220, 120, 175)
LIGHT_BLUE = (140, 235, 245)
DARK_BLUE = (165, 195, 245)

width = 1230
height = 830
screen = pygame.display.set_mode(size=(width,height))
pygame.display.set_caption("Farm Game Prototype")







class draw:
    def __init__(self):
        self.margin = 10
        self.area_x = 700
        self.area_y = 400
        self.side_box_x = 500
        self.side_box_y = (height / 3) - (self.margin+3)
        self.plot_size = 100
        
        self.current_seed = LIGHT_GREEN
        self.garden_tiles = [] #Create garden plots
        self.garden_colors = [] #List of their colors
        self.garden_timers = [] #Timers

        for i in range(7): #7 x 4 for no particular reason
            self.garden_tiles.append([])
            self.garden_colors.append([])
            self.garden_timers.append([])
            for j in range(4):
                k = self.plot_size*i
                l = self.plot_size*j
                self.garden_tiles[i].append(pygame.Rect(k+self.margin+10, l+self.margin+10, 80, 80)) #each plot is 80x80 and 20px from the next plot
                self.garden_colors[i].append(DARK_BROWN) #all start as just dirt
                self.garden_timers[i].append(-1) #Timers start at 10

        self.seed_young = [LIGHT_GREEN, LIGHT_BLUE, LIGHT_PURPLE] #list of seed colors
        self.seed_old = [DARK_GREEN, DARK_BLUE, DARK_PURPLE] #seed colors once mature
        self.shop_seeds = []
        for i in range(len(self.seed_young)): #create seed list
            self.shop_seeds.append(pygame.Rect(self.area_x + self.margin*3, 40*i + self.margin*2, 20, 20)) #each plot is 80x80 and 20px from the next plot
        self.game_font = pygame.font.Font(None, 28)
    
    def draw_screen(self):
            screen.fill(GREEN)

            #create farming area
            farm_area = pygame.Rect(10, 10, 700, 400)
            #animal_area = pygame.Rect(self.margin, self.margin*2 + self.area_y, self.area_x, self.area_y)
            pygame.draw.rect(screen, MEDIUM_BROWN, farm_area)
            pygame.draw.rect(screen, MEDIUM_BROWN, ANIMALS)
            
            #side_box_1 = pygame.Rect(self.margin*2 + self.area_x, self.margin, self.side_box_x, self.side_box_y)
            #side_box_2 = pygame.Rect(self.margin*2 + self.area_x, self.margin*2 + self.side_box_y, self.side_box_x, self.side_box_y)
            #side_box_3 = pygame.Rect(self.margin*2 + self.area_x, self.margin*3 + self.side_box_y*2, self.side_box_x, self.side_box_y)
            pygame.draw.rect(screen, MEDIUM_BROWN, NEWS)
            pygame.draw.rect(screen, MEDIUM_BROWN, INVENTORY)
            pygame.draw.rect(screen, MEDIUM_BROWN, SHOP)

            #draw garden
            for i in range(7):
                for j in range(4):
                    pygame.draw.rect(screen, self.garden_colors[i][j], self.garden_tiles[i][j])
            
            #draw shop seeds
            for i in range(len(self.shop_seeds)):
                pygame.draw.rect(screen, self.seed_young[i], self.shop_seeds[i])

    def draw_window(self):
        WIN.fill(LIGHT_BROWN)

        #pygame.draw.rect(WIN, BROWN, CROPS)
        pygame.draw.rect(WIN, BROWN, ANIMALS)
        pygame.draw.rect(WIN, BROWN, NEWS)
        pygame.draw.rect(WIN, BROWN, INVENTORY)
        pygame.draw.rect(WIN, BROWN, SHOP)

        #WIN.blit(current_animal.pen_sprite, (ANIMALS.x + 20, ANIMALS.y + 20))
        #for rect in current_animal.rectangles:
        #    WIN.blit(rect[1], (rect[0].x, rect[0].y))

    def render(self):
        self.draw_window()
        pygame.display.update()


#Initialize Pygame
pygame.init()
draw = draw()

#Determine FPS
FPS = 60


#run game
def main():
    #Create Clock and run game
    clock = pygame.time.Clock()
    run = True

    #runs the game
    while run:

        #makes it run at the desired frame rate
        clock.tick(FPS)

        #closes game if window is closed
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
        
        #draw the screen every frame
        draw.render()

    pygame.quit()








"""""""""
def draw_window(current_animal):
    WIN.fill(GREEN)

    pygame.draw.rect(WIN, BROWN, CROPS)
    pygame.draw.rect(WIN, BROWN, ANIMALS)
    pygame.draw.rect(WIN, BROWN, NEWS)
    pygame.draw.rect(WIN, BROWN, INVENTORY)
    pygame.draw.rect(WIN, BROWN, SHOP)

    WIN.blit(current_animal.pen_sprite, (ANIMALS.x + 20, ANIMALS.y + 20))
    for rect in current_animal.rectangles:
        WIN.blit(current_animal.animal_sprite, (rect.x, rect.y))

    pygame.display.update()
    """""""""