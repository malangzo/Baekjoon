# 백준 10870번 문제 풀이

num = int(input())

i, j = 0, 1

if num <= 1:
    print(num)

else:
    for _ in range(2, num + 1):
        k = i + j
        i, j = j, k
    print(k)
