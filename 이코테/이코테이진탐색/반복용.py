from bisect import bisect_left, bisect_right
import sys
input = sys.stdin.readline


def count_by_range(a, left_value, right_value):
    left_index = bisect_left(a, left_value)
    right_index = bisect_right(a, right_value)
    return right_index - left_index


def solution(words, queries):
    answer = []

    array = [[] for _ in range(10001)]
    reverseArray = [[] for _ in range(10001)]

    for word in words:
        array[len(word)].append(word)
        reverseArray[len(word)].append(word[::-1])

    for i in range(10001):
        array[i].sort()
        reverseArray[i].sort()

    for q in queries:
        if q[0] != '?':
            res = count_by_range(array[len(q)], q.replace(
                'a', '?'), q.replace('z', '?'))
        else:
            res = count_by_range(
                reverseArray[len(q)], q[::-1].replace('a', '?'), q[::-1].replace('z', '?'))
        answer.append(res)

    print(answer)
