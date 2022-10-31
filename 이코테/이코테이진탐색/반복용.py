# 가사 검색
from bisect import bisect_left, bisect_right


def count(a, left, right):
    leftIdx = bisect_left(a, left)
    rightIdx = bisect_right(a, right)
    return rightIdx - leftIdx


def solution(words, queries):
    answer = []

    array = [[] for _ in range(10001)]
    reverArray = [[] for _ in range(10001)]

    for word in words:
        array[len(word)].append(word)
        reverArray[len(word)].append(word[::-1])

    for i in range(10001):
        array[i].sort()
        reverArray[i].sort()

    for q in queries:
        if q[0] != '?':
            res = count(array[len(q)], q.replace(
                '?', 'a'), q.replace('?', 'z'))
        else:
            res = count(
                reverArray[len(q)], q[::-1].replace('?', 'a'), q[::-1].replace('?', 'z'))
        answer.append(res)

    return answer
