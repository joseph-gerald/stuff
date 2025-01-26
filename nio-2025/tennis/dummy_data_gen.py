import random

game_duration = 20_000
variations = 200

game = ""

for i in range(game_duration):
    game += random.choice("AB")

print(game)

with open("test.txt", "a") as txt:
    txt.write(f"{game_duration} {variations}\n")
    
    txt.write(game + "\n")

    for i in range(variations):
        txt.write(f"{random.randint(1, game_duration)} {random.randint(1, game_duration)}\n")