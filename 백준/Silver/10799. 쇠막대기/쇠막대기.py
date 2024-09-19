# 백준 10799번 문제 풀이

arrange = input()

def cut(arrange):
    stack = []
    pieces = 0

    for i in range(len(arrange)):
        
        # 쇠막대기 스택에 추가
        if arrange[i] == '(':
            stack.append('(')

        # 여는 괄호가 레이저인 경우
        elif arrange[i - 1] == '(':
            stack.pop()
            pieces += len(stack)  # 쇠막대기 개수만큼 스택에 추가

        # 쇠막대기 끝인 경우
        else:
            stack.pop()
            pieces += 1  # 쇠막대기 하나 추가
    
    return pieces

print(cut(arrange))