def login(TOTAL_COINS):
    with open("users.txt", "r") as f:
        users = f.readlines()
        if len(users) > 0:
            u = users[0].split(";")
            return u
    
        else:
            vallet = input("Enter Your vallet id: ")

            with open("users.txt", "w") as f:
                f.write(f"{vallet};{5000};{0};{TOTAL_COINS}")
                
            return [vallet, 5000, 0, TOTAL_COINS]