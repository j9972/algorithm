# 뉴스전하기
import sys
input = sys.stdin.readline

n = int(input())
data = list(map(int, input().split()))
tree = [[] for _ in range(n)]
child_cnt = [0] * n

for i in range(1, len(data)):
    tree[data[i]].append(i)


def go(x):
    global child_cnt
    child_node = []

    if len(tree[x]) == 0:
        child_cnt[x] = 0

    else:
        for child in tree[x]:
            go(child)
            child_node.append(child_cnt[child])
        child_node.sort(reverse=True)
        child_node = [child_node[i] + i + 1 for i in range(len(child_node))]
        child_cnt[x] = max(child_node)


go(0)
print(child_cnt[0])
