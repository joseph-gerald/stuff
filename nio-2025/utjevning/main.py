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

    venstre = 0
    høyre = 1

    # print()
    # print("#"*20)
    # print("HØYDE MÅL", mål)
    # print("#"*20)
    # print()
    
    for i in range(len(mål_priser) - index):
        budsjett = max_budsjett

        while høyre < len(mål_priser):
            total = sum(mål_priser[venstre:høyre])
            
            if (total <= max_budsjett):
                høyre += 1
            else:
                venstre += 1

            lengde = høyre - venstre
            print("□"*lengde)

        # print("local_lengste", local_lengste, local_lengste_index)

lengste_flate = høyre - venstre + 1
print(lengste_flate)
#print(priser)

if (dev):
    pass