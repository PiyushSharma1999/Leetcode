import math

piles = [3, 6, 7, 11]
h = 8

def kokoEatB(piles, h):
    l, r = 1, max(piles)
    res = r

    while l <= r:
        k = (l + r) // 2
        hours = 0
        for p in piles:
            hours += math.ceil(float(p) / k)

        if hours <= h:
            res = k
            r = k - 1
        else:
            l = k + 1

    return res

print(kokoEatB(piles, h))
            


