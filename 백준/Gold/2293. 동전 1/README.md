## 📌 문제 번호

- 문제 번호: 2293

## 📚 사용한 자료구조/알고리즘

- 자료구조/알고리즘: 동적 프로그래밍

## 🔍 문제의 핵심 포인트

문제를 이해하는 데 중요한 부분
> dp[i]가 i원을 만드는 방법의 수라고 할 때, 0원부터 시작해 i원까지 만드는 방법을 점차 누적하여 계산
- dp[0]의 경우 0원을 만드는 방법은 1가지이므로 dp[0] = 1
- 이후 1원이 추가되었을 때, 2원이 추가되었을 때를 차차 누적해 가며 각 dp[0]부터 dp[i]까지의 값을 계산
- 모든 가짓수를 누적하고 나면, 종류별로 동전을 조합해서(중복 조합) 목표 금액을 만드는 dp[k] 계산 가능
- dp[i] = dp[i] + dp[i - coin]을 통해 dp[k] 계산

## ⏱️ 코드의 시간복잡도

- 시간복잡도: 동전 1개당 k번 반복되므로 n * k번 수행 → O(n * k)

## 🧠 코드의 공간복잡도

- 공간복잡도: 동전 n 개의 공간 및 dp[i]의 공간 k → O(n + k)


# [Gold V] 동전 1 - 2293 

[문제 링크](https://www.acmicpc.net/problem/2293) 

### 성능 요약

메모리: 31120 KB, 시간: 156 ms

### 분류

다이나믹 프로그래밍

### 제출 일자

2024년 9월 23일 05:19:27

### 문제 설명

<p>n가지 종류의 동전이 있다. 각각의 동전이 나타내는 가치는 다르다. 이 동전을 적당히 사용해서, 그 가치의 합이 k원이 되도록 하고 싶다. 그 경우의 수를 구하시오. 각각의 동전은 몇 개라도 사용할 수 있다.</p>

<p>사용한 동전의 구성이 같은데, 순서만 다른 것은 같은 경우이다.</p>

### 입력 

 <p>첫째 줄에 n, k가 주어진다. (1 ≤ n ≤ 100, 1 ≤ k ≤ 10,000) 다음 n개의 줄에는 각각의 동전의 가치가 주어진다. 동전의 가치는 100,000보다 작거나 같은 자연수이다.</p>

### 출력 

 <p>첫째 줄에 경우의 수를 출력한다. 경우의 수는 2<sup>31</sup>보다 작다.</p>

