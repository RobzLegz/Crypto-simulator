import random


def mine():
    mineable_cryptos = random.randint(0,10)

    mine_cryptos = input("How many cryptos You want to mine? ")

    if int(mine_cryptos) <= int(mineable_cryptos):
        with open("users.txt", "r") as f:
            users = f.readlines()
            if len(users) > 0:
                for u in users:
                    u = str(u).split(";")

                    cryptos = int(u[2])
                    cryptos += int(mine_cryptos)

                    cryptos_left = int(u[3]) - cryptos

                    with open("users.txt", "w") as f:
                        f.write(f"{u[0]};{u[1]};{cryptos};{cryptos_left}")
            else:
                from simulator import start_game
                start_game()

        
        from simulator import start_game
        start_game()
    else:
        print("You can't mine that many cryptos!")
        print("")
        from simulator import start_game
        start_game()

mine()

