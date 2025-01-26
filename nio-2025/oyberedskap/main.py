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

antall_øyer, antall_bruer, antall_instruksjoner = map(int, input().split(" "))

øyer = []

for i in range(antall_øyer):
    øyer.append({
        "år": int(input()),
        "til": [],
        "vannannlegg": False
    })

for i in range(antall_bruer):
    index_fra, index_til = map(int, input().split(" "))
    øyer[index_fra]["til"].append(index_til)
    øyer[index_til]["til"].append(index_fra)

def finn_vannannlegg(øy, øyer_gått_gjenom=[]):
    if øyer[øy]["vannannlegg"]:
        print("BRUH")
        return øyer[øy]["år"]

    for nabo in øyer[øy]["til"]:
        if nabo not in øyer_gått_gjenom:
            øyer_gått_gjenom.append(nabo)
            if finn_vannannlegg(nabo, øyer_gått_gjenom):
                return øyer[øy]["år"] + 1

    return -1

for i in range(antall_instruksjoner):
    instruksjon, øy = input().split(" ")
    øy = int(øy)

    if instruksjon == "!":
        øyer[øy]["vannannlegg"] = True
    else:
        år_til_ingen_vann = finn_vannannlegg(øy, [])

        print(år_til_ingen_vann)




if (dev):
    # write data to a file or something
    pass