def solution(N, stages):
    answer = []
    stage = 1
    fail = [0] * (N+1)

    for i in range(1, N+1):
        until = stages.count(i)  # 아직 클리어 못한 사람 수
        reach = [i for i in stages if i >= stage]  # 도달한 사람 수
        fail = until / len(reach) if len(reach) != 0 else 0  # 실패율 계산
        stage += 1  # stage 이동
        answer.append((i, fail))

    answer = sorted(answer, key=lambda x: -x[1])

    return [i[0] for i in answer]
