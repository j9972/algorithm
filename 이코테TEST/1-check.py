from collections import deque
import heapq
import sys
input = sys.stdin.readline


def solution(s):
    length = len(s)

    for step in range(1, len(s)//2 + 1):
        cnt = 1
        prev = s[:step]
        ans = ""

        for i in range(step, len(s), step):
            if prev == s[i:i+step]:
                cnt += 1
            else:
                ans += str(cnt) + prev if cnt >= 2 else prev
                cnt = 1
                prev = s[i:i+step]
        ans += str(cnt) + prev if cnt >= 2 else prev
        length = min(length, len(ans))
    return length
