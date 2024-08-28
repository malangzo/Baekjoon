# 백준 1406번 문제 풀이

import sys

input = sys.stdin.readline

stack1 = list(input().strip())
stack2 = []

for _ in range(int(input())):
    command = input().split()

    if command[0] == 'L' and stack1:
        stack2.append(stack1.pop())
    
    elif command[0] == 'D' and stack2:
        stack1.append(stack2.pop())
    
    elif command[0] == 'B' and stack1:
        stack1.pop()
    
    elif command[0] == 'P':
        stack1.append(command[1])

result = stack1 + stack2[::-1]

print(''.join(result))
