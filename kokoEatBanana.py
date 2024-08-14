import math

piles = [1, 4, 3, 2]
h = 9

def kokoEatBanana(piles, h):
    l, r = 1, max(piles)
    res = r

    while l<=r:
        hours = 0
        k = (l + r)//2
        for p in piles:
            hours += math.ceil(p / k)
            if hours <= h:
                l = k + 1
            