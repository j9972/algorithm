import sys
input = sys.stdin.readline

n = int(input())
data = list(map(int, input().split()))
# 트리 구조
tree = [[] for _ in range(n)]
# 각 노드까지의 거리 ( 시간 )
child_cnt = [0] * n

# 민식이는 사장이니까 뺀다 -> data로 tree 파트 채우기, tree를 2차원 배열로 만듬
for i in range(1, len(data)):
    tree[data[i]].append(i)

# 내가 두명의 부하 직원에게 연락하라고 시키면 결과적으로 총 걸리는 시간은 둘 중에 가장 큰 값


def go(x):
    global child_cnt
    # 각 노드까지 가는데 걸리는 시간
    child_tree = []

    # 이 말은 leaf node가 0 -> 자식이 더 이상 없다
    if len(tree[x]) == 0:
        child_cnt[x] = 0
    else:
        for child in tree[x]:
            go(child)
            child_tree.append(child_cnt[child])

        # 오래걸리는 것부터 나오게 내림차순
        child_tree.sort(reverse=True)
        # child_tree[i] + (i + 1) = 서브트리에 전파하는시간 +( 이번 단계에서 걸리는 시간 )
        child_tree = [child_tree[i] + (i + 1) for i in range(len(child_tree))]
        child_cnt[x] = max(child_tree)


go(0)
print(child_cnt[0])
