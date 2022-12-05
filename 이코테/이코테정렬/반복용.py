def solution(N, stages):
    answer = []
    stage = 1
    fail = [0] * (N+1)

    for i in range(1, N+1):  # 1부터인 이유는 stages의 최솟값이 1
        nopeClear = stages.count(i)  # stages 의 값들의 갯수
        reach = [i for i in stages if i >= stage]
        fail = nopeClear / len(reach) if len(reach) != 0 else 0
        stage += 1
        answer.append((i, fail))

    answer.sort(key=lambda x: -x[1])
    return [i[0] for i in answer]
