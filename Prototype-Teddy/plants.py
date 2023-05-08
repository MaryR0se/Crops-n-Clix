import pygame
import random

#main color palette
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
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
        self.area_x = 780
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
                self.garden_tiles[i].append(pygame.Rect(k+self.margin+10+40, l+self.margin+10, 80, 80)) #each plot is 80x80 and 20px from the next plot
                self.garden_colors[i].append(DARK_BROWN) #all start as just dirt
                self.garden_timers[i].append(-1) #Timers start at 10

        #list of plants: starting color, then mature color, then low time to mature, then high time, then counter, then plant name
        self.plants = [[LIGHT_GREEN, DARK_GREEN, 1200, 1500, 0, 'Green Plants'], [LIGHT_BLUE, DARK_BLUE, 3000, 4000, 0, 'Blue Plants'], [LIGHT_PURPLE, DARK_PURPLE, 300, 600, 0, 'Pink Plants'], [BLACK, WHITE, 700, 800, 0, 'Weeds']] 

        self.available_seeds = [self.plants[0]] #list of all plants you have, starts with just the normal green one

    def unlock_seed(self, seed_color):
        for i in range(len(self.available_seeds)): #check to see if you already have the seed unlocked
            if seed_color in self.available_seeds[i]: #if you do end here
                return False
        
        for j in range(len(self.plants)): #if you dont already have it unlocked check if its a plant that exists
            if seed_color == self.plants[j][0]: 
               self.available_seeds.append(self.plants[j]) #if it is unlock the seed

    def count_planted(self, seed_color):
        for i in range(len(self.plants)):
            if self.plants[i][0] == seed_color:
                self.plants[i][4] += 1 #increase the counter for that plant by 1
                if i+1 < len(self.plants): #make sure not to index out of range
                    if self.plants[i][4] >= 5:
                        self.unlock_seed(self.plants[i+1][0]) #if you've planted more than 10 then unlock the next seed
    
    def plant_seed(self, i, j):
        for plant in self.plants:
            if plant[0] == self.current_seed:
                self.garden_timers[i][j] = random.randrange(plant[2], plant[3])
                self.garden_colors[i][j] = self.current_seed
                self.count_planted(self.current_seed)

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
        self.shop_seeds = []
        for i in range(len(self.available_seeds)): #create seed list
            self.shop_seeds.append(pygame.Rect(self.area_x + self.margin*3 + 20, 40*i + self.margin*2, 20, 20)) #each plot is 80x80 and 20px from the next plot
            self.font = pygame.font.Font("freesansbold.ttf", 20)
            self.text = self.font.render(f"{(self.available_seeds[i][5])}: {str(self.available_seeds[i][4])}", True, "#000000")
            screen.blit(self.text, (self.area_x + self.margin*3 + 45, 40*i + self.margin*2))
        for i in range(len(self.shop_seeds)):
            pygame.draw.rect(screen, self.available_seeds[i][0], self.shop_seeds[i])
    
    def update_game(self): #update the game every tick
        for i in range(7):
            for j in range(4):

                if self.garden_colors[i][j] == DARK_BROWN and random.randrange(0,10000) == 1: #chance to randomly spawn a weed
                    temp = self.current_seed
                    self.current_seed = BLACK
                    self.plant_seed(i,j)
                    self.current_seed = temp

                if self.garden_timers[i][j] > 0:
                    self.garden_timers[i][j] -= random.randrange(0,5)
                    if self.garden_timers[i][j] < 1:
                        for plant in self.plants:
                            if self.garden_colors[i][j] == plant[0]:
                                self.garden_colors[i][j] = plant[1]

    def click_button(self):
        self.mouse_pos = pygame.mouse.get_pos() #get mouse location

        if pygame.mouse.get_pressed()[0]: #if a plot is clicked plant a seed

            for i in range(7):
                for j in range(4):
                    if self.garden_tiles[i][j].collidepoint(self.mouse_pos):
                        if self.garden_colors[i][j] == DARK_BROWN and self.garden_timers[i][j] < 1:
                            self.plant_seed(i,j)
                        if self.garden_colors[i][j] != DARK_BROWN and self.garden_timers[i][j] < 1:
                            self.garden_timers[i][j] = 100
                            self.garden_colors[i][j] = DARK_BROWN
            
            #create shop area with all available seeds
            for i in range(len(self.shop_seeds)):
                if self.shop_seeds[i].collidepoint(self.mouse_pos):
                    self.current_seed = self.plants[i][0] #change your type of seed when click on a different seed

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

if __name__ == "__main__":
    main()
