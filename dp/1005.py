from collections import deque
import sys
input = sys.stdin.readline

# 예시에서 1 -> 2 -> 4 / 1 -> 3 -> 4 이런 순서로 선수관계가 있어서 위상정렬을 적용해야함.
for tc in range(int(input())):
    n, k = map(int, input().split())  # k 는 건설 규칙 개수

    # 빌딩에 대한 번호랑 시간이랑 같이 저장 ( 번호는 +1 해서 사용하기 )
    time = list(map(int, input().split()))

    seq = [[] for _ in range(n+1)]  # 2차원 배열로 트리구조로 데이터가 들어 올거임

    inDegree = [0 for _ in range(n+1)]  # 진입 차수
    dp = [0 for _ in range(n+1)]  # 시간들의 합이 나타나는 장소

    queue = deque()  # 큐를 이용한 위상 정렬

    for i in range(k):  # k 번동안 a->b 로 이동을 하면서 전입차수의 개수를 체크해준다
        a, b = map(int, input().split())
        seq[a].append(b)
        inDegree[b] += 1

    target = int(input())

    # 모든 노드 체크 ( 노드 번호는 1부터 시작 ) 하면서, 전입 차수 없으면 큐에 넣어줌
    # 위상 정렬 알고리즘 ( dp의 시간의 합을 time[i-1] 까지 구해서 넣어준다 )
    for i in range(1, n+1):
        if inDegree[i] == 0:
            queue.append(i)
            dp[i] = time[i-1]

    while queue:
        tmp = queue.popleft()

        for i in seq[tmp]:  # queue에서 꺼낸 값을 인덱스로 하는 k_way
            inDegree[i] -= 1
            dp[i] = max(dp[i], time[i-1] + dp[tmp])
            if inDegree[i] == 0:
                queue.append(i)

    print(dp[target])
