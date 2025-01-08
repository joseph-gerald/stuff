# make so that contest server won't load dummy data

try:
    import requests

    dummydata = open("test.txt", "r").read().splitlines()
    dummydata.reverse()

    def input():
        return dummydata.pop()
except:
    pass

N = int(input())

klosse_grupper = {}

for i in range(N):
    høyde, bredde = map(int, input().split())
    
    if (bredde - 1 not in klosse_grupper): klosse_grupper[bredde - 1] = []
    klosse_grupper[bredde - 1].append(høyde)

total_høyde = 0

for gruppe in klosse_grupper.values():
    if (len(gruppe) == 0): continue
    total_høyde += max(gruppe)

print(total_høyde)