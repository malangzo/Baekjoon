# 백준 1914번 문제 풀이

# 재귀 함수 정의
def hanoi(n, first, second, thrid):
    
    if n == 1: # 원판 한 개만 옮기는 경우
        print(first, thrid)
    
    else: # 원판을 n개(<= 20) 옮기는 경우
        hanoi(n-1, first, thrid, second) # 첫 번째에서 두 번째 장대로 n-1개 원판 이동
        print(first, thrid) # n번째 원판을 첫 번째에서 세 번째 장대로 이동
        hanoi(n-1, second, first, thrid) # 두 번째에서 세 번째 장대로  n-1개 원판 이동
        
n = int(input())

count = 2**n -1 # 총 이동 횟수

print(count)

if n <= 20:
    hanoi(n, 1, 2, 3)