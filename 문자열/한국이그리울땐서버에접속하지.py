# 실버3 - 9996
import sys
input = sys.stdin.readline

n = int(input())
pattern = input().rstrip().split('*')
length = len(pattern[0]) + len(pattern[1])

for i in range(n):
    words = input().rstrip()
    if length > len(words):
        print('NE')
    else:
        if pattern[0] == words[:len(pattern[0])] and pattern[1] == words[-len(pattern[1]):]:
            print('DA')
        else:
            print('NE')