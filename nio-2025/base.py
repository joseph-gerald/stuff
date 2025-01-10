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



# Code goes here

N = int(input())


if (dev):
    # write data to a file or something
    pass