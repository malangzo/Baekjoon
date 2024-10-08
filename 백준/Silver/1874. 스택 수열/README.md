## 📌 문제 번호

- 문제 번호: 1874

## 📚 사용한 자료구조/알고리즘

- 자료구조/알고리즘: 스택 활용 및 반복문, 조건문 사용

## 🔍 문제의 핵심 포인트

- 문제 조건에 따라 스택에 추가(push)되는 순서가 오름차순이 되게 해야 함
- 임의의 수열을 만들기 위해서는 임의의 n까지 추가된 스택에서 n을 pop해야 함

## ⏱️ 코드의 시간복잡도

n 입력 → O(1)
for문 및 while 루프 → n번 반복하므로 O(n)
조건문 → O(1)
결과 출력 → O(n)

따라서 전체 시간 복잡도는 O(n)이 됨

## 🧠 코드의 공간복잡도

1차 코드: for _ in range(int(input()))으로 n을 입력받고 및 바로 결과를 print로 출력 (출력 초과 뜸)
2차 코드: n을 따로 변수 지정하고, 결과 리스트를 생성해 출력

→ 1차 코드와 2차 코드의 공간 복잡도는 O(n)으로 똑같음
→ 하지만 1차 코드의 경우 입출력의 효율성 문제 및 출력 초과 문제 존재

# [Silver II] 스택 수열 - 1874 

[문제 링크](https://www.acmicpc.net/problem/1874) 

### 성능 요약

메모리: 33488 KB, 시간: 2416 ms

### 분류

자료 구조, 스택

### 제출 일자

2024년 9월 4일 00:09:37

### 문제 설명

<p>스택 (stack)은 기본적인 자료구조 중 하나로, 컴퓨터 프로그램을 작성할 때 자주 이용되는 개념이다. 스택은 자료를 넣는 (push) 입구와 자료를 뽑는 (pop) 입구가 같아 제일 나중에 들어간 자료가 제일 먼저 나오는 (LIFO, Last in First out) 특성을 가지고 있다.</p>

<p>1부터 n까지의 수를 스택에 넣었다가 뽑아 늘어놓음으로써, 하나의 수열을 만들 수 있다. 이때, 스택에 push하는 순서는 반드시 오름차순을 지키도록 한다고 하자. 임의의 수열이 주어졌을 때 스택을 이용해 그 수열을 만들 수 있는지 없는지, 있다면 어떤 순서로 push와 pop 연산을 수행해야 하는지를 알아낼 수 있다. 이를 계산하는 프로그램을 작성하라.</p>

### 입력 

 <p>첫 줄에 n (1 ≤ n ≤ 100,000)이 주어진다. 둘째 줄부터 n개의 줄에는 수열을 이루는 1이상 n이하의 정수가 하나씩 순서대로 주어진다. 물론 같은 정수가 두 번 나오는 일은 없다.</p>

### 출력 

 <p>입력된 수열을 만들기 위해 필요한 연산을 한 줄에 한 개씩 출력한다. push연산은 +로, pop 연산은 -로 표현하도록 한다. 불가능한 경우 NO를 출력한다.</p>

