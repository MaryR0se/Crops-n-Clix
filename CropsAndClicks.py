import pygame
import random
import makeBackground as B
#import fromAlex as A
import plants as A
import farm_animals as M
#import Player_and_Shop_Classes as PSC
#import Player_Class as PC

#Initialize Pygame
pygame.init()
game = A.Game()
mgame = M.game()

#Determine FPS
FPS = 60
#current_animal_index = 0





#run game
def main():
    #Create Clock and run game
    clock = pygame.time.Clock()
    run = True

    #All_animals = mgame.create_animals()
    
    def render():
        #global current_animal_index
        #B.draw.draw_window()
        A.game.draw_screen()
        A.game.update_game()
        A.game.click_button()
        mgame.draw_window()
        #mgame.unlock()
        #mgame.update(All_animals)
        #mgame.click()
        pygame.display.update()
    

    #runs the game
    while run:

        #makes it run at the desired frame rate
        clock.tick(FPS)

        #closes game if window is closed
        #print(len(pygame.event.get()))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT: #later change to a click of an arrow icon on screen
                    mgame.keyR()
                if event.key == pygame.K_LEFT: #later change to a click of an arrow icon on screen  
                    mgame.keyL()              
            if event.type == pygame.MOUSEBUTTONUP:
                mgame.click()

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


