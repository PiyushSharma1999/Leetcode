ops = ["5","-2","4","C","D","9","+","+"]
stack = []
res = 0
for i in ops:
    if i.isnumeric() or i.match("/^-\d+$/"):
        stack.append(int(i))
    elif i == "C" and len(stack) != 0:
        stack.pop()
    elif i == "D" and len(stack) != 0:
        stack.append(stack[-1]*2)
        res += stack[-1]
    elif i == "+" and len(stack) >=2:
        stack.append(stack[-1]+stack[-2])
        res += stack[-1]

for i in stack:
    res+=i

print(("-2").isnumeric())