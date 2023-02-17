from itertools import permutations as pm


def solution(n, weak, dist):
    ans = len(dist) + 1
    length = len(weak)

    for i in range(length):
        weak.append(weak[i]+n)

    for start in range(length):
        for friends in list(pm(dist, len(dist))):
            cnt = 1
            pos = weak[start] + friends[cnt-1]

            for idx in range(start, start+length):
                if pos < weak[idx]:
                    cnt += 1
                    if cnt > len(dist):
                        break
                    pos = weak[idx] + friends[cnt-1]
            ans = min(ans, cnt)

    if ans > len(dist):
        return -1
    return ans


print(solution(12, [1, 5, 6, 10], [1, 2, 3, 4]))
