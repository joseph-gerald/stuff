dev = False

try:
    import requests

    dev = True

    dummydata = open("test.txt", "r").read().splitlines()
    dummydata.reverse()

    def input():
        return dummydata.pop()
except:
    pass

N, max_budsjett = map(int, input().split(" "))
høyder = list(map(int, input().split(" ")))

lengste_flate = -1

laveste = min(høyder)
høyeste = max(høyder)

høyde_range = høyeste - laveste + 1

priser = [[]] * høyde_range

for index, pris in enumerate(priser):
    mål = laveste + index

    mål_priser = priser[index] = list(map(lambda høyde: abs(mål - høyde), høyder))

    # print()
    # print("#"*20)
    # print("HØYDE MÅL", mål)
    # print("#"*20)
    # print()
    
    for i in range(len(mål_priser) - index):
        budsjett = max_budsjett
        local_lengste = -1
        for i2 in range(len(mål_priser) - index - i):
            pris_for_å_flatne = mål_priser[i2 + i]
            
            budsjett_post = budsjett - pris_for_å_flatne

            if (budsjett_post < 0):
                break

            # print("budsjett_post", budsjett_post)
            budsjett = budsjett_post
            
            if (lengste_flate < i2 + 1):
                lengste_flate = i2 + 1
        # print("local_lengste", local_lengste, local_lengste_index)

print("lengste_flate", lengste_flate)

print(priser)

if (dev):
    pass