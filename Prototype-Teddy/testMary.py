import pygame
import os
import random
pygame.font.init()

#caption
pygame.display.set_caption("Prototype 1-Mary!")
#window
WIDTH = 1200 #825
HEIGHT = 800 #WIDTH / 1.61803398875 #thought a golden(-ish) rectangle would be cute here
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
#primary colors
DARK_BROWN = ( 71,  43,  30)
BROWN = (186, 167, 131)
YELLOW = (235, 249, 201)
GREEN = (185, 251, 192)
CYAN = (142, 236, 245)
BLUE = (163, 196, 243)
MAGENTA = (241, 192, 232)
RED = (218, 119, 175)  #""""""red""""""
#frames per second (the one I chose is arbitrary)
FPS = 60
#windows
CROPS = pygame.Rect(10, 10, HEIGHT - 20, HEIGHT / 2 - 20)
ANIMALS = pygame.Rect(10, HEIGHT / 2 + 30, HEIGHT - 20, HEIGHT / 2 - 20)
NEWS = pygame.Rect(HEIGHT + 10, 10, WIDTH - HEIGHT - 20, HEIGHT / 3 - 20)
INVENTORY = pygame.Rect(HEIGHT + 10, HEIGHT / 3 + 10, WIDTH - HEIGHT - 20, HEIGHT / 3 - 20)
SHOP = pygame.Rect(HEIGHT + 10, HEIGHT / 3 * 2 + 10, WIDTH - HEIGHT - 20, HEIGHT / 3 - 20)
#animal pens
PEN_SIZE = (HEIGHT - 60, HEIGHT / 2 - 60)
CHICKEN_PEN_IMG = pygame.image.load(os.path.join("Assets", "chickens.png"))
CHICKEN_PEN = pygame.transform.scale(CHICKEN_PEN_IMG, PEN_SIZE)
GOOSE_PEN_IMG = pygame.image.load(os.path.join("Assets", "geese.png"))
GOOSE_PEN = pygame.transform.scale(GOOSE_PEN_IMG, PEN_SIZE)
GOAT_PEN_IMG = pygame.image.load(os.path.join("Assets", "goats.png"))
GOAT_PEN = pygame.transform.scale(GOAT_PEN_IMG, PEN_SIZE)
PIG_PEN_IMG = pygame.image.load(os.path.join("Assets", "pigs.png"))
PIG_PEN = pygame.transform.scale(PIG_PEN_IMG, PEN_SIZE)
SHEEP_PEN_IMG = pygame.image.load(os.path.join("Assets", "sheeps.png"))
SHEEP_PEN = pygame.transform.scale(SHEEP_PEN_IMG, PEN_SIZE)
#animal sprites
ANIMAL_SIZE = (100, 100)
CHICKEN_IMG = [
    pygame.image.load(os.path.join("Assets", "chicken0.png")),
    pygame.image.load(os.path.join("Assets", "chicken1.png"))
]
CHICKEN = [
    pygame.transform.scale(CHICKEN_IMG[0], ANIMAL_SIZE),
    pygame.transform.scale(CHICKEN_IMG[1], ANIMAL_SIZE)
]
GOOSE_IMG = [
    pygame.image.load(os.path.join("Assets", "goose0.png")),
    pygame.image.load(os.path.join("Assets", "goose1.png"))
]
GOOSE = [
    pygame.transform.scale(GOOSE_IMG[0], ANIMAL_SIZE),
    pygame.transform.scale(GOOSE_IMG[1], ANIMAL_SIZE)
]
GOAT_IMG = [
    pygame.image.load(os.path.join("Assets", "goat0.png")),
    pygame.image.load(os.path.join("Assets", "goat1.png"))
]
GOAT = [
    pygame.transform.scale(GOAT_IMG[0], ANIMAL_SIZE),
    pygame.transform.scale(GOAT_IMG[1], ANIMAL_SIZE)
]
PIG_IMG = [
    pygame.image.load(os.path.join("Assets", "pig0.png")),
    pygame.image.load(os.path.join("Assets", "pig1.png"))
]
PIG = [
    pygame.transform.scale(PIG_IMG[0], ANIMAL_SIZE),
    pygame.transform.scale(PIG_IMG[1], ANIMAL_SIZE)
]
SHEEP_IMG = [
    pygame.image.load(os.path.join("Assets", "sheep0.png")),
    pygame.image.load(os.path.join("Assets", "sheep1.png"))
]
SHEEP = [
    pygame.transform.scale(SHEEP_IMG[0], ANIMAL_SIZE),
    pygame.transform.scale(SHEEP_IMG[1], ANIMAL_SIZE)
]





    #def create_animals(self, num_chickens=0, num_geese=0, num_goats=0, num_pigs=0, num_sheep=0):
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
            rects.append((pygame.Rect(random.randint(ANIMALS.x + 20, ANIMALS.x + ANIMALS.width - 20 - ANIMAL_SIZE[0]), random.randint(ANIMALS.y + 20, ANIMALS.y + ANIMALS.height - 20 - ANIMAL_SIZE[1]), 50, 50), random.choice(self.animal_sprite)))
        rects = self.sort(rects)
        return rects

    def add_animal(self):
        self.num_animals += 1
        self.rectangles = self.shuffle()
    
    def sub_animal(self):
        self.num_animals -= 1
        self.rectangles = self.shuffle()

    def sort(self, rects):
        for i in range(1, len(rects)):
            j = i
            while j > 0 and rects[j-1][0].y > rects[j][0].y:
                rects[j], rects[j - 1] = rects[j - 1], rects[j]
                j -= 1
        return rects

#



#current_animal_index = 0


class game:
    def __init__(self):
        #window
        self.WIDTH = 1200 #825
        self.HEIGHT = 800 #WIDTH / 1.61803398875 #thought a golden(-ish) rectangle would be cute here
        #self.WIN = pygame.display.set_mode((WIDTH, HEIGHT))
        #windows
        self.CROPS = pygame.Rect(10, 10, self.HEIGHT - 20, self.HEIGHT / 2 - 20)
        self.ANIMALS = pygame.Rect(10, self.HEIGHT / 2 + 30, self.HEIGHT - 20, self.HEIGHT / 2 - 20)
        self.NEWS = pygame.Rect(self.HEIGHT + 10, 10, WIDTH - HEIGHT - 20, HEIGHT / 3 - 20)
        self.INVENTORY = pygame.Rect(HEIGHT + 10, HEIGHT / 3 + 10, WIDTH - HEIGHT - 20, HEIGHT / 3 - 20)
        self.SHOP = pygame.Rect(HEIGHT + 10, HEIGHT / 3 * 2 + 10, WIDTH - HEIGHT - 20, HEIGHT / 3 - 20)
        #animal pens
        self.PEN_SIZE = (HEIGHT - 60, HEIGHT / 2 - 60)
        self.CHICKEN_PEN_IMG = pygame.image.load(os.path.join("Assets", "chickens.png"))
        self.CHICKEN_PEN = pygame.transform.scale(CHICKEN_PEN_IMG, PEN_SIZE)
        self.GOOSE_PEN_IMG = pygame.image.load(os.path.join("Assets", "geese.png"))
        self.GOOSE_PEN = pygame.transform.scale(GOOSE_PEN_IMG, PEN_SIZE)
        self.GOAT_PEN_IMG = pygame.image.load(os.path.join("Assets", "goats.png"))
        self.GOAT_PEN = pygame.transform.scale(GOAT_PEN_IMG, PEN_SIZE)
        self.PIG_PEN_IMG = pygame.image.load(os.path.join("Assets", "pigs.png"))
        self.PIG_PEN = pygame.transform.scale(PIG_PEN_IMG, PEN_SIZE)
        self.SHEEP_PEN_IMG = pygame.image.load(os.path.join("Assets", "sheeps.png"))
        self.SHEEP_PEN = pygame.transform.scale(SHEEP_PEN_IMG, PEN_SIZE)
        #animal sprites
        self.ANIMAL_SIZE = (100, 100)
        self.CHICKEN_IMG = [
            pygame.image.load(os.path.join("Assets", "chicken0.png")),
            pygame.image.load(os.path.join("Assets", "chicken1.png"))
        ]
        self.CHICKEN = [
            pygame.transform.scale(CHICKEN_IMG[0], ANIMAL_SIZE),
            pygame.transform.scale(CHICKEN_IMG[1], ANIMAL_SIZE)
        ]
        self.GOOSE_IMG = [
            pygame.image.load(os.path.join("Assets", "goose0.png")),
            pygame.image.load(os.path.join("Assets", "goose1.png"))
        ]
        self.GOOSE = [
            pygame.transform.scale(GOOSE_IMG[0], ANIMAL_SIZE),
            pygame.transform.scale(GOOSE_IMG[1], ANIMAL_SIZE)
        ]
        self.GOAT_IMG = [
            pygame.image.load(os.path.join("Assets", "goat0.png")),
            pygame.image.load(os.path.join("Assets", "goat1.png"))
        ]
        self.GOAT = [
            pygame.transform.scale(GOAT_IMG[0], ANIMAL_SIZE),
            pygame.transform.scale(GOAT_IMG[1], ANIMAL_SIZE)
        ]
        self.PIG_IMG = [
            pygame.image.load(os.path.join("Assets", "pig0.png")),
            pygame.image.load(os.path.join("Assets", "pig1.png"))
        ]
        self.PIG = [
            pygame.transform.scale(PIG_IMG[0], ANIMAL_SIZE),
            pygame.transform.scale(PIG_IMG[1], ANIMAL_SIZE)
        ]
        self.SHEEP_IMG = [
            pygame.image.load(os.path.join("Assets", "sheep0.png")),
            pygame.image.load(os.path.join("Assets", "sheep1.png"))
        ]
        self.SHEEP = [
            pygame.transform.scale(SHEEP_IMG[0], ANIMAL_SIZE),
            pygame.transform.scale(SHEEP_IMG[1], ANIMAL_SIZE)
        ]
    def draw_window(self, current_animal):
        WIN.fill(GREEN)

        pygame.draw.rect(WIN, BROWN, CROPS)
        pygame.draw.rect(WIN, BROWN, ANIMALS)
        pygame.draw.rect(WIN, BROWN, NEWS)
        pygame.draw.rect(WIN, BROWN, INVENTORY)
        pygame.draw.rect(WIN, BROWN, SHOP)

        WIN.blit(current_animal[1], (ANIMALS.x + 20, ANIMALS.y + 22.5))
        for rect in range(current_animal[4]):
            WIN.blit(rect[1], (rect[0].x, rect[0].y))


        #pygame.display.update()

    def shuffle(animal):
        rects = []
        for i in range(animal[3]):
            rects.append((pygame.Rect(random.randint(ANIMALS.x + 20, ANIMALS.x + ANIMALS.width - 20 - ANIMAL_SIZE[0]), random.randint(ANIMALS.y + 20, ANIMALS.y + ANIMALS.height - 20 - ANIMAL_SIZE[1]), 50, 50), random.choice(animal[2])))
        rects = animal.sort(rects)
        return rects

    def add_animal(animal):
        animal[3] += 1
        animal.shuffle()
    
    def sub_animal(animal):
        animal[3] -= 1
        animal.shuffle()

    def sort(rects):
        for i in range(1, len(rects)):
            j = i
            while j > 0 and rects[j-1][0].y > rects[j][0].y:
                rects[j], rects[j - 1] = rects[j - 1], rects[j]
                j -= 1
        return rects


    def create_animals(self, num_chickens=0, num_geese=0, num_goats=0, num_pigs=0, num_sheep=0):
        #animal class
        '''''''''
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
                    rects.append((pygame.Rect(random.randint(ANIMALS.x + 20, ANIMALS.x + ANIMALS.width - 20 - ANIMAL_SIZE[0]), random.randint(ANIMALS.y + 20, ANIMALS.y + ANIMALS.height - 20 - ANIMAL_SIZE[1]), 50, 50), random.choice(self.animal_sprite)))
                rects = self.sort(rects)
                return rects

            def add_animal(self):
                self.num_animals += 1
                self.rectangles = self.shuffle()
            
            def sub_animal(self):
                self.num_animals -= 1
                self.rectangles = self.shuffle()

            def sort(self, rects):
                for i in range(1, len(rects)):
                    j = i
                    while j > 0 and rects[j-1][0].y > rects[j][0].y:
                        rects[j], rects[j - 1] = rects[j - 1], rects[j]
                        j -= 1
                return rects

        chickens = Animal("chickens", CHICKEN_PEN, CHICKEN, num_chickens)
        geese = Animal("chickens", GOOSE_PEN, GOOSE, num_geese)
        goats = Animal("goats", GOAT_PEN, GOAT, num_goats)
        pigs = Animal("pigs", PIG_PEN, PIG, num_pigs)
        sheep = Animal("sheep", SHEEP_PEN, SHEEP, num_sheep)

        all_animals = [
            chickens,
            geese,
            goats,
            pigs,
            sheep
        ]
        '''''''''
        chickens = ["chickens", CHICKEN_PEN, CHICKEN, 0, 0]
        geese = ["chickens", GOOSE_PEN, GOOSE, 0, 0]
        goats = ["goats", GOAT_PEN, GOAT, 0, 0]
        pigs = ["pigs", PIG_PEN, PIG, 0, 0]
        sheep = ["sheep", SHEEP_PEN, SHEEP, 0, 0]

        all_animals = [
            chickens,
            geese,
            goats,
            pigs,
            sheep
        ]
        return all_animals
    
    def update(self, all_animals, current_animal, current_animal_index):
        #current_animal_index = 0
        current_animal = all_animals[current_animal_index]
        self.mouse_pos = pygame.mouse.get_pos()
        for self.event in pygame.event.get():
            if self.event.type == pygame.KEYDOWN:
                    if self.event.key == pygame.K_RIGHT: #later change to a click of an arrow icon on screen
                        current_animal_index = (current_animal_index + 1) % len(all_animals)
                        print(current_animal.name)
                    if self.event.key == pygame.K_LEFT: #later change to a click of an arrow icon on screen
                        current_animal_index = (current_animal_index - 1) % len(all_animals)
                        print(current_animal.name)
            if self.event.type == pygame.MOUSEBUTTONUP:
                #if pygame.Rect(740, 340, 30, 440).collidepoint(self.mouse_pos):
                all_animals[current_animal_index][3] += 1
                all_animals[current_animal_index][4] = all_animals[current_animal_index][4].shuffle(all_animals[current_animal_index])
                #print(all_animals[current_animal_index].num_animals)

    def render(self, current_animal_index):
        all_animals = self.create_animals()
        current_animal = all_animals[current_animal_index]
        self.update(all_animals, current_animal, current_animal_index)
        self.draw_window(current_animal)
        #self.update(all_animals, current_animal)
        pygame.display.update()

#Initialize Pygame
pygame.init()

current_animal_index = 0
def main():
    clock = pygame.time.Clock()
    run = True

    while run:
        clock.tick(FPS)

        #current_animal = all_animals[current_animal_index]
        #draw_window(current_animal)

        for event in pygame.event.get():
            if event.type == pygame.QUIT: #Without this, the x button doesn't work!!
                run = False
                
        global current_animal_index
        game().render(current_animal_index)

    pygame.quit()

''''''''' 
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT: #later change to a click of an arrow icon on screen
                    current_animal_index = (current_animal_index + 1) % len(all_animals)
                    #print(current_animal.name)
                if event.key == pygame.K_LEFT: #later change to a click of an arrow icon on screen
                    current_animal_index = (current_animal_index - 1) % len(all_animals)
                    #print(current_animal.name)
            if event.type == pygame.MOUSEBUTTONUP:
                if SHOP.collidepoint(SHOP.x, SHOP.y):
                    current_animal.add_animal()
                    '''''''''
                    #print(all_animals[0].num_animals)
        


if __name__ == "__main__":
    main()