from auth import login
from setup import set_up as play


def start_game():
    TOTAL_COINS = 5000

    user_data = login(TOTAL_COINS)
    vallet_id = user_data[0]

    play(vallet_id)

start_game()