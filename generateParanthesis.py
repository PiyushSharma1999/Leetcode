n = 3

def generateParanthesis(n):

    stack = []
    res = []

    def backtrack(openN, closedN):
        print("openN: ",openN," ", "closedN: ",closedN)
        if openN == closedN == n:
            res.append("".join(stack))

        if openN < n:
            print("openN < n, ","openN: ", openN, "n: ",n, "closedN: ",closedN)
            stack.append("(")
            print(stack)
            backtrack(openN + 1, closedN)
            print("openN < n, ","openN: ", openN, "closedN: ",closedN)
            stack.pop()
            print(stack)
        
        if closedN < openN:
            print("closedN < openN, ","openN: ", openN, "closedN: ",closedN)
            stack.append(")")
            print(stack)
            backtrack(openN, closedN + 1)
            print("closedN < openN, ","openN: ", openN, "closedN: ",closedN)
            stack.pop()
            print(stack)
    
    backtrack(0, 0)
    return res

print(generateParanthesis(n))