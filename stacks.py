ops = ["5","-2","4","C","D","9","+","+"]
stack = []
res = 0
temp = 0
for i in ops:
    if i == "C" and len(stack) != 0:
        stack.pop()
    elif i == "D" and len(stack) != 0:
        stack.append(stack[-1]*2)
        
    elif i == "+" and len(stack) >=2:
        stack.append(stack[-1]+stack[-2])
        
    else:
        stack.append(int(i))

for i in stack:
    res+=i

print(res)