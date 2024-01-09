
def bytify(input):
    return divmod(input, 256)
    
def flatten(xss):
    return [x for xs in xss for x in xs]

def chunkify(list, size):
    return [list[x:x+size] for x in range(0, len(list), size)]