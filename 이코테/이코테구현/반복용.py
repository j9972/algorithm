from itertools import permutations


def solution(n, weak, dist):

    dist.sort(reverse=True)
    length = len(weak)
    ans = len(dist) + 1

    for i in range(length):
        weak.append(weak[i]+n)

    for start in range(length):
        for friends in list(permutations(dist, len(dist))):
            cnt = 1
            position = weak[start] + friends[cnt - 1]

            for index in range(start, start+length):
                if weak[index] > position:
                    cnt += 1
                    if cnt > len(dist):
                        break
                    position = weak[index] + friends[cnt - 1]

            ans = min(ans, cnt)
    if ans > len(dist):
        return -1

    return ans
