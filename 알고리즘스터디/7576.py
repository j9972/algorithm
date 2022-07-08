# 토마토가 익는 최소 일수 구하기 BFS 문제
from collections import deque

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

# 가로 세로 순서 ( 원래대로 풀면 된다 ) 2 ~ 1000
m, n = map(int, input().split())
