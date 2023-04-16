import pygame
import os
import random
pygame.font.init()

#caption
pygame.display.set_caption("Prototype 0!")
#window
WIDTH = 1200 #825
HEIGHT = 800 #WIDTH / 1.61803398875 #thought a golden(-ish) rectangle would be cute here
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
#primary colors
DARK_BROWN = ( 71,  43,  30)
BROWN = (186, 167, 131)
YELLOW = (235, 250, 200)
GREEN = (185, 251, 192)
CYAN = (142, 236, 245)
BLUE = (163, 196, 243)
MAGENTA = (241, 192, 232)
RED = (218, 119, 175)  #""""""red""""""
#frames per second (the one I chose is arbitrary)
FPS = 24
#windows
CROPS = pygame.Rect(10, 10, HEIGHT - 20, HEIGHT / 2 - 20)
ANIMALS = pygame.Rect(10, HEIGHT / 2 + 10, HEIGHT - 20, HEIGHT / 2 - 20)
NEWS = pygame.Rect(HEIGHT + 10, 10, WIDTH - HEIGHT - 20, HEIGHT / 3 - 20)
INVENTORY = pygame.Rect(HEIGHT + 10, HEIGHT / 3 + 10, WIDTH - HEIGHT - 20, HEIGHT / 3 - 20)
SHOP = pygame.Rect(HEIGHT + 10, HEIGHT / 3 * 2 + 10, WIDTH - HEIGHT - 20, HEIGHT / 3 - 20)
#animal pens
PEN_SIZE = (HEIGHT - 60, HEIGHT / 2 - 60)
CHICKEN_PEN_IMG = pygame.image.load(os.path.join("Assets", "chickens.png"))
CHICKEN_PEN = pygame.transform.scale(CHICKEN_PEN_IMG, PEN_SIZE)
GOAT_PEN_IMG = pygame.image.load(os.path.join("Assets", "goats.png"))
GOAT_PEN = pygame.transform.scale(GOAT_PEN_IMG, PEN_SIZE)
PIG_PEN_IMG = pygame.image.load(os.path.join("Assets", "pigs.png"))
PIG_PEN = pygame.transform.scale(PIG_PEN_IMG, PEN_SIZE)
#animal sprites
ANIMAL_SIZE = (50, 50)
CHICKEN_IMG = pygame.image.load(os.path.join("Assets", "chicken.png"))
CHICKEN = pygame.transform.scale(CHICKEN_IMG, ANIMAL_SIZE)
GOAT_IMG = pygame.image.load(os.path.join("Assets", "goat.png"))
GOAT = pygame.transform.scale(GOAT_IMG, ANIMAL_SIZE)
PIG_IMG = pygame.image.load(os.path.join("Assets", "pig.png"))
PIG = pygame.transform.scale(PIG_IMG, ANIMAL_SIZE)



def draw_window(current_animal):
    WIN.fill(YELLOW)

    pygame.draw.rect(WIN, BROWN, CROPS)
    pygame.draw.rect(WIN, BROWN, ANIMALS)
    pygame.draw.rect(WIN, BROWN, NEWS)
    pygame.draw.rect(WIN, BROWN, INVENTORY)
    pygame.draw.rect(WIN, BROWN, SHOP)

    WIN.blit(current_animal.pen_sprite, (ANIMALS.x + 20, ANIMALS.y + 20))
    for rect in current_animal.rectangles:
        WIN.blit(current_animal.animal_sprite, (rect.x, rect.y))


    pygame.display.update()

def create_animals(num_chickens=0, num_goats=0, num_pigs=0):
    #animal class
    class Animal:
        def __init__(self, name, pen_sprite, animal_sprite, num_animals):
            self.name = name
            self.pen_sprite = pen_sprite
            self.animal_sprite = animal_sprite
            self.num_animals = num_animals
            self.rectangles = self.shuffle()

        def shuffle(self):
            rects = []
            for i in range(self.num_animals):
                rects.append(pygame.Rect(random.randint(ANIMALS.x + 20, ANIMALS.x + ANIMALS.width - 20 - 50), random.randint(ANIMALS.y + 20, ANIMALS.y + ANIMALS.height - 20 - 50), 50, 50))
            return rects

        def add_animal(self):
            self.num_animals += 1
            self.rectangles = self.shuffle()
        
        def sub_animal(self):
            self.num_animals -= 1
            self.rectangles = self.shuffle()

    chickens = Animal("chickens", CHICKEN_PEN, CHICKEN, num_chickens)
    goats = Animal("goats", GOAT_PEN, GOAT, num_goats)
    pigs = Animal("pigs", PIG_PEN, PIG, num_pigs)

    all_animals = [
        chickens,
        goats,
        pigs
    ]
    return all_animals

def main():

    all_animals = create_animals()
    current_animal_index = 0

    clock = pygame.time.Clock()
    run = True
    while run:
        clock.tick(FPS)

        current_animal = all_animals[current_animal_index]
        draw_window(current_animal)

        for event in pygame.event.get():
            if event.type == pygame.QUIT: #Without this, the x button doesn't work!!
                run = False
                pygame.quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT: #later change to a click of an arrow icon on screen
                    current_animal_index = (current_animal_index + 1) % len(all_animals)
                    #print(current_animal.name)
                if event.key == pygame.K_LEFT: #later change to a click of an arrow icon on screen
                    current_animal_index = (current_animal_index - 1) % len(all_animals)
                    #print(current_animal.name)
            if event.type == pygame.MOUSEBUTTONUP:
                if SHOP.collidepoint(SHOP.x, SHOP.y):
                    all_animals[0].add_animal()
                    #print(all_animals[0].num_animals)
        


if __name__ == "__main__":
    main()