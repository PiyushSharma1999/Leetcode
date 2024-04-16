tempr = [73,74,75,71,69,72,76,73]

def dailyTempratures(tempr):
    res = [0] * len(tempr)
    stack = []

    for i, t in enumerate(tempr):
        while stack and t > stack[-1][0]:
            stackT, stackInd = stack.pop()
            res[stackInd] = (i - stackInd)
        stack.append([t, i])
    return res


print(dailyTempratures(tempr))

