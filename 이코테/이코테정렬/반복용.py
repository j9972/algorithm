def solution(N, stages):
    answer = []
    fail = [0] * (N+1)
    stage = 1

    for i in range(1, N+1):
        notClear = stages.count(i)
        reach = [i for i in stages if i >= stage]
        fail = notClear / len(reach) if len(reach) != 0 else 0
        stage += 1
        answer.append((i, fail))

    answer.sort(key=lambda x: -x[1])
    return [i[0] for i in answer]
