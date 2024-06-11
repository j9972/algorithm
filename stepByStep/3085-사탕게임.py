n = int(input())

arr = [
    list(input())
    for _ in range(n)
]


def in_range(x, y):
    return 0 <= x < n and 0 <= y < n


ans = 1



def checkCurMaxNum():
    max_cnt = 1  # total_max_cnt
    for i in range(n):
        # 가로 먼저 확인
        cnt = 1
        for j in range(1, n):
            if arr[i][j] == arr[i][j - 1]:
                cnt += 1
            else:
                cnt = 1
            max_cnt = max(cnt, max_cnt)
        # 세로 확인
        cnt = 1
        for j in range(1, n):
            if arr[j][i] == arr[j - 1][i]:
                cnt += 1
            else:
                cnt = 1
            max_cnt = max(cnt, max_cnt)

    return max_cnt

for i in range(n):
    for j in range(n - 1):
        if in_range(i, j + 1) and arr[i][j] != arr[i][j + 1]:
            arr[i][j], arr[i][j + 1] = arr[i][j + 1], arr[i][j]
            ans = max(ans, counting())
            arr[i][j], arr[i][j + 1] = arr[i][j + 1], arr[i][j]
        elif in_range(i + 1, j) and arr[i][j] != arr[i + 1][j]:
            arr[i][j], arr[i + 1][j] = arr[i + 1][j], arr[i][j]
            ans = max(ans, counting())
            arr[i][j], arr[i + 1][j] = arr[i + 1][j], arr[i][j]
print(ans)
