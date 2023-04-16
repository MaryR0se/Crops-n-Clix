import pygame
import random

#main color palette
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

#Create Window
width = 1230
height = 830
screen = pygame.display.set_mode(size=(width,height))
pygame.display.set_caption("Farm Game Prototype")

class Game:
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
        #screen.fill(LIGHT_BROWN)

        #create farming area
        farm_area = pygame.Rect(self.margin, self.margin, self.area_x, self.area_y)
        #animal_area = pygame.Rect(self.margin, self.margin*2 + self.area_y, self.area_x, self.area_y)
        pygame.draw.rect(screen, MEDIUM_BROWN, farm_area)
        #pygame.draw.rect(screen, MEDIUM_BROWN, animal_area)
        
        #side_box_1 = pygame.Rect(self.margin*2 + self.area_x, self.margin, self.side_box_x, self.side_box_y)
        #side_box_2 = pygame.Rect(self.margin*2 + self.area_x, self.margin*2 + self.side_box_y, self.side_box_x, self.side_box_y)
        #side_box_3 = pygame.Rect(self.margin*2 + self.area_x, self.margin*3 + self.side_box_y*2, self.side_box_x, self.side_box_y)
        #pygame.draw.rect(screen, MEDIUM_BROWN, side_box_1)
        #pygame.draw.rect(screen, MEDIUM_BROWN, side_box_2)
        #pygame.draw.rect(screen, MEDIUM_BROWN, side_box_3)

        #draw garden
        for i in range(7):
            for j in range(4):
                pygame.draw.rect(screen, self.garden_colors[i][j], self.garden_tiles[i][j])
        
        #draw shop seeds
        for i in range(len(self.shop_seeds)):
            pygame.draw.rect(screen, self.seed_young[i], self.shop_seeds[i])
    

    def update_game(self): #updat the game every tick
        for i in range(7):
            for j in range(4):
                if self.garden_timers[i][j] > 0:
                    self.garden_timers[i][j] -= random.randrange(0,5)
                    if self.garden_timers[i][j] < 1:
                        if self.garden_colors[i][j] == LIGHT_GREEN:
                            self.garden_colors[i][j] = DARK_GREEN
                        if self.garden_colors[i][j] == LIGHT_PURPLE:
                            self.garden_colors[i][j] = DARK_PURPLE
                        if self.garden_colors[i][j] == LIGHT_BLUE:
                            self.garden_colors[i][j] = DARK_BLUE


    def click_button(self):
        self.mouse_pos = pygame.mouse.get_pos() #get mouse location

        for i in range(7):
            for j in range(4):
                if self.garden_tiles[i][j].collidepoint(self.mouse_pos):
                    if pygame.mouse.get_pressed()[0]: #if a plot is clicked make it dark green
                        if self.garden_colors[i][j] == DARK_BROWN and self.garden_timers[i][j] < 1:
                            self.garden_timers[i][j] = random.randrange(800, 1000)
                            self.garden_colors[i][j] = self.current_seed
        
        #create shop area with all available seeds
        for i in range(len(self.shop_seeds)):
            if self.shop_seeds[i].collidepoint(self.mouse_pos):
                self.current_seed = self.seed_young[i] #change your type of seed


    #render the game and update the screen
    def render(self):
        self.draw_screen()
        self.update_game()
        self.click_button()
        pygame.display.update()


#Initialize Pygame
pygame.init()
game = Game()

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
        game.render()

    pygame.quit()


#if __name__ == "__main__":
#    main()