import sys
input = sys.stdin.readline

n = int(input())

set_list = set()

for i in range(n):
    word = input().rstrip()

    set_list.add(word)

for i in sorted(set_list, key = lambda x : (len(x),x)):
    print(i)

