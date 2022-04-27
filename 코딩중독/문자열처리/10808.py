import sys
input = sys.stdin.readline

if __name__ == "__main__":
    arr = input()
    counting = [0] * 26

    for i in range(arr):
        counting[ord(i) - 97] = arr.count(i)

    for i in counting:
        print(i, end=" ")
