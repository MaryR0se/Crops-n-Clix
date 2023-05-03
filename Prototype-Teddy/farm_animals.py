import pygame
import os
import random
#pygame.font.init()

#caption
#pygame.display.set_caption("Prototype 1-Mary!")
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
COW_PEN_IMG = pygame.image.load(os.path.join("Assets", "cows.png"))
COWS_PEN = pygame.transform.scale(COW_PEN_IMG, PEN_SIZE)
LLAMA_PEN_IMG = pygame.image.load(os.path.join("Assets", "llamas.png"))
LLAMA_PEN = pygame.transform.scale(LLAMA_PEN_IMG, PEN_SIZE)
BEAR_PEN_IMG = pygame.image.load(os.path.join("Assets", "bears.png"))
BEAR_PEN = pygame.transform.scale(BEAR_PEN_IMG, PEN_SIZE)
RHINO_PEN_IMG = pygame.image.load(os.path.join("Assets", "rhinos.png"))
RHINO_PEN = pygame.transform.scale(RHINO_PEN_IMG, PEN_SIZE)
MONKEY_PEN_IMG = pygame.image.load(os.path.join("Assets", "monkeys.png"))
MONKEY_PEN = pygame.transform.scale(MONKEY_PEN_IMG, PEN_SIZE)
PENGUIN_PEN_IMG = pygame.image.load(os.path.join("Assets", "penguins.png"))
PENGUIN_PEN = pygame.transform.scale(PENGUIN_PEN_IMG, PEN_SIZE)
#----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#FIX YEEN-TIGER
YEEN_PEN_IMG = pygame.image.load(os.path.join("Assets", "chickens.png"))
YEEN_PEN = pygame.transform.scale(YEEN_PEN_IMG, PEN_SIZE)
CAT_PEN_IMG = pygame.image.load(os.path.join("Assets", "chickens.png"))
CAT_PEN = pygame.transform.scale(CAT_PEN_IMG, PEN_SIZE)
TIGER_PEN_IMG = pygame.image.load(os.path.join("Assets", "chickens.png"))
TIGER_PEN = pygame.transform.scale(TIGER_PEN_IMG, PEN_SIZE)
#----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
SHARK_PEN_IMG = pygame.image.load(os.path.join("Assets", "sharks.png"))
SHARK_PEN = pygame.transform.scale(SHARK_PEN_IMG, PEN_SIZE)







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
COW_IMG = [
    pygame.image.load(os.path.join("Assets", "cow0.png")),
    pygame.image.load(os.path.join("Assets", "cow1.png"))
]
COWS = [
    pygame.transform.scale(COW_IMG[0], ANIMAL_SIZE)
]
ALPACA_IMG = [
    pygame.image.load(os.path.join("Assets", "alpaca0.png")),
    pygame.image.load(os.path.join("Assets", "alpaca1.png"))
]
ALPACAS = [
    pygame.transform.scale(ALPACA_IMG[0], ANIMAL_SIZE),
    pygame.transform.scale(ALPACA_IMG[1], ANIMAL_SIZE)
]
BEAR_IMG = [
    pygame.image.load(os.path.join("Assets", "bear0.png")),
    pygame.image.load(os.path.join("Assets", "bear1.png")),
    pygame.image.load(os.path.join("Assets", "bear2.png")),
    pygame.image.load(os.path.join("Assets", "bear3.png")),
    pygame.image.load(os.path.join("Assets", "bear4.png")),
    pygame.image.load(os.path.join("Assets", "bear5.png"))
]
BEARS = [
    pygame.transform.scale(BEAR_IMG[0], ANIMAL_SIZE),
    pygame.transform.scale(BEAR_IMG[1], ANIMAL_SIZE),
    pygame.transform.scale(BEAR_IMG[2], ANIMAL_SIZE),
    pygame.transform.scale(BEAR_IMG[3], ANIMAL_SIZE),
    pygame.transform.scale(BEAR_IMG[4], ANIMAL_SIZE),
    pygame.transform.scale(BEAR_IMG[5], ANIMAL_SIZE)
]
RHINO_IMG = [
    pygame.image.load(os.path.join("Assets", "rhino0.png")),
    pygame.image.load(os.path.join("Assets", "rhino1.png"))
]
RHINOS = [
    pygame.transform.scale(RHINO_IMG[0], ANIMAL_SIZE),
    pygame.transform.scale(RHINO_IMG[1], ANIMAL_SIZE)
]

MONKEY_IMG = [
    pygame.image.load(os.path.join("Assets", "monke0.png")),
    pygame.image.load(os.path.join("Assets", "monke1.png"))
]
MONKEYS = [
    pygame.transform.scale(MONKEY_IMG[0], ANIMAL_SIZE),
    pygame.transform.scale(MONKEY_IMG[1], ANIMAL_SIZE)
]
PENGUIN_IMG = [
    pygame.image.load(os.path.join("Assets", "penguin0.png")),
    pygame.image.load(os.path.join("Assets", "penguin1.png"))
]
PENGUINS = [
    pygame.transform.scale(PENGUIN_IMG[0], ANIMAL_SIZE),
    pygame.transform.scale(PENGUIN_IMG[1], ANIMAL_SIZE)
]
YEEN_IMG = [
    pygame.image.load(os.path.join("Assets", "hyena0.png")),
    pygame.image.load(os.path.join("Assets", "hyena1.png"))
]
YEENS = [
    pygame.transform.scale(YEEN_IMG[0], ANIMAL_SIZE),
    pygame.transform.scale(YEEN_IMG[1], ANIMAL_SIZE)
]
CAT_IMG = [
    pygame.image.load(os.path.join("Assets", "cat0.png")),
    pygame.image.load(os.path.join("Assets", "cat1.png"))
]
CATS = [
    pygame.transform.scale(CAT_IMG[0], ANIMAL_SIZE),
    pygame.transform.scale(CAT_IMG[0], ANIMAL_SIZE)
]
TIGER_IMG = [
    pygame.image.load(os.path.join("Assets", "tiger0.png")),
    pygame.image.load(os.path.join("Assets", "tiger1.png"))
]
TIGERS = [
    pygame.transform.scale(TIGER_IMG[0], ANIMAL_SIZE),
    pygame.transform.scale(TIGER_IMG[1], ANIMAL_SIZE)
]
SHARK_IMG = [
    pygame.image.load(os.path.join("Assets", "shark0.png")),
    pygame.image.load(os.path.join("Assets", "shark1.png")),
    pygame.image.load(os.path.join("Assets", "shark2.png")),
    pygame.image.load(os.path.join("Assets", "shark3.png"))
]
SHARKS = [
    pygame.transform.scale(SHARK_IMG[0], ANIMAL_SIZE),
    pygame.transform.scale(SHARK_IMG[1], ANIMAL_SIZE),
    pygame.transform.scale(SHARK_IMG[2], ANIMAL_SIZE),
    pygame.transform.scale(SHARK_IMG[3], ANIMAL_SIZE)
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
        if self.num_animals < 50:
            sprites = self.num_animals
        else:
            sprites = 50
        for i in range(sprites):
            rects.append((pygame.Rect(random.randint(ANIMALS.x + 20, ANIMALS.x + ANIMALS.width - 20 - ANIMAL_SIZE[0]), random.randint(ANIMALS.y + 20, ANIMALS.y + ANIMALS.height - 20 - ANIMAL_SIZE[1]), 50, 50), random.choice(self.animal_sprite)))
        rects = self.sort(rects)
        return rects

    def add_animal(self):
        self.num_animals += 1
        self.rectangles = self.shuffle()
    
    def sub_animal(self):
        if self.num_animals > 0:
            self.num_animals -= 1
        self.rectangles = self.shuffle()

    def sort(self, rects):
        for i in range(1, len(rects)):
            j = i
            while j > 0 and rects[j-1][0].y > rects[j][0].y:
                rects[j], rects[j - 1] = rects[j - 1], rects[j]
                j -= 1
        return rects





#current_animal_index = 0


class game:
    def __init__(self):
        #window
        self.WIDTH = 1200 #825
        self.HEIGHT = 800 #WIDTH / 1.61803398875 #thought a golden(-ish) rectangle would be cute here
        #self.WIN = pygame.display.set_mode((WIDTH, HEIGHT))
        #windows
        self.CROPS = pygame.Rect(10, 10, HEIGHT - 20, HEIGHT / 2 - 20)
        self.ANIMALS = pygame.Rect(10, HEIGHT / 2 + 30, HEIGHT - 20, HEIGHT / 2 - 20)
        self.NEWS = pygame.Rect(HEIGHT + 10, 10, WIDTH - HEIGHT - 20, HEIGHT / 3 - 20)
        self.INVENTORY = pygame.Rect(HEIGHT + 10, HEIGHT / 3 + 10, WIDTH - HEIGHT - 20, HEIGHT / 3 - 20)
        self.SHOP = pygame.Rect(HEIGHT + 10, HEIGHT / 3 * 2 + 10, WIDTH - HEIGHT - 20, HEIGHT / 3 - 20)

        #animal pens
        '''''''''
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
        '''''''''
        self.current_animal_index = 0
        self.num_chickens = 0
        self.num_geese = 0
        self.num_goats = 0
        self.num_pigs = 0
        self.num_sheep = 0
        self.num_cows = 0
        self.num_alpacas = 0
        self.num_bears = 0
        self.num_rhinos = 0
        self.num_monkeys = 0
        self.num_penguins = 0
        self.num_yeens = 0
        self.num_cats = 0
        self.num_tigers = 0
        self.num_sharks = 0

        chickens = Animal("chickens", CHICKEN_PEN, CHICKEN, self.num_chickens)
        geese = Animal("geese", GOOSE_PEN, GOOSE, self.num_geese)
        goats = Animal("goats", GOAT_PEN, GOAT, self.num_goats)
        pigs = Animal("pigs", PIG_PEN, PIG, self.num_pigs)
        sheep = Animal("sheep", SHEEP_PEN, SHEEP, self.num_sheep)
        cows = Animal("cows", COWS_PEN, COWS, self.num_cows)
        alpacas = Animal("lapacas", LLAMA_PEN, ALPACAS, self.num_alpacas)
        bears = Animal("bears", BEAR_PEN, BEARS, self.num_bears)
        rhinos = Animal("rhinos", RHINO_PEN, RHINOS, self.num_rhinos)
        monkeys = Animal("monkeys", MONKEY_PEN, MONKEYS, self.num_monkeys)
        penguins = (Animal("penguins", PENGUIN_PEN, PENGUINS, self.num_penguins ))
        yeens = Animal("hyeenas", YEEN_PEN, YEENS, self.num_yeens)
        cats = Animal("cats", CAT_PEN, CATS, self.num_cats)
        tigers = Animal("tigers", TIGER_PEN, TIGERS, self.num_tigers)
        sharks = Animal("sharks", SHARK_PEN, SHARKS, self.num_sharks)


        self.all_animals = [
            chickens,
            geese,
            goats,
            pigs,
            sheep,
            cows,
            alpacas,
            bears,
            rhinos,
            monkeys,
            penguins,
            yeens,
            cats,
            tigers,
            sharks
        ]
        self.current_animal = self.all_animals[self.current_animal_index]




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




    def draw_window(self):
        #WIN.fill(GREEN)

        #pygame.draw.rect(WIN, BROWN, CROPS)
        #pygame.draw.rect(WIN, BROWN, ANIMALS)
        #pygame.draw.rect(WIN, BROWN, NEWS)
        #pygame.draw.rect(WIN, BROWN, INVENTORY)
        #pygame.draw.rect(WIN, BROWN, SHOP)

        WIN.blit(self.current_animal.pen_sprite, (ANIMALS.x + 20, ANIMALS.y + 22.5))
        for rect in self.all_animals[self.current_animal_index].rectangles:
            WIN.blit(rect[1], (rect[0].x, rect[0].y))


        self.font = pygame.font.Font("freesansbold.ttf", 32)
        self.text = self.font.render(f"{(self.current_animal.name)}: {str(self.current_animal.num_animals)}", True, "#000000")
        #self.textRect = self.text.get_rect()
        WIN.blit(self.text, ((HEIGHT + 20), HEIGHT / 3 + 120))
        #print("Number of", self.current_animal.name, "is", self.current_animal.num_animals)

        #pygame.display.update()
    '''''''''
    def create_animals(self, num_chickens=0, num_geese=0, num_goats=0, num_pigs=0, num_sheep=0):
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
        
        chickens = Animal("chickens", CHICKEN_PEN, CHICKEN, num_chickens)
        geese = Animal("geese", GOOSE_PEN, GOOSE, num_geese)
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
        #return all_animals
        '''''''''
    '''''''''
    def update(self):
        #animal_index = 0
        current_animal = all_animals[self.current_animal_index]
        self.mouse_pos = pygame.mouse.get_pos()
        print(WIN)
        for self.event in pygame.event.get():
            if self.event.type == pygame.KEYDOWN:
                    if self.event.key == pygame.K_RIGHT: #later change to a click of an arrow icon on screen
                        self.current_animal_index = (self.current_animal_index + 1) % len(all_animals)
                        current_animal = all_animals[self.current_animal_index]
                        self.draw_window(current_animal)
                        print(current_animal.name)
                        print(self.current_animal_index)
                    if self.event.key == pygame.K_LEFT: #later change to a click of an arrow icon on screen
                        self.current_animal_index = (self.current_animal_index - 1) % len(all_animals)
                        current_animal = all_animals[self.current_animal_index]
                        self.draw_window(current_animal)
                        print(current_animal.name)
                        print(self.current_animal_index)
            if self.event.type == pygame.MOUSEBUTTONUP:
                if pygame.Rect(ANIMALS.x + 20, ANIMALS.y + 22.5, HEIGHT - 60, HEIGHT / 2 - 60).collidepoint(self.mouse_pos):
                    all_animals[self.current_animal_index].num_animals += 1
                    all_animals[self.current_animal_index].rectangles = all_animals[self.current_animal_index].shuffle
                print("hello")
        #self.draw_window(current_animal)
                #print(all_animals[current_animal_index].num_animals)
'''''''''


    def click(self):
        self.mouse_pos = pygame.mouse.get_pos()
        if pygame.Rect(ANIMALS.x + 20, ANIMALS.y + 22.5, HEIGHT - 60, HEIGHT / 2 - 60).collidepoint(self.mouse_pos):
            #if pygame.mouse.get_pressed()[0]:
            self.all_animals[self.current_animal_index].num_animals += 1
            #print("click")
            self.all_animals[self.current_animal_index].rectangles = self.all_animals[self.current_animal_index].shuffle()

    def keyR(self):
        #print("Key R")
        #if self.event.key == pygame.K_RIGHT: #later change to a click of an arrow icon on screen
        self.current_animal_index = (self.current_animal_index + 1) % len(self.all_animals)
        self.current_animal = self.all_animals[self.current_animal_index]
        self.draw_window()
        #print(self.current_animal.name)
        #print(self.current_animal_index)

    def keyL(self):
        #print("Key L")
        #if self.event.key == pygame.K_LEFT: #later change to a click of an arrow icon on screen
        self.current_animal_index = (self.current_animal_index - 1) % len(self.all_animals)
        self.current_animal = self.all_animals[self.current_animal_index]
        self.draw_window()
        #print(self.current_animal.name)
        #print(self.current_animal_index)

    def render(self, current_animal_index):
        all_animals = self.create_animals()
        current_animal = all_animals[current_animal_index]
        self.update(all_animals, current_animal, current_animal_index)
        self.draw_window(current_animal)
        #self.update(all_animals, current_animal)
        pygame.display.update()

#Initialize Pygame
#pygame.init()

#current_animal_index = 0
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
        


#if __name__ == "__main__":
#    main()