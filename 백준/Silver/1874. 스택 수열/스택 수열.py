count = int(input())
stack, now, result = [], 1, []

for _ in range(count):
    num = int(input())
    while now <= num:
        stack.append(now)
        now += 1
        result.append('+')
    if stack[-1] == num:
        stack.pop()
        result.append('-')
    else:
        result = ['NO']
        break

print('\n'.join(result))