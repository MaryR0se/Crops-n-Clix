import pygame
import random
import makeBackground as B
#import fromAlex as A
import alex_prototype_2 as A
import fromMary as M
import Player_and_Shop_Classes as PSC
import Player_Class as PC

#Initialize Pygame
pygame.init()
game = A.Game()

#Determine FPS
FPS = 60
current_animal_index = 0

def render():
    global current_animal_index
    #B.draw.draw_window()
    A.game.draw_screen()
    A.game.update_game()
    A.game.click_button()
    all_animals = M.game().create_animals()
    current_animal = all_animals[current_animal_index]
    M.game().update(all_animals, current_animal, current_animal_index)
    M.game().draw_window(current_animal)
    pygame.display.update()



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
        B.draw.draw_window()
        #A.game.render()
        #M.game().render()
        render()

    pygame.quit()



if __name__ == "__main__":
    #M.main()
    #A.main()
    #B.main()
    main()


