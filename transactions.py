def buy(vallet_id, x):
    user_info = get_user_info(vallet_id)

    amount = int(user_info[1])
    user_coins = int(user_info[2])
    coins_left = int(user_info[3])

    coin_price = calculate_price(coins_left)

    pay = coin_price * x


    if amount >= pay:
        amount -= pay
        user_coins += x
        coins_left -= x

        with open("users.txt", "r") as f:
            scan_count = 0

            users = f.readlines()
            for user in users:
                user_data = user.split(";")
                if vallet_id == user_data[0]:
                    users.pop(scan_count)
                
                scan_count += 1


        with open("users.txt", "w") as f:
            f.write(f"{vallet_id};{amount};{user_coins};{coins_left}")
    
def buy_all(vallet_id):
    user_info = get_user_info(vallet_id)

    amount = int(user_info[1])
    coins_left = int(user_info[3])

    coin_price = calculate_price(coins_left)
    while amount >= coin_price:
        user_info = get_user_info(vallet_id)

        user_coins = int(user_info[2])
        amount = int(user_info[1])
        coins_left = int(user_info[3])

        coin_price = calculate_price(coins_left)

        user_coins += 1
        amount -= coin_price
        coins_left -= 1

        with open("users.txt", "w") as f:
            f.write(f"{vallet_id};{amount};{user_coins};{coins_left}")


def sell(vallet_id):
    user_info = get_user_info(vallet_id)

    amount = int(user_info[1])
    user_coins = int(user_info[2])
    coins_left = int(user_info[3])

    coin_price = calculate_price(coins_left)

    receive = coin_price * user_coins

    coins_left += user_coins
    user_coins = 0
    amount += receive
        

    with open("users.txt", "r") as f:
        scan_count = 0

        users = f.readlines()
        for user in users:
            user_data = user.split(";")
            if vallet_id == user_data[0]:
                users.pop(scan_count)
            
            scan_count += 1

    with open("users.txt", "w") as f:
        f.write(f"{vallet_id};{amount};{user_coins};{coins_left}")


def refresh_user_info(vallet_id):
    with open("users.txt", "r") as f:
        users = f.readlines()
        for user in users:
            user_data = user.split(";")
            if vallet_id == user_data[0]:
                return user_data
            

    
def calculate_price(coins_left):
    if coins_left > 0:
        coin_price = 100000 / coins_left 

        search_dot = str(coin_price).find(".")
            
        if search_dot:
            price_arr = str(coin_price).split(".")
            coin_price = int(price_arr[0])
        
        return coin_price


def get_user_info(vallet_id):
    scan_count = 0

    with open("users.txt", "r") as f:
        users = f.readlines()

        for user in users:
            user_data = user.split(";")


            if vallet_id == user_data[0]:
                return user_data
            
            scan_count += 1