n = 3

def generateParanthesis(n):

    stack = []
    res = []

    def backtrack(openN, closedN):
        print("openN: ",openN," ", "closedN: ",closedN)
        if openN == closedN == n:
            res.append("".join(stack))

        if openN < n:
            stack.append("(")
            backtrack(openN + 1, closedN)
            stack.pop()
        
        if closedN < openN:
            stack.append(")")
            
            backtrack(openN, closedN + 1)
            print("closedN < openN, ","openN: ", openN, "closedN: ",closedN)
            stack.pop()
    
    backtrack(0, 0)
    return res

print(generateParanthesis(n))