from itertools import permutations as pm
import sys
input = sys.stdin.readline


def solution(n, weak, dist):
    ans = len(dist) + 1

    dist.sort(reverse=True)
    length = len(weak)

    for i in range(length):
        weak.append(weak[i]+n)

    for start in range(length):
        for friend in list(pm(dist, len(dist))):
            friendCnt = 1
            pos = weak[start] + friend[friendCnt-1]

            for idx in range(start, start+length):
                if pos < weak[idx]:
                    friendCnt += 1
                    if friendCnt > len(dist):
                        break
                    pos = weak[idx] + friend[friendCnt-1]
            ans = min(ans, friendCnt)
    if ans > len(dist):
        return -1
    return ans
