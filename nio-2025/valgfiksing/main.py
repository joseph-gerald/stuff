import math

# make so that contest server won't load dummy data

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

N = int(input())

folk = [[-1]]

for i in range(N-1):
    sjef = int(input())

    folk.append([sjef])

folk_copy = folk.copy()

for i in range(N):
    julegave, bestikk = input().split(" ")
    
    folk[i].append(julegave)
    folk[i].append(int(bestikk))

for index, person in enumerate(folk):
    if (index == 0): continue
    folk[person[0]].append(index)

def få_hierarki(person):
    return {
        "person": person,
        "under": list(map(lambda index: få_hierarki(folk[index]), person[3:]))
    }

def finn_stemme(hierarki_obj: dict):
    person: dict
    under: list
    person, under = hierarki_obj.values()

    g_stemmer, s_stemmer = 0, 0
    stemme = None

    for underordnet in under:
        personlig_stemme = finn_stemme(underordnet)

        if personlig_stemme == "G":
            g_stemmer += 1
        else:
            s_stemmer += 1
    
    if person[1] == "G":
        g_stemmer += 1
    else:
        s_stemmer += 1

    if (g_stemmer == s_stemmer):
        stemme = person[1]
    else:
        stemme = "G" if g_stemmer > s_stemmer else "S"

    hierarki_obj["g_stemmer"] = g_stemmer
    hierarki_obj["s_stemmer"] = s_stemmer
    hierarki_obj["og_stemme"] = person[1]
    hierarki_obj["stemme"] = stemme
    hierarki_obj["bribe"] = person[2]
    return stemme

def bestikk(hierarki_obj: dict):
    person: list
    under: list
    person, under, g_stemmer, s_stemmer, og_stemme, stemme, bribe = hierarki_obj.values()
    bestikk_mengde = 0

    if (len(under) == 0):
        if (stemme == "G"): bestikk_mengde = bribe
    else:
        bestikk_trengt = math.ceil((g_stemmer - s_stemmer) / 2)
        # print("bestikk_trengt", bestikk_trengt)
        under.sort(key=lambda ansatt: bestikk(ansatt))
        bestikk_mengder = list(map(lambda ansatt: ansatt["bestikk_total"], under))
        bestikk_mengder = [i for i in bestikk_mengder if i != 0]
        index_of_leader = 9999999

        if og_stemme == "G":
            bestikk_mengder += [bribe]

            index_of_leader = bestikk_mengder.index(bribe)

        tie_break_needed = (g_stemmer - bestikk_trengt) - (s_stemmer + bestikk_trengt) == 0 and og_stemme == "G" and index_of_leader > bestikk_trengt

        if tie_break_needed:
            bestikk_trengt += 1
            # print("TIE BREAK NEEDED")

        bestikk_mengder.sort()
        # print(bestikk_mengder)

        if (bestikk_trengt == 0 and hierarki_obj["stemme"] == "G"):
            bestikk_trengt = 1

        while bestikk_trengt > 0:
            bestikk_størelse = bestikk_mengder[0]

            bestikk_mengde += bestikk_mengder.pop()
            bestikk_trengt -= 1
            # print("PAID", bestikk_mengder[i])

            #hierarki_obj["s_stemmer"] += 1
            #hierarki_obj["g_stemmer"] -= 1

        hierarki_obj["bestikk_trengt"] = bestikk_trengt

    del hierarki_obj["person"]
        
    hierarki_obj["bestikk_total"] = bestikk_mengde

    return bestikk_mengde

hierarki = få_hierarki(folk[0])

stemme = finn_stemme(hierarki)
bestikk = bestikk(hierarki)

print(bestikk)

if (dev):
    import json

    with open("test.json", "w") as txt:
        txt.write(json.dumps(hierarki))