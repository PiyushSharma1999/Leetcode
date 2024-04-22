def carfleet(target, position, speed):
    pair = [[p, s] for p, s in zip(position, speed)]
    pair.sort(reverse=True)
    stack = []

    for p, s in pair:
        stack.append((target - p) / s)
        if len(stack) >= 2 and stack[-1] <= stack[-2]:
            stack.pop()
    print(len(stack))
    return len(stack)

target = 10
position = [6, 8]
speed = [3, 2]

print(carfleet(target, position, speed))