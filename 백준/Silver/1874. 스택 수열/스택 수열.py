# 백준 1874번 문제 풀이

n = int(input()) # n까지의 수열 입력
stack, now, result = [], 1, [] # 수열 담을 리스트, 넣을 숫자, 결과 넣을 리스트 생성

for _ in range(n):

    num = int(input()) # stack에 몇까지 숫자 추가할 건지 입력

    while now <= num:
        stack.append(now) # stack에 num까지 추가
        now += 1
        result.append('+') # stack에 push 했으므로 결과에 + 추가

    if stack[-1] == num: # stack 맨 뒤가 입력한 num과 같을 경우
        stack.pop() # stack에서 해당 숫자 제거
        result.append('-') # stack에서 pop 되었으므로 결과에 - 추가

    else:
        result = ['NO'] # 수열을 만들 수 없을 경우 result에는 NO만 들어가게 함
        break

print('\n'.join(result))
