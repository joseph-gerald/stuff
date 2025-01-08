import random

klosser = 200

with open("test.txt", "a") as txt:
    txt.write(str(klosser) + "\n")

    for i in range(klosser):
        txt.write(f"{random.randint(1,200)} {random.randint(1,200)}\n")