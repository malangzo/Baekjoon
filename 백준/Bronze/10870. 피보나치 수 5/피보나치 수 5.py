# 백준 10870번 문제 풀이

num = int(input())

i, j = 0, 1 # 0번째, 1번째 피보나치 수 정의

if num <= 1: # 0번째, 1번째일 경우 그대로 출력
    print(num)

else:
    for _ in range(2, num + 1): # 2번째 피보나치 수부터 i와 j를 더해 피보나치 수 구함
        k = i + j
        i, j = j, k
    print(k)
