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
N, Q = map(int, input().split(" "))
S = input()

forslag = []

for i in range(Q):
    forslag.append(list(map(int, input().split(" "))) + [0,0,(0,0), False])
    # [K, M, S1s, S2s, S1p, S2p]
    # K = poeng trengt
    # M = set trengt

    # S1s = Spiller 1 sets vunnet
    # S2s = Spiller 2 sets vunnet

    # Poeng Skip Tuple
    
    # Ferdig = Stop

poeng_a = 0
poeng_b = 0

calculerte_poeng = [(0, 0)]

for char in S:
    last_a, last_b = calculerte_poeng[-1]
    calculerte_poeng.append((last_a + (char == 'A'), last_b + (char == 'B')))

for et_forslag in forslag:
    K, M, S1s, S2s, skip_tuple, ferdig = et_forslag
    S1p, S2p = skip_tuple

    for i in range(len(S)):
        S1_poeng, S2_poeng = calculerte_poeng[i+1]
        S1_poeng -= S1p
        S2_poeng -= S2p

        if S1_poeng >= K or S2_poeng >= K:
            delta_poeng = S1_poeng - S2_poeng
            if abs(delta_poeng) >= 2:
                if delta_poeng > 0:
                    S1s += 1
                else:
                    S2s += 1
                
                S1p, S2p = calculerte_poeng[i+1]
                
                if S1s >= M or S2s >= M:
                    et_forslag[2:] = [S1s, S2s, (S1p, S2p), True]
                    break
    
    if not et_forslag[5]:
        print("X")
    else:
        print("A" if et_forslag[2] > et_forslag[3] else "B", sum(et_forslag[4]))