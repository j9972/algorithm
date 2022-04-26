
import sys
input = sys.stdin.readline


if __name__ == "__main__":
    for test in range(int(input())):
        n = int(input())
        arr = [[0]*100000, [0]*100000]

        for idx, var in enumerate(map(int, input().split())):
            arr[0][idx] = var
        for idx, var in enumerate(map(int, input().split())):
            arr[1][idx] = var

        arr[0][1] += arr[1][0]
        arr[1][1] += arr[0][0]

        for i in range(2, n):
            arr[0][i] += max(arr[1][i-1], arr[1][i-2])
            arr[1][i] += max(arr[0][i-1], arr[0][i-2])
        print(max(arr[0][n-1], arr[1][n-1]))
