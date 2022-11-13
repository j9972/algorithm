from itertools import permutations


def solution(n, weak, dist):
    # 최솟값을 구해야하니까 초기화 시키기
    answer = len(dist) + 1

    # 내림 차순으로 해서 거리가 가장 긴 거리친구부터 배치
    dist.sort(reverse=True)

    length = len(weak)

    # 배열 확장 -> 반시계 / 시계 방향 체크 할 필요가 없음
    for i in range(length):
        weak.append(weak[i]+n)

    for start in range(length):
        for friends in list(permutations(dist, len(dist))):
            count = 1

            # 점검 가능한 마지막 위치
            position = weak[start] + friends[count - 1]

            for index in range(start, start+length):
                # 점검 범위를 벗어나면
                if position < weak[index]:
                    count += 1
                    # 친구의 명수가 부족하면
                    if count > len(dist):
                        break
                    position = weak[index] + friends[count - 1]

            answer = min(answer, count)

    # 취약점 모두를 찾을 수 없는 경우
    if answer > len(dist):
        return -1
    return answer
