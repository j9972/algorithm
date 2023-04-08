from bisect import bisect_right, bisect_left


def count_by__range(a, left_value, right_value):
    return bisect_right(a, right_value)- bisect_left(a, left_value)


def solution(words, queries):
    answer = []

    array = [[] for _ in range(10001)]
    reverse_array = [[] for _ in range(10001)]

    for word in words:
        array[len(word)].append(word)
        reverse_array[len(word)].append(word[::-1])

    for i in range(10001):
        array[i].sort()
        reverse_array[i].sort()

    for q in queries:
        if q[0] != '?':  # 접두사 있ㅇ,ㅁ
            res = count_by__range(array[len(q)], q.replace(
                '?', 'a'), q.replace('?', 'z'))
        else:  # 접미사 있음
            res = count_by__range(
                reverse_array[len(q)], q[::-1].replace('?', 'a'), q[::-1].replace('?', 'z'))
        answer.append(res)

    return answer
