import pygame
import random

from transactions import buy, sell, refresh_user_info, calculate_price

def set_up(vallet_id):
    user_data = refresh_user_info(vallet_id)
    vallet_id, ammount, crypto_count, total_coins = user_data[0], user_data[1], user_data[2], user_data[3]
    price = calculate_price(int(total_coins))

    pygame.init()
    width, height = 800, 500
    

    WHITE = (255, 255, 255)
    BLACK = (0, 0, 0)
    SMALL_FONT = pygame.font.Font("freesansbold.ttf", 20)
    LARGE_FONT = pygame.font.Font("freesansbold.ttf", 30)

    sell_btn = pygame.Rect(300, 200, 100, 100)
    buy_btn = pygame.Rect(500, 200, 100, 100)

    sell_btn_text = LARGE_FONT.render("SELL", True, BLACK, WHITE)
    buy_btn_text = LARGE_FONT.render("BUY", True, BLACK, WHITE)

    #ACTIVE_IMAGE = get_random_image()
    WALL_STREET_IMAGE = pygame.image.load("images/wall-street.jpg")

    while True:
        screen = pygame.display.set_mode([width, height])
        pygame.display.set_caption("Crypto trader")

        screen.fill(WHITE)

        vallet_text = SMALL_FONT.render(f"{vallet_id}", True, BLACK, WHITE)
        amount_text = SMALL_FONT.render(f"{ammount}$", True, BLACK, WHITE)
        crypto_text = SMALL_FONT.render(f"{crypto_count}", True, BLACK, WHITE)
        price_text = SMALL_FONT.render(f"{price}", True, BLACK, WHITE)

        pygame.draw.rect(screen, BLACK, sell_btn)
        pygame.draw.rect(screen, BLACK, buy_btn)
    
        screen.blit(sell_btn_text, [300, 200])
        screen.blit(buy_btn_text, [500, 200])

        screen.blit(price_text, [350, 100])
        screen.blit(vallet_text, [300, 10])
        screen.blit(amount_text, [350, 10])
        screen.blit(crypto_text, [450, 10])

        screen.blit(WALL_STREET_IMAGE, [200, 330])
        #screen.blit(ACTIVE_IMAGE, [-200, 0])
    
        for event in pygame.event.get():
    
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    if sell_btn.collidepoint(event.pos):
                        sell(vallet_id)

                        user_data = refresh_user_info(vallet_id)
                        vallet_id, ammount, crypto_count, total_coins = user_data[0], user_data[1], user_data[2], user_data[3]
                        price = calculate_price(int(total_coins))

                        #ACTIVE_IMAGE = get_random_image()

                    elif buy_btn.collidepoint(event.pos):
                        buy(vallet_id, 1)

                        user_data = refresh_user_info(vallet_id)
                        vallet_id, ammount, crypto_count, total_coins = user_data[0], user_data[1], user_data[2], user_data[3]
                        price = calculate_price(int(total_coins))

                        #ACTIVE_IMAGE = get_random_image()

            pygame.display.update()

def get_random_image():
    ROADSTER_IMAGE = pygame.image.load("images/roadster.jpg")
    STOCKS_IMAGE = pygame.image.load("images/stocks.jpg")
    STOCKS_UP_IMAGE = pygame.image.load("images/stocks-up.jpg")
    HELP_IMAGE = pygame.image.load("images/help.jpg")

    images = [
        ROADSTER_IMAGE,
        STOCKS_IMAGE,
        STOCKS_UP_IMAGE,
        HELP_IMAGE
    ]

    rand_image_index = random.randint(0,2)

    return images[3]