import pygame
from Purchasables import *
from Player_and_Shop_Classes import *

#WINDOW DIMENSIONS
WIDTH = 1200
HEIGHT = 800
#NEWS = pygame.Rect((HEIGHT + 10), 30, (WIDTH - HEIGHT- 30), (HEIGHT / 3 - 15))
INVENTORY = pygame.Rect((HEIGHT + 10), (HEIGHT / 3 + 30), (WIDTH - HEIGHT - 30), (HEIGHT / 3 - 15))
SHOP = pygame.Rect((HEIGHT + 10), (HEIGHT / 3 * 2 + 30), (WIDTH - HEIGHT - 30), (HEIGHT / 3 - 15))
WIN = pygame.display.set_mode((WIDTH, HEIGHT))

#INITIALIZE PYGAME
pygame.init()
FPS = 60
player = Player("playername")
pygame.display.set_caption("Shop")

#COLORS
DARK_BROWN = (70, 40, 30)
BROWN = (185, 165, 130)
YELLOW = (235, 250, 200)
GREEN = (185, 250, 190)
CYAN = (140, 235, 245)
BLUE = (165, 195, 245)
MAGENTA = (240, 190, 230)
RED = (218, 119, 175)
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

shop = Shop()
shop.set_shop_stock()
stock = shop.get_shop_stock()

def create_shop_pages(stock):
    global pages
    pages = []
    stock_index = 0

    for items in stock:
        current_page = []

        while (len(current_page) < 5) and (stock_index < len(stock)):
            current_page.append(stock[stock_index])
            stock_index += 1

        if len(current_page) > 0:
            pages.append(current_page)


font = pygame.font.Font("freesansbold.ttf", 20)         #for shop items and prices
smallfont = pygame.font.Font("freesansbold.ttf", 15)    #for BUY/SELL/NEXT/BACK buttons



def display_shop_contents(page_index):
    current_page = pages[page_index]
    global line_spacing
    line_spacing = 25
    button_spacing = 10

    #NEXT BUTTON TEXT INFO
    global nexttext
    nexttext = smallfont.render("NEXT", True, "#000000")
    nexttextRect = nexttext.get_rect()
    global nexttextw 
    global nexttexth 
    nexttextw = nexttext.get_width()
    nexttexth= nexttext.get_height()

    #BACK BUTTON TEXT INFO
    global backtext
    backtext = smallfont.render("BACK", True, "#000000")
    backtextRect = backtext.get_rect()
    global backtextw 
    global backtexth 
    backtextw = backtext.get_width()
    backtexth= backtext.get_height()

    #NEXT/BACK BUTTON DIMENSIONS
    global NEXT
    global BACK
    NEXT = pygame.Rect((WIDTH - nexttextw - 40),        #NEXT X
                       (HEIGHT - 25),                   #NEXT Y
                       (nexttextw + 10),                #NEXT WIDTH
                       (nexttexth + 10))                #NEXT HEIGHT
    
    BACK = pygame.Rect((HEIGHT + 20),               #BACK X
                       (HEIGHT - 25),               #BACK Y
                       (backtextw + 10),            #BACK WIDTH
                       (backtexth + 10))            #BACK HEIGHT

    #CREATE NEXT/BACK BUTTONS
    pygame.draw.rect(WIN, BLUE, NEXT)
    pygame.draw.rect(WIN, BLUE, BACK)
    WIN.blit(nexttext, ((WIDTH - nexttextw - 35), (HEIGHT - 20)))
    WIN.blit(backtext, ((HEIGHT + 25), (HEIGHT - 20)))

    buy_buttons = []
    sell_buttons = []

    for item in current_page:

        #SHOP PRICE TEXT INFO / CREATION
        global shoptext
        shoptext = font.render(f"{item}: ${item.get_cost()} / ${item.get_sell_price()}", True, "#000000")
        shoptextRect = shoptext.get_rect()
        global shoptextw 
        global shoptexth 
        shoptextw = shoptext.get_width()
        shoptexth= shoptext.get_height()

        WIN.blit(shoptext, ((HEIGHT + 20), (HEIGHT / 3 * 2 + 20 + line_spacing)))

        #BUY BUTTON TEXT INFO
        buytext = smallfont.render("BUY", True, WHITE)
        buytextRect = buytext.get_rect()
        global buytextw 
        global buytexth
        buytextw = buytext.get_width()
        buytexth = buytext.get_height()

        #SELL BUTTON TEXT INFO
        selltext = smallfont.render("SELL", True, WHITE)
        selltextRect = selltext.get_rect()
        global selltextw
        global selltexth
        selltextw = selltext.get_width()
        selltexth = selltext.get_height()

        #CREATE BUY BUTTON
        global BUY
        BUY = pygame.Rect((HEIGHT + 35 + shoptextw),              #BUY X
                        (HEIGHT / 3 * 2 + 20 + line_spacing),     #BUY Y
                        (buytextw + 10),                          #BUY WIDTH
                        shoptexth)                                #BUY HEIGHT
        pygame.draw.rect(WIN, DARK_GREEN, BUY)
        WIN.blit(buytext, ((HEIGHT + 40 + shoptextw), (HEIGHT / 3 * 2 + 25 + line_spacing)))
        buy_buttons.append(BUY)

        #CREATE SELL BUTTON
        global SELL
        SELL = pygame.Rect((HEIGHT + 45 + shoptextw + buytextw),    #SELL X
                        (HEIGHT / 3 * 2 + 20 + line_spacing),       #SELL Y
                        (selltextw + 10),                           #SELL WIDTH
                        shoptexth)                                  #SELL HEIGHT
        pygame.draw.rect(WIN, RED, SELL)
        WIN.blit(selltext, ((HEIGHT + 50 + shoptextw + buytextw), (HEIGHT / 3 * 2 + 25 + line_spacing)))
        sell_buttons.append(SELL)
        
        line_spacing += 30          #increment line spacing for items in shop (new item = new line)

    global BUY0
    global BUY1
    global BUY2
    global BUY3
    global BUY4

    global SELL0
    global SELL1
    global SELL2
    global SELL3
    global SELL4

    #naming buy and sell buttons so they can be mapped to corresponding shop items
    BUY0 = buy_buttons[0]
    BUY1 = buy_buttons[1]
    BUY2 = buy_buttons[2]
    BUY3 = buy_buttons[3]
    BUY4 = buy_buttons[4]

    SELL0 = sell_buttons[0]
    SELL1 = sell_buttons[1]
    SELL2 = sell_buttons[2]
    SELL3 = sell_buttons[3]
    SELL4 = sell_buttons[4]

    buy_buttons = [BUY0, BUY1, BUY2, BUY3, BUY4]
    sell_buttons = [SELL0, SELL1, SELL2, SELL3, SELL4]


def clear_shop_page():
    #CREATE NEW SHOP WINDOW AND NEXT/BACK BUTTONS
    pygame.draw.rect(WIN, BROWN, SHOP)
    pygame.draw.rect(WIN, BLUE, NEXT)
    pygame.draw.rect(WIN, BLUE, BACK)
    WIN.blit(nexttext, ((WIDTH - nexttextw - 35), (HEIGHT - 20)))
    WIN.blit(backtext, ((HEIGHT + 25), (HEIGHT - 20)))



class Game():

    def __init__(self):
        pass

    def draw_window(self):

        #pygame.draw.rect(WIN, BROWN, NEWS)
        pygame.draw.rect(WIN, BROWN, INVENTORY)
        pygame.draw.rect(WIN, BROWN, SHOP)

        create_shop_pages(stock)
        display_shop_contents(0)
        
    def click(self):
        self.clicked = pygame.mouse.get_pressed()[0]    #i think this is the reason it works when you click
        self.mouse_pos = pygame.mouse.get_pos()         #and not when you release, but i can't get anything
        global page_index                               #else to work at all
        page_index = 0

        if NEXT.collidepoint(self.mouse_pos) and self.clicked == True:      #advance one page in shop

            if page_index < (len(pages) - 1):
                page_index += 1
            
            elif page_index == (len(pages) - 1):
                page_index = 0

            clear_shop_page()                           #erase current shop page
            display_shop_contents(page_index)           #display new page

        elif BACK.collidepoint(self.mouse_pos) and self.clicked == True:    #go back one page in shop

            if page_index > 0:
                page_index -= 1
            
            elif page_index == 0:
                page_index = (len(pages) - 1)

            clear_shop_page()                           #erase current shop page
            display_shop_contents(page_index)           #display new page

        elif BUY0.collidepoint(self.mouse_pos) and self.clicked == True:    #it understands what item0 is and how
            item0 = (pages[page_index])[0]                                  #much it costs, but actually buying it
            player.buy(item0)                                               #doesn't work and idk why
            print(player.get_inventory())
            print(player.get_money())

        elif BUY1.collidepoint(self.mouse_pos) and self.clicked == True:
            player.buy((pages[page_index])[1])

        elif BUY2.collidepoint(self.mouse_pos) and self.clicked == True:
            player.buy((pages[page_index])[2])

        elif BUY3.collidepoint(self.mouse_pos) and self.clicked == True:
            player.buy((pages[page_index])[3])

        elif BUY4.collidepoint(self.mouse_pos) and self.clicked == True:
            player.buy((pages[page_index])[4])

        elif SELL0.collidepoint(self.mouse_pos) and self.clicked == True:
            player.sell((pages[page_index])[0])

        elif SELL1.collidepoint(self.mouse_pos) and self.clicked == True:
            player.sell((pages[page_index])[1])

        elif SELL2.collidepoint(self.mouse_pos) and self.clicked == True:
            player.sell((pages[page_index])[2])

        elif SELL3.collidepoint(self.mouse_pos) and self.clicked == True:
            player.sell((pages[page_index])[3])

        elif SELL4.collidepoint(self.mouse_pos) and self.clicked == True:
            player.sell((pages[page_index])[4])

        pygame.display.update()

                    


    def render(self):
        self.draw_window()
        self.click()
        pygame.display.update()

#WIN.fill(LIGHT_BROWN)

game = Game()
player = Player("playername")

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

            elif event.type == pygame.MOUSEBUTTONDOWN:  #neither MOUSEBUTTONDOWN or MOUSEBUTTONUP
                game.click()                            #seem to do anything at all

            elif event.type == pygame.MOUSEBUTTONUP:
                game.click()

        
        #draw the screen every frame
        game.render()

    pygame.quit()

main()

