# 백준 1406번 문제 풀이

import sys

input = sys.stdin.readline # 빠른 입력 처리를 위한 함수 사용

stack1 = list(input().strip()) # 커서 왼쪽 문자들 저장, 개행 문자 포함되므로 제거
stack2 = [] # 커서 오른쪽 문자들 저장

for _ in range(int(input())): # 입력된 명령어의 개수만큼 반복
    command = input().split() # 명령어를 입력받고, 공백 기준으로 분리해 리스트로 저장

    # 커서 왼쪽 이동
    # stack1이 있을 경우, 가장 오른쪽 문자(마지막 요소)를 리스트에서 제거 후 stack2에 추가
    if command[0] == 'L' and stack1:
        stack2.append(stack1.pop())
    
    # 커서 오른쪽 이동
    # 왼쪽 이동의 반대로 실행
    elif command[0] == 'D' and stack2:
        stack1.append(stack2.pop())
    
    # 커서 왼쪽 문자 삭제
    # stack1이 있을 경우, 가장 오른쪽 문자(마지막 요소)를 제거
    elif command[0] == 'B' and stack1:
        stack1.pop()
    
    # 커서 왼쪽에 새로운 문자 추가
    # stack1에 새로 추가할 문자(command[1])를 추가
    elif command[0] == 'P':
        stack1.append(command[1])

# stack2에 있는 문자를 stack1에 모두 추가
stack1.extend(reversed(stack2)) # stack2는 커서 오른쪽 문자이므로 뒤집을 것

print(''.join(stack1)) # stack1의 문자들을 하나의 문자열로 합쳐 출력
