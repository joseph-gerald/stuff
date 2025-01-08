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

